Summary:	Cloud image initramfs management utilities
Name:		cloud-initramfs-tools
Version:	0.20
Release:	1%{?dist}
License:	GPLv3
Group:		System Environment/Base
URL:		https://launchpad.net/ubuntu/saucy/+source/cloud-initramfs-tools/0.20ubuntu1/+files/cloud-initramfs-tools_0.20ubuntu1.tar.gz

Source0:	%{name}_%{version}ubuntu1.tar.gz

BuildArch:	noarch


%description
dracut-modules-growroot: Automatically resize the root partition on first boot


%package -n dracut-modules-growroot
Summary:	Automatically resize the root partition on first boot
Group:		System Environment/Base

Requires:	cloud-utils-growpart
Requires:	dracut
Requires:	util-linux


%description -n dracut-modules-growroot
This dracut module will re-write the partition table of a disk so that the
root partition has as much space as possible, bumping it up to the edge of the
disk, or the edge of the next partition.


%prep
%setup -q -n %{name}-%{version}ubuntu1


%build


%install

%if 0%{?fedora}
make install-fedora DESTDIR=$RPM_BUILD_ROOT/%{_prefix}/lib/
%else
%if 0%{?rhel}
make install-epel DESTDIR=$RPM_BUILD_ROOT/%{_prefix}/share/
%endif
%endif


%files -n dracut-modules-growroot
%doc COPYING README growroot/doc/example.txt
%if 0%{?fedora}
%dir %{_prefix}/lib/dracut/modules.d/50growroot
%{_prefix}/lib/dracut/modules.d/50growroot/growroot.sh
%{_prefix}/lib/dracut/modules.d/50growroot/module-setup.sh
%else
%if 0%{?rhel}
%dir %{_prefix}/share/dracut/modules.d/50growroot
%{_prefix}/share/dracut/modules.d/50growroot/growroot.sh
%{_prefix}/share/dracut/modules.d/50growroot/install
%endif
%endif


%changelog
* Fri Sep 13 2013 Juerg Haefliger <juergh@gmail.com> - 0.20-1
- Rebase to upstream version 0.20ubuntu1.

* Fri Sep 13 2013 Juerg Haefliger <juergh@gmail.com> - 0.20-0.6.bzr85
- [1003153] Mark the 50growroot directory as owned by the package.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-0.5.bzr85
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jun 17 2013 Juerg Haefliger <juergh@gmail.com> - 0.20-0.4.bzr85
- Require cloud-utils-growpart (instead of cloud-utils) which provides the
  growpart script now.

* Tue May  7 2013 Juerg Haefliger <juergh@gmail.com> - 0.20-0.3.bzr85
- Fix growroot.sh path for EPEL builds.

* Fri Mar  8 2013 Juerg Haefliger <juergh@gmail.com> - 0.20-0.2.bzr85
- Spec file fixes per reviewers comments.

* Wed Feb 27 2013 Juerg Haefliger <juergh@gmail.com> - 0.20-0.1.bzr85
- Initial build based on upstream revision bzr85.
