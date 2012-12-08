#!/usr/bin/perl -w
use strict;

my $VERSION = "2.1";

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

#  Bill Chmura (Bill@Explosivo.com)

# lightwatch2.pl - a perl script based on the concept set forth by lightwatch.pl 
#	lightwatch.pl was written by Frederick Dean (http://fdd.com/software/)
#	without that script showing how to do it, this would not have happened as fast!
#
# NOTE:	if you set the PM_STATE_TO_BLANK_ON to none, the script will simply exit
# NOTE:	this script requires both XScreensaver-command and radeontools be installed
# NOTE:	KDE does not run Xscreensaver, but it can easily do so (See xscreensaver web site for more info)

my $PATH_TO_XSCREENSAVER = '/usr/bin/';
my $PM_TYPE = 'acpi';	#options:   acpi, apm, none
my $PM_STATE_TO_BLANK_ON = 'battery'; 	#options: battery, ac, all, none


######## NO USER SERVICABLE PARTS BELOW ##############################

$<=0;  # Become root (Radeontools requires this)

my $AC_CHECK_MATCH = 0;

if ($PM_STATE_TO_BLANK_ON eq 'battery') {
	$AC_CHECK_MATCH = 0;
} elsif ($PM_STATE_TO_BLANK_ON eq 'ac') {
	$AC_CHECK_MATCH = 1;
}

if ($PM_STATE_TO_BLANK_ON eq 'none') {
	print "Current settings will never blank screen - exiting\n";
	exit();
} elsif ($PM_TYPE eq 'acpi' && ($PM_STATE_TO_BLANK_ON eq 'battery' || $PM_STATE_TO_BLANK_ON eq 'ac')) {
	&LoopACPI($AC_CHECK_MATCH);
} elsif ($PM_TYPE eq 'apm' && ($PM_STATE_TO_BLANK_ON eq 'battery' || $PM_STATE_TO_BLANK_ON eq 'ac'))  {
	&LoopAPM($AC_CHECK_MATCH);	#Will be apm soon hopefully
} else {
	&LoopNormal();
}

exit;

sub LoopNormal {
	
	print "Loopnormal\n";
	open(XS,$PATH_TO_XSCREENSAVER . 'xscreensaver-command -watch|') or die "Error: Could not find or execute xscreensaver-command\n\n";

	while(<XS>) {
   		if(/^BLANK/io) {
      			system("radeontool light off");
   		} elsif(/^UNBLANK/i) {
      			system("radeontool light on");
		}
   	}
	close(XS);
}

sub LoopAPM {
	my $PM_STATE_TO_BLANK_ON = shift;
	&LoopNormal();

}



sub LoopACPI {
	print "Loopacpi\n";
	my $AC_CHECK_MATCH = shift;
	open(XS,$PATH_TO_XSCREENSAVER . 'xscreensaver-command -watch|') or die "Error: Could not find or execute xscreensaver-command\n\n";
	
	while(<XS>) {
   		if(/^BLANK/io && (CheckACPI_ACPOWER() == $AC_CHECK_MATCH)) {
      			system("radeontool light off");
   		} elsif(/^UNBLANK/i) {
      			system("radeontool light on");
   		}
	}
	close(XS);
}

sub CheckACPI_ACPOWER {
	my $retval = 0;
	open (F,'/proc/acpi/ac_adapter/ACAD/state') || die "Error: Cannot find acpi state file\n\n";
		$retval = 1 if (<F> =~ /on-line/o);
	close (F);
	print "ACPI power is $retval\n";
	return ($retval);
}

sub CheckAPM_ACPOWER {
	my $retval = 0;
	my $apmout = `apm`;
	$retval = 1 if $apmout =~ /AC\s+on-line/i;
	print "APM power is $retval\n";
	return ($retval);
}

