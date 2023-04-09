Summary:	Display and control your Android device
Name:		scrcpy
Version:	2.0
Release:	1
License:	Apache v2.0
Group:		Applications
Source0:	https://github.com/Genymobile/scrcpy/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	7aaf3494112e8127cbafddcacf04d53d
Source1:	https://github.com/Genymobile/scrcpy/releases/download/v%{version}/%{name}-server-v%{version}
# Source1-md5:	5ea87ea427c3fd63965db46a18342794
URL:		https://github.com/Genymobile/scrcpy
BuildRequires:	SDL2-devel >= 2.0.5
BuildRequires:	ffmpeg-devel
BuildRequires:	libusb-devel
BuildRequires:	meson >= 0.48
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.736
Requires:	SDL2 >= 2.0.5
Requires:	android-tools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Display and control your Android device.

%package -n bash-completion-scrcpy
Summary:	bash-completion for scrcpy
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	bash-completion >= 1:2.0
BuildArch:	noarch

%description -n bash-completion-scrcpy
bash-completion for scrcpy.

%package -n zsh-completion-scrcpy
Summary:	zsh-completion for scrcpy
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	zsh
BuildArch:	noarch

%description -n zsh-completion-scrcpy
zsh-completion for scrcpy.

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

%files -n bash-completion-scrcpy
%defattr(644,root,root,755)
%{bash_compdir}/scrcpy

%files -n zsh-completion-scrcpy
%defattr(644,root,root,755)
%{zsh_compdir}/_scrcpy
