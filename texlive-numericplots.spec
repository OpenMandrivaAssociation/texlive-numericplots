# revision 23241
# category Package
# catalog-ctan /graphics/pstricks/contrib/numericplots
# catalog-date 2011-07-14 20:05:24 +0200
# catalog-license gpl3
# catalog-version 1.0
Name:		texlive-numericplots
Version:	1.0
Release:	3
Summary:	Plot numeric data (including Matlab export) using PSTricks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/numericplots
License:	GPL3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/numericplots.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/numericplots.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Plotting numeric data is a task which has often to be done for
scientific papers. LaTeX itself provides no facilities for
drawing more than the simplest plots from supplied data. The
package will process user input, and uses PSTricks to plot the
results. The package provides Matlab functions to transform
Matlab results to plottable data.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/numericplots/NumericPlots.sty
%doc %{_texmfdistdir}/doc/latex/numericplots/BasicFunctionality.tex
%doc %{_texmfdistdir}/doc/latex/numericplots/DataTestRealData.tex
%doc %{_texmfdistdir}/doc/latex/numericplots/FurtherExamples.tex
%doc %{_texmfdistdir}/doc/latex/numericplots/License.txt
%doc %{_texmfdistdir}/doc/latex/numericplots/MatlabSupport.tex
%doc %{_texmfdistdir}/doc/latex/numericplots/MultiplePlots.tex
%doc %{_texmfdistdir}/doc/latex/numericplots/NumericPlots.pdf
%doc %{_texmfdistdir}/doc/latex/numericplots/NumericPlotsDoc.tex
%doc %{_texmfdistdir}/doc/latex/numericplots/README.TEXLIVE
%doc %{_texmfdistdir}/doc/latex/numericplots/README.doc
%doc %{_texmfdistdir}/doc/latex/numericplots/Roll406_Ref2288.tex
%doc %{_texmfdistdir}/doc/latex/numericplots/TechnicalDetails.tex
%doc %{_texmfdistdir}/doc/latex/numericplots/TestPlots.tex
%doc %{_texmfdistdir}/doc/latex/numericplots/history.tex
%doc %{_texmfdistdir}/doc/latex/numericplots/keys_NumericDataPlot.tex
%doc %{_texmfdistdir}/doc/latex/numericplots/options.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 754448
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 719142
- texlive-numericplots
- texlive-numericplots
- texlive-numericplots
- texlive-numericplots

