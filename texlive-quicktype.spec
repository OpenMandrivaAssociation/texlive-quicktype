Name:		texlive-quicktype
Version:	42183
Release:	2
Summary:	LaTeX package for quick typesetting
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/quicktype
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/quicktype.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/quicktype.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Intended for the quick typesetting of basic documents using
LaTeX using shortcuts to existing commands and specific
commands for quick formatting and creation of tables and title
pages with a graphic image.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/quicktype
%doc %{_texmfdistdir}/doc/latex/quicktype

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
