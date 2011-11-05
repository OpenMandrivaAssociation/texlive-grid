# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/grid
# catalog-date 2009-11-09 22:36:07 +0100
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-grid
Version:	1.0
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package enables grid typesetting in double column
documents. Grid typesetting (vertical aligning of lines of text
in adjacent columns) is a difficult task in LaTeX, and the
present package is no more than an attempt to help users to
achieve it in a limited way. An example document, grid.tex, is
provided with simple instructions to typeset it using the
package. The package needs a lot of, this is only a
beginning...

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
