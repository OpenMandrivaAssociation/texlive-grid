# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/grid
# catalog-date 2009-11-09 22:36:07 +0100
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-grid
Version:	1.0
Release:	10
Summary:	Grid typesetting in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/grid
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/grid.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/grid.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/grid.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package enables grid typesetting in double column
documents. Grid typesetting (vertical aligning of lines of text
in adjacent columns) is a difficult task in LaTeX, and the
present package is no more than an attempt to help users to
achieve it in a limited way. An example document, grid.tex, is
provided with simple instructions to typeset it using the
package. The package needs a lot of, this is only a
beginning...

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/grid/grid.sty
%doc %{_texmfdistdir}/doc/latex/grid/README
%doc %{_texmfdistdir}/doc/latex/grid/grid.pdf
%doc %{_texmfdistdir}/doc/latex/grid/grid.tex
%doc %{_texmfdistdir}/doc/latex/grid/manifest.txt
%doc %{_texmfdistdir}/doc/latex/grid/rvdtx.sty
#- source
%doc %{_texmfdistdir}/source/latex/grid/Makefile

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 752447
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 718585
- texlive-grid
- texlive-grid
- texlive-grid
- texlive-grid

