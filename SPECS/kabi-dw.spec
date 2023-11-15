%global commitdate 20230223
%global commit eedfcbf9c60feedb532ad3d4d111ca93f7c32a26
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           kabi-dw
Version:        0
Release:        0.25.%{commitdate}git%{shortcommit}%{?dist}
Summary:        Detect changes in the ABI between kernel builds
License:        GPLv3+
URL:            https://github.com/skozina/%{name}
Source0:        %{name}-%{shortcommit}.tar.gz

BuildRequires:  elfutils-devel
BuildRequires:  gcc
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  glib2-devel
BuildRequires:  redhat-rpm-config
BuildRequires:  make

%description
The aim of kabi-dw is to detect any changes in the ABI between the successive
builds of the Linux kernel. This is done by dumping the DWARF type information
(the .debug_info section) for the specific symbols into the text files and
later comparing the text files.

%prep
%setup -q -n %{name}-%{commit}

%build
#CFLAGS=$RPM_OPT_FLAGS LDFLAGS=$RPM_LD_FLAGS make debug
%set_build_flags
%make_build

%install
install -dm 755 %{buildroot}%{_bindir}
install -m 0755 %{name} %{buildroot}%{_bindir}/

%files
%{_bindir}/%{name}
%doc README.md
%license COPYING

%changelog
* Mon Jul 03 2023 Čestmír Kalina <ckalina@redhat.com> - 0-0.25.20230223giteedfcbf
- Update to eedfcbf
- Resolves: rhbz#2213162

* Wed Jun 10 2020 Cestmir Kalina <ckalina@redhat.com> - 0-0.10.20200515gitb52ac13
- Upload Source0
- Resolves RHBZ#1778928

* Tue Jun 09 2020 Cestmir Kalina <ckalina@redhat.com> - 0-0.9.20200515gitb52ac13
- Update to b52ac13 to include latest upstream changes
- Resolves RHBZ#1778928

* Wed Nov 21 2018 Jerome Marchand <jmarchan@redhat.com> - 0-0.8.20181112git6fbd644
- Update to 6fbd644 to fix RHBZ 1642806

* Mon Mar 12 2018 Zamir SUN <zsun@fedoraproject.org> - 0-0.7.20180308gitb8863d0
- Update to b8863d05565e91bd3fb40d9e9d562be081f09669
- Fixes RHBZ#1543803

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.20180130git545535a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Zamir SUN <zsun@fedoraproject.org> - 0-0.5-20180130git545535a
- Update to upstream 545535ab2d5ea093074f5df5723901756d22f298
- Fixes RHBZ#1538977

* Wed Jan 24 2018 Zamir SUN <zsun@fedoraproject.org> - 0-0.4.20171201gita6bced6
- Update do upstream a6bced6ef7b263380ac0309bdbd4a98c6f9055eb

* Wed Jan 24 2018 Zamir SUN <zsun@fedoraproject.org> - 0-0.3.20171018gite6af311
- Add libasan-devel per request

* Fri Oct 27 2017 Zamir SUN <zsun@fedoraproject.org> - 0-0.2.20171018gite6af311
- Update to upstream e6af311e3182417f86742a5b1a78e488593f975a

* Mon Oct 16 2017 Zamir SUN <zsun@fedoraproject.org> - 0-0.1.20171012git2ef3f81
- Initial package kabi-dw
