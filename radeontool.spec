Summary:	Enable/disable ATI Radeon external display/backlight
Name:		radeontool
Version:	1.6.3
Release:	20
License:	BSD
Group:		System/Configuration/Hardware
Url:		https://people.freedesktop.org/~airlied/radeontool/
Source0:	http://people.freedesktop.org/~airlied/%{name}/%{name}-%{version}.tar.bz2
Source1:	http://www.fdd.com/software/radeon/lightwatch2.pl
BuildRequires:	pkgconfig(pciaccess)

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
cp %{SOURCE1} .

%build
%configure2_5x --bindir=%{_sbindir}
%make

%install
%makeinstall_std

%files
%doc lightwatch2.pl
%{_sbindir}/radeontool
%{_sbindir}/avivotool
%{_sbindir}/radeonreg

