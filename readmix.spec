Name:		readmix
Version:	2.0.0
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

BuildRequires:	R-devel

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
* Wed Apr 01 2015 Kozlov Konstantin <mackoel@gmail.com> - 2.0.0-0
- First release

