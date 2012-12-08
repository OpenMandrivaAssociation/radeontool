Name:		radeontool
Version:	1.6.0
Release:	%mkrel 3
Summary:	Enable/disable ATI Radeon external display/backlight
Source0:	http://people.freedesktop.org/~airlied/%{name}/%{name}-%{version}.tar.bz2
Source1:	http://www.fdd.com/software/radeon/lightwatch2.pl
Patch1:		radeontool-1.6.0-fix-str-fmt.patch
URL:		http://people.freedesktop.org/~airlied/radeontool/
License:	BSD
Group:		System/Configuration/Hardware
BuildRoot:	%_tmppath/%name-%version-buildroot
BuildRequires:	libpciaccess-devel

%description
This utility should enable/disable the external display for ATI Radeon video
cards.
It should also enable/disable the backlight on a laptop equipped with a an ATI
Radeon Mobility video card.
Since it was engineered without access to the Radeon documents, it may as well
break your hardware.
USE RADEONTOOL AT YOUR OWN RISK


%prep
%setup -q
%patch1 -p1 -b .str
cp %{SOURCE1} .

%build
%configure2_5x --bindir=%{_sbindir}
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,755)
%doc lightwatch2.pl
%{_sbindir}/radeontool
%{_sbindir}/avivotool




%changelog
* Mon Feb 20 2012 abf
- The release updated by ABF

* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 1.6.0-2mdv2011.0
+ Revision: 669395
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.6.0-1mdv2011.0
+ Revision: 607293
- rebuild

* Mon Feb 08 2010 Frederik Himpe <fhimpe@mandriva.org> 1.6.0-0mdv2010.1
+ Revision: 502461
- Fix BuildRequires
- Update to new version 1.6.0
- Remove patch which is not needed anymore (partly merged upstream,
  other part does not apply anymore)
- Update string format patch

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.5-9mdv2010.0
+ Revision: 426855
- rebuild

* Sat Apr 11 2009 Funda Wang <fwang@mandriva.org> 1.5-8mdv2009.1
+ Revision: 366211
- fix str fmt
- fix patch num

* Mon Aug 25 2008 Luca Berra <bluca@mandriva.org> 1.5-8mdv2009.0
+ Revision: 275705
- revert buildrequire kernel-headers
- use sysconf(_SC_PAGESIZE) instead of PAGE_SIZE
- BuildRequires kernel-headers
- fix segfault when using --debug (#43128)

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Dec 19 2007 Thierry Vignaud <tv@mandriva.org> 1.5-4mdv2008.1
+ Revision: 134671
- rebuild

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.5-3mdv2008.1
+ Revision: 126435
- kill re-definition of %%buildroot on Pixel's request


* Sun Jan 21 2007 Emmanuel Andry <eandry@mandriva.org> 1.5-3mdv2007.0
+ Revision: 111399
- bunzip patch /
  %%mkrel
- Import radeontool

* Mon Aug 29 2005 Luca Berra <bluca@vodka.it> 1.5-2mdk
- rebuild

* Sat Jul 24 2004 Luca Berra <bluca@vodka.it> 1.5-1mdk
- 1.5
- added lightwatch2.pl to docs

