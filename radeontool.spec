Name:		radeontool
Version:	1.5
Release:	%mkrel 3
Summary:	Enable/disable ATI Radeon external display/backlight
Source0:	http://www.fdd.com/software/radeon/radeontool-%{version}.tar.bz2
Source1:	http://www.fdd.com/software/radeon/lightwatch2.pl
Patch0:		radeontool-1.5.patch
URL:		http://www.fdd.com/software/radeon
License:	BSD
Group:		System/Configuration/Hardware

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
%patch -p1 -b .orig
cp %{SOURCE1} .

%build
%make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_sbindir}
install radeontool %{buildroot}%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,755)
%doc CHANGES lightwatch.pl lightwatch2.pl
%{_sbindir}/radeontool


