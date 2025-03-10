Summary:	Context manager for mocking/wrapping stdin/stdout/stderr
Summary(pl.UTF-8):	Zarządca kontekstu do tworzenia atrap/opakowań stdin/stdout/stderr
Name:		python3-stdio_mgr
Version:	1.0.1
Release:	2
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/stdio-mgr/
Source0:	https://files.pythonhosted.org/packages/source/s/stdio-mgr/stdio-mgr-%{version}.tar.gz
# Source0-md5:	027b7e83918676ce44698883cab3d37c
URL:		https://pypi.org/project/stdio-mgr/
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Context manager for mocking/wrapping stdin/stdout/stderr.

%description -l pl.UTF-8
Zarządca kontekstu do tworzenia atrap/opakowań stdin/stdout/stderr.

%prep
%setup -q -n stdio-mgr-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE.txt README.rst
%{py3_sitescriptdir}/stdio_mgr
%{py3_sitescriptdir}/stdio_mgr-%{version}-py*.egg-info
