Summary:	Display and control your Android device
Name:		scrcpy
Version:	1.25
Release:	1
License:	Apache v2.0
Group:		Applications
Source0:	https://github.com/Genymobile/scrcpy/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	1e2173b606870aa28d81265f634a31d4
Source1:	https://github.com/Genymobile/scrcpy/releases/download/v%{version}/%{name}-server-v%{version}
# Source1-md5:	f636d4bacae28c10943e44266bebc967
URL:		https://github.com/Genymobile/scrcpy
BuildRequires:	SDL2-devel >= 2.0.5
BuildRequires:	ffmpeg-devel
BuildRequires:	libusb-devel
BuildRequires:	meson >= 0.48
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
Requires:	SDL2 >= 2.0.5
Requires:	android-tools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Display and control your Android device.

%prep
%setup -q
cp -p %{SOURCE1} %{name}-server

%build
%meson build \
	-Dprebuilt_server=%{name}-server

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/scrcpy
%dir %{_datadir}/scrcpy
%attr(755,root,root) %{_datadir}/scrcpy/scrcpy-server
%{_desktopdir}/scrcpy.desktop
%{_desktopdir}/scrcpy-console.desktop
%{_iconsdir}/hicolor/256x256/apps/scrcpy.png
%{_mandir}/man1/scrcpy.1*
