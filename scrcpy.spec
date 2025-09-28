Summary:	Display and control your Android device
Name:		scrcpy
Version:	3.3.3
Release:	1
License:	Apache v2.0
Group:		Applications
Source0:	https://github.com/Genymobile/scrcpy/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	24377eea8265ebc9f20c8d0dba0146d1
Source1:	https://github.com/Genymobile/scrcpy/releases/download/v%{version}/%{name}-server-v%{version}
# Source1-md5:	3c0efc256603ef2fb9575de0862178fd
URL:		https://github.com/Genymobile/scrcpy
BuildRequires:	SDL2-devel >= 2.0.5
BuildRequires:	ffmpeg-devel
BuildRequires:	libusb-devel
BuildRequires:	meson >= 0.49
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 2.042
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires:	SDL2 >= 2.0.5
Requires:	android-tools
Requires:	hicolor-icon-theme
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
%meson \
	-Dprebuilt_server=%{name}-server

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post
%update_icon_cache hicolor

%postun
%update_desktop_database_postun
%update_icon_cache hicolor

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
