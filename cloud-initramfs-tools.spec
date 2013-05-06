Summary:	Cloud image initramfs management utilities
Name:		cloud-initramfs-tools
Version:	0.20
Release:	0.2.bzr85%{?dist}
License:	GPLv3
Group:		System Environment/Base
URL:		https://launchpad.net/cloud-initramfs-tools

# bzr export -r 85 cloud-initramfs-tools-0.20-bzr85.tar.gz lp:cloud-initramfs-tools
Source0:	%{name}-%{version}-bzr85.tar.gz

BuildArch:	noarch


%description
dracut-modules-growroot: Automatically resize the root partition on first boot


%package -n dracut-modules-growroot
Summary:	Automatically resize the root partition on first boot
Group:		System Environment/Base

Requires:	cloud-utils
Requires:	dracut
Requires:	util-linux


%description -n dracut-modules-growroot
This dracut module will re-write the partition table of a disk so that the
root partition has as much space as possible, bumping it up to the edge of the
disk, or the edge of the next partition.


%prep
%setup -q -n %{name}-%{version}-bzr85


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
%{_prefix}/lib/dracut/modules.d/50growroot/growroot.sh
%if 0%{?fedora}
%{_prefix}/lib/dracut/modules.d/50growroot/module-setup.sh
%else
%if 0%{?rhel}
%{_prefix}/share/dracut/modules.d/50growroot/install
%endif
%endif


%changelog
* Fri Mar  8 2013 Juerg Haefliger <juergh@gmail.com> - 0.20-0.2.bzr85
- Spec file fixes per reviewers comments.

* Wed Feb 27 2013 Juerg Haefliger <juergh@gmail.com> - 0.20-0.1.bzr85
- Initial build based on upstream revision bzr85.
