%global debug_package %{nil} 
Name:		readmix
Version:	2.2.0
Release:	0%{?dist}
Summary:	Geographic Population Structure Prediction Tool

Group:		Science
License:	Custom
URL:		https://bitbucket.org/mackoel/readmix
Source0:	https://bitbucket.org/mackoel/readmix/files/%{name}-%{version}.tar.gz
#BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

Requires:	R-core
Requires:	deepmethod

%description
Geographic Population Structure Prediction Tool used at http://chcb.saban-chla.usc.edu/.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc %{_docdir}
%{_bindir}/deep-admixture
%{_bindir}/deep-admixture-group
%{_bindir}/printscore-readmix-group
%{_bindir}/printscore-readmix-seq
%{_datadir}/readmix

%changelog
* Wed Jul 06 2016 Kozlov Konstantin <mackoel@gmail.com> - 2.2.0-0
- Next version adapted for deepmethod 2

* Wed Jul 06 2016 Kozlov Konstantin <mackoel@gmail.com> - 2.1.0-1
- Fix debuginfo for F23+

* Mon Aug 24 2015 Kozlov Konstantin <mackoel@gmail.com> - 2.1.0-0
- Fix filenames with brackets

* Wed Apr 01 2015 Kozlov Konstantin <mackoel@gmail.com> - 2.0.0-0
- First release

