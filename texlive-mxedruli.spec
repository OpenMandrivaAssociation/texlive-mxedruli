%global tl_name mxedruli
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.3c
Release:	%{tl_revision}.1
Summary:	A pair of fonts for different Georgian alphabets
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/georgian/mxedruli
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mxedruli.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mxedruli.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Two Georgian fonts, in both Metafont and Type 1 formats, which cover the
Mxedruli and the Xucuri alphabets.

