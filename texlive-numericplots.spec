Name:		texlive-numericplots
Version:	31729
Release:	2
Summary:	Plot numeric data (including Matlab export) using PSTricks
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/numericplots
License:	GPL3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/numericplots.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/numericplots.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/numericplots/NumericPlots_TickLabels.tex
%{_texmfdistdir}/tex/latex/numericplots/NumericPlots_labels.tex
%{_texmfdistdir}/tex/latex/numericplots/NumericPlots_legend.tex
%{_texmfdistdir}/tex/latex/numericplots/NumericPlots_macros.tex
%{_texmfdistdir}/tex/latex/numericplots/NumericPlots_styles.tex
%doc %{_texmfdistdir}/doc/latex/numericplots/License.txt
%doc %{_texmfdistdir}/doc/latex/numericplots/NumericPlots.pdf
%doc %{_texmfdistdir}/doc/latex/numericplots/README
%doc %{_texmfdistdir}/doc/latex/numericplots/README.TEXLIVE
%doc %{_texmfdistdir}/doc/latex/numericplots/src/BasicFunctionality.tex
%doc %{_texmfdistdir}/doc/latex/numericplots/src/FurtherExamples.tex
%doc %{_texmfdistdir}/doc/latex/numericplots/src/MatlabSupport.tex
%doc %{_texmfdistdir}/doc/latex/numericplots/src/MultiplePlots.tex
%doc %{_texmfdistdir}/doc/latex/numericplots/src/NumericPlotsDoc.tex
%doc %{_texmfdistdir}/doc/latex/numericplots/src/Roll406_Ref2288.tex
%doc %{_texmfdistdir}/doc/latex/numericplots/src/TechnicalDetails.tex
%doc %{_texmfdistdir}/doc/latex/numericplots/src/TestPlots.tex
%doc %{_texmfdistdir}/doc/latex/numericplots/src/examples/BodeDiagramm.tex
%doc %{_texmfdistdir}/doc/latex/numericplots/src/examples/DataTestRealData.tex
%doc %{_texmfdistdir}/doc/latex/numericplots/src/examples/DefineData.tex
%doc %{_texmfdistdir}/doc/latex/numericplots/src/examples/LabelsNTickLabels.tex
%doc %{_texmfdistdir}/doc/latex/numericplots/src/examples/NyquistPlot.tex
%doc %{_texmfdistdir}/doc/latex/numericplots/src/examples/Sprungantwort_PT1Glied.tex
%doc %{_texmfdistdir}/doc/latex/numericplots/src/examples/basic_Boxes.tex
%doc %{_texmfdistdir}/doc/latex/numericplots/src/examples/basic_EasyPlot.tex
%doc %{_texmfdistdir}/doc/latex/numericplots/src/examples/basic_Grid.tex
%doc %{_texmfdistdir}/doc/latex/numericplots/src/examples/basic_Labels.tex
%doc %{_texmfdistdir}/doc/latex/numericplots/src/examples/basic_Legend.tex
%doc %{_texmfdistdir}/doc/latex/numericplots/src/examples/basic_LegendI.tex
%doc %{_texmfdistdir}/doc/latex/numericplots/src/examples/basic_LegendII.tex
%doc %{_texmfdistdir}/doc/latex/numericplots/src/examples/basic_LegendIII.tex
%doc %{_texmfdistdir}/doc/latex/numericplots/src/examples/basic_LineStyles.tex
%doc %{_texmfdistdir}/doc/latex/numericplots/src/examples/basic_Lines.tex
%doc %{_texmfdistdir}/doc/latex/numericplots/src/examples/basic_LogarithmicI.tex
%doc %{_texmfdistdir}/doc/latex/numericplots/src/examples/basic_LogarithmicII.tex
%doc %{_texmfdistdir}/doc/latex/numericplots/src/examples/basic_LogarithmicIII.tex
%doc %{_texmfdistdir}/doc/latex/numericplots/src/examples/basic_MultipleData.tex
%doc %{_texmfdistdir}/doc/latex/numericplots/src/examples/basic_Objects.tex
%doc %{_texmfdistdir}/doc/latex/numericplots/src/examples/basic_PlaceObjects.tex
%doc %{_texmfdistdir}/doc/latex/numericplots/src/examples/basic_PlaceObjectsII.tex
%doc %{_texmfdistdir}/doc/latex/numericplots/src/examples/basic_PlotWHoles.tex
%doc %{_texmfdistdir}/doc/latex/numericplots/src/examples/basic_UseRput.tex
%doc %{_texmfdistdir}/doc/latex/numericplots/src/examples/basic_UserLinestyles.tex
%doc %{_texmfdistdir}/doc/latex/numericplots/src/examples/data_BodeDiagrammLinearerTerm.tex
%doc %{_texmfdistdir}/doc/latex/numericplots/src/examples/data_Nyquist.tex
%doc %{_texmfdistdir}/doc/latex/numericplots/src/examples/data_SprungantwortPT1Glied.tex
%doc %{_texmfdistdir}/doc/latex/numericplots/src/examples/furtherEx_TickLabels.tex
%doc %{_texmfdistdir}/doc/latex/numericplots/src/examples/multiplots_exampleI.tex
%doc %{_texmfdistdir}/doc/latex/numericplots/src/examples/multiplots_exampleII.tex
%doc %{_texmfdistdir}/doc/latex/numericplots/src/examples/multiplots_exampleIII.tex
%doc %{_texmfdistdir}/doc/latex/numericplots/src/fig_NoiseData_ClosedLine.eps
%doc %{_texmfdistdir}/doc/latex/numericplots/src/fig_NoiseData_OpenLine.eps
%doc %{_texmfdistdir}/doc/latex/numericplots/src/history.tex
%doc %{_texmfdistdir}/doc/latex/numericplots/src/keys_NumericDataPlot.tex
%doc %{_texmfdistdir}/doc/latex/numericplots/src/options.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
