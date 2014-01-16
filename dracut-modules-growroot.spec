Summary:	Dracut module to automatically resize the root partition on first boot
Name:		dracut-modules-growroot
Version:	0.20
Release:	3%{?dist}
License:	GPLv3
Group:		System Environment/Base
Source0:	https://launchpad.net/ubuntu/saucy/+source/cloud-initramfs-tools/%{version}ubuntu1/+files/cloud-initramfs-tools_%{version}ubuntu1.tar.gz
Patch0:		0000-strip-p-from-rootdisk.patch
Patch1:		0001-run-in-pre-mount-stage.patch

Requires:	cloud-utils-growpart
Requires:	dracut
Requires:	grep
Requires:	util-linux

BuildArch:	noarch

%description
This dracut module will re-write the partition table of a disk so that the
root partition has as much space as possible, bumping it up to the edge of the
disk, or the edge of the next partition.


%prep
%setup -q -n cloud-initramfs-tools-%{version}ubuntu1
%patch0
%patch1


%build


%install

%if 0%{?fedora}
make install-fedora DESTDIR=$RPM_BUILD_ROOT/%{_prefix}/lib/
%else
%if 0%{?rhel}
make install-epel DESTDIR=$RPM_BUILD_ROOT/%{_prefix}/share/
%endif
%endif


%files
%doc COPYING README growroot/doc/example.txt
%if 0%{?fedora}
%dir %{_prefix}/lib/dracut/modules.d/50growroot
%{_prefix}/lib/dracut/modules.d/50growroot/growroot-dummy.sh
%{_prefix}/lib/dracut/modules.d/50growroot/growroot.sh
%{_prefix}/lib/dracut/modules.d/50growroot/module-setup.sh
%else
%if 0%{?rhel}
%dir %{_prefix}/share/dracut/modules.d/50growroot
%{_prefix}/share/dracut/modules.d/50growroot/growroot-dummy.sh
%{_prefix}/share/dracut/modules.d/50growroot/growroot.sh
%{_prefix}/share/dracut/modules.d/50growroot/install
%endif
%endif


%changelog
* Wed Jan 15 2014 Lars Kellogg-Stedman <lars@redhat.com> - 0.20-3
- initial import from Fedora package.

