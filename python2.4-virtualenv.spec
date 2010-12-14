%define module	virtualenv
%define name	python2.4-%{module}
%define version	1.5.1

Name:		%{name}
Version:	%{version}
Release:	%mkrel 1
Summary:	Virtual Python Environment builder
Group:		Development/Python
License:	MIT
URL:		http://pypi.python.org/pypi/virtualenv
Source0:	http://pypi.python.org/packages/source/v/virtualenv/%{module}-%{version}.tar.gz
Patch0:		multiarch.patch
BuildArch:	noarch
BuildRequires:	python2.4-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}
%py_requires -d

%description
virtualenv is a tool to create isolated Python environments.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p0 -b .multiarch

%build
PYTHONDONTWRITEBYTECODE= python2.4 setup.py build

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= python2.4 setup.py install --root=%{buildroot} --record=FILE_LIST

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root,-)
%doc docs/*.txt
