Name:		radeontool
Version:	1.6.0
Release:	%mkrel 0
Summary:	Enable/disable ATI Radeon external display/backlight
Source0:	http://people.freedesktop.org/~airlied/%{name}/%{name}-%{version}.tar.bz2
Source1:	http://www.fdd.com/software/radeon/lightwatch2.pl
Patch1:		radeontool-1.6.0-fix-str-fmt.patch
URL:		http://people.freedesktop.org/~airlied/radeontool/
License:	BSD
Group:		System/Configuration/Hardware
BuildRoot:	%_tmppath/%name-%version-buildroot

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


