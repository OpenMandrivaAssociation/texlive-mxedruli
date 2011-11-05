# revision 15878
# category Package
# catalog-ctan /fonts/georgian/mxedruli
# catalog-date 2009-01-23 11:09:06 +0100
# catalog-license noinfo
# catalog-version 3.3c
Name:		texlive-mxedruli
Version:	3.3c
Release:	1
Summary:	A pair of Georgian fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/georgian/mxedruli
License:	NOINFO
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mxedruli.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mxedruli.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Two Georgian fonts, written in MetaFont, which cover the
Mxedruli and the Xucuri alphabets.

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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
