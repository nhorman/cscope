Summary: cscope is an interactive, screen-oriented tool that allows the user to browse through C source files for specified elements of code.
Name: cscope
Version: 15.0bl3
Release: 1
Copyright: BSD
Group: Development/Tools
Source: cscope-15.0bl3.tar.gz
Buildroot: /tmp/%{name}-%{version}

%description
cscope is an interactive, screen-oriented tool that allows the user to browse through C source files for specified elements of code.

%prep
%setup

%build
./configure
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/bin
mkdir -p $RPM_BUILD_ROOT/usr/local/man/man1

install -s -m 755 src/cscope $RPM_BUILD_ROOT/usr/local/bin/cscope
install -m 755 doc/cscope.1 $RPM_BUILD_ROOT/usr/local/man/man1/cscope.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc TODO COPYING ChangeLog AUTHORS README NEWS INSTALL

/usr/local/bin/cscope
/usr/local/man/man1/cscope.1

%changelog
* Tue May 15 2000 Cscope development team
- Version 15.0bl2 (build 2) pre-alpha release
- Fixes and enhancements
- Updated documentation
- Autoconf/automake support
- directory restructuring
* Sun Apr 16 2000 Petr Sorfa <petrs@sco.com>
- Initial Open Source release
- Ported to GNU environment
- Created rpm package