Name:		fio
Version:	3.7
Release:	1%{?dist}
Summary:	Multithreaded IO generation tool

Group:		Applications/System
License:	GPLv2
URL:		http://git.kernel.dk/?p=fio.git;a=summary
Source:		http://brick.kernel.dk/snaps/%{name}-%{version}.tar.bz2

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	libaio-devel
BuildRequires:	zlib-devel
%ifarch x86_64
BuildRequires:	libpmem-devel
BuildRequires:	libpmemblk-devel
%endif
BuildRequires:	librbd1-devel
%ifnarch %{arm} s390 s390x
BuildRequires:	numactl-devel
BuildRequires:	librdmacm-devel
%endif

%description
fio is an I/O tool that will spawn a number of threads or processes doing
a particular type of io action as specified by the user.  fio takes a
number of global parameters, each inherited by the thread unless
otherwise parameters given to them overriding that setting is given.
The typical use of fio is to write a job file matching the io load
one wants to simulate.

%prep
%setup -q

%build
./configure --disable-optimizations
EXTFLAGS="$RPM_OPT_FLAGS" make V=1 %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install prefix=%{_prefix} mandir=%{_mandir} DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README REPORTING-BUGS COPYING HOWTO examples
%doc MORAL-LICENSE GFIO-TODO SERVER-TODO STEADYSTATE-TODO
%dir %{_datadir}/%{name}
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/%{name}/*

%changelog
* Mon Feb 25 2019 Eric Sandeen <sandeen@redhat.com> 3.7-1
- New upstream version
- Adds libpmem ioengine (#1672362)

* Tue Oct 24 2017 Eric Sandeen <sandeen@redhat.com> 3.1-2
- Add new build deps for more features

* Wed Oct 18 2017 Eric Sandeen <sandeen@redhat.com> 3.1-1
- New upstream version

* Fri Aug 25 2017 Adam Williamson <awilliam@redhat.com> - 3.0-3
- Re-enable ceph deps on ppc64 (it's building again)
- Disable RDMA support on 32-bit ARM (#1484155)

* Thu Aug 17 2017 Eric Sandeen <sandeen@redhat.com> 3.0-2
- Include more files as doc (#1482372)

* Wed Aug 16 2017 Eric Sandeen <sandeen@redhat.com> 3.0-1
- New upstream version

* Mon Jul 31 2017 Eric Sandeen <sandeen@redhat.com> 2.99-3
- Exclude ceph-related deps on ppc64

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.99-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 10 2017 Eric Sandeen <sandeen@redhat.com> 2.99-1
- New upstream version

* Fri Jun 16 2017 Eric Sandeen <sandeen@redhat.com> 2.21-1
- New upstream version

* Wed Apr 05 2017 Eric Sandeen <sandeen@redhat.com> 2.19-2
- Enable dev-dax engine on x86_64

* Wed Apr 05 2017 Eric Sandeen <sandeen@redhat.com> 2.19-1
- New upstream version

* Thu Feb 23 2017 Eric Sandeen <sandeen@redhat.com> 2.18-1
- New upstream version

* Thu Feb 23 2017 Eric Sandeen <sandeen@redhat.com> 2.17-1
- New upstream version

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 20 2016 Eric Sandeen <sandeen@redhat.com> 2.16-1
- New upstream version

* Sat Nov 19 2016 Peter Robinson <pbrobinson@fedoraproject.org> 2.15-2
- Rebuild (Power64)

* Thu Oct 27 2016 Eric Sandeen <sandeen@redhat.com> 2.15-1
- New upstream version

* Tue Oct 04 2016 Eric Sandeen <sandeen@redhat.com> 2.14-1
- New upstream version

* Mon Aug 29 2016 Eric Sandeen <sandeen@redhat.com> 2.13-1
- New upstream version

* Wed Jun 15 2016 Eric Sandeen <sandeen@redhat.com> 2.12-1
- New upstream version

* Wed May 25 2016 Eric Sandeen <sandeen@redhat.com> 2.11-1
- New upstream version

* Fri Apr 29 2016 Eric Sandeen <sandeen@redhat.com> 2.9-1
- New upstream version

* Thu Mar 17 2016 Eric Sandeen <sandeen@redhat.com> 2.8-1
- New upstream version

* Fri Mar 11 2016 Eric Sandeen <sandeen@redhat.com> 2.7-1
- New upstream version

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 27 2016 Eric Sandeen <sandeen@redhat.com> 2.6-1
- New upstream version

* Thu Jan 14 2016 Eric Sandeen <sandeen@redhat.com> 2.3-1
- New upstream version

* Mon Dec 21 2015 Eric Sandeen <sandeen@redhat.com> 2.2.13-1
- New upstream version
- Add librdmacm-devel as build dependency (enable RDMA)

* Tue Nov 10 2015 Eric Sandeen <sandeen@redhat.com> 2.2.11-1
- New upstream version
- Add zlib-devel as build dependency

* Tue Sep 22 2015 Eric Sandeen <sandeen@redhat.com> 2.2.10-1
- New upstream version

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 07 2015 Eric Sandeen <sandeen@redhat.com> 2.2.8-1
- New upstream version

* Wed Apr 15 2015 Eric Sandeen <sandeen@redhat.com> 2.2.7-1
- New upstream version
- Add librbd ioengine support

* Fri Apr 10 2015 Eric Sandeen <sandeen@redhat.com> 2.2.6-1
- New upstream version

* Tue Feb 17 2015 Eric Sandeen <sandeen@redhat.com> 2.2.5-1
- New upstream version

* Mon Jan 05 2015 Eric Sandeen <sandeen@redhat.com> 2.2.4-1
- New upstream version

* Fri Jan 02 2015 Eric Sandeen <sandeen@redhat.com> 2.2.3-1
- New upstream version

* Wed Nov 12 2014 Eric Sandeen <sandeen@redhat.com> 2.1.14-1
- New upstream version

* Wed Sep 17 2014 Eric Sandeen <sandeen@redhat.com> 2.1.12-1
- New upstream version

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 15 2014 Eric Sandeen <sandeen@redhat.com> 2.1.11-1 
- New upstream version

* Mon Jun 16 2014 Eric Sandeen <sandeen@redhat.com> 2.1.10-1 
- New upstream version

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 13 2014 Eric Sandeen <sandeen@redhat.com> 2.1.9-1 
- New upstream version

* Mon Apr 14 2014 Eric Sandeen <sandeen@redhat.com> 2.1.8-1 
- New upstream version

* Mon Apr 07 2014 Eric Sandeen <sandeen@redhat.com> 2.1.7-1 
- New upstream version

* Wed Feb 12 2014 Eric Sandeen <sandeen@redhat.com> 2.1.5-1 
- New upstream version

* Wed Sep 25 2013 Eric Sandeen <sandeen@redhat.com> 2.1.3-1 
- New upstream version

* Thu Aug 08 2013 Eric Sandeen <sandeen@redhat.com> 2.1.2-1 
- New upstream version

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed May 15 2013 Eric Sandeen <sandeen@redhat.com> 2.1-1 
- New upstream version

* Wed Apr 17 2013 Eric Sandeen <sandeen@redhat.com> 2.0.15-1 
- New upstream version

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan  9 2013 Peter Robinson <pbrobinson@fedoraproject.org> 2.0.13-1
- New upstream 2.0.13 release

* Tue Jan 01 2013 Dan Horák <dan[at]danny.cz> - 2.0.12.2-2
- fix build on arches without ARCH_HAVE_CPU_CLOCK (arm, s390)

* Fri Dec 21 2012 Eric Sandeen <sandeen@redhat.com> 2.0.12.2-1 
- New upstream version

* Sat Nov 24 2012 Eric Sandeen <sandeen@redhat.com> 2.0.11-1 
- New upstream version

* Thu Nov 15 2012 Peter Robinson <pbrobinson@fedoraproject.org> 2.0.10-2
- Merge latest from F16 to master, bump release

* Fri Oct 12 2012 Eric Sandeen <sandeen@redhat.com> 2.0.10-1 
- New upstream version

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jul 13 2012 Eric Sandeen <sandeen@redhat.com> 2.0.8-1
- New upstream version

* Fri Mar 23 2012 Eric Sandeen <sandeen@redhat.com> 2.0.6-1
- New upstream version

* Tue Feb 28 2012 Eric Sandeen <sandeen@redhat.com> 2.0.5-1
- New upstream version

* Mon Jan 23 2012 Eric Sandeen <sandeen@redhat.com> 2.0.1-1
- New upstream version

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 08 2011 Eric Sandeen <sandeen@redhat.com> 2.0-1
- New upstream version

* Fri Nov 11 2011 Eric Sandeen <sandeen@redhat.com> 1.99.12-1
- New upstream version

* Tue Sep 27 2011 Eric Sandeen <sandeen@redhat.com> 1.58-1
- New upstream version

* Thu Aug 11 2011 Eric Sandeen <sandeen@redhat.com> 1.57-1
- New upstream version

* Tue May 31 2011 Eric Sandeen <sandeen@redhat.com> 1.55-1
- New upstream version

* Mon May 09 2011 Eric Sandeen <sandeen@redhat.com> 1.53-1
- New upstream version

* Fri Apr 29 2011 Eric Sandeen <sandeen@redhat.com> 1.52-1
- New upstream version

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.50.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 28 2011 Eric Sandeen <sandeen@redhat.com> 1.50.2-1
- New upstream version

* Wed Jan 26 2011 Eric Sandeen <sandeen@redhat.com> 1.50-1
- New upstream version

* Wed Dec 15 2010 Eric Sandeen <sandeen@redhat.com> 1.44.3-1
- New upstream version

* Fri Oct 22 2010 Eric Sandeen <sandeen@redhat.com> 1.44.1-1
- New upstream version

* Fri Oct 22 2010 Eric Sandeen <sandeen@redhat.com> 1.44-1
- New upstream version

* Thu Sep 23 2010 Eric Sandeen <sandeen@redhat.com> 1.43.2-1
- New upstream version

* Tue Jun 29 2010 Eric Sandeen <sandeen@redhat.com> 1.41.5-1
- New upstream version

* Tue Jun 22 2010 Eric Sandeen <sandeen@redhat.com> 1.41.3-1
- New upstream version

* Tue Jun 22 2010 Eric Sandeen <sandeen@redhat.com> 1.41-1
- New upstream version

* Fri Jun 18 2010 Eric Sandeen <sandeen@redhat.com> 1.40-1
- New upstream version

* Thu Jun 03 2010 Eric Sandeen <sandeen@redhat.com> 1.39-1
- New upstream version

* Tue Mar 23 2010 Eric Sandeen <sandeen@redhat.com> 1.38-1
- New upstream version

* Tue Feb 23 2010 Eric Sandeen <sandeen@redhat.com> 1.37-1
- New upstream version

* Tue Dec 15 2009 Eric Sandeen <sandeen@redhat.com> 1.36-1
- New upstream version

* Thu Nov 05 2009 Eric Sandeen <sandeen@redhat.com> 1.35-1
- New upstream version

* Mon Sep 14 2009 Eric Sandeen <sandeen@redhat.com> 1.34-1
- New upstream version

* Thu Sep 10 2009 Eric Sandeen <sandeen@redhat.com> 1.33.1-1
- New upstream version

* Tue Sep 08 2009 Eric Sandeen <sandeen@redhat.com> 1.33-1
- New upstream version

* Fri Jul 31 2009 Eric Sandeen <sandeen@redhat.com> 1.32-1
- New upstream version

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 11 2009 Eric Sandeen <sandeen@redhat.com> 1.31-1
- Much newer upstream version

* Fri Mar 06 2009 Eric Sandeen <sandeen@redhat.com> 1.24-1
- New upstream version

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Nov 20 2008 Eric Sandeen <sandeen@redhat.com> 1.23-1
- New upstream version, several bugs fixed.

* Mon Oct 13 2008 Eric Sandeen <sandeen@redhat.com> 1.22-1
- New upstream version, several bugs fixed.

* Thu Jun 19 2008 Eric Sandeen <sandeen@redhat.com> 1.21-1
- New upstream version
- Build verbosely and with RPM cflags

* Fri Apr 25 2008 Eric Sandeen <sandeen@redhat.com> 1.20-1
- New upstream version

* Thu Apr 10 2008 Eric Sandeen <sandeen@redhat.com> 1.19-1
- New upstream version

* Wed Feb 13 2008 Eric Sandeen <sandeen@redhat.com> 1.18-1
- Initial build
