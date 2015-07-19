# revision 30021
# category Package
# catalog-ctan /fonts/georgian/mxedruli
# catalog-date 2013-04-18 13:20:04 +0200
# catalog-license lppl
# catalog-version 3.3c
Name:		texlive-mxedruli
Version:	3.3c
Release:	11
Summary:	A pair of fonts for different Georgian alphabets
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/georgian/mxedruli
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mxedruli.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mxedruli.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Two Georgian fonts, in both Metafont and Type 1 formats, which
cover the Mxedruli and the Xucuri alphabets.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/mxedruli/mxed10.afm
%{_texmfdistdir}/fonts/afm/public/mxedruli/mxedbf10.afm
%{_texmfdistdir}/fonts/afm/public/mxedruli/mxedc10.afm
%{_texmfdistdir}/fonts/afm/public/mxedruli/mxedi10.afm
%{_texmfdistdir}/fonts/afm/public/mxedruli/xuc10.afm
%{_texmfdistdir}/fonts/map/dvips/mxedruli/mxedruli.map
%{_texmfdistdir}/fonts/source/public/mxedruli/mxed.mf
%{_texmfdistdir}/fonts/source/public/mxedruli/mxed10.mf
%{_texmfdistdir}/fonts/source/public/mxedruli/mxedacc.mf
%{_texmfdistdir}/fonts/source/public/mxedruli/mxedbase.mf
%{_texmfdistdir}/fonts/source/public/mxedruli/mxedbf10.mf
%{_texmfdistdir}/fonts/source/public/mxedruli/mxedc10.mf
%{_texmfdistdir}/fonts/source/public/mxedruli/mxedcaps.mf
%{_texmfdistdir}/fonts/source/public/mxedruli/mxedd.mf
%{_texmfdistdir}/fonts/source/public/mxedruli/mxedfont.mf
%{_texmfdistdir}/fonts/source/public/mxedruli/mxedi10.mf
%{_texmfdistdir}/fonts/source/public/mxedruli/mxedp.mf
%{_texmfdistdir}/fonts/source/public/mxedruli/xuc.mf
%{_texmfdistdir}/fonts/source/public/mxedruli/xuc10.mf
%{_texmfdistdir}/fonts/source/public/mxedruli/xucbase.mf
%{_texmfdistdir}/fonts/source/public/mxedruli/xucd.mf
%{_texmfdistdir}/fonts/source/public/mxedruli/xucfont.mf
%{_texmfdistdir}/fonts/source/public/mxedruli/xucl.mf
%{_texmfdistdir}/fonts/source/public/mxedruli/xucp.mf
%{_texmfdistdir}/fonts/tfm/public/mxedruli/mxed10.tfm
%{_texmfdistdir}/fonts/tfm/public/mxedruli/mxedbf10.tfm
%{_texmfdistdir}/fonts/tfm/public/mxedruli/mxedc10.tfm
%{_texmfdistdir}/fonts/tfm/public/mxedruli/mxedi10.tfm
%{_texmfdistdir}/fonts/tfm/public/mxedruli/xuc10.tfm
%{_texmfdistdir}/fonts/type1/public/mxedruli/mxed10.pfb
%{_texmfdistdir}/fonts/type1/public/mxedruli/mxedbf10.pfb
%{_texmfdistdir}/fonts/type1/public/mxedruli/mxedc10.pfb
%{_texmfdistdir}/fonts/type1/public/mxedruli/mxedi10.pfb
%{_texmfdistdir}/fonts/type1/public/mxedruli/xuc10.pfb
%{_texmfdistdir}/tex/latex/mxedruli/mxedruli.sty
%{_texmfdistdir}/tex/latex/mxedruli/umxed.fd
%{_texmfdistdir}/tex/latex/mxedruli/uxuc.fd
%{_texmfdistdir}/tex/latex/mxedruli/xucuri.sty
%doc %{_texmfdistdir}/doc/fonts/mxedruli/README
%doc %{_texmfdistdir}/doc/fonts/mxedruli/alphabets.tex
%doc %{_texmfdistdir}/doc/fonts/mxedruli/mxeddoc.pdf
%doc %{_texmfdistdir}/doc/fonts/mxedruli/mxeddoc.tex
%doc %{_texmfdistdir}/doc/fonts/mxedruli/ossetic.tex
%doc %{_texmfdistdir}/doc/fonts/mxedruli/vepxis.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
