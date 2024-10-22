import os


def crear_carpeta_informe(libro):
    # Definimos el nombre de la carpeta y los archivos .tex y .bib
    carpeta = os.path.join("Universidad/Cuarto", libro)
    capitulos = os.path.join(carpeta, "Chapters")
    glosario = os.path.join(capitulos, "Glossary.tex")
    image = os.path.join(carpeta, "Images")
    compile = os.path.join(carpeta, "compileall.sh")
    main = os.path.join(carpeta, "main.tex")
    archivo_bib = os.path.join(carpeta, "main.bib")
    kao = os.path.join(carpeta, "kao.sty")
    kaobiblio = os.path.join(carpeta, "kaobiblio.sty")
    kaobook = os.path.join(carpeta, "kaobook.cls")
    kaorefs = os.path.join(carpeta, "kaorefs.sty")
    kaotheorems = os.path.join(carpeta, "kaotheorems.sty")

    # Creamos la carpeta y los archivos
    os.makedirs(carpeta, exist_ok=True)
    os.makedirs(capitulos, exist_ok=True)
    os.makedirs(image, exist_ok=True)

    contenido_tex = r"""
\documentclass[
	a4paper, 
	fontsize=10pt,
	twoside=true, 
	%open=any,
	%chapterentrydots=true, 
	numbers=noenddot, 
]{kaobook}

\ifxetexorluatex
	\usepackage{polyglossia}
	\setmainlanguage{spanish}
\else
	\usepackage[spanish]{babel} 
\fi
\usepackage[spanish]{csquotes}	


\usepackage{blindtext}
%\usepackage{showframe} % Uncomment to show boxes around the text area, margin, header and footer
%\usepackage{showlabels} % Uncomment to output the content of \label commands to the document where they are used

% Load the bibliography package
\usepackage{kaobiblio}
\addbibresource{main.bib} % Bibliography file

% Load mathematical packages for theorems and related environments
\usepackage[framed=true]{kaotheorems}

% Load the package for hyperreferences
\usepackage{kaorefs}

%%%%%%%%%%%%%%%%Paquetes%%%%%%%%%%%%%%%%%%%%%%%
\usepackage{witharrows}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\graphicspath{{../Images}{images/}} % Paths in which to look for images

\makeindex[columns=3, title=Alphabetical Index, intoc] % Make LaTeX produce the files required to compile the index

\makeglossaries % Make LaTeX produce the files required to compile the glossary
\input{Chapters/Glossary.tex} % Include the glossary definitions

\makenomenclature % Make LaTeX produce the files required to compile the nomenclature

% Reset sidenote counter at chapters
\counterwithin*{sidenote}{chapter}

\begin{document}

\titlehead{Apuntes de }
\subject{Asignatura}

\title[]{Título}
\subtitle{Customise this page according to your needs}

\author[]{}

\date{\today}

\publishers{An Awesome Publisher}

\frontmatter

\makeatletter
\uppertitleback{\@titlehead}

\makeatletter
\uppertitleback{\@titlehead} % Header

\lowertitleback{
  \textbf{Disclaimer}\\
  You can edit this page to suit your needs. For instance, here we have a no copyright statement, a colophon and some other information. This page is based on the corresponding page of Ken Arroyo Ohori's thesis, with minimal changes.

  \medskip

  \textbf{No copyright}\\
  \cczero\ This book is released into the public domain using the CC0 code. To the extent possible under law, I waive all copyright and related or neighbouring rights to this work.

  To view a copy of the CC0 code, visit: \\\url{http://creativecommons.org/publicdomain/zero/1.0/}

  \medskip

  \textbf{Colophon} \\
  This document was typeset with the help of \href{https://sourceforge.net/projects/koma-script/}{\KOMAScript} and \href{https://www.latex-project.org/}{\LaTeX} using the \href{https://github.com/fmarotta/kaobook/}{kaobook} class.

  The source code of this book is available at:\\\url{https://github.com/fmarotta/kaobook}

  (You are welcome to contribute!)

  \medskip

  \textbf{Publisher} \\
  First printed in May 2019 by \@publishers
}
\makeatother

\maketitle

\begingroup % Local scope for the following commands

% Define the style for the TOC, LOF, and LOT
%\setstretch{1} % Uncomment to modify line spacing in the ToC
%\hypersetup{linkcolor=blue} % Uncomment to set the colour of links in the ToC
\setlength{\textheight}{230\hscale} % Manually adjust the height of the ToC pages

% Turn on compatibility mode for the etoc package
\etocstandarddisplaystyle % "toc display" as if etoc was not loaded
\etocstandardlines % "toc lines" as if etoc was not loaded

\tableofcontents % Output the table of contents

\listoffigures % Output the list of figures

% Comment both of the following lines to have the LOF and the LOT on different pages
\let\cleardoublepage\bigskip
\let\clearpage\bigskip

\listoftables % Output the list of tables

\endgroup

%----------------------------------------------------------------------------------------
%	MAIN BODY
%----------------------------------------------------------------------------------------

\mainmatter % Denotes the start of the main document content, resets page numbering and uses arabic numbers
\setchapterstyle{kao} % Choose the default chapter heading style



\pagelayout{wide}

\addpart{Class Options, Commands and Environments}

\pagelayout{margin}

\end{document}
"""

    contenido_bib = r"""
    @article{sample,
    title={Sample Title},
    author={Sample Author},
    journal={Sample Journal},
    year={2023},
    }
"""

    contenido_glosar = r"""
    
    \newglossaryentry{computer}{
      name=computer,
      description={is a programmable machine that receives input, stores and manipulates data, and provides output in a useful format}
    }

    % Glossary entries (used in text with e.g. \acrfull{fpsLabel} or \acrshort{fpsLabel})
    \newacronym[longplural={Frames per Second}]{fpsLabel}{FPS}{Frame per Second}
"""
    contenido_compile = r"""
    
    #!/bin/bash

# Compile document
pdflatex -interaction=nonstopmode main

# Compile nomenclature
makeindex main.nlo -s nomencl.ist -o main.nls

# Compile index
makeindex main

# Compile bibliography
biber main

# Compile document
pdflatex main

# Compile glossary
makeglossaries main

# Compile document
pdflatex main
"""

    contenido_kao = r"""
    
\ProvidesPackage{kao}

%----------------------------------------------------------------------------------------
%	USEFUL PACKAGES AND COMMANDS
%----------------------------------------------------------------------------------------

\RequirePackage{etoolbox} % Easy programming to modify TeX stuff
\RequirePackage{calc} % Make calculations
\RequirePackage[usenames,dvipsnames,table]{xcolor} % Colours
\RequirePackage{iftex} % Check wether XeTeX is being used
\RequirePackage{xifthen} % Easy conditionals
\RequirePackage{options} % Manage class options
\RequirePackage{xparse} % Parse arguments for macros
\RequirePackage{xpatch} % Patch LaTeX code in external packages
\RequirePackage{xstring} % Parse strings
\RequirePackage{afterpage} % Run commands after specific pages
\RequirePackage{imakeidx} % For the index; must be loaded before the 'caption' and 'hyperref' packages
\RequirePackage{varioref} % For the cross-references; must be loaded before the 'hyperref' and 'cleveref' packages

% Define \Ifthispageodd (with a capital 'i') to make kaobook compatible with older KOMAScript versions
\@ifpackagelater{scrbase}{2019/12/22}{%
}{%
    \let\Ifthispageodd\ifthispageodd%
}

%----------------------------------------------------------------------------------------
%	TITLE AND AUTHOR MACROS
%----------------------------------------------------------------------------------------

% Provide an optional argument to the \title command in which to store a plain text title, without any formatting
% Usage: \title[Plain Title]{Actual Title}
\newcommand{\@plaintitle}{}
\renewcommand{\title}[2][]{%
	\gdef\@title{#2} % Store the full title in @title
	\ifthenelse{\isempty{#1}}{ % If there is no plain title
		\renewcommand{\@plaintitle}{\@title} % Use full title
	}{ % If there is a plain title
		\renewcommand{\@plaintitle}{#1} % Use provided plain-text title
	}%
	\hypersetup{pdftitle={\@plaintitle}} % Set the PDF metadata title
}

% Provide an optional argument to the \author command in which to store a plain text author, without any formatting
% Usage: \author[Plain Author]{Actual Author}
\newcommand{\@plainauthor}{}
\renewcommand{\author}[2][]{%
	\gdef\@author{#2} % Store the full author in @author
	\ifthenelse{\isempty{#1}}{ % If there is no plain author
		\renewcommand{\@plainauthor}{\@author}% Use full author
  	}{ % If there is a plain author
		\renewcommand{\@plainauthor}{#1}% Use provided plain-text author
	}%
	\hypersetup{pdfauthor={\@plainauthor}} % Set the PDF metadata author
}

% Make a bookmark to the title page
\pretocmd{\maketitle}{\pdfbookmark[1]{\@plaintitle}{title}}{}{}%

%----------------------------------------------------------------------------------------
%	PAGE LAYOUT
%----------------------------------------------------------------------------------------

% Define lengths to set the scale of the document. Changing these 
% lengths should affect all the other pagesize-dependent elements in the 
% layout, such as the geometry of the page, the spacing between 
% paragraphs, and so on. (As of now, not all the elements rely on hscale 
% and vscale; future work will address this shortcoming.)
\newlength{\hscale}
\newlength{\vscale}

% By default, the scales are set to work for a4paper
\setlength{\hscale}{1mm}
\setlength{\vscale}{1mm}

\@ifclasswith{\@baseclass}{a0paper}{\setlength{\hscale}{4mm}\setlength{\vscale}{4mm}}{}
\@ifclasswith{\@baseclass}{a1paper}{\setlength{\hscale}{2.828mm}\setlength{\vscale}{2.828mm}}{}
\@ifclasswith{\@baseclass}{a2paper}{\setlength{\hscale}{2mm}\setlength{\vscale}{2mm}}{}
\@ifclasswith{\@baseclass}{a3paper}{\setlength{\hscale}{1.414mm}\setlength{\vscale}{1.414mm}}{}
\@ifclasswith{\@baseclass}{a4paper}{\setlength{\hscale}{1mm}\setlength{\vscale}{1mm}}{}
\@ifclasswith{\@baseclass}{a5paper}{\setlength{\hscale}{0.704mm}\setlength{\vscale}{0.704mm}}{}
\@ifclasswith{\@baseclass}{a6paper}{\setlength{\hscale}{0.5mm}\setlength{\vscale}{0.5mm}}{}
\@ifclasswith{\@baseclass}{b0paper}{\setlength{\hscale}{4.761mm}\setlength{\vscale}{4.761mm}}{}
\@ifclasswith{\@baseclass}{b1paper}{\setlength{\hscale}{3.367mm}\setlength{\vscale}{3.367mm}}{}
\@ifclasswith{\@baseclass}{b2paper}{\setlength{\hscale}{2.380mm}\setlength{\vscale}{2.380mm}}{}
\@ifclasswith{\@baseclass}{b3paper}{\setlength{\hscale}{1.681mm}\setlength{\vscale}{1.681mm}}{}
\@ifclasswith{\@baseclass}{b4paper}{\setlength{\hscale}{1.190mm}\setlength{\vscale}{1.190mm}}{}
\@ifclasswith{\@baseclass}{b5paper}{\setlength{\hscale}{0.837mm}\setlength{\vscale}{0.837mm}}{}
\@ifclasswith{\@baseclass}{b6paper}{\setlength{\hscale}{0.570mm}\setlength{\vscale}{0.570mm}}{}
\@ifclasswith{\@baseclass}{c0paper}{\setlength{\hscale}{4.367mm}\setlength{\vscale}{4.367mm}}{}
\@ifclasswith{\@baseclass}{c1paper}{\setlength{\hscale}{3.085mm}\setlength{\vscale}{3.085mm}}{}
\@ifclasswith{\@baseclass}{c2paper}{\setlength{\hscale}{2.180mm}\setlength{\vscale}{2.180mm}}{}
\@ifclasswith{\@baseclass}{c3paper}{\setlength{\hscale}{1.542mm}\setlength{\vscale}{1.542mm}}{}
\@ifclasswith{\@baseclass}{c4paper}{\setlength{\hscale}{1.090mm}\setlength{\vscale}{1.090mm}}{}
\@ifclasswith{\@baseclass}{c5paper}{\setlength{\hscale}{0.771mm}\setlength{\vscale}{0.771mm}}{}
\@ifclasswith{\@baseclass}{c6paper}{\setlength{\hscale}{0.542mm}\setlength{\vscale}{0.542mm}}{}
\@ifclasswith{\@baseclass}{b0j}{\setlength{\hscale}{4.904mm}\setlength{\vscale}{4.904mm}}{}
\@ifclasswith{\@baseclass}{b1j}{\setlength{\hscale}{3.467mm}\setlength{\vscale}{3.467mm}}{}
\@ifclasswith{\@baseclass}{b2j}{\setlength{\hscale}{2.452mm}\setlength{\vscale}{2.452mm}}{}
\@ifclasswith{\@baseclass}{b3j}{\setlength{\hscale}{1.733mm}\setlength{\vscale}{1.733mm}}{}
\@ifclasswith{\@baseclass}{b4j}{\setlength{\hscale}{1.226mm}\setlength{\vscale}{1.226mm}}{}
\@ifclasswith{\@baseclass}{b5j}{\setlength{\hscale}{0.867mm}\setlength{\vscale}{0.867mm}}{}
\@ifclasswith{\@baseclass}{b6j}{\setlength{\hscale}{0.613mm}\setlength{\vscale}{0.613mm}}{}
\@ifclasswith{\@baseclass}{ansiapaper}{\setlength{\hscale}{1.028mm}\setlength{\vscale}{0.939mm}}{}
\@ifclasswith{\@baseclass}{ansibpaper}{\setlength{\hscale}{1.328mm}\setlength{\vscale}{1.454mm}}{}
\@ifclasswith{\@baseclass}{ansicpaper}{\setlength{\hscale}{2.057mm}\setlength{\vscale}{1.882mm}}{}
\@ifclasswith{\@baseclass}{ansidpaper}{\setlength{\hscale}{2.662mm}\setlength{\vscale}{2.909mm}}{}
\@ifclasswith{\@baseclass}{ansiepaper}{\setlength{\hscale}{4.114mm}\setlength{\vscale}{3.764mm}}{}
\@ifclasswith{\@baseclass}{letterpaper}{\setlength{\hscale}{1.028mm}\setlength{\vscale}{0.939mm}}{}
\@ifclasswith{\@baseclass}{executivepaper}{\setlength{\hscale}{0.876mm}\setlength{\vscale}{0.898mm}}{}
\@ifclasswith{\@baseclass}{legalpaper}{\setlength{\hscale}{1.028mm}\setlength{\vscale}{1.198mm}}{}
\@ifclasswith{\@baseclass}{smallpocketpaper}{\setlength{\hscale}{0.571mm}\setlength{\vscale}{0.639mm}}{}
\@ifclasswith{\@baseclass}{pocketpaper}{\setlength{\hscale}{0.642mm}\setlength{\vscale}{0.723mm}}{}
\@ifclasswith{\@baseclass}{juvenilepaper}{\setlength{\hscale}{0.738mm}\setlength{\vscale}{0.740mm}}{}
\@ifclasswith{\@baseclass}{smallphotopaper}{\setlength{\hscale}{0.809mm}\setlength{\vscale}{0.572mm}}{}
\@ifclasswith{\@baseclass}{photopaper}{\setlength{\hscale}{1.00mm}\setlength{\vscale}{0.707mm}}{}
\@ifclasswith{\@baseclass}{appendixpaper}{\setlength{\hscale}{1.000mm}\setlength{\vscale}{0.505mm}}{}
\@ifclasswith{\@baseclass}{cookpaper}{\setlength{\hscale}{0.809mm}\setlength{\vscale}{0.740mm}}{}
\@ifclasswith{\@baseclass}{illustratedpaper}{\setlength{\hscale}{0.905mm}\setlength{\vscale}{0.909mm}}{}
\@ifclasswith{\@baseclass}{f24paper}{\setlength{\hscale}{0.762mm}\setlength{\vscale}{0.808mm}}{}
\@ifclasswith{\@baseclass}{a4paperlandscape}{\setlength{\hscale}{1.414mm}\setlength{\vscale}{0.707mm}}{}

% Set the default page layout
\RequirePackage[
	paperwidth=210\hscale,
	paperheight=297\vscale,
]{geometry}

% Command to choose among the three possible layouts
\DeclareDocumentCommand{\pagelayout}{m}{%
	\ifthenelse{\equal{margin}{#1}}{\marginlayout\marginfloatsetup}{}%
	\ifthenelse{\equal{wide}{#1}}{\widelayout\widefloatsetup}{}%
	\ifthenelse{\equal{fullwidth}{#1}}{\fullwidthlayout\widefloatsetup}{}%
}

% Layout #1: large margins
\newcommand{\marginlayout}{%
	\newgeometry{
		top=27.4\vscale,
		bottom=27.4\vscale,
		inner=24.8\hscale,
		textwidth=107\hscale,
        marginparsep=6.2\hscale,
		marginparwidth=47.7\hscale,
    }%
    \recalchead%
}

% Layout #2: small, symmetric margins
\newcommand{\widelayout}{%
	\newgeometry{
		top=27.4\vscale,
		bottom=27.4\vscale,
		inner=24.8\hscale,
		outer=24.8\hscale,
		marginparsep=0mm,
		marginparwidth=0mm,
	}%
    \recalchead%
}

% Layout #3: no margins and no space above or below the body
\newcommand{\fullwidthpage}{%
	\newgeometry{
		top=0mm,
		bottom=0mm,
		inner=0mm,
		outer=0mm,
		marginparwidth=0mm,
		marginparsep=0mm,
	}%
    \recalchead%
}

% Set the default page layout
\AtBeginDocument{\pagelayout{margin}}

%----------------------------------------------------------------------------------------
%	HEADERS AND FOOTERS
%----------------------------------------------------------------------------------------

\RequirePackage{scrlayer-scrpage}		% Customise head and foot regions

% Set the header height to prevent a warning
%\setlength{\headheight}{27.4\vscale}
% Increase the space between header and text
\setlength{\headsep}{11\vscale}

% Define some LaTeX lengths used in the page headers
\newlength{\headtextwidth}
\newlength{\headmarginparsep}
\newlength{\headmarginparwidth}
\newlength{\headtotal} % This is the total width of the header
\newcommand{\recalchead}{%
    \setlength{\headtextwidth}{\textwidth}%
	\setlength{\headmarginparsep}{\marginparsep}%
	\setlength{\headmarginparwidth}{\marginparwidth}%
	\setlength{\headtotal}{\headtextwidth+\headmarginparsep+\headmarginparwidth}%
}

\AtBeginDocument{% Recalculate the header-related lengths
    \recalchead%
}

% Style with chapter number, chapter title, and page in the header (used throughout the document)
\renewpagestyle{scrheadings}{%
    {\smash{\hspace{-\headmarginparwidth}\hspace{-\headmarginparsep}\makebox[\headtotal][l]{%
        \makebox[7\hscale][r]{\thepage}%
		\makebox[3\hscale]{}\rule[-1mm]{0.5pt}{19\vscale-1mm}\makebox[3\hscale]{}%
		\makebox[\headtextwidth][l]{\leftmark}}}}%
	{\smash{\makebox[0pt][l]{\makebox[\headtotal][r]{%
		\makebox[\headtextwidth][r]{\hfill\rightmark}%
		\makebox[3\hscale]{}\rule[-1mm]{0.5pt}{19\vscale-1mm}\makebox[3\hscale]{}%
		\makebox[7\hscale][l]{\thepage}}}}}%
	{\smash{\makebox[0pt][l]{\makebox[\headtotal][r]{%
		\makebox[\headtextwidth][r]{\hfill\rightmark}%
		\makebox[3\hscale]{}\rule[-1mm]{0.5pt}{19\vscale-1mm}\makebox[3\hscale]{}%
		\makebox[7\hscale][l]{\thepage}}}}}%
}{%
    {}%
	{}%
	{}%
}

% Style with neither header nor footer (used for special pages)
\renewpagestyle{plain.scrheadings}{%
	{}%
	{}%
	{}%
}{%
	{}%
	{}%
	{}%
}

% Style with an empty header and the page number in the footer
\newpagestyle{pagenum.scrheadings}{%
    {}%
    {}%
    {}%
}{%
    {\makebox[\textwidth][r]{\thepage}}%
    {\makebox[\textwidth][l]{\thepage}}%
    {\makebox[\textwidth][l]{\thepage}}%
}

% Style with an empty header and the page number in the footer
\newpagestyle{centeredpagenum.scrheadings}{%
    {}%
    {}%
    {}%
}{%
    {\hspace{-\headmarginparwidth}\hspace{-\headmarginparsep}\makebox[\headtotal][l]{\hfill\thepage\hfill}}
    {\makebox[0pt][l]{\makebox[\headtotal][r]{\hfill\thepage\hfill}}}%
    {\makebox[0pt][l]{\makebox[\headtotal][r]{\hfill\thepage\hfill}}}%
}

% Command to print a blank page
\newcommand\blankpage{%
	\null%
	\thispagestyle{empty}%
	\newpage%
}

% Set the default page style
\pagestyle{plain.scrheadings}

%----------------------------------------------------------------------------------------
%	PARAGRAPH FORMATTING
%----------------------------------------------------------------------------------------

\RequirePackage{ragged2e} % Required to achieve better ragged paragraphs
\RequirePackage{setspace} % Required to easily set the space between lines
\RequirePackage{hyphenat} % Hyphenation for special fonts
\RequirePackage{microtype} % Improves character and word spacing
\RequirePackage{needspace} % Required to prevent page break right after a sectioning command
\RequirePackage{xspace} % Better print trailing whitespace

% TODO: recognize space/indent justified/raggedright class options

% Settings for a normal paragraph
\newcommand{\@body@par}{%
	\justifying% Justify text
	\singlespacing% Set the interline space to a single line
	\frenchspacing% No additional space after periods
	\normalfont% Use the default font
	\normalsize% Use the default size
}

% Settings for paragraphs in the margins
\newcommand{\@margin@par}{%
	\justifying% justify text
	\setlength{\RaggedRightParindent}{0em}% Suppress indentation
	\setlength{\parindent}{0em}% Suppress indentation
	\setlength{\parskip}{0.5pc}% Set the space between paragraphs
	%\singlespacing% Set the space between lines
	\frenchspacing% No additional space after periods
	\normalfont% Use the default font
	\footnotesize% Use a smaller size
}

% By default, use @body@par settings
\@body@par

%----------------------------------------------------------------------------------------
%	WIDE PARAGRAPHS
%----------------------------------------------------------------------------------------

% Environment for a wide paragraph
\NewDocumentEnvironment{widepar}{}{%
  \if@twoside%
	\Ifthispageodd{%
	  \begin{addmargin}[0cm]{-\marginparwidth-\marginparsep}%
	}{%
	  \begin{addmargin}[-\marginparwidth-\marginparsep]{0cm}%
	}%
  \else%
	\begin{addmargin}[0cm]{-\marginparwidth-\marginparsep}%
  \fi%
}{%
	\end{addmargin}%
}

% Environment for a full width paragraph
\NewDocumentEnvironment{fullwidthpar}{}{%
  \if@twoside%
    \Ifthispageodd{%
      \begin{addmargin}[-1in-\hoffset-\oddsidemargin]{-\paperwidth+1in+\hoffset+\oddsidemargin+\textwidth}%
    }{%
      \begin{addmargin}[-\paperwidth+1in+\hoffset+\oddsidemargin+\textwidth]{-\paperwidth+1in+\hoffset+\oddsidemargin+\marginparsep+\marginparwidth+\textwidth}%
    }%
  \else%
    \begin{addmargin}[-1in-\hoffset-\oddsidemargin]{-\paperwidth+1in+\hoffset+\oddsidemargin+\textwidth}%
  \fi% 
}{%
    \end{addmargin}%
}

% Environment for a wide equation
\NewDocumentEnvironment{wideequation}{}{%
  \begin{widepar}%
	\begin{equation}%
}{%
	\end{equation}%
  \end{widepar}%
}

%----------------------------------------------------------------------------------------
%	FOOTNOTES, MARGINNOTES AND SIDENOTES
%----------------------------------------------------------------------------------------

\RequirePackage[section]{placeins} % Prevent floats to cross sections
\extrafloats{100} % Require more floats

\RequirePackage{marginnote} % Provides options for margin notes
\RequirePackage{marginfix} % Make marginpars float freely
\RequirePackage{sidenotes} % Use sidenotes
\RequirePackage{chngcntr} % Reset counters at sections

% TODO: see also page 440 of the KOMA-script guide
\RequirePackage[
	bottom,
	symbol*,
	hang,
	flushmargin,
	% perpage,
	stable,
]{footmisc} % Required to set up the footnotes
\RequirePackage{footnotebackref} % Creates back references from footnotes to text

% Fix the color of the footnote marker when back-referenced
\patchcmd{\footref}{\ref}{\hypersetup{colorlinks=black}\ref}{}{}%
% Workaround to fix back references
\edef\BackrefFootnoteTag{bhfn:\theBackrefHyperFootnoteCounter}%

% FIXME: I am not able to choose the paragraph layout of footnotes, probably the footnotes package conflicts with scrbook.
%\renewcommand{\footnotelayout}{\@margin@par}

%----------------------------------------------------------------------------------------

% Justify and format margin notes
\renewcommand*{\raggedleftmarginnote}{} % Suppress left margin
\renewcommand*{\raggedrightmarginnote}{} % Suppress right margin
\renewcommand*{\marginfont}{\@margin@par} % Format marginnotes according to \@marginpar (see above)
\renewcommand{\marginnotevadjust}{0.8\vscale} % Bring all marginnotes downwards a bit
\marginposadjustment=0.1mm % Bring downwards also the marginpars
\marginheightadjustment=.5cm % Bring downwards also the marginpars
%\RequirePackage[marginnote=true]{snotez} % Provides options for sidenotes

% Copied from snotez's \sidenote
\def\kao@if@nblskip#1{%
	\expandafter\ifx\@car#1\@nil*%
		\expandafter\@firstoftwo%
	\else%
		\expandafter\@secondoftwo%
	\fi%
}

% Command to detect whether we are inside an mdframed environment
\newif\ifinfloat
\AtBeginEnvironment{mdframed}{\infloattrue}
\AtBeginEnvironment{minipage}{\infloattrue}

\def\IfInFloatingEnvir{%
    \ifinfloat%
        \expandafter\@firstoftwo%
    \else%
        \expandafter\@secondoftwo%
    \fi%
}


% Redefine the command to print marginnotes:
% (a) the optional offset argument goes at the first position
% (b) the offset can also be a multiple of baselineskip, like for snotez's \sidenote
% Usage: \marginnote[<offset>]{Text of the note.}
\let\oldmarginnote\marginnote%
\RenewDocumentCommand\marginnote{ o m }{%
	\IfNoValueOrEmptyTF{#1}{%
		\IfInFloatingEnvir{%
			\oldmarginnote{#2}%
		}{%
            \marginpar{\@margin@par#2}%
        }%
	}{%
		\oldmarginnote{#2}[\kao@if@nblskip{#1}{\@cdr#1\@nil\baselineskip}{#1}]%
	}%
}

% Initially set the counter to zero instead of 1, and update it before printing the sidenote.
\setcounter{sidenote}{0}%
\RenewDocumentCommand\sidenote{ o o +m }{%
	\IfNoValueOrEmptyTF{#1}{%
		\refstepcounter{sidenote}% This command has been moved here
	}{%
	}%
	\sidenotemark[#1]%
	\sidenotetext[#1][#2]{#3}%
	\@sidenotes@multimarker%
}

% % Formatting sidenotes
% \setsidenotes{
% 	text-mark-format=\textsuperscript{\normalfont#1}, % Use a superscript for the marker in the text
% 	note-mark-format=#1:, % Use a normal font for the marker in the margin; use a colon after the sidenote number
% 	note-mark-sep=\enskip, % Set the space after the marker
% }

% Formatting sidenotes
\RenewDocumentCommand\@sidenotes@thesidenotemark{ m }{%
	\leavevmode%
	\ifhmode%
		\edef\@x@sf{\the\spacefactor}%
		\nobreak%
	\fi%
	\hbox{\@textsuperscript{\normalfont#1}}%
	\ifhmode%
		\spacefactor\@x@sf%
	\fi%
	\relax%
}%

\RenewDocumentCommand\sidenotetext{ o o +m }{% number, offset, text
	\IfNoValueOrEmptyTF{#1}{%
        \marginnote[#2]{\thesidenote:\enskip#3}%
    }{%
        \marginnote[#2]{#1:\enskip#3}%
    }%
}

%----------------------------------------------------------------------------------------
%	FIGURES, TABLES, LISTINGS AND CAPTIONS
%----------------------------------------------------------------------------------------

\RequirePackage{graphicx} % Include figures
\setkeys{Gin}{width=\linewidth,totalheight=\textheight,keepaspectratio} % Improves figure scaling
\RequirePackage{tikz} % Allows to draw custom shapes
\RequirePackage{tikzpagenodes} % Allows to anchor tikz nodes to page elements
\RequirePackage{booktabs} % Nicer tables
\RequirePackage{multirow} % Cells occupying multiple rows in tables
\RequirePackage{multicol} % Multiple columns in dictionary
\RequirePackage{rotating} % Allows tables and figures to be rotated
\RequirePackage{listings} % Print code listings
%\RequirePackage{minted}
\RequirePackage[hypcap=true]{caption} % Correctly placed anchors for hyperlinks
% \RequirePackage{atbegshi}
% \RequirePackage{perpage}
\let\c@abspage\relax
% \newcommand{\pp@g@sidenote}{}
\RequirePackage{floatrow} % Set up captions of floats
%\RequirePackage{dblfloatfix} % Better positioning of wide figures and tables
\AtEndPreamble{\RequirePackage{scrhack}} % Make packages compatible with KOMA Script (must be loaded last: https://tex.stackexchange.com/questions/156240/latex-packages-minted-and-scrhack)

% Improve the figure placing (see https://www.overleaf.com/learn/latex/Tips)
\def\topfraction{.9}%
\def\textfraction{0.35}%
\def\floatpagefraction{0.8}%

% Set the space between floats and main text
\renewcommand\FBaskip{.4\topskip}%
\renewcommand\FBbskip{\FBaskip}%

% Tighten up space between displays (e.g., equations) and make symmetric (from tufte-latex)
\setlength\abovedisplayskip{6pt plus 2pt minus 4pt}%
\setlength\belowdisplayskip{6pt plus 2pt minus 4pt}%
\abovedisplayskip 10\p@ \@plus2\p@ \@minus5\p@%
\abovedisplayshortskip \z@ \@plus3\p@%
\belowdisplayskip \abovedisplayskip%
\belowdisplayshortskip 6\p@ \@plus3\p@ \@minus3\p@%

\setlength\columnseprule{.4pt} % Set the width of vertical rules in tables

\newlength{\kaomarginskipabove} % Specify the space above a marginfigure, margintable or marginlisting
\newlength{\kaomarginskipbelow} % Specify the space below a marginfigure, margintable or marginlisting
\setlength{\kaomarginskipabove}{3mm plus 2pt minus 2pt}
\setlength{\kaomarginskipbelow}{3mm plus 2pt minus 2pt}

% Environment to hold a margin figure (from the sidenotes package)
% We redefine it here because we want to use our own caption formatting.
\RenewDocumentEnvironment{marginfigure}{o}{%
  \FloatBarrier%
  \marginskip{\kaomarginskipabove}%
  \begin{lrbox}{\@sidenotes@marginfigurebox}%
	\begin{minipage}{\marginparwidth}%
	  \captionsetup{type=figure}%
}{%
    \end{minipage}%
  \end{lrbox}%
  \marginnote[#1]{\usebox{\@sidenotes@marginfigurebox}}%
  \marginskip{\kaomarginskipbelow}%
}

% Environment to hold a margin table (from the sidenotes package)
\RenewDocumentEnvironment{margintable}{o}{%
  \FloatBarrier%
  \marginskip{\kaomarginskipabove}%
  \begin{lrbox}{\@sidenotes@margintablebox}%
	\begin{minipage}{\marginparwidth}%
	  \captionsetup{type=table}%
}{%
    \end{minipage}%
  \end{lrbox}%
  \marginnote[#1]{\usebox{\@sidenotes@margintablebox}}%
  \marginskip{\kaomarginskipbelow}%
}

% Environment to hold a margin listing
\newsavebox{\@sidenotes@marginlistingbox}%
\NewDocumentEnvironment{marginlisting}{o}{% The optional parameter is the vertical offset
  \FloatBarrier%
  \marginskip{\kaomarginskipabove}%
  \begin{lrbox}{\@sidenotes@marginlistingbox}%
	\begin{minipage}{\marginparwidth}%
	  \captionsetup{type=lstlisting}%
}{%
	\end{minipage}%
  \end{lrbox}%
  \marginnote[#1]{\usebox{\@sidenotes@marginlistingbox}}%
  \marginskip{\kaomarginskipbelow}%
}

% Change the position of the captions
\DeclareFloatSeparators{marginparsep}{\hskip\marginparsep}%

% Detect whether there is a caption in the current environment by switching the kaocaption toggle when \caption is called. If there is no caption, reset the floatsetup. Without this fix, the floatrow package will align the environment to the main text if there is a caption, but to the margin if there is no caption.
\newtoggle{kaocaption}
\AtBeginEnvironment{figure}{%
	\let\oldcaption\caption%
	\RenewDocumentCommand{\caption}{s o m}{%
		\IfBooleanTF{#1}{%
			\oldcaption*{#3}%
		}{%
			\IfValueTF{#2}{%
				\oldcaption[#2]{#3}%
			}{%
				\oldcaption{#3}%
			}%
		}%
		\toggletrue{kaocaption}%
	}%
}
\AtEndEnvironment{figure}{%
	\iftoggle{kaocaption}{%
	}{%
		\RawFloats%
		\centering%
	}%
	\togglefalse{kaocaption}%
}
\AtBeginEnvironment{table}{%
	\let\oldcaption\caption%
	\RenewDocumentCommand{\caption}{s o m}{%
		\IfBooleanTF{#1}{%
			\oldcaption*{#3}%
		}{%
			\IfValueTF{#2}{%
				\oldcaption[#2]{#3}%
			}{%
				\oldcaption{#3}%
			}%
		}%
		\toggletrue{kaocaption}%
	}%
}
\AtEndEnvironment{table}{%
	\iftoggle{kaocaption}{%
	}{%
		\RawFloats%
		\centering%
	}%
    \togglefalse{kaocaption}%
}

% Change the formatting of the captions
\addtokomafont{captionlabel}{\bfseries} % Bold font for the figure label
% Declare a new style to format the caption according to \@margin@par (see above)
\DeclareCaptionFormat{margin}{\@margin@par #1#2#3}
% Declare a new caption style for lstlistings
\newsavebox\mycap
\DeclareCaptionFormat{llap}{%
	\begin{lrbox}{\mycap}%
	\begin{minipage}{\marginparwidth}%
	\@margin@par #1:#2#3%
	\end{minipage}%
	\end{lrbox}%
	\marginnote[0.2cm]{\usebox\mycap}%
}
% Set the global caption style
\captionsetup{
	format=margin, % Use the style previously declared
	strut=no,%
	%hypcap=true, % Links point to the top of the figure
	singlelinecheck=false,%
	%width=\marginparwidth,
	indention=0pt, % Suppress indentation
	parindent=0pt, % Suppress space between paragraphs
	aboveskip=6pt, % Increase the space between the figure and the caption
	belowskip=6pt, % Increase the space between the caption and the table
}

% Needed to have continued figures and tables (https://en.wikibooks.org/wiki/LaTeX/Floats,_Figures_and_Captions#Figures_in_multiple_parts)
\DeclareCaptionLabelFormat{cont}{#1~#2\alph{ContinuedFloat}}
\captionsetup[ContinuedFloat]{labelformat=cont}

% Captions for the 'margin' layout
\NewDocumentCommand{\marginfloatsetup}{}{%
\if@twoside%
	\floatsetup[figure]{% Captions for figures
		margins=hangoutside,% Put captions in the margins
		facing=yes,%
		capposition=beside,%
		capbesideposition={bottom,outside},%
		capbesideframe=yes,%
		capbesidewidth=\marginparwidth,% Width of the caption equal to the width of the margin
		capbesidesep=marginparsep,%
		floatwidth=\textwidth,% Width of the figure equal to the width of the text
	}%
	\floatsetup[widefigure]{% Captions for wide figures
		margins=hangoutside,% Put captions below the figure
		facing=yes,%
		capposition=bottom%
	}%
	\floatsetup[table]{% Captions for tables
		margins=hangoutside,% Put captions in the margin
		facing=yes,%
		capposition=beside,%
		capbesideposition={top,outside},%
		%capbesideposition=outside,
		capbesideframe=yes,%
		capbesidewidth=\marginparwidth,% Width of the caption equal to the width of the margin
		capbesidesep=marginparsep,%
		floatwidth=\textwidth,% Width of the figure equal to the width of the text
	}%
	\floatsetup[widetable]{% Captions for wide tables
		margins=hangoutside,% Put captions above the table
		facing=yes,%
		capposition=above%
	}%
    \floatsetup[longtable]{% Captions for longtables
        margins=raggedright,% Overwrite the hangright setting from the `table' environment
        %LTcapwidth=table,% Set the width of the caption equal to the table's
    }%
	\floatsetup[lstlisting]{% Captions for lstlistings
		margins=hangoutside,% Put captions in the margin
		facing=yes,%
		capposition=beside,%
		capbesideposition={top,outside},%
		%capbesideposition=outside,
		capbesideframe=yes,%
		capbesidewidth=\marginparwidth,% Width of the caption equal to the width of the margin
		capbesidesep=marginparsep,%
		floatwidth=\textwidth,% Width of the figure equal to the width of the text
	}%
	\floatsetup[listing]{% Captions for listings (minted package)
		margins=hangoutside,% Put captions in the margin
		facing=yes,%
		capposition=beside,%
		capbesideposition={top,outside},%
		%capbesideposition=outside,
		capbesideframe=yes,%
		capbesidewidth=\marginparwidth,% Width of the caption equal to the width of the margin
		capbesidesep=marginparsep,%
		floatwidth=\textwidth,%Width of the figure equal to the width of the text
	}%
	\captionsetup*[lstlisting]{%
		format=llap,%
		labelsep=space,%
		singlelinecheck=no,%
		belowskip=-0.6cm,%
	}%
\else%
	\floatsetup[figure]{% Captions for figures
		margins=hangright,% Put captions in the margins
		facing=yes,%
		capposition=beside,%
		capbesideposition={bottom,right},%
		capbesideframe=yes,%
		capbesidewidth=\marginparwidth,% Width of the caption equal to the width of the margin
		capbesidesep=marginparsep,%
		floatwidth=\textwidth,% Width of the figure equal to the width of the text
	}%
	\floatsetup[widefigure]{% Captions for wide figures
		margins=hangright,% Put captions below the figure
		facing=no,%
		capposition=bottom%
	}%
	\floatsetup[table]{% Captions for tables
		margins=hangright,% Put captions in the margin
		facing=yes,%
		capposition=beside,%
		capbesideposition={top,right},%
		%capbesideposition=outside,
		capbesideframe=yes,%
		capbesidewidth=\marginparwidth,% Width of the caption equal to the width of the margin
		capbesidesep=marginparsep,%
		floatwidth=\textwidth,% Width of the figure equal to the width of the text
	}%
	\floatsetup[widetable]{% Captions for wide tables
		margins=hangright,% Put captions above the table
		facing=no,%
		capposition=above%
	}%
    \floatsetup[longtable]{% Captions for longtables
        margins=raggedright,% Overwrite the hangright setting from the `table' environment
        %LTcapwidth=table,% Set the width of the caption equal to the table's
    }%
	\floatsetup[lstlisting]{% Captions for lstlisting
		margins=hangright,% Put captions in the margin
		facing=yes,%
		capposition=beside,%
		capbesideposition={top,right},%
		%capbesideposition=outside,
		capbesideframe=yes,%
		capbesidewidth=\marginparwidth,% Width of the caption equal to the width of the margin
		capbesidesep=marginparsep,%
		floatwidth=\textwidth,% Width of the figure equal to the width of the text
	}%
	\floatsetup[listing]{% Captions for listing (minted package)
		margins=hangright,% Put captions in the margin
		facing=yes,%
		capposition=beside,%
		capbesideposition={top,right},%
		%capbesideposition=outside,
		capbesideframe=yes,%
		capbesidewidth=\marginparwidth,% Width of the caption equal to the width of the margin
		capbesidesep=marginparsep,%
		floatwidth=\textwidth,% Width of the figure equal to the width of the text
	}%
	\captionsetup*[lstlisting]{%
		format=llap,%
		labelsep=space,%
		singlelinecheck=no,%
		belowskip=-0.6cm,%
	}%
\fi%
}

% Captions for the 'wide' layout
\NewDocumentCommand{\widefloatsetup}{}{%
	\floatsetup[figure]{ % Captions for figures
		capposition=bottom,%
		margins=centering,%
		floatwidth=\textwidth%
	}
	\floatsetup[widefigure]{ % Captions for wide figures
		margins=hangoutside, % Put captions below the figure
		facing=yes,%
		capposition=bottom%
	}
	\floatsetup[table]{ % Captions for tables
		capposition=above,%
		margins=centering,%
		floatwidth=\textwidth%
	}
	\floatsetup[widetable]{ % Captions for wide tables
		margins=hangoutside, % Put captions above the table
		facing=yes,%
		capposition=above%
	}
	\floatsetup[lstlisting]{ % Captions for lstlistings
		capposition=above,%
		margins=centering,%
		floatwidth=\textwidth%
	}
	\floatsetup[listing]{ % Captions for listings (minted package)
		capposition=above,%
		margins=centering,%
		floatwidth=\textwidth%
	}
	\captionsetup*[lstlisting]{% Captions style for lstlistings
		%format=margin,%
		labelsep=colon,%
		strut=no,%
		singlelinecheck=false,%
		indention=0pt,%
		parindent=0pt,%
    	aboveskip=6pt,%
		belowskip=6pt,%
		belowskip=-0.1cm%
	}
}

%----------------------------------------------------------------------------------------
%	TOC, LOF & LOT
%----------------------------------------------------------------------------------------

\RequirePackage{tocbasic}

% Show an entry for the TOC in the TOC
\setuptoc{toc}{totoc}

% Choose the levels in table of contents
\setcounter{tocdepth}{\subparagraphtocdepth}

% Define the style for toc entries
\@ifpackagelater{scrbase}{2019/10/11}{%
    \DeclareTOCStyleEntries[indent=0em,numwidth=2em,dynnumwidth=yes,pagenumberwidth=2.1em]{tocline}{figure,table}%
    \DeclareTOCStyleEntries[dynnumwidth=yes]{tocline}{subsubsection,subsection,section,chapter,part}%
    \DeclareTOCStyleEntries[pagenumberwidth=2.5em]{tocline}{chapter,part}%
    \DeclareTOCStyleEntries[pagenumberwidth=2.1em]{tocline}{subsubsection,subsection,section}%
}{%
    \DeclareTOCStyleEntries[indent=0em,numwidth=2em,dynnumwidth=yes]{tocline}{figure,table}%
    \DeclareTOCStyleEntries[dynnumwidth=yes]{tocline}{subsubsection,subsection,section,chapter,part}%
}

% Define the names for the headings
% \renewcaptionname{english}{\contentsname}{Detailed Contents}
% \renewcaptionname{english}{\listfigurename}{Figures}
% \renewcaptionname{english}{\listtablename}{Tables}
% \newcaptionname{english}{\listtheoremname}{Theorems}

%----------------------------------------------------------------------------------------
%	MARGIN TOC
%----------------------------------------------------------------------------------------

\RequirePackage{etoc} % Required to insert local tables of contents

\newcounter{margintocdepth} % Set the depth of the margintoc
\setcounter{margintocdepth}{\subparagraphtocdepth}

\newlength{\mtocshift} % Length of the vertical offset used for margin tocs
\setlength{\mtocshift}{1\vscale}% \mtocshift is overridden by \setchapterstyle

% Optional title for margintoc (by hCarlFelix, 
% https://github.com/fmarotta/kaobook/issues/101)
% We want to create an additional entries in the toc which is to be used for the margintoc
% We define these as mtocsection and mtocsubsection for section and subsection`
\newcommand{\mtocsection}[1]{
    \addcontentsline{toc}{mtocsection}{%
        \ifnum\value{secnumdepth}>0 \protect\numberline{\thesection}%
        \else \protect\nonumberline%
        \fi #1}%
}
\newcommand{\mtocsubsection}[1]{
    \addcontentsline{toc}{mtocsubsection}{%
        \ifnum\value{secnumdepth}>1 \protect\numberline{\thesubsection}%
        \else \protect\nonumberline%
        \fi #1}%
}

% Next, we redefine \section and \subsection so that they accept an additional parameter
% \section[alternative-title-for-toc]{title-as-written-in-text}[alternative-title-for-margintoc]

% Adapted from Frank Mittelbach's answer at Stackexchange
% https://tex.stackexchange.com/a/109560/226693
\let\oldsection\section  % save the old command
\let\oldsubsection\subsection  % save the old command

\RenewDocumentCommand\section{s o m o}{%
    \IfBooleanTF{#1}{%
        \oldsection*{#3}
        \IfNoValueF{#2}{% if TOC arg is given create a TOC entry
            \addxcontentsline{toc}{section}[\thesection]{#2}%
        }%
    }{% no star given
        \IfNoValueTF{#2}{%
            \oldsection{#3}%
        }{% no TOC arg
            \oldsection[#2]{#3}%
        }%
        \IfNoValueTF{#4}{% optional label given, if not we do nothing
            \mtocsection{#3}%
        }{%
            \mtocsection{#4}%
        }%
    }%
}

\RenewDocumentCommand\subsection{s o m o}{
    \IfBooleanTF{#1}{%
        \oldsubsection*{#3}%
        \IfNoValueF{#2}{% if TOC arg is given create a TOC entry
            \addxcontentsline{toc}{subsection}[\thesubsection]{#2}%
        }%
    }{% no star given
        \IfNoValueTF{#2}{%
            \oldsubsection{#3}%
        }{% no TOC arg
            \oldsubsection[#2]{#3}%
        }%
        \IfNoValueTF{#4}{% optional label given, if not we do nothing
            \mtocsubsection{#3}%
        }{%
            \mtocsubsection{#4}%
        }%
    }%
}

\etocsetlevel{mtocsection}{6}% dummy sectioning level
\etocsetlevel{mtocsubsection}{6}% dummy sectioning level

% Command to print a table of contents in the margin
\NewDocumentCommand{\margintoc}{O{\mtocshift}}{ % The first parameter is the vertical offset; by default it is \mtocshift
    \begingroup%
        % Move regular section and subsection to level 6 so that they won't be included and instead set let the mtoc versions take their place.
        % Adapted from https://tex.stackexchange.com/a/133559/226693
        \etocsetlevel{section}{6}
        \etocsetlevel{subsection}{6}
        \etocsetlevel{mtocsection}{1}
        \etocsetlevel{mtocsubsection}{2}

        % Define default widths
        \def\margintocnumwidth{-.8mm}%
        \def\margintocpagenumwidth{8pt}%
        \setlength{\RaggedRightParfillskip}{0pt}

        % Dry run to get the needed widths
        \etocsetstyle{mtocsection}%
          {}%
          {\setbox0\hbox{\usekomafont{section}\small\etocthenumber\kern.8mm}%%
           \setbox1\hbox{\usekomafont{section}\small\etocthepage}}%
          {\ifdim\wd0>\margintocnumwidth \edef\margintocnumwidth{\the\wd0} \fi%%
           \ifdim\wd1>\margintocpagenumwidth \edef\margintocpagenumwidth{\the\wd1} \fi}%
          {}%
        \etocsetstyle{mtocsubsection}%
          {}%
          {\setbox0\hbox{\usekomafont{section}\small\etocthenumber\kern.8mm}%
           \setbox1\hbox{\usekomafont{section}\small\etocthepage}}%
          {\ifdim\wd0>\margintocnumwidth \edef\margintocnumwidth{\the\wd0} \fi%
           \ifdim\wd1>\margintocpagenumwidth \edef\margintocpagenumwidth{\the\wd1} \fi}%
          {}%
        \etocsetstyle{subsubsection}%
          {}%
          {}%
          {}%
          {}%
        \etocsetstyle{paragraph}%
          {}%
          {}%
          {}%
          {}%
        \etocsettocstyle{}{%
          \global\let\margintocnumwidth\margintocnumwidth%
          \global\let\margintocpagenumwidth\margintocpagenumwidth%
        }%
        \localtableofcontents%

        % Set the style for section entries
        \etocsetstyle{mtocsection}%
        {\parindent 0pt \parskip 2.5pt \parfillskip 0pt \RaggedRight}%
        {\leftskip \margintocnumwidth \rightskip \margintocpagenumwidth} %
        {\makebox[0pt][r]{\makebox[\margintocnumwidth][l]{\etocnumber}}\etocname\nobreak\leaders\hbox{\hbox to 1.5ex {\hss.\hss}}\hfill\rlap{\makebox[\margintocpagenumwidth][r]{\etocpage}}\par}%
        {}%
		% Set the style for subsection entries
        \etocsetstyle{mtocsubsection}%
        {\parindent 0pt \parskip 0pt \parfillskip 0pt \RaggedRight}%
        {\leftskip \margintocnumwidth \rightskip \margintocpagenumwidth}%
        {\makebox[0pt][r]{\makebox[\margintocnumwidth][l]{\etocnumber}}\etocname\nobreak\leaders\hbox{\hbox to 1.5ex {\hss.\hss}}\hfill\rlap{\makebox[\margintocpagenumwidth][r]{\etocpage}}\par}%
        {\parskip 2.5pt}%
		% Set the global style of the toc
        \etocsettocstyle{\usekomafont{section}\small}{}%
		\etocsetnexttocdepth{\themargintocdepth}%
        % Print the table of contents in the margin
        \marginnote[#1]{\localtableofcontents}%
        \FloatBarrier%
    \endgroup%
}

%----------------------------------------------------------------------------------------
%	ENCODING AND FONTS
%----------------------------------------------------------------------------------------

% https://tex.stackexchange.com/questions/47576/combining-ifxetex-and-ifluatex-with-the-logical-or-operation
% Introduce a command to find out whether the compiler is XeTeX or LuaTeX
\newif\ifxetexorluatex
\ifxetex
	\xetexorluatextrue
\else
	\ifluatex
		\xetexorluatextrue
	\else
		\xetexorluatexfalse
	\fi
\fi

\ifxetexorluatex
	\RequirePackage{amssymb} % Must be loaded before unicode-math
	\RequirePackage[force]{filehook} % Fixes an error
	\RequirePackage{unicode-math} % Math fonts in xetexorluatex
    \setromanfont[
		Scale=1.04
	]{Libertinus Serif}
	\setsansfont[
		Scale=1
	]{Libertinus Sans}
	\setmonofont[
		Scale=.89
	]{Liberation Mono}
	\setmathfont{Libertinus Math}
    \ifluatex
    \else
        \RequirePackage{morewrites} % Fix some errors related to floats
    \fi
\else
	\RequirePackage[utf8]{inputenc} % utf8 encoding in the input (.tex) file
	\RequirePackage[T1]{fontenc} % utf8 encoding in the output (.pdf) file

	\RequirePackage{amssymb} % Math symbols, including \blacktriangleright, used for bullets
	\RequirePackage[scaled=.97,helvratio=.93,p,theoremfont]{newpxtext} % Serif palatino font
	\RequirePackage[vvarbb,smallerops,bigdelims]{newpxmath} % Math palatino font
	\RequirePackage[scaled=.85]{beramono} % Monospace font
	\RequirePackage[scr=rsfso,cal=boondoxo]{mathalfa} % Mathcal from STIX, unslanted a bit
    \RequirePackage{morewrites} % Fix some errors related to floats
\fi

% When using the Palatino (newpxtext) font, it is better to use a 
% slightly larger stretch.
%\setstretch{1.10}
\linespread{1.07} % Give Palatino more leading (space between lines)

%----------------------------------------------------------------------------------------
%	HYPERREFERENCES
%----------------------------------------------------------------------------------------

\RequirePackage{hyperref} % Required for hyperlinks
\RequirePackage{bookmark} % Required for pdf bookmarks

\PassOptionsToPackage{hyphens}{url} % Break long URLs and use hyphens to separate the pieces

\hypersetup{ % Set up hyperref options
	unicode, % Use unicode for links
	pdfborder={0 0 0}, % Suppress border around pdf
	%xetex,
	%pagebackref=true,
	%hyperfootnotes=false, % We already use footmisc
	bookmarksdepth=section,
	bookmarksopen=true, % Expand the bookmarks as soon as the pdf file is opened
	%bookmarksopenlevel=4,
	linktoc=all, % Toc entries and numbers links to pages
	breaklinks=true,
	colorlinks=true,
	%allcolors=DarkGreen,
	citecolor = DarkOrange,
    linkcolor = Blue,
    %pagecolor = Blue,
	urlcolor = OliveGreen,
}

% Define a new color for the footnote marks
\def\@footnotecolor{black}
\define@key{Hyp}{footnotecolor}{%
	\HyColor@HyperrefColor{#1}\@footnotecolor%
}
\def\@footnotemark{%
	\leavevmode
	\ifhmode\edef\@x@sf{\the\spacefactor}\nobreak\fi
	\stepcounter{Hfootnote}%
	\global\let\Hy@saved@currentHref\@currentHref
	\hyper@makecurrent{Hfootnote}%
	\global\let\Hy@footnote@currentHref\@currentHref
	\global\let\@currentHref\Hy@saved@currentHref
	\hyper@linkstart{footnote}{\Hy@footnote@currentHref}%
	\@makefnmark
	\hyper@linkend
	\ifhmode\spacefactor\@x@sf\fi
	\relax
}

\let\oldthanks\thanks
\renewcommand\thanks[1]{%
    \label{bhfn:0}%
    \oldthanks{#1}%
}

% Adjust the colour of the footnotes marks using the colour defined above
\renewcommand\@makefntext[1]{%
	\renewcommand\@makefnmark{%
		\mbox{\textsuperscript{\normalfont%
			\hyperref[\BackrefFootnoteTag]{%
				\color{\@footnotecolor}{\@thefnmark}%
			}}\,%
		}%
	}%
	\BHFN@OldMakefntext{#1}%
}

%----------------------------------------------------------------------------------------
%	COLOURS
%----------------------------------------------------------------------------------------

% Uncomment to have coloured headings
%\addtokomafont{title}{\color{Maroon}}
%\addtokomafont{part}{\color{Maroon}}
%\addtokomafont{chapter}{\color{Maroon}}
%\addtokomafont{section}{\color{Maroon}}
%\addtokomafont{subsection}{\color{Maroon}}
%\addtokomafont{subsubsection}{\color{Maroon}}
%\addtokomafont{paragraph}{\color{Maroon}}
%\addtokomafont{captionlabel}{\color{Blue}}
%\addtokomafont{pagenumber}{\color{Maroon}}

\hypersetup{
	%anchorcolor=Red,
	%citecolor=DarkOrange!70!black,
	citecolor=OliveGreen,
	filecolor=OliveGreen,
    %linkcolor=Blue,
	linkcolor=Black,
	%menucolor=Red,
	%runcolor=Red,
	urlcolor=OliveGreen,
}

%----------------------------------------------------------------------------------------
%	ITEMS
%----------------------------------------------------------------------------------------

\renewcommand{\labelitemi}{\small$\blacktriangleright$}
\renewcommand{\labelitemii}{\textbullet}
\RequirePackage{enumitem}
\setlist[itemize]{noitemsep}
\setlist[enumerate]{noitemsep}
\setlist[description]{noitemsep}

%----------------------------------------------------------------------------------------
%	SIMPLE BOXED ENVIRONMENT
%----------------------------------------------------------------------------------------

% kaobox (while tcolorbox may be more rich, I find it too complicated so I prefer mdframed)
\RequirePackage{tikz}
\RequirePackage[framemethod=TikZ]{mdframed}

%\mdfsetup{skipabove=\topskip,skipbelow=0pt}
\mdfdefinestyle{kaoboxstyle}{
	skipabove=1.5\topskip,
	skipbelow=.5\topskip,
	rightmargin=0pt,
	leftmargin=0pt,
	%innertopmargin=3pt,
	%innerbottommargin=3pt,
	innerrightmargin=7pt,
	innerleftmargin=7pt,
	topline=false,
	bottomline=false,
	rightline=false,
	leftline=false,
	%linewidth=1pt,
	%roundcorner=0pt,
	%font={},
	%frametitlefont={},
	frametitlerule=true,
	linecolor=black,
	%backgroundcolor=LightBlue,
	fontcolor=black,
	%frametitlebackgroundcolor=LightBlue,
}

\newmdenv[
	style=kaoboxstyle,
	backgroundcolor=Gray!25!White,
	frametitlebackgroundcolor=RoyalBlue!25!White,
]{kaobox}

%----------------------------------------------------------------------------------------
%	ENVIRONMENT WITH A COUNTER
%----------------------------------------------------------------------------------------

\newenvironment{kaocounter}{
	\refstepcounter{kaocounter}
	\begin{kaobox}[frametitle=Comment~\thekaocounter\autodot]
}{
	\end{kaobox}
}

\newcounter{kaocounter}
\counterwithin{kaocounter}{section}
\newcommand*{\kaocounterformat}{% Format for the caption
	Comment~\thekaocounter\csname autodot\endcsname}
\newcommand*{\fnum@kaocounter}{\kaocounterformat}


%----------------------------------------------------------------------------------------
%	FLOATING ENVIRONMENT WITH TOC ENTRIES
%----------------------------------------------------------------------------------------

\newenvironment{kaofloating}{%
	\@float{kaofloating}%
}{%
	\end@float%
}

\newcommand*{\fps@floatingbox}{tbph}
\newcommand*{\ftype@floatingbox}{5}
\newcommand*{\floatingboxformat}{%
	Insight~\thefloatingbox\csname autodot\endcsname}
\newcommand*{\fnum@floatingbox}{\floatingboxformat}
\newcommand*{\ext@floatingbox}{loi}

\addtotoclist[float]{loi}
\newcommand*{\listofloiname}{List of Insights}
\newcommand*{\l@floatingbox}{\l@figure}
\newcommand*{\listofinsights}{\listoftoc{loi}}

%----------------------------------------------------------------------------------------
%	ADDITIONAL PACKAGES
%----------------------------------------------------------------------------------------

% Productivity
\RequirePackage{pdfpages} % Insert PDF pages
\RequirePackage{subfiles} % Adopt a modular structure
\RequirePackage{todonotes} % Add useful notes in the margins

% Listings code
\RequirePackage{listings} % Code
%\RequirePackage{minted}

\definecolor{listingkeywords}{rgb}{0.0, 0.5, 0.0}
\definecolor{listingidentifiers}{rgb}{0, 0, 0}
\definecolor{listingcomments}{rgb}{0.25, 0.5, 0.5}
\definecolor{listingstrings}{rgb}{0.73, 0.13, 0.13}
\definecolor{listingnumbers}{rgb}{0.25, 0.25, 0.25}
\lstdefinestyle{kaolst}{
	aboveskip=0.7\topskip,
	belowskip=0.1\topskip,
	basicstyle=\small\ttfamily,
	commentstyle=\color{listingcomments}\itshape,
	keywordstyle=\color{listingkeywords}\bfseries,
	numberstyle=\scriptsize\color{listingnumbers}\ttfamily,
	stringstyle=\color{listingstrings},
	identifierstyle=\color{listingidentifiers},
	backgroundcolor=\color{White},
	breakatwhitespace=false,
	breaklines=true,
	captionpos=t,
	keepspaces=true,
	showspaces=false,
	showstringspaces=false,
	showtabs=false,
	numbers=left,
	numbersep=1em,
	%frame=lines,
	frame=l,
	framerule=.7pt,
	tabsize=4,
	defaultdialect=[LaTeX]Tex,
}
\lstdefinestyle{kaolstplain}{
	aboveskip=0.6\topskip,
	belowskip=-0.1\topskip,
	basicstyle=\small\ttfamily,
	commentstyle=\color{listingcomments}\itshape,
	keywordstyle=\color{listingkeywords}\bfseries,
	numberstyle=\scriptsize\color{listingnumbers}\ttfamily,
	stringstyle=\color{listingstrings},
	identifierstyle=\color{listingidentifiers},
	backgroundcolor=\color{White},
	breakatwhitespace=false,
	breaklines=true,
	captionpos=b,
	keepspaces=true,
	showspaces=false,
	showstringspaces=false,
	showtabs=false,
	numbers=none,
	frame=none,
	tabsize=4,
	defaultdialect=[LaTeX]Tex,
}
\lstset{style=kaolst}

% Verbatim
%\RequirePackage{fancyvrb} % Customization of verbatim environments
%\fvset{fontsize=\normalsize} % Change here the font size of all 
%verbatim \preto{\@verbatim}{\topsep=0pt \partopsep=0pt }

% Algorithms
\RequirePackage[linesnumbered, ruled, vlined]{algorithm2e} % Algorithms

% Special gliphs
\RequirePackage{ccicons} % Creative Commons icons
\RequirePackage{metalogo} % XeTeX logo

% Index, glossary and nomenclature
\RequirePackage{imakeidx}
\RequirePackage[xindy,toc,numberedsection=nameref]{glossaries}
\RequirePackage[intoc]{nomencl}

% Commands to print specific words always in the same way
% TODO: in \Command, automatically escape braces {} and replace backslashes with \textbackslash
\newcommand{\Class}[1]{\texttt{#1}}
\newcommand{\Package}[1]{\texttt{#1}}
\newcommand{\Option}[1]{\texttt{#1}}
\newcommand{\Command}[1]{\texttt{\textbackslash#1}}
\newcommand{\Environment}[1]{\texttt{#1}}
\newcommand{\Path}[1]{\texttt{#1}}

% Print latin words in italics (The xspace package is required but we already loaded it in the class)
\newcommand{\hairsp}{\hspace{1pt}} % Command to print a very short space
\newcommand{\invitro}{\textit{in vitro}\xspace}
\newcommand{\invivo}{\textit{in vivo}\xspace}
\newcommand{\cis}{\textit{cis}\xspace}
\newcommand{\trans}{\textit{trans}\xspace}
\newcommand{\etal}{\textit{et al.}\xspace}
\newcommand{\denovo}{\textit{de novo}\xspace}
\newcommand{\adhoc}{\textit{ad hoc}\xspace}
\newcommand{\etcetera}{\textit{et cetera}\xspace}
\newcommand{\etc}{\textit{etc.}\xspace}
\newcommand{\ie}{\textit{i.\nobreak\hairsp{}e.}\xspace}
\newcommand{\eg}{\textit{e.\nobreak\hairsp{}g.}\xspace}
\newcommand{\vs}{\textit{vs}\xspace}
\newcommand{\cfr}{\textit{cfr.}\xspace}

% Tables
\newcommand{\na}{\quad--} % Used in tables for N/A cells
\newcommand{\hangp}[1]{\makebox[0pt][r]{(}#1\makebox[0pt][l]{)}} % Create parentheses around text in tables which take up no horizontal space - this improves column spacing
\newcommand{\hangstar}{\makebox[0pt][l]{*}} % Create asterisks in tables which take up no horizontal space - this improves column spacing

% A command to print the current month and year (from tufte-latex)
\newcommand{\monthyear}{\ifcase\month\or January\or February\or March\or 
April\or May\or June\or July\or August\or September\or October\or 
November\or December\fi\space\number\year}


"""

    contenido_kaobiblio = r"""
    
\ProvidesPackage{kaobiblio}

\RequirePackage{etoolbox} % Easy programming to modify TeX stuff
\RequirePackage{perpage} % Reset counters
\RequirePackage{iflang} % Check the document language
\RequirePackage{xparse} % Parse arguments for macros
\RequirePackage{xstring} % Parse strings
\RequirePackage{hyperref} % Required for hyperlinks
\RequirePackage{kvoptions} % Handle package options

\SetupKeyvalOptions{
    family = kaobiblio,
    prefix = kaobiblio@
}

\DeclareBoolOption{addspace}
\DeclareBoolOption{linkeverything}

% Choose the default options, which will be overwritten by the options 
% passed to this package.
\PassOptionsToPackage{
    %style=numeric-comp,
    %citestyle=authortitle-icomp,
    citestyle=numeric-comp,
    %bibstyle=authoryear,
    bibstyle=numeric,
    sorting=none,
    %sorting=nyt,
    %sortcites=true,
    %autocite=footnote,
    backend=biber, % Compile the bibliography with biber
    hyperref=true,
    backref=true,
    citecounter=true,
    pagetracker=true,
    citetracker=true,
    ibidtracker=context,
    autopunct=true,
    autocite=plain,
}{biblatex}

% Pass the unknown options to biblatex, overwriting the previous settings. Avoid passing the kao-specific options.
\DeclareDefaultOption{%
    \IfBeginWith{\CurrentOption}{addspace}{}{%
    \IfBeginWith{\CurrentOption}{linkeverything}{}{%
        \PassOptionsToPackage{\CurrentOption}{biblatex}%
    }}%
}

% Process the options
\ProcessKeyvalOptions{kaobiblio}

% Load biblatex
\RequirePackage{biblatex}

% Remove some unwanted entries from the bibliography
\AtEveryBibitem{
	\clearfield{issn}
	\clearfield{isbn}
	\clearfield{archivePrefix}
	\clearfield{arxivId}
	\clearfield{pmid}
	\clearfield{eprint}
	\ifentrytype{online}{}{\ifentrytype{misc}{}{\clearfield{url}}}
	\ifentrytype{book}{\clearfield{doi}}{}
}

% Convert months to integers
\DeclareSourcemap{
    \maps[datatype=bibtex]{
        \map[overwrite]{
            \step[fieldsource=month, match={jan}, replace=${1}]
            \step[fieldsource=month, match={feb}, replace=${2}]
            \step[fieldsource=month, match={mar}, replace=${3}]
            \step[fieldsource=month, match={apr}, replace=${4}]
            \step[fieldsource=month, match={may}, replace=${5}]
            \step[fieldsource=month, match={jun}, replace=${6}]
            \step[fieldsource=month, match={jul}, replace=${7}]
            \step[fieldsource=month, match={aug}, replace=${8}]
            \step[fieldsource=month, match={sep}, replace=${9}]
            \step[fieldsource=month, match={oct}, replace=${10}]
            \step[fieldsource=month, match={nov}, replace=${11}]
            \step[fieldsource=month, match={dec}, replace=${12}]
        }
    }
}

%----------------------------------------------------------------------------------------
%	BACK REFERENCES
%----------------------------------------------------------------------------------------

% Check if a string is in a comma-separated list
\newcommand\IfStringInList[2]{\IfSubStr{,#2,}{,#1,}}

% Set the language-specific back reference strings
% #LANGUAGE
\@ifpackageloaded{polyglossia}{%
	\IfLanguageName{danish}{%
		\DefineBibliographyStrings{danish}{%
			backrefpage = {citeret på side},
			backrefpages = {citeret på sider},
		}
	}{}
	\IfLanguageName{english}{%
		\DefineBibliographyStrings{english}{%
			backrefpage = {cited on page},
			backrefpages = {cited on pages},
		}
	}{}
	\IfLanguageName{italian}{%
		\DefineBibliographyStrings{italian}{%
			backrefpage = {citato a pag.},
			backrefpages = {citato a pagg.},
		}
	}{}
}{
	\@ifpackageloaded{babel}{%
		\IfStringInList{danish}{\bbl@loaded}{%
			\DefineBibliographyStrings{danish}{%
				backrefpage = {citeret på side},
				backrefpages = {citeret på sider},
			}
		}{}
		\IfStringInList{english}{\bbl@loaded}{%
			\DefineBibliographyStrings{english}{%
				backrefpage = {cited on page},
				backrefpages = {cited on pages},
			}
		}{}
		\IfStringInList{italian}{\bbl@loaded}{%
			\DefineBibliographyStrings{italian}{%
				backrefpage = {citato a pag.},
				backrefpages = {citato a pagg.},
			}
		}{}
	}{}
}

%----------------------------------------------------------------------------------------
%	CITATION COMMANDS
%----------------------------------------------------------------------------------------

% Command to format the marginnote created for cited items
\NewDocumentCommand{\formatmargincitation}{m}{% The parameter is a single citation key
	\parencite{#1}: \citeauthor*{#1} (\citeyear{#1}), \citetitle{#1}%
}

% Command to format the marginnote created for supercited items
\NewDocumentCommand{\formatmarginsupercitation}{m}{% The parameter is a single citation key
    \supercite{#1} \citeauthor*{#1} (\citeyear{#1})%
}

% The following command needs to be redefined every time \sidecite is called in order for \DeclareCiteCommand's wrapper to work correctly
\NewDocumentCommand{\kaobiblio@marginnote}{m}{%
    \marginnote{#1}%
}

% biblatex-like commands that also print a citation in the margin
% Usage:
    % First optional argument is always vertical shift and must be given as an (empty) argument when using following a postnote and/or prenote
    % Second optional argument is always the postnote if the third argument isn't specified or is the prenote if the third argument is specified (same pattern as the biblatex commands)
    % Third optional argument is always the postnote
    % Mandatory argument is always the citation key(s)

% Command to \cite and print a citation in the margin
% First optional argument: vertical shift
% Second optional argument: postnote if the third argument isn't specified; prenote if the third argument is specified (same pattern as the \textcite command)
% Third optional argument: postnote
% Mandatory argument: citation key
\NewDocumentCommand{\sidecite}{o o o m}{%
    \RenewDocumentCommand{\kaobiblio@marginnote}{m}{%
        \marginnote[#1]{##1}%
    }%
	\DeclareCiteCommand{\kaobiblio@sidecite}[\kaobiblio@marginnote]{%
	}{%
		\formatmargincitation{\thefield{entrykey}}%
	}{%
		\\% separator between multiple citations
	}{%
	}%
    % With this we print the marker in the text and add the item to the bibliography at the end
    \IfNoValueOrEmptyTF{#2}%
    {\def\@tempa{\cite{#4}\kaobiblio@sidecite{#4}}}%
    {\IfNoValueOrEmptyTF{#3}%
        {\IfNoValueTF{#3}%
            {\def\@tempa{\cite[#2]{#4}\kaobiblio@sidecite{#4}}}%
            {\def\@tempa{\cite[#2][]{#4}\kaobook@sidecite{#4}}}% postnote is empty, so pass empty postnote
        }%
        {\def\@tempa{\cite[#2][#3]{#4}\kaobiblio@sidecite{#4}}}%
    }%
    \ifkaobiblio@addspace%
        \unskip~\@tempa%
    \else%
        \@tempa%
    \fi%
}

% Command to \supercite and print a citation in the margin
% First optional argument: vertical shift
% Second optional argument: postnote if the third argument isn't specified; prenote if the third argument is specified (same pattern as the \textcite command)
% Third optional argument: postnote
% Mandatory argument: citation key
\NewDocumentCommand{\sidesupercite}{o o o m}{%
    \RenewDocumentCommand{\kaobiblio@marginnote}{m}{%
        \marginnote[#1]{##1}%
    }%
    \DeclareCiteCommand{\kaobiblio@sidesupercite}[\kaobiblio@marginnote]{%
	}{%
        \formatmarginsupercitation{\thefield{entrykey}}%
	}{%
		\\% separator between multiple citations
	}{%
	}%
    % With this we print the marker in the text and add the item to the bibliography at the end
    \IfNoValueOrEmptyTF{#2}%
    {\def\@tempa{\supercite{#4}\kaobiblio@sidesupercite{#4}}}%
    {\IfNoValueOrEmptyTF{#3}%
        {\IfNoValueTF{#3}%
            {\def\@tempa{\supercite[#2]{#4}\kaobiblio@sidesupercite{#4}}}%
            {\def\@tempa{\supercite[#2][]{#4}\kaobook@sidesupercite{#4}}}% postnote is empty, so pass empty postnote
        }%
        {\def\@tempa{\supercite[#2][#3]{#4}\kaobiblio@sidesupercite{#4}}}%
    }%
    \@tempa%
}

% Command to \textcite and print a citation in the margin
% First optional argument: vertical shift
% Second optional argument: postnote if the third argument isn't specified; prenote if the third argument is specified (same pattern as the \textcite command)
% Third optional argument: postnote
% Mandatory argument: citation key
\NewDocumentCommand{\sidetextcite}{o o o m}{%
	\RenewDocumentCommand{\kaobiblio@marginnote}{m}{%
		\marginnote[#1]{##1}%
	}%
	\DeclareCiteCommand{\kaobiblio@sidecite}[\kaobiblio@marginnote]{%
	}{%
		\formatmargincitation{\thefield{entrykey}}%
	}{%
		\\% separator between multiple citations
	}{%
	}%
    % With this we print the marker in the text and add the item to the bibliography at the end
	\IfNoValueOrEmptyTF{#2}%
        {\def\@tempa{\textcite{#4}\kaobiblio@sidecite{#4}}}%
		{\IfNoValueOrEmptyTF{#3}%
			{\IfNoValueTF{#3}%
                {\def\@tempa{\textcite[#2]{#4}\kaobiblio@sidecite{#4}}}%
                {\def\@tempa{\textcite[#2][]{#4}\kaobook@sidecite{#4}}}% postnote is empty, so pass empty postnote
			}%
            {\def\@tempa{\textcite[#2][#3]{#4}\kaobiblio@sidecite{#4}}}%
        }%
    \ifkaobiblio@addspace%
        \unskip~\@tempa%
    \else%
        \@tempa%
    \fi%
}

% Command to \parencite or \parencite* and print a citation in the margin
% First optional (star) argument: use \parencite* if included; otherwise use \parencite
% Second optional argument: vertical shift
% Third optional argument: postnote if the fourth argument isn't specified; prenote if the fourth argument is specified (same pattern as the \parencite command)
% Fourth optional argument: postnote
% Mandatory argument: citation key
\NewDocumentCommand{\sideparencite}{s o o o m}{%
	\RenewDocumentCommand{\kaobiblio@marginnote}{m}{%
		\marginnote[#2]{##1}%
	}%
	\DeclareCiteCommand{\kaobiblio@sidecite}[\kaobiblio@marginnote]{%
	}{%
		\formatmargincitation{\thefield{entrykey}}%
	}{%
		\\% separator between multiple citations
	}{%
	}%
    % With this we print the marker in the text and add the item to the bibliography at the end
    \IfBooleanTF#1%
        {\IfNoValueOrEmptyTF{#3}%
            {\parencite*{#5}}%
            {\IfNoValueOrEmptyTF{#4}%
                {\IfNoValueTF{#4}%
                    {\def\@tempa{\parencite*[#3]{#5}}}%
                    {\def\@tempa{\parencite*[#3][]{#5}}}% postnote is empty, so pass empty postnote
                }%
                {\def\@tempa{\parencite*[#3][#4]{#5}}}%
            }%
        }%
        {\IfNoValueOrEmptyTF{#3}%
            {\def\@tempa{\parencite{#5}}}%
            {\IfNoValueOrEmptyTF{#4}%
                {\IfNoValueTF{#4}%
                    {\def\@tempa{\parencite[#3]{#5}}}%
                    {\def\@tempa{\parencite[#3][]{#5}}}% postnote is empty, so pass empty postnote
                }%
                {\def\@tempa{\parencite[#3][#4]{#5}}}%
            }%
        }%
    \ifkaobiblio@addspace%
        \unskip~\@tempa%
    \else%
        \@tempa%
    \fi%
}


%----------------------------------------------------------------------------------------
%	LINKING THE AUTHOR'S NAME
%----------------------------------------------------------------------------------------

% In biblatex, when citing with the style authoryear or using \textcite, only the year is linked to the reference in the bibliography. Despite the arguments of one of the mantainers of the biblatex package (https://github.com/plk/biblatex/issues/428), some users think that in the author* style the author name should be a link as well. The `linkname' option provides an easy way to activate this behaviour.

\ifkaobiblio@linkeverything
  \xpatchbibmacro{cite}
    {\usebibmacro{cite:label}%
     \setunit{\printdelim{nonameyeardelim}}%
     \usebibmacro{cite:labeldate+extradate}}
    {\printtext[bibhyperref]{%
       \DeclareFieldAlias{bibhyperref}{default}%
       \usebibmacro{cite:label}%
       \setunit{\printdelim{nonameyeardelim}}%
       \usebibmacro{cite:labeldate+extradate}}}
    {}
    {\PackageWarning{biblatex-patch}
       {Failed to patch cite bibmacro}}

  % Include labelname in labelyear link
  \xpatchbibmacro{cite}
    {\printnames{labelname}%
     \setunit{\printdelim{nameyeardelim}}%
     \usebibmacro{cite:labeldate+extradate}}
    {\printtext[bibhyperref]{%
       \DeclareFieldAlias{bibhyperref}{default}%
       \printnames{labelname}%
       \setunit{\printdelim{nameyeardelim}}%
       \usebibmacro{cite:labeldate+extradate}}}
    {}
    {\PackageWarning{biblatex-patch}
       {Failed to patch cite bibmacro}}

  % Access hyperref's citation link start/end commands
  \makeatletter
  \protected\def\blx@imc@biblinkstart{%
    \@ifnextchar[%]
      {\blx@biblinkstart}
      {\blx@biblinkstart[\abx@field@entrykey]}}
  \def\blx@biblinkstart[#1]{%
    \blx@sfsave\hyper@natlinkstart{\the\c@refsection @#1}\blx@sfrest}
  \protected\def\blx@imc@biblinkend{%
    \blx@sfsave\hyper@natlinkend\blx@sfrest}
  \blx@regimcs{\biblinkstart \biblinkend}
  \makeatother

  \newbool{cbx:link}

  % Include parentheses around labelyear in \textcite only in
  % single citations without pre- and postnotes
  \def\iflinkparens{%
    \ifboolexpr{ test {\ifnumequal{\value{multicitetotal}}{0}} and
                 test {\ifnumequal{\value{citetotal}}{1}} and
                 test {\iffieldundef{prenote}} and
                 test {\iffieldundef{postnote}} }}

  \xpatchbibmacro{textcite}
    {\printnames{labelname}}
    {\iflinkparens
       {\DeclareFieldAlias{bibhyperref}{default}%
        \global\booltrue{cbx:link}\biblinkstart%
        \printnames{labelname}}
       {\printtext[bibhyperref]{\printnames{labelname}}}}
    {}
    {\PackageWarning{biblatex-patch}
       {Failed to patch textcite bibmacro}}

  \xpatchbibmacro{textcite}
    {\usebibmacro{cite:label}}
    {\iflinkparens
       {\DeclareFieldAlias{bibhyperref}{default}%
        \global\booltrue{cbx:link}\biblinkstart%
        \usebibmacro{cite:label}}
       {\usebibmacro{cite:label}}}
    {}
    {\PackageWarning{biblatex-patch}
       {Failed to patch textcite bibmacro}}

  \xpretobibmacro{textcite:postnote}
    {\ifbool{cbx:link}
       {\ifbool{cbx:parens}
          {\bibcloseparen\global\boolfalse{cbx:parens}}
          {}%
        \biblinkend\global\boolfalse{cbx:link}}
       {}}
    {}
    {\PackageWarning{biblatex-patch}
       {Failed to patch textcite:postnote bibmacro}}
\else
\fi

%----------------------------------------------------------------------------------------
%	CITATION ENVIRONMENTS
%----------------------------------------------------------------------------------------

% TODO: create a fancy environment for this. Perhaps printing also the 
% abstract.

% Cite commands (assuming biblatex is loaded)
\DeclareCiteCommand{\fullcite}{%
	\defcounter{maxnames}{99}%
	\usebibmacro{prenote}}
	{\clearfield{url}%
	\clearfield{pages}%
	\clearfield{pagetotal}%
	\clearfield{edition}%
	\clearfield{issn}%
	\clearfield{doi}%
	\usedriver
	{\DeclareNameAlias{sortname}{default}}
	{\thefield{entrytype}}
}
{\multicitedelim}
{\usebibmacro{postnote}}


"""

    contenido_kaoobook = r"""
    
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% kaobook
% LaTeX Class
% Version 0.9.7 (2021/06/02)
%
% This template originates from:
% https://www.LaTeXTemplates.com
%
% For the latest template development version and to make contributions:
% https://github.com/fmarotta/kaobook
%
% Authors:
% Federico Marotta (federicomarotta@mail.com)
% Based on the doctoral thesis of Ken Arroyo Ohori (https://3d.bk.tudelft.nl/ken/en)
% and on the Tufte-LaTeX class.
% Modified for LaTeX Templates by Vel (vel@latextemplates.com)
%
% License:
% LPPL (see included MANIFEST.md file)
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%----------------------------------------------------------------------------------------
%	CLASS CONFIGURATION
%----------------------------------------------------------------------------------------

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{kaobook}[2021/06/02 v0.9.7 kaobook]
\newcommand{\@baseclass}{scrbook} % Base class name

%\RequirePackage{kvoptions} % Manage class key-value options

%\SetupKeyvalOptions{
%    family = kao,
%    prefix = kao@
%}

% Set the default options
\PassOptionsToClass{a4paper}{\@baseclass}
\PassOptionsToClass{fontsize=10pt}{\@baseclass}
\PassOptionsToClass{parskip=half}{\@baseclass}
\PassOptionsToClass{headings=optiontoheadandtoc}{\@baseclass}

% Pass through any other options to the base class
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{\@baseclass}} 

%\ProcessKeyvalOptions*
\ProcessOptions\relax % Process the options

\LoadClass{\@baseclass} % Load the base class

% Define kao-specific options
%\DeclareStringOption[1]{secnumdepth}
\DefineFamily{kao}
\DefineFamilyMember[kaobook]{kao}
\DefineFamilyKey[kaobook]{kao}{secnumdepth}[1]{\setcounter{secnumdepth}{#1}\FamilyKeyStateProcessed}
\FamilyProcessOptions[kaobook]{kao}

\RequirePackage{kao} % Load the code common to all classes

%----------------------------------------------------------------------------------------
%	FRONT-, MAIN-, BACK- MATTERS BEHAVIOUR
%----------------------------------------------------------------------------------------

% Front matter
\let\oldfrontmatter\frontmatter % Store the old command
\renewcommand{\frontmatter}{%
	\oldfrontmatter% First of all, call the old command
	\pagestyle{plain.scrheadings}% Use a plain style for the header and the footer
	\pagelayout{wide}% Use a wide page layout
	\setchapterstyle{plain} % Choose the default chapter heading style
	% \sloppy % Required to better break long lines
}

%------------------------------------------------

% Main matter
\let\oldmainmatter\mainmatter % Store the old command
\renewcommand{\mainmatter}{%
    \oldmainmatter% Call the old command
	\pagestyle{scrheadings}% Use a fancy style for the header and the footer
	\pagelayout{margin}% Use a 1.5 column layout
	\setchapterstyle{kao} % Choose the default chapter heading style
}

%------------------------------------------------

% Appendix
\let\oldappendix\appendix% Store the old command
\renewcommand{\appendix}{%
	\oldappendix% Call the old command
	\bookmarksetup{startatroot}% Reset the bookmark depth
}

%------------------------------------------------

% Back matter
\let\oldbackmatter\backmatter% Store the old command
\renewcommand{\backmatter}{%
	\oldbackmatter% Call the old command
	\bookmarksetup{startatroot}% Reset the bookmark depth
	\pagestyle{plain.scrheadings}% Use a plain style for the header and the footer
	\pagelayout{wide}% Use a wide page layout
	\setchapterstyle{plain} % Choose the default chapter heading style
}

%----------------------------------------------------------------------------------------
%	CHAPTER HEADING STYLES
%----------------------------------------------------------------------------------------

\DeclareDocumentCommand{\setchapterstyle}{m}{%
	\ifthenelse{\equal{plain}{#1}}{\chapterstyleplain}{}
    \ifthenelse{\equal{bar}{#1}}{\chapterstylebar}{}
	\ifthenelse{\equal{lines}{#1}}{\chapterstylelines}{}
    \ifthenelse{\equal{kao}{#1}}{\chapterstylekao}{}
}

% The default definition in KOMA script
\DeclareDocumentCommand{\chapterstyleplain}{}{%
	\renewcommand{\chapterlinesformat}[3]{%
		\@hangfrom{##2}{##3}}
	\renewcommand*{\chapterformat}{%
		\mbox{\chapappifchapterprefix{\nobreakspace}\thechapter%
		\autodot\IfUsePrefixLine{}{\enskip}}}
    \RedeclareSectionCommand[beforeskip=0cm,afterskip=10\vscale]{chapter}
	\setlength{\mtocshift}{-1\vscale}
}

% Gray bar
\DeclareDocumentCommand{\chapterstylebar}{}{%
	\renewcommand*{\chapterformat}{%
		\mbox{\chapappifchapterprefix{\nobreakspace}\thechapter%
		\autodot\IfUsePrefixLine{}{\enskip}}%
	}
	\renewcommand{\chapterlinesformat}[3]{%
		\begin{tikzpicture}[remember picture, overlay]
			\node[
				anchor=south west,
				xshift=\dimexpr - \hoffset - \oddsidemargin - 1in -1mm,%-30\hscale,
				yshift=4.3mm,
				rectangle,
				fill=gray!20!white,
				fill opacity=0.8,
				inner ysep=5\vscale,
				inner xsep=\dimexpr \hoffset + \oddsidemargin + 1in,%30\hscale,
				text opacity=1,
				text width=\paperwidth-40\hscale,
			]{\@hangfrom{##2}{##3}};
		\end{tikzpicture}
	}
    \RedeclareSectionCommand[beforeskip=-55\vscale,afterskip=6\vscale]{chapter}
	\setlength{\mtocshift}{-1\vscale}
}

% Lines
\renewcommand{\hrulefill}[1][0.4pt]{%
	\leavevmode\leaders\hrule height #1\hfill\kern\z@%
}
\DeclareDocumentCommand{\chapterstylelines}{}{%
	\renewcommand*{\chapterformat}{%
		\chapappifchapterprefix{\nobreakspace}\scalebox{3.5}{\thechapter\autodot}%
	}%
	\renewcommand\chapterlinesformat[3]{%
	  %\vspace*{-1cm}%
	  \leavevmode%
	  \makebox[0pt][l]{%
		\makebox[\textwidth][l]{\hrulefill[1pt]##2}%\hfill%\par%\bigskip
		\makebox[\marginparsep][l]{}%
		\makebox[\marginparwidth][l]{}%
	  }\\
	  %\vspace{.5cm}
	  \makebox[0pt][l]{%
		\makebox[\textwidth][l]{##3}%
		\makebox[\marginparsep][l]{}%
		\makebox[\marginparwidth][l]{}%
	  }\\
	  \makebox[0pt][l]{%
		\makebox[\textwidth+\marginparsep+\marginparwidth][l]{\hrulefill[1.1pt]}%
	  }%
	}%
	\RedeclareSectionCommand[beforeskip=0cm,afterskip=10\vscale]{chapter}
	\setlength{\mtocshift}{-1\vscale}%
}

% The Kao style
\DeclareDocumentCommand{\chapterstylekao}{}{%
	\renewcommand*{\chapterformat}{%
		\mbox{\chapappifchapterprefix{\nobreakspace}\scalebox{2.85}{\thechapter\autodot}}%
	}%
	\renewcommand\chapterlinesformat[3]{%
		\vspace{3.5\vscale}%
		\if@twoside%
			\Ifthispageodd{%
				\smash{\makebox[0pt][l]{%
					\parbox[b]{\textwidth}{\flushright{##3}}%
					\makebox[\marginparsep][c]{\rule[-2\vscale]{1pt}{27.4\vscale+\f@size mm}}%
					\parbox[b]{\marginparwidth}{##2}%
				}}%
			}{
				\smash{\makebox[\textwidth][r]{%
					\parbox[b]{\marginparwidth}{\flushright{##2}}%
					\makebox[\marginparsep][c]{\rule[-2\vscale]{1pt}{27.4\vscale+\f@size mm}}%
					\parbox[b]{\textwidth}{\flushleft{##3}}%
				}}%
			}
		\else%
			\smash{\makebox[0pt][l]{%
				\parbox[b]{\textwidth}{\flushright{##3}}%
				\makebox[\marginparsep][c]{\rule[-2\vscale]{1pt}{27.4\vscale+\f@size mm}}%
				\parbox[b]{\marginparwidth}{##2}%
			}}%
		\fi%
	}%
	\RedeclareSectionCommand[beforeskip=0cm,afterskip=10\vscale]{chapter}%
    \setlength{\mtocshift}{-3\vscale}%
}

% Takes as input the image path and optionally the "beforeskip"
\DeclareDocumentCommand{\setchapterimage}{O{55\vscale} m}{%
	\setchapterpreamble[o]{%
		\vspace*{-27\vscale}\hspace*{\dimexpr - \hoffset - \oddsidemargin - 1in}%
		\includegraphics[width=\paperwidth,height=#1+27\vscale,keepaspectratio=false]{#2}%
	}%
    \chapterstylebar%
	% beforeskip=-(figure_height-top_margin)
    \RedeclareSectionCommand[beforeskip=-#1, afterskip=6\vscale]{chapter}%
    \setlength{\mtocshift}{0cm}%
}

% By default start with plain style
\chapterstyleplain

%----------------------------------------------------------------------------------------
%	FONTS AND STYLES
%----------------------------------------------------------------------------------------

% Set KOMA fonts for book-specific elements
\addtokomafont{part}{\normalfont\scshape\bfseries}
\addtokomafont{partentry}{\normalfont\scshape\bfseries}
\addtokomafont{chapter}{\normalfont\bfseries}
\addtokomafont{chapterentry}{\normalfont\bfseries}

% Set KOMA fonts for elements common to all classes
\addtokomafont{section}{\normalfont\bfseries}
\addtokomafont{subsection}{\normalfont\bfseries}
\addtokomafont{subsubsection}{\normalfont\bfseries}
\addtokomafont{paragraph}{\normalfont\bfseries}
\setkomafont{descriptionlabel}{\normalfont\bfseries}

%----------------------------------------------------------------------------------------
%	TOC, LOF & LOT
%----------------------------------------------------------------------------------------

\PassOptionsToClass{toc=listof}{\@baseclass}
\PassOptionsToClass{toc=index}{\@baseclass}
\PassOptionsToClass{toc=bibliography}{\@baseclass}

%----------------------------------------------------------------------------------------
%	NUMBERING
%----------------------------------------------------------------------------------------

%\setcounter{secnumdepth}{\kao@secnumdepth} % Set section numbering 
%depth

\counterwithin*{sidenote}{chapter} % Uncomment to reset the sidenote counter at each chapter
%\counterwithout{sidenote}{chapter} % Uncomment to have one sidenote counter for the whole document


"""

    contenido_kaorefs = r"""
    
\ProvidesPackage{kaorefs}

% Easily label and reference elements
% Note that \label must appear after \caption
% Load this package last

% Pass this package's options to hyperref and varioref
\DeclareOption*{\PassOptionsToPackage{\CurrentOption}{varioref}}
\DeclareOption*{\PassOptionsToPackage{\CurrentOption}{hyperref}}
\DeclareOption*{\PassOptionsToPackage{\CurrentOption}{cleveref}}
\ProcessOptions\relax

\let\thmname\relax % Workaround to get rid of an annoying error
\RequirePackage{varioref}
\RequirePackage{hyperref}
\RequirePackage[capitalise,nameinlink,noabbrev]{cleveref}


% Language-specific strings
% #LANGUAGE
\newcommand{\chapternameshort}{}
\newcommand{\sectionname}{}
\newcommand{\sectionnameshort}{}
\newcommand{\subsectionname}{}
\newcommand{\subsectionnameplural}{}
\newcommand{\subsectionnameshort}{}
\newcommand{\figurenameshort}{}
\newcommand{\tablenameshort}{}
\newcommand{\eqname}{}
\newcommand{\eqnameshort}{}
\newcommand{\defname}{}
\newcommand{\assumname}{}
\newcommand{\thmname}{}
\newcommand{\propname}{}
\newcommand{\lemmaname}{}
\newcommand{\remarkname}{}
\newcommand{\examplename}{}
\newcommand{\exercisename}{}

\addto\captionsdanish{%
  \renewcommand{\chapternameshort}{Kap.}
  \renewcommand{\sectionname}{Sektion}
  \renewcommand{\sectionnameshort}{Sek.}
  \renewcommand{\subsectionname}{Undersektion}
  \renewcommand{\subsectionnameplural}{Undersectioner}
  \renewcommand{\subsectionnameshort}{Undersek.}
  \renewcommand{\figurenameshort}{Fig.}
  \renewcommand{\tablenameshort}{Tab.}
  \renewcommand{\eqname}{Formel}
  \renewcommand{\eqnameshort}{Frml.}
  \renewcommand{\defname}{Definition}
  \renewcommand{\assumname}{Hypotese}
  \renewcommand{\thmname}{Sætning}
  \renewcommand{\propname}{Postulat}
  \renewcommand{\lemmaname}{Hjælpesætning}
  \renewcommand{\remarkname}{Bemærkning}
  \renewcommand{\examplename}{Eksempel}
  \renewcommand{\exercisename}{Øvelse}
}
\addto\captionsenglish{%
  \renewcommand{\chapternameshort}{Chap.}
  \renewcommand{\sectionname}{Section}
  \renewcommand{\sectionnameshort}{Sec.}
  \renewcommand{\subsectionname}{Subsection}
  \renewcommand{\subsectionnameplural}{Subsections}
  \renewcommand{\subsectionnameshort}{Subsec.}
  \renewcommand{\figurenameshort}{Fig.}
  \renewcommand{\tablenameshort}{Tab.}
  \renewcommand{\eqname}{Equation}
  \renewcommand{\eqnameshort}{Eq.}
  \renewcommand{\defname}{Definition}
  \renewcommand{\assumname}{Assumption}
  \renewcommand{\thmname}{Theorem}
  \renewcommand{\propname}{Proposition}
  \renewcommand{\lemmaname}{Lemma}
  \renewcommand{\remarkname}{Remark}
  \renewcommand{\examplename}{Example}
  \renewcommand{\exercisename}{Exercise}
}
\addto\captionsitalian{%
  \renewcommand{\chapternameshort}{Cap.}
  \renewcommand{\sectionname}{Sezione}
  \renewcommand{\sectionnameshort}{Sez.}
  \renewcommand{\subsectionname}{Sottosezione}
  \renewcommand{\subsectionnameplural}{Sottosezioni}
  \renewcommand{\subsectionnameshort}{Sottosezione}
  \renewcommand{\figurenameshort}{Fig.}
  \renewcommand{\tablenameshort}{Tab.}
  \renewcommand{\eqname}{Equazione}
  \renewcommand{\eqnameshort}{Eq.}
  \renewcommand{\defname}{Definizione}
  \renewcommand{\assumname}{Assunzione}
  \renewcommand{\thmname}{Teorema}
  \renewcommand{\propname}{Proposizione}
  \renewcommand{\lemmaname}{Lemma}
  \renewcommand{\remarkname}{Osservazione}
  \renewcommand{\examplename}{Esempio}
  \renewcommand{\exercisename}{Esercizio}
}
% Do you speak other languages? Please, feel free to add the captions!


% Labelling commands
\newcommand{\labpage}[1]{\label{page:#1}}
\newcommand{\labpart}[1]{\label{part:#1}}
\newcommand{\labch}[1]{\label{ch:#1}}
\newcommand{\labsec}[1]{\label{sec:#1}}
\newcommand{\labsubsec}[1]{\label{subsec:#1}}
\newcommand{\labfig}[1]{\label{fig:#1}}
\newcommand{\labtab}[1]{\label{tab:#1}}
\newcommand{\labeq}[1]{\label{eq:#1}}
\newcommand{\labdef}[1]{\label{def:#1}}
\newcommand{\labthm}[1]{\label{thm:#1}}
\newcommand{\labassum}[1]{\label{assum:#1}}
\newcommand{\labprop}[1]{\label{prop:#1}}
\newcommand{\lablemma}[1]{\label{lemma:#1}}
\newcommand{\labremark}[1]{\label{remark:#1}}
\newcommand{\labexample}[1]{\label{example:#1}}
\newcommand{\labexercise}[1]{\label{exercise:#1}}


% Referencing commands
\newcommand{\refpage}[1]{\hyperref[#1]{\pagename}\xspace\pageref{page:#1}} % Page 84
\newcommand{\vrefpage}[1]{\vpageref*{page:#1}} % on the following page, on page 84

% For unnumbered parts
\newcommand{\arefpart}[1]{\hyperref[part:#1]{\partname}\xspace`\nameref{part:#1}'} % Part `Name of the Part'
\newcommand{\avrefpart}[1]{\hyperref[part:#1]{\partname}\xspace`\nameref{part:#1}' \vpageref{part:#1}} % Part `Name of the Part' on page 84

% For numbered parts
\newcommand{\refpart}[1]{\hyperref[part:#1]{\partname}\xspace\ref{part:#1}} % Part IV
\newcommand{\vrefpart}[1]{\hyperref[part:#1]{\partname}\xspace\vref{part:#1}} % Part IV, Part IV on the following page, Part IV on page 84
\newcommand{\nrefpart}[1]{\hyperref[part:#1]{\partname}\xspace\ref{part:#1} (\nameref{part:#1})}
\newcommand{\frefpart}[1]{\hyperref[part:#1]{\partname\xspace\ref{part:#1} (\nameref{part:#1}) \vpageref{part:#1}}} % Part IV (Name of the Part), Part IV (Name of the Part) on the following page, Part IV (Name of the Part) on page 84)

%\newcommand{\refch}[1]{\hyperref[#1]{\chaptername\xspace\usekomafont{chapter}\normalsize\nameref{ch:#1}}\xspace\vpageref{ch:#1}\,}
\newcommand{\refchshort}[1]{\hyperref[ch:#1]{\chapternameshort\xspace\ref{ch:#1}}}
\newcommand{\refch}[1]{\hyperref[ch:#1]{\chaptername\xspace\ref{ch:#1}}}
\newcommand{\vrefch}[1]{\hyperref[ch:#1]{\chaptername\xspace\ref{ch:#1} \vpageref{ch:#1}}}
\newcommand{\nrefch}[1]{\hyperref[ch:#1]{\chaptername\xspace\ref{ch:#1} (\nameref{ch:#1})}}
\newcommand{\frefch}[1]{\hyperref[ch:#1]{\chaptername\xspace\ref{ch:#1} (\nameref{ch:#1}) \vpageref{ch:#1}}}

%\newcommand{\refsec}[1]{Section~{\usekomafont{section}\normalsize\nameref{sec:#1}}\xspace\vpageref{sec:#1}\,}
\newcommand{\refsecshort}[1]{\hyperref[sec:#1]{\sectionnameshort\xspace\ref{sec:#1}}}
\newcommand{\refsec}[1]{\hyperref[sec:#1]{\sectionname\xspace\ref{sec:#1}}}
\newcommand{\vrefsec}[1]{\hyperref[sec:#1]{\sectionname\xspace\vref{sec:#1}}}
\newcommand{\nrefsec}[1]{\hyperref[sec:#1]{\sectionname\xspace\ref{sec:#1} (\nameref{sec:#1})}}
\newcommand{\frefsec}[1]{\hyperref[sec:#1]{\sectionname\xspace\ref{sec:#1} (\nameref{sec:#1}) \vpageref{sec:#1}}}

\newcommand{\refsubsecshort}[1]{\hyperref[subsec:#1]{\sectionnameshort\xspace\ref{subsec:#1}}}
\newcommand{\refsubsec}[1]{\hyperref[subsec:#1]{\subsectionname\xspace\ref{subsec:#1}}}
\newcommand{\vrefsubsec}[1]{\hyperref[subsec:#1]{\subsectionname\xspace\vref{subsec:#1}}}
\newcommand{\nrefsubsec}[1]{\hyperref[subsec:#1]{\subsectionname\xspace\ref{subsec:#1} (\nameref{subsec:#1})}}
\newcommand{\frefsubsec}[1]{\hyperref[subsec:#1]{\subsectionname\xspace\ref{subsec:#1} (\nameref{subsec:#1}) \vpageref{subsec:#1}}}

%\newcommand{\reffig}[1]{{\hypersetup{colorlinks=false}\usekomafont{captionlabel}\hyperref[fig:#1]{Figure}\xspace\ref{fig:#1}}}
\newcommand{\reffigshort}[1]{\hyperref[fig:#1]{\figurenameshort\xspace\ref{fig:#1}}}
\newcommand{\reffig}[1]{\hyperref[fig:#1]{\figurename}\xspace\ref{fig:#1}}
\newcommand{\vreffig}[1]{\hyperref[fig:#1]{\figurename\xspace\vref{fig:#1}}}

%\newcommand{\reftab}[1]{{\hypersetup{colorlinks=false}\usekomafont{captionlabel}\hyperref[tab:#1]{Table}\xspace\ref{tab:#1}}}
\newcommand{\reftab}[1]{\hyperref[tab:#1]{\tablename}\xspace\ref{tab:#1}}
\newcommand{\vreftab}[1]{\hyperref[tab:#1]{\tablename\xspace\vref{tab:#1}}}

\newcommand{\refeqshort}[1]{\hyperref[eq:#1]\eqnameshort\xspace(\ref{eq:#1})}
\newcommand{\refeq}[1]{\hyperref[eq:#1]\eqname\xspace\ref{eq:#1}}
\newcommand{\vrefeq}[1]{\hyperref[eq:#1]\eqname\xspace\vref{eq:#1}}

\newcommand{\refdef}[1]{\hyperref[def:#1]\defname\xspace\ref{def:#1}}
\newcommand{\vrefdef}[1]{\hyperref[def:#1]\defname\xspace\vref{def:#1}}

\newcommand{\refassum}[1]{\hyperref[assum:#1]\assumname\xspace\ref{assum:#1}}
\newcommand{\vrefassum}[1]{\hyperref[assum:#1]\assumname\xspace\vref{assum:#1}}

\newcommand{\refthm}[1]{\hyperref[thm:#1]\thmname\xspace\ref{thm:#1}}
\newcommand{\vrefthm}[1]{\hyperref[thm:#1]\thmname\xspace\vref{thm:#1}}

\newcommand{\refprop}[1]{\hyperref[prop:#1]\propname\xspace\ref{prop:#1}}
\newcommand{\vrefprop}[1]{\hyperref[prop:#1]\propname\xspace\vref{prop:#1}}

\newcommand{\reflemma}[1]{\hyperref[lemma:#1]\lemmaname\xspace\ref{lemma:#1}}
\newcommand{\vreflemma}[1]{\hyperref[lemma:#1]\lemmaname\xspace\vref{lemma:#1}}

\newcommand{\refremark}[1]{\hyperref[remark:#1]\remarkname\xspace\ref{remark:#1}}
\newcommand{\vrefremark}[1]{\hyperref[remark:#1]\remarkname\xspace\vref{remark:#1}}

\newcommand{\refexample}[1]{\hyperref[example:#1]\examplename\xspace\ref{example:#1}}
\newcommand{\vrefexample}[1]{\hyperref[example:#1]\examplename\xspace\vref{example:#1}}

\newcommand{\refexercise}[1]{\hyperref[exercise:#1]\exercisename\xspace\ref{exercise:#1}}
\newcommand{\vrefexercise}[1]{\hyperref[exercise:#1]\exercisename\xspace\vref{exercise:#1}}


% cleveref customisation

% Hyperlink the page reference as well
\let\oldvpageref\vpageref
\renewcommand{\vpageref}[1]{\hyperref[#1]{\oldvpageref{#1}}}

% Remove parentheses around equations
\creflabelformat{equation}{#2\textup{#1}#3}

% Set the refname for subsections
\crefname{subsection}{\subsectionname}{\subsectionnameplural}
\Crefname{subsection}{\subsectionname}{\subsectionnameplural}


"""

    contenido_kaotheorems = r"""
    
\ProvidesPackage{kaotheorems}

\RequirePackage{kvoptions} % Handle package options
\SetupKeyvalOptions{
    family = kaotheorems,
    prefix = kaotheorems@
}

\DeclareBoolOption{framed}

\newcommand{\kaotheorems@defaultbg}{Gray!45!white}
\DeclareStringOption[\kaotheorems@defaultbg]{background}
\DeclareStringOption[\kaotheorems@defaultbg]{theorembackground}
\DeclareStringOption[\kaotheorems@defaultbg]{propositionbackground}
\DeclareStringOption[\kaotheorems@defaultbg]{lemmabackground}
\DeclareStringOption[\kaotheorems@defaultbg]{corollarybackground}
\DeclareStringOption[\kaotheorems@defaultbg]{definitionbackground}
\DeclareStringOption[\kaotheorems@defaultbg]{assumptionbackground}
\DeclareStringOption[\kaotheorems@defaultbg]{remarkbackground}
\DeclareStringOption[\kaotheorems@defaultbg]{examplebackground}
\DeclareStringOption[\kaotheorems@defaultbg]{exercisebackground}

\ProcessKeyvalOptions{kaotheorems}

\let\openbox\relax
\RequirePackage{amsmath} % Improved mathematics
\RequirePackage{amsthm} % Mathematical environments
\RequirePackage{thmtools} % Theorem styles

\ifkaotheorems@framed%
    \RequirePackage{tikz} % Colorful boxes
    \RequirePackage[framemethod=TikZ]{mdframed}

    % Box style
    \mdfsetup{skipabove=\topskip,skipbelow=0pt}%-.5\topskip}
    \mdfdefinestyle{mdfkao}{
    	skipabove=\topskip,
    	skipbelow=\topskip, % Does not work :(
    	rightmargin=0pt,
    	leftmargin=0pt,
    	innertopmargin=7pt,
    	innerbottommargin=3pt,
    	innerrightmargin=5pt,
    	innerleftmargin=5pt,
    	topline=false,
    	bottomline=false,
    	rightline=false,
    	leftline=false,
    	%linewidth=1pt,
    	%roundcorner=0pt,
    	%font={},
    	%frametitlefont={},
    	frametitlerule=true,
    	%linecolor=black,
    	%backgroundcolor=LightBlue,
    	%fontcolor=black,
    	%frametitlebackgroundcolor=LightBlue,
    }

    % Theorem styles
    \declaretheoremstyle[
    	%spaceabove=.5\thm@preskip,
    	%spacebelow=.5\thm@postskip,
    	%headfont=\normalfont\bfseries,%\scshape,
    	%notefont=\normalfont, notebraces={ (}{)},
    	bodyfont=\normalfont\itshape,
    	%headformat={\NAME\space\NUMBER\space\NOTE},
    	headpunct={},
    	%postheadspace={.5em plus .1em minus .1em},
    	%prefoothook={\hfill\qedsymbol}
    ]{kaoplain}
    \declaretheoremstyle[
    	%spaceabove=.5\thm@preskip,
    	%spacebelow=.5\thm@postskip,
    	%headfont=\normalfont\bfseries,%\scshape,
    	%notefont=\normalfont, notebraces={ (}{)},
    	bodyfont=\normalfont\itshape,
    	%headformat={\NAME\space\NUMBER\space\NOTE},
    	headpunct={},
    	postheadspace={.5em plus .1em minus .1em},
    	%prefoothook={\hfill\qedsymbol}
    ]{kaodefinition}
    \declaretheoremstyle[
    	%spaceabove=.5\thm@preskip,
    	%spacebelow=.5\thm@postskip,
    	%headfont=\normalfont\bfseries,%\scshape,
    	%notefont=\normalfont, notebraces={ (}{)},
    	bodyfont=\normalfont\itshape,
    	%headformat={\NAME\space\NUMBER\space\NOTE},
    	headpunct={},
    	postheadspace={.5em plus .1em minus .1em},
    	%prefoothook={\hfill\qedsymbol}
    ]{kaoassumption}
    \declaretheoremstyle[
    	%spaceabove=.5\thm@preskip,
    	%spacebelow=.5\thm@postskip,
    	%headfont=\normalfont\bfseries,
    	%notefont=\normalfont, notebraces={ (}{)},
    	%bodyfont=\normalfont,
    	%headformat={\footnotesize$\triangleright$\space\normalsize\NAME\space\NUMBER\space\NOTE},
    	%headformat={\NAME\space\NUMBER\space\NOTE},
    	headpunct={},
    	postheadspace={.5em plus .1em minus .1em},
    	%refname={theorem,theorems},
    	%Refname={Theorem,Theorems},
    ]{kaoremark}
    \declaretheoremstyle[
    	%spaceabove=.5\thm@preskip,
    	%spacebelow=.5\thm@postskip,
    	%headfont=\normalfont\bfseries,
    	%notefont=\normalfont, notebraces={ (}{)},
    	%bodyfont=\normalfont,
    	%headformat={\NAME\space\NUMBER\space\NOTE},
    	headpunct={},
    	postheadspace={.5em plus .1em minus .1em},
    	%prefoothook={\hfill\qedsymbol}
    	%refname={theorem,theorems},
    	%Refname={Theorem,Theorems},
    ]{kaoexample}
    \declaretheoremstyle[
    	%spaceabove=.5\thm@preskip,
    	%spacebelow=.5\thm@postskip,
    	%headfont=\normalfont\bfseries,
    	%notefont=\normalfont, notebraces={ (}{)},
    	%bodyfont=\small,
    	%headformat={\NAME\space\NUMBER\space\NOTE},
    	headpunct={},
    	postheadspace={.5em plus .1em minus .1em},
    	%prefoothook={\hfill\qedsymbol}
    	%refname={theorem,theorems},
    	%Refname={Theorem,Theorems},
    ]{kaoexercise}

    \theoremstyle{kaoplain}
    \declaretheorem[
    	name=Theorem,
    	style=kaoplain,
    	%refname={theorem,theorems},
    	refname={Theorem,Theorems},
    	Refname={Theorem,Theorems},
    	numberwithin=section,
    	mdframed={
    		style=mdfkao,
            backgroundcolor=\kaotheorems@theorembackground,
    		%frametitlebackgroundcolor=\@theorembackground,
    	},
    ]{theorem}
    \declaretheorem[
    	name=Proposition,
    	%refname={proposition,propositions},
    	refname={Proposition,Propositions},
    	Refname={Proposition,Propositions},
    	sibling=theorem,
    	mdframed={
    		style=mdfkao,
            backgroundcolor=\kaotheorems@propositionbackground,
    		%frametitlebackgroundcolor=\@theorembackground,
    	},
    ]{proposition}
    \declaretheorem[
    	name=Lemma,
    	%refname={lemma,lemmas},
    	refname={Lemma,Lemmas},
    	Refname={Lemma,Lemmas},
    	sibling=theorem,
    	mdframed={
    		style=mdfkao,
            backgroundcolor=\kaotheorems@lemmabackground,
    		%frametitlebackgroundcolor=\@theorembackground,
    	},
    ]{lemma}
    \declaretheorem[
    	name=Corollary,
    	%refname={corollary,corollaries},
    	refname={Corollary,Corollaries},
    	Refname={Corollary,Corollaries},
    	sibling=theorem,
    	mdframed={
    		style=mdfkao,
            backgroundcolor=\kaotheorems@corollarybackground,
    		%frametitlebackgroundcolor=\@theorembackground,
    	},
    ]{corollary}

    \theoremstyle{kaodefinition}
    \declaretheorem[
    	name=Definition,
    	%refname={definition,definitions},
    	refname={Definition,Definitions},
    	Refname={Definition,Definitions},
    	numberwithin=section,
    	mdframed={
    		style=mdfkao,
            backgroundcolor=\kaotheorems@definitionbackground,
    		%frametitlebackgroundcolor=\@theorembackground,
    	},
    ]{definition}

    \theoremstyle{kaoassumption}
    \declaretheorem[
    	name=Assumption,
    	%refname={assumption,assumptions},
    	refname={Assumption,Assumptions},
    	Refname={Assumption,Assumptions},
    	numberwithin=section,
    	mdframed={
    		style=mdfkao,
            backgroundcolor=\kaotheorems@assumptionbackground,
    		%frametitlebackgroundcolor=\@theorembackground,
    	},
    ]{assumption}

    \theoremstyle{kaoremark}
    \declaretheorem[
    	name=Remark,
    	%refname={remark,remarks},
    	refname={Remark,Remarks},
    	Refname={Remark,Remarks},
    	numberwithin=section,
    	mdframed={
    		style=mdfkao,
            backgroundcolor=\kaotheorems@remarkbackground,
    		%frametitlebackgroundcolor=\@theorembackground,
    	},
    ]{remark}

    \theoremstyle{kaoexample}
    \declaretheorem[
    	name=Example,
    	%refname={example,examples},
    	refname={Example,Examples},
    	Refname={Example,Examples},
    	numberwithin=section,
    	mdframed={
    		style=mdfkao,
            backgroundcolor=\kaotheorems@examplebackground,
    		%frametitlebackgroundcolor=\@theorembackground,
    	},
    ]{example}

    \theoremstyle{kaoexercise}
    \declaretheorem[
    	name=Exercise,
    	%refname={example,examples},
    	refname={Exercise,Exercises},
    	Refname={Exercise,Exercises},
    	numberwithin=section,
    	mdframed={
    		style=mdfkao,
            backgroundcolor=\kaotheorems@exercisebackground,
    		%frametitlebackgroundcolor=\@theorembackground,
    	},
    ]{exercise}

    %\renewcommand{\thetheorem}{\arabic{chapter}.\arabic{section}.\arabic{theorem}}
    %\renewcommand{\thetheorem}{\arabic{subsection}.\arabic{theorem}}
    %\renewcommand{\qedsymbol}{$\blacksquare$}
\else

    % Theorem styles
    \declaretheoremstyle[
    	spaceabove=.6\thm@preskip,
    	spacebelow=.1\thm@postskip,
    	%headfont=\normalfont\bfseries,%\scshape,
    	%notefont=\normalfont, notebraces={ (}{)},
    	bodyfont=\normalfont\itshape,
    	%headformat={\NAME\space\NUMBER\space\NOTE},
    	headpunct={},
    	%postheadspace={.5em plus .1em minus .1em},
    	%prefoothook={\hfill\qedsymbol}
    ]{kaoplain}
    \declaretheoremstyle[
    	spaceabove=.6\thm@preskip,
    	spacebelow=.1\thm@postskip,
    	%headfont=\normalfont\bfseries,%\scshape,
    	%notefont=\normalfont, notebraces={ (}{)},
    	bodyfont=\normalfont\itshape,
    	%headformat={\NAME\space\NUMBER\space\NOTE},
    	headpunct={},
    	%postheadspace={.5em plus .1em minus .1em},
    	%prefoothook={\hfill\qedsymbol}
    ]{kaodefinition}
    \declaretheoremstyle[
    	spaceabove=.6\thm@preskip,
    	spacebelow=.1\thm@postskip,
    	%headfont=\normalfont\bfseries,
    	%notefont=\normalfont, notebraces={ (}{)},
    	%bodyfont=\normalfont,
    	%headformat={\footnotesize$\triangleright$\space\normalsize\NAME\space\NUMBER\space\NOTE},
    	%headformat={\NAME\space\NUMBER\space\NOTE},
    	headpunct={},
    	%postheadspace={.5em plus .1em minus .1em},
    	%refname={theorem,theorems},
    	%Refname={Theorem,Theorems},
    ]{kaoremark}
    \declaretheoremstyle[
    	spaceabove=.6\thm@preskip,
    	spacebelow=.1\thm@postskip,
    	%headfont=\normalfont\bfseries,
    	%notefont=\normalfont, notebraces={ (}{)},
    	%bodyfont=\normalfont,
    	%headformat={\NAME\space\NUMBER\space\NOTE},
    	headpunct={},
    	%postheadspace={.5em plus .1em minus .1em},
    	%prefoothook={\hfill\qedsymbol}
    	%refname={theorem,theorems},
    	%Refname={Theorem,Theorems},
    ]{kaoexample}
    \declaretheoremstyle[
    	%spaceabove=.5\thm@preskip,
    	%spacebelow=.5\thm@postskip,
    	%headfont=\normalfont\bfseries,
    	%notefont=\normalfont, notebraces={ (}{)},
    	%bodyfont=\normalfont,
    	%headformat={\NAME\space\NUMBER\space\NOTE},
    	headpunct={},
    	postheadspace={.5em plus .1em minus .1em},
    	%prefoothook={\hfill\qedsymbol}
    	%refname={theorem,theorems},
    	%Refname={Theorem,Theorems},
    ]{kaoexercise}

    \theoremstyle{kaoplain}
    \declaretheorem[
    	name=Theorem,
    	refname={theorem,theorems},
    	Refname={Theorem,Theorems},
    	numberwithin=section,
    ]{theorem}
    \declaretheorem[
    	name=Proposition,
    	refname={proposition,propositions},
    	Refname={Proposition,Propositions},
    	sibling=theorem,
    ]{proposition}
    \declaretheorem[
    	name=Lemma,
    	refname={lemma,lemmas},
    	Refname={Lemma,Lemmas},
    	sibling=theorem,
    ]{lemma}
    \declaretheorem[
    	name=Corollary,
    	refname={corollary,corollaries},
    	Refname={Corollary,Corollaries},
    	sibling=theorem,
    ]{corollary}

    \theoremstyle{kaodefinition}
    \declaretheorem[
    	name=Definition,
    	refname={definition,definitions},
    	Refname={Definition,Definitions},
    	numberwithin=section,
    ]{definition}

    \theoremstyle{kaoremark}
    \declaretheorem[
    	name=Remark,
    	refname={remark,remarks},
    	Refname={Remark,Remarks},
    	numberwithin=section,
    ]{remark}

    \theoremstyle{kaoexample}
    \declaretheorem[
    	name=Example,
    	refname={example,examples},
    	Refname={Example,Examples},
    	numberwithin=section,
    ]{example}

    \theoremstyle{kaoexercise}
    \declaretheorem[
    	name=Exercise,
    	%refname={example,examples},
    	refname={Exercise,Exercises},
    	Refname={Exercise,Exercises},
    	numberwithin=section,
    	mdframed={
    		style=mdfkao,
    		backgroundcolor=\@exercisebackground,
    		%frametitlebackgroundcolor=\@theorembackground,
    	},
    ]{exercise}

    %\renewcommand{\thetheorem}{\arabic{chapter}.\arabic{section}.\arabic{theorem}}
    %\renewcommand{\thetheorem}{\arabic{subsection}.\arabic{theorem}}
    %\renewcommand{\qedsymbol}{$\blacksquare$}
\fi



"""

    with open(main, 'w', encoding='utf-8') as f:
        f.write(contenido_tex)

    with open(archivo_bib, 'w', encoding='utf-8') as f:
        f.write(contenido_bib)

    with open(glosario, 'w', encoding='utf-8') as f:
        f.write(contenido_glosar)

    with open(compile, 'w', encoding='utf-8') as f:
        f.write(contenido_compile)

    with open(kao, 'w', encoding='utf-8') as f:
        f.write(contenido_kao)
    with open(kaobiblio, 'w', encoding='utf-8') as f:
        f.write(contenido_kaobiblio)
    with open(kaobook, 'w', encoding='utf-8') as f:
        f.write(contenido_kaoobook)
    with open(kaorefs, 'w', encoding='utf-8') as f:
        f.write(contenido_kaorefs)
    with open(kaotheorems, 'w', encoding='utf-8') as f:
        f.write(contenido_kaotheorems)

    print(
        f"Carpeta y archivos para el libro '{libro}' creados con éxito.")


# Ejemplo de uso
libro = input("Ingresa el nombre del libro: ")
crear_carpeta_informe(libro)
