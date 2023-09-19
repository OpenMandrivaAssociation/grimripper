%define oname GrimRipper

Summary:	GTK+-based audio CD ripper and encoder

Name:		grimripper
Version:	3.0.2
Release:	1
License:	GPLv2
Group:		Archiving/Cd burning
URL:		https://gitlab.gnome.org/Salamandar/GrimRipper
Source0:	https://gitlab.gnome.org/Salamandar/GrimRipper/-/archive/v%{version}/%{oname}-v%{version}.tar.bz2

BuildRequires:	meson
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libcddb)
BuildRequires:	intltool >= 0.34.90

Requires:	cdparanoia
Suggests:	lame
Suggests:	vorbis-tools
Suggests:	flac
Suggests:	wavpack

%description
Asunder is a graphical Audio CD ripper and encoder for Linux. You can 
use it to save tracks from an Audio CD as WAV, MP3, OGG, Musepack, AAC,
Monkey Audio, and/or FLAC.

%prep
%setup -qn %{oname}-v%{version}

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{oname}

%files -f %{oname}.lang
%doc AUTHORS ChangeLog Readme.md TODO
%{_bindir}/%{name}
%{_datadir}/applications/*.%{name}.desktop
%{_datadir}/metainfo/org.gnome.gitlab.%{name}*
%{_iconsdir}/hicolor/*/apps/org.gnome.gitlab.%{name}*



