import os


def crear_carpeta_informe(nombre_informe):
    ni = str(nombre_informe).replace(' ', '_')
    # Definimos el nombre de la carpeta y los archivos .tex y .bib
    carpeta = os.path.join("Universidad/Informes", ni)
    archivo_tex = os.path.join(carpeta,  "main.tex")
    archivo_bib = os.path.join(carpeta,  "references.bib")

    # Creamos la carpeta y los archivos
    os.makedirs(carpeta, exist_ok=True)

    contenido_tex = r"""
\documentclass[esp]{../ajceam-class}

\title{}

\shorttitle{}

\author[1]{\'Alvaro M\'endez Rodr\'iguez de Tembleque}

\affil[1]{Universidad Europea de Madrid, Proyecto experimental III, Madrid, España}

\thisvolume{}
\thisnumber{}
\thismonth{}
\thisyear{2023}
\receptiondate{//2023}
\acceptancedate{//2023}
\publicationdate{-}

\espabstract{}

\espkeywords{}

\begin{document}

\maketitle
\thispagestyle{fancy}

\section{Introducci\'on}

\firstword{A}{}

\section{Materiales y métodos}
\subsection{Materiales y montaje}
Los materiales que vamos a utilizar en esta práctica son:
\begin{figure}[H]
  \centering
  \includegraphics[width=0.8\columnwidth]{Images/}
  \caption{Montaje experimental}
  \label{fig:mont}
\end{figure}
\begin{enumerate}
  \item 
\end{enumerate}

\subsection{Método}

\section{Presentaci\'on y an\'alisis de resultados}

En esta sección analizaremos los resultados obtenidos. Estos resultados se encuentran expuestos en el Anexo \ref{an:data}

\section{Conclusiones}
\firstword{A}{}

Aquí escribirías las conclusiones de tu informe.

\insertbibliography{References}

\appendix

\section{Anexo}
\subsection{Cálculo de errores}\label{an:err}

\subsection{Datos}\label{an:data}

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

    with open(archivo_tex, 'w', encoding='utf-8') as f:
        f.write(contenido_tex)

    with open(archivo_bib, 'w', encoding='utf-8') as f:
        f.write(contenido_bib)

    print(
        f"Carpeta y archivos para el informe '{nombre_informe}' creados con éxito.")


# Ejemplo de uso
nombre_informe = input("Ingresa el nombre del informe: ")
crear_carpeta_informe(nombre_informe)
