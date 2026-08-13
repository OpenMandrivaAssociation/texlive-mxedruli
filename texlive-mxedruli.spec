%global tl_name mxedruli
%global tl_revision 79618
%global tl_version 3.3c

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	A pair of fonts for different Georgian alphabets
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/georgian/mxedruli
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mxedruli.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mxedruli.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
Two Georgian fonts, in both Metafont and Type 1 formats, which cover the
Mxedruli and the Xucuri alphabets.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from mxedruli:
Map mxedruli.map
TL_DROPIN_EOF
