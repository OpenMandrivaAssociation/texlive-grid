%global tl_name grid
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Grid typesetting in LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/grid
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/grid.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/grid.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/grid.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package helps to enables grid typesetting in double column
documents. Grid typesetting (vertical aligning of lines of text in
adjacent columns) is a difficult task in LaTeX, and the present package
is no more than an attempt to help users to achieve it in a limited way.
An example document, grid.tex, is provided with simple instructions to
typeset it using the package. The package needs a lot more work: this is
only a beginning...

