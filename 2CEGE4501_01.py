#!/usr/bin/env python
# coding: utf-8

# \documentclass[9pt]{beamer}
# 
# \usepackage{lmodern}
# \usepackage{ragged2e}
# \usepackage{amsmath}
# \usepackage{amssymb}
# \usepackage{amsthm}
# \usepackage{enumitem}
# \usepackage{graphicx}
# \usepackage{media9}
# \usepackage{color}
# \usepackage{geometry}
# 
# 
# %\hypersetup{colorlinks=false,linkbordercolor=blue}
# 
# %\usepackage[bookmarks=false,linkcolor=red]{hyperref}
# %
# 
# \setlist{leftmargin=2mm}
# 
# \definecolor{umn_maroon}{RGB}{125,0,25}
# 
# \newcommand{\red}[1]{\textcolor{red}{#1}}
# \newcommand{\blue}[1]{\textcolor{blue}{#1}}
# \newcommand{\black}[1]{\textcolor{black}{#1}}
# \newcommand{\tsp}[1]{\textsuperscript{#1}}
# 
# \setbeamercolor{title}{fg=umn_maroon}
# \setbeamercolor{frametitle}{fg=umn_maroon}
# \setbeamercolor{itemize item}{fg=umn_maroon}
# \setbeamercolor{enumerate item}{fg=umn_maroon}
# \setbeamercolor{itemize subitem}{fg=umn_maroon}
# \setbeamercolor{caption name}{fg=umn_maroon}
# \setbeamercolor{section number projected}{fg=umn_maroon}
# \setbeamercolor{section in toc}{fg=black}
# \setbeamercolor{subsection in toc}{fg=black}
# \setbeamerfont{section in toc}{size=\large}
# 
# \title{\bf \Huge \black{CEGE 4501: Hydrologic Design} \\ \vspace{20mm} \huge Chapter 1: \\ Hydrologic Cycle and Mass Balanace}
# 
# \author{\includegraphics[width=0.45\textwidth]{UMN_logo.png} \\ \vspace{10mm}\small Ardeshir Ebtehaj \\ Department of Civil, Environmental, and Geo-Engineering}
# \setbeamertemplate{caption}[numbered]
# \setbeamertemplate{footline}[page number]
# \setbeamerfont{caption}{size=\scriptsize}
# 
# 
# \graphicspath{{./Figures/}}
# \addmediapath{{./Figures/}}
# %-- footline text
# \setbeamertemplate{footline}[text line]{%
# \parbox{\linewidth}{\vspace*{-8pt}\textcolor{gray}{Hydrology and Design--CEGE 4501, Chapter 1: Hydrologic Cycle and Mass Balance}\hfill\textcolor{gray}{Ardeshir Ebtehaj\hfill\insertpagenumber}}}
# \setbeamertemplate{navigation symbols}{}
# 
# \hypersetup{hidelinks=true, colorlinks=true,urlcolor  = blue, linkbordercolor=blue, pdfborderstyle={/S/U/W 1}}
# 
# 
# 
# \makeatother
# %-- BEGIN DOCUMENT
# 
# \begin{document}
# \thispagestyle{empty}
# \pagenumbering{gobble}
# \begin{frame}
#     \titlepage
# \end{frame}
# 
# %------------------------------------------------------- Outline
# 
# \frame{
# 
# \frametitle{\bf Outline}
# 
# \tableofcontents{}
# }
# \cleardoublepage
# \pagenumbering{arabic}
# %--- FRAME 1
# 
# \section{Water and Human Societies}
# 
# 
# \begin{frame}[t]
# 	\frametitle{\bf Water and Human Societies} \footnotesize
# 	\begin{itemize}
# 	\item<1-> Spread of human populations and formation of civilizations are correlated with the availability of fresh water. The {\bf Mesopotamian civilization}, widely considered as the cradle of civilization, was in the the area between the {\bf Tigris and Euphrates Rivers}. Contemporary distribution of human population in the United State is not an exemption. It is easy to see that the climatology of precipitation somewhat has dictated the density of human population in the US. Most of the biggest cities and economies of the country are in the vicinity of lakes, rivers and estuaries.  
# 	\item<1-> The explained correlation clearly does not come as a surprise because water is an essential element not only for survival of human populations but it is the most critical ingredient for food production, formation of central governance, and thus fundamental to human societies.
# 	\item<1-> \red{{\bf Hydrology}} is the study of water and its transport in all of its phases (i.e., solid, liquid, vapor) across different elements of {\bf hydrosphere}, which is a region between 1 km deep in the lithosphere and 15 km high in the atmosphere. These days, {\it hydrology is a science} and largely focuses on {\bf terrestrial water cycle} in continental and global scales under {\bf natural condition}, without direct human control or intervention, which makes it distinct from classic {\it hydrologic and hydraulic engineering}.
# 	\end{itemize} \vspace{-2mm}
# 	\begin{figure}
# 	\includegraphics[height=0.3\textwidth]{US_population} \hspace{5mm}
# 	\includegraphics[height=0.3\textwidth]{PRISM_30_annual_precip}
# 	\caption{Left: U.S. population density. Right: U.S. mean annual precipitation [mm].}
# 	\end{figure}
# \end{frame}
# 
# 
# \begin{frame}[t]
# 	\frametitle{\bf Water and Human Societies} \footnotesize
# 	\begin{itemize}
# 	\item[] In Minnesota it is easy to see that the population is centered around the metropolitan area of the Twin Cities, which, not surprisingly, is on the confluence of the Mississippi and Minnesota Rivers. Twin Cities are also located in the southeastern portion of the state that receives the most rainfall.  These water resources are essential to the establishment of major populations and the study of hydrology plays a pivotal role in sustaining these populations.
# 	\end{itemize}
# 	\begin{figure}
# 	\includegraphics[width=0.80\textwidth]{Minnesota_WeatherPop} 
# 	\caption{Minnesota population density (left) and the mean annual precipitation [in] (right).}
# 	\end{figure}
# 	
# \end{frame}
# 
# \begin{frame}[t]
# 	\frametitle{\bf Applications of Hydrology} \footnotesize
# 	\begin{itemize}
# 	\item<1->  For engineers, hydrologic knowledge is applied to the use and control of water resources on the land areas of the Earth.
# 	\item<1->  Particular applications include:
# 	\begin{itemize}
# 	\item[-] Design of hydraulic structures
# 	\item[-] Water supply
# 	\item[-] Wastewater treatment 
# 	\item[-] Irrigation, drainage
# 	\item[-] Hydropower, flood and drought control 
# 	\item[-] Navigation and erosion
# 	\item[-] Fish and wildlife protection
# 		\begin{figure}
# 	\includegraphics[height=0.20\textwidth]{hydraulic_struct_01} 
# 	\includegraphics[height=0.20\textwidth]{hydraulic_struct_02} 
# 	\includegraphics[height=0.20\textwidth]{hydraulic_struct_03} 
#       \includegraphics[height=0.20\textwidth]{irrigation_schem}
#       \includegraphics[height=0.20\textwidth]{navigation}
# 	\end{figure}
# 	\end{itemize}
# 	\end{itemize}
# \end{frame}
# 
# 
# \section {Water Resource Management}
# \begin{frame}[t]
#     \frametitle{\bf Water Resource Management: An Interdicsiplinary Science} \footnotesize
#     	\begin{figure}
# 	\includegraphics[width=1\textwidth]{fig_01_001_anot} 
# 	\caption{Components of water resources management (Mays 1996).}
# 	\end{figure}
# \end{frame}
# 
# 
# \section {Water use purposes}
# \begin{frame}[t]
#     \frametitle{\bf Water use purpose} \footnotesize
#     	\begin{figure}
# 	\includegraphics[width=0.90\textwidth]{water_use_01} 
# 	\caption{Water use purposes.}
# 	\end{figure}
# \end{frame}
# 
# \section {Water use in the United States}
# \begin{frame}[t]
#     \frametitle{\bf Water use in the United States} \footnotesize
#     	\begin{figure}
# 	\includegraphics[width=0.55\textwidth]{water_use_03} 
# 	\caption{Water use in the United States in billion gallon per day (bgd). Irrigation and livestock are the largest consumptive users.}
# 	\end{figure}
# \end{frame}
# 
# \section {Hydrologic Cycle}
# 
# \begin{frame}[t]
#     \frametitle{\bf Hydrologic Cycle} \footnotesize
# 	\begin{itemize} 
#        \item Study of the circulation of water between the earth surface and its atmosphere, known as the {\bf hydrologic cycle}, is central to hydrology. The hydrologic cycle explains {\bf flux of water} across different {\bf water reservoirs}. 
#     	\end{itemize}
#    	\begin{figure}[p] 
# 	\includemedia[
# 		label=water_cycle,
# 		width=0.88\textwidth,height=0.5\textwidth,
# 		activate=pageopen,
# 		addresource=A_Tour_of_the_Water_Cycle.mp4,
# 		flashvars={
# 		src=A_Tour_of_the_Water_Cycle.mp4
# 		&volume=0.5}
# 				]{}{StrobeMediaPlayback.swf}
# 
# 	\caption{A simple explanation of hydrologic cycle (Credit: NASA SVS).}
# 	\end{figure}	 
# \end{frame}
# 
# \begin{frame}[t]
#     \frametitle{\bf Water Reservoirs on the Earth} \footnotesize
# 
#     	\begin{figure} \vspace{-1.1cm}
# 	\includegraphics[width=1\textwidth]{Table_1_2_1_Mays} 
# 
# 	\end{figure}
#           \begin{itemize} \vspace{-0.9cm}
#        \item Continental access to freshwater resources: Europe (4-10\%), North America (17-38\%), Africa (5-30\%), Asia (3-44.56\%), South America (17-60\%).
#     	\end{itemize}
# \end{frame}
# \begin{frame}[t]
#     \frametitle{\bf Hydrologic Cycle  and Water  Reservoirs} \footnotesize
#     \begin{itemize}
#     \item[] {\bf Oceans, glaciers, groundwater, soil moisture, lakes, rivers, and atmosphere} are the earth's main water reservoirs. 
#     \item[] Depending on the net outflow ($Q, [\text{L}^3\text{T}^{-1}]$) and volume of these reservoirs ($\forall, [\text{L}^3]$), each has a different {\bf residence time} ($t_r = \forall/Q, [\text{T}]$).  
#     \item[] Residence times of the main water reservoirs are -- ocean ($\sim$2500 yr), groundwater ($\sim$8 yr), lakes and rivers ($\sim$88 days), soil moisture ($\sim$47 days), and atmosphere ($\sim$9 days). Among these reservoirs, atmosphere shows the minimum residence time, an indication of its fast evolving dynamics. Groundwater residence time needs to be taken into consideration for sustainable developments in arid and semi-arid regions. 
#     \end{itemize}
#     	 \begin{figure}[p] 
#         	\includegraphics[height=0.4\textwidth]{storages_HC}
# 	\caption{Hydrologic reservoirs and their approximate volumes [m\tsp3] (right).}
# 	\end{figure}
# \end{frame}
# 
# \begin{frame}[t]
#     \frametitle{\bf Hydrologic Cycle - Processes and Fluxes} \footnotesize
#         \begin{itemize}
#     \item Hydrologic cycle occurs through {\bf water fluxes} across different water reservoirs. Water flux is the mass of water, per unit area and time (e.g., kg\,m\tsp{-2}\,s\tsp{-1}), across the water reservoirs in the hydrosphere. The water fluxes can be in various phases such as vapor, liquid, and/or solid. A conceptual schematic of the fluxes between the Earth's water reservoirs is shown in the following figure.
#     \end{itemize} \vspace{-5mm}
#     	\begin{figure}
# 	\includegraphics[width=0.8\textwidth]{hyd_proc_} \vspace{-0.4cm}
# 	\caption{Hydrologic water cycle and fluxes.}
# 	\end{figure}
# \end{frame}
# 
#    
#     \begin{frame}[t]
#     \frametitle{\bf Hydrologic Cycle - Processes and Fluxes} \footnotesize
#     \begin{itemize}
#     \item {\bf Precipitation:} conversion of atmospheric water to liquid or solid water that reaches the earth's surface.
#     \item {\bf Interception:} refers to precipitation that does not reach the soil, but is intercepted by the leaves, branches of plants and canopy.
#     \item {\bf Infiltration:} downward flux of water at soil surface.
#     \item{\bf Overland flow:} is the portion of rain, snow or irrigation water that is more than the surface infiltration capacity and flows across the land surface and enters into the channel flow.
#     \item{\bf Evapotranspiration:} conversion of surface liquid water to water vapor through combination of direct "evaporation" from the soil/water surfaces and "transpiration" due to the vegetation metabolism.  
#     \item{\bf Interflow:} is the lateral flux of water in shallow depth, above the groundwater table, into the stream flows. 
#     \item {\bf Percolation:} downward flux of water between the soil surface and water table. 
#     \item {\bf Recharge:} downward flux of water at the water table.
#     \item{\bf Baseflow:} lateral flow of groundwater into the stream flows. 
#     \hrule
#     \item {\bf Sublimation:} direct phase change from ice to water vapor. Direct phase change of water vapor to ice is called {\bf deposition}. 
#     \item{\bf Throughfall:} flux of intercepted precipitation water from plants' leaves and stems to the soil surface.
#     \item{\bf Exfiltration:} the upward flux of water in soil layers, mainly due to capillary forces and suction heads in soil textures.
#   
#     \end{itemize}
#     \hrule
#     \end{frame}
# 
# \begin{frame}[t,allowframebreaks]
#     \frametitle{\bf Hydrologic Cycle - Driver} \footnotesize
# 	\begin{itemize} 
#        \item The question still remains--{\bf what causes the hydrologic cycle?} The answer is simple, {\bf solar radiation}. Although the earth is a closed thermodynamic system (no mass exchange with its environment), it is not an isolated system as it exchanges energy with the outer space. This exchange is a consequence of the average solar radiation flux of 342 $W \text{m}^{-2}$ being delivered at the top of Earth's atmosphere. This energy is the driver of the hydrologic water cycle. 
# 	\item Due to the ellipsoidal shape and orbital geometry of earth, the equators receive more energy than polar regions. This differential energy budget  eventually leads to a pressure gradient that circulates the earth atmosphere. The moving air masses transport water vapor from tropical oceans and precipitate them over lands. The precipitation water returns back to the atmosphere and oceans through the explained fluxes and processes such as infiltration, percolation, evapotranspiration, runoff and streamflow.  
# 
#    	\begin{figure}[p] 
# 	\vspace{-2mm}
# 	      \includegraphics[width=0.40\textwidth]{insolation} 
# 
# 	\caption{ A schematic of the differential solar radiation that drives the water cycle (Credit: The COMET Program).} \label{fig:10}
# 	\end{figure}	
# 	\item As explained, the convective motions of air and water masses, in atmosphere, are mainly because of an existing {\bf pressure gradient}.
# 	\item We will discuss in the next chapter that, as a general rule, when the temperature of an air parcel increases at a constant pressure, based on the ideal gas law, its density reduces and vice versa.
# 
# %	\begin{figure}
# %	\includegraphics[width=0.4\textwidth]{atmos_pressure}	\hspace{5mm}
# %	\caption{Pressure decays faster in a cold air column than a warm one.}
# %	\end{figure}	
# 	
# 	\item Therefore, in general, {\bf a cold air mass is denser than a warm air mass} at constant pressure. Because the {\bf air is compressible}, the density of cold air column decays faster than the density of a warm air column from earth surface to higher altitudes. Due to higher pressure of warm air column aloft than the cold air column,  the air flows from warm to cold regions at high elevations (Figure \ref{fig:circ}, left).
# 	\item As the air flows from warm to cold areas, the cold air column becomes heavier and its pressure increases at the surface. As a result, a surface air flow forms from cold to warm areas which eventually gives rise to a circulation pattern (Figure \ref{fig:circ}, right).
# 	
# 	\begin{figure}
# 	\includegraphics[width=0.80\textwidth]{circulation}
# 		\caption{The circulation of the earth's atmosphere is due to formation of a pressure gradient from warm (tropics) to cold (polar regions) air masses.   \label{fig:circ}}
# 	\end{figure}	
# 
# 
# 	\item According to the above simple conceptualization of the atmospheric circulation, one may think of the earth atmospheric circulation as shown below: \vspace{-2mm}
#           \begin{figure}
# 	\includegraphics[height=0.30\textwidth]{globe_single_cell}	\hspace{5mm} 
#       \includegraphics[height=0.30\textwidth]{Hadley_cells} \\ 
# 	\hspace{2mm}
# 	\includegraphics[width=0.45\textwidth]{cells_mod}
# 	\caption{Schematic of a one (top left) and a three-cell model(top-right) for atmospheric circulation. The three-cell model represents the observed Earth's atmospheric circulation pattern.}  \label{fig:11}
# 	\end{figure} \vspace{-5mm}
#      \item However, the one-cell circulation model does not exist because these large eddies are unstable and more importantly there are other forces acting on air parcels that break these large hypothetical eddies apart. This force is the called the \href{https://www.youtube.com/watch?v=dt_XJp77-mk}{Coriolis force}.	
#      \item In simple terms, with respect to the a rotating reference frame, it appears that the Coriolis force is deflecting an object that moves from the center to the perimeter and vice versa.
# 	\begin{figure}
# 	\includegraphics[height=0.22\textwidth]{coriolis_01}	\vspace{-1mm} \hspace{10 mm}
# 		\includegraphics[height=0.2\textwidth]{angular_velocity}
# 	\caption{Coriolis force deflects an object thrown from point A to point B to the right of its path in a counter clockwise rotational system. This force is due to a combined effect of the angular ($\vec{\omega}$) and linear velocity ($\vec{v}$).   \label{fig:disk}}
# 	\end{figure} \vspace{-8mm}
# 
# 	\begin{figure}
# 	\includegraphics[height=0.26\textwidth]{coriolis_02}	\hspace{5mm}
# 	\caption{The Coriolis force deflects air parcels to the right and left of the their moving direction in the Northern and Southern Hemisphere, respectively, for the shown view points. \label{fig:cor_01}}
# 	\end{figure} 
# 
# \item As a result of the Coriolis and pressure gradient forces, those large hypothetical circulation cells (Figure \ref{fig:11}, left) breaks into three smaller cells as shown below. As we know how the Coriolis force deflects air parcel movements, it is easy to conclude that the ``surface'' air flows from mid-latitudes high-pressure areas towards the tropical low-pressure convergence zones are deflected towards east. These surface airflows are called easterlies or trade winds. On the other hand, surface airflows from high-pressure horse latitudes towards polar fronts are deflected to the west and create the westerlies. \vspace{-3mm} 
# 	\begin{figure}
# 	\includegraphics[height=0.34\textwidth]{globe_hadleycell}	\hspace{1mm}
# 	\includegraphics[height=0.38\textwidth]{coriolis_03}	
# 	\caption{Schematic of a three-cell atmospheric circulation model and deflection of airflows in northern and southern hemisphere.  \label{fig:cor_02}}
# 	\end{figure}
# 	
# 	\item In regions within $\pm$5-20 latitudes, the Coriolis force is strong enough to creates cyclonic activities around the high and low pressure areas. Based on the explained Coriolis effect, it is easy to understand that the air flows counter clockwise around lows and clockwise around highs in northern hemisphere. 
# 
# 	\begin{figure}[c]
# 	\includemedia[
# 		label=water_cycle,
# 		width=0.22\linewidth,height=0.22\linewidth,
# 		activate=pageopen,
# 		addresource=low_cd.mp4,
# 		flashvars={
# 		src=low_cd.mp4
# 		&volume=0.5}
# 				]{}{StrobeMediaPlayback.swf} \hspace{10mm}
# 				\includegraphics[width=0.28\textwidth]{lows}
# 	\caption{A schematic of airflow in a low pressure cell, convergence at the surface and divergence aloft. A satellite footage of the \href{https://www.youtube.com/watch?v=ywQBfPtgEOM}{Hurricane Irma} shows its counter clock-wise rotation around a strong low-pressure system.}
# 		\includemedia[
# 		label=water_cycle,
# 		width=0.22\linewidth,height=0.22\linewidth,
# 		activate=pageopen,
# 		addresource=high_cd.mp4,
# 		flashvars={
# 		src=high_cd.mp4
# 		&volume=0.5}
# 				]{}{StrobeMediaPlayback.swf} \hspace{10mm}
# 				\includegraphics[width=0.28\textwidth]{highs}
# 	\caption{A schematic of airflow in a high pressure cell, divergence at the surface and convergence aloft.}
# 	
# 	\end{figure}
# 	
#     	\end{itemize}	
# \end{frame}
# 
# \begin{frame}[t]
#     \frametitle{\bf Water Physical Properties} \footnotesize
# 	\begin{itemize} 
#            \item The unique physical properties of water characterize the hydrologic processes.  Unlike other planets in our solar system, the pressure and temperature found on Earth allow water to occur naturally in all three phases, as shown in the phase diagram below.  This is obvious, especially in areas like Minnesota, where we have rainstorms in summer and snowstorms in the winter. 
#            
# 	\item Due to unique polar structure of water molecules, water has a very high values of {\bf specific heat capacity} ($c_{p}$=4186 J\,kg\tsp{-1}\,K\tsp{-1}\, at \,T=15$^{\circ}$C) and {\bf latent heat of vaporization} ($L_{V}=2.5\times10^{6}$\, J\,kg\tsp{-1}\, at \,T=15$^{\circ}$C)  which have significant effects on our weather and climate systems.
#     	\end{itemize}
#    	\begin{figure}[p] 
# 	\includegraphics[height=0.35\textwidth]{PolarWater}
# 	\hspace{2mm}
# 	\includegraphics[height=0.35\textwidth]{WaterPhaseDiagram.jpg}
# 	\caption{ Polar structure of a water molecule (left).  The water phase diagram showing that water occurs naturally in all three phases on earth (right). At the \href{https://www.youtube.com/watch?v=XEbMHmDhq2I}{triple point}, all three phases of water exist.  }
# 	\end{figure}	
# \end{frame}
# 
# 
# 
# %--------------------------------------------------------------------
# % the following is a working example using VPlayer.swf
# %--------------------------------------------------------------------
# %\begin{frame}[c]
# %\begin{center}
# %\includemedia[
# %	label=water_cycle,
# %	width=0.64\linewidth,height=0.36\linewidth,
# %	activate=pageopen,      
# %    deactivate=onclick,
# %	addresource=water_cycle_01.m4v,
# %	passcontext,
# %	flashvars={
# %	source=water_cycle_01.m4v
# %      &loop=true,
# %			}
# %]{}{VPlayer.swf}
# %\end{center}
# %\end{frame}
# 
# \begin{frame}[t]
#     \frametitle{\bf Water Properties} \footnotesize
# 	\begin{itemize} 
#        \item[-] {\bf Water density:} $\rho_w=1000$ [kg m\tsp{-3}]
#        \item[-] {\bf Ice density:} $\rho_c=917$ [kg m\tsp{-3}]
#        \item[-] {\bf Specific heat capacity:} is the heat $Q$ [J] required to raise the temperature $T$ of the unit mass of a given substance by  one degree of Kelvin, which is $c=Q/(m\,\Delta T)$ [Joule Kg\tsp{-1} K\tsp{-1}] . Depending on the temperature  $5 ^{\circ}\leq T\leq 100^{\circ} C$, the specific heat capacity of water varies between 4180 to 4220 [Joule Kg\tsp{-1} K\tsp{-1}].      
#           	\begin{figure} 
# 	        \includegraphics[width=0.75\textwidth]{water_physic_prop_01}
# 	      \end{figure}	
# 	 \item[-] {\bf Latent heat capacity ($\mathcal L$):} is the heat $Q$ required for phase change of unit mass of a substance, that is $\mathcal{L}=Q/m$. During the phase change, the temperature of the substance remains unchanged.
# 	 \item[]  \hspace{1 cm} Latent heat of vaporization: $\mathcal{L}_{\ell v}=2.5\times10^6$ [J Kg\tsp{-1}]
# 	 \item[] \hspace{1 cm} Latent heat of melting (fusion): $\mathcal{L}_{s\ell}=3.34\times10^5$ [J Kg\tsp{-1}]
# 	 \item[] \hspace{1 cm} Latent heat of sublimation: $\mathcal{L}_{sv}=2.86\times10^6$ [J Kg\tsp{-1}] and thus $\mathcal{L}_{sv} = \mathcal{L}_{s\ell}+\mathcal{L}_{\ell v}$
#    
# 	\begin{figure} 
# 	        \includegraphics[width=0.6\textwidth]{heat_budget_globa}
# 	        \caption{Mean global heat budget at the earth surface in [W m\tsp{-2}], where $R_n$ is the net solar radiation at the surface, $L_eE$ is the latent heat flux and $H$ denotes the sensible heat flux.}
# 	      \end{figure}	
#     	\end{itemize}
# \end{frame} 
#  
# \section{Hydrologic Mass Balance}   
# \begin{frame}[t]
#     \frametitle{\bf Water Budget and Mass Balance} \footnotesize
#     \begin{itemize}
#     \item[] Water budget analysis is extremely important for sustainability of water resources management. Water mass balance analysis in hydrologic systems assesses storage of water in natural or man-made reservoirs and evaluates continuity of water flow across those reservoirs. 
#     \item[] We often use a system approach to explain hydrologic processes. Mass of water parcels is considered as a conserved quantity and a simple mass balance over a system of water storage can be cast as follows: 
#     \item[] \begin{center} \includegraphics[width=0.45\textwidth]{system_hyd} 
#     \includegraphics[width=0.45\textwidth]{res_system}\end{center}
#     \item[] \[\text{accumulation}\,(\Delta S)=\text{Input}\,(I)-\text{Output}(O) \,\,\, \text{[L\tsp{3}]}.\]  
#     \item[] We naturally evaluate the above mass balance equation over a certain of period time $\Delta t$ as:
#     \item[] \[ \frac{\Delta S}{\Delta t}=\frac{I}{\Delta t}-\frac{O}{\Delta t} \qquad  [L^3 \,T^{-1}],\]
#     \item[] Thus we have  \[\frac{\Delta s}{\Delta t}=Q_{in}-Q_{out} \qquad [L\tsp{3}T\tsp{-1}] .\]
#     \item[] In a steady state condition the mass balance reduces to $Q_{in}=Q_{out}$ as $\frac{\Delta s}{\Delta t}\rightarrow 0$. Note that we often express hydrologic flow/fluxes per unit area such as  [m\tsp{3}\,m\tsp{-2}\,s\tsp{-1}]={\bf[{m\,s\tsp{-1}}]} or {\bf [mm\,hr\tsp{-1}]} or {\bf [mm\,day\tsp{-1}]}, which is common for representation of the precipitation or evapotranspiration fluxes. 
#    
#     \end{itemize}
# \end{frame}
#  
# \begin{frame}[t]
#     \frametitle{\bf Reservoir Water Budget} \footnotesize
#     \begin{itemize}
#     \item Review of some important units:
#     \begin{itemize}
#     \item[-] {\bf Length:} 1 [inch]  = 2.54 [cm], 12 [inches] = 1 [ft]
#     \item[-] {\bf Area:} 1 [acre]= $\frac{1}{640}$ [miles\tsp{2}] = 43,560 [ft\tsp{2}] = 4,047 [m\tsp{2}]
#     \item[-] {\bf Volume:} [ac.ft] = 43,560 [ft\tsp{3}] = 1233.5 [m\tsp{3}]
#     \item[-] {\bf Discharge:}  [m\tsp{3}\,s\tsp{-1}] or [\text{cfs}], where 100 [cfs] = 2.83 [m\tsp{3}\,s\tsp{-1}]
#     \end{itemize} \vspace{3mm}
#     \item \begin{center} \includegraphics[width=0.75\textwidth]{mas_bal} \end{center} 
#     \item \[P\,A +Q_{in} + G_{in} -E\,A -Q_{out} -G_{out} = \frac{\Delta S}{\Delta t}\,\,\, \text{ [L\tsp{3} T\tsp{-1}] }\] 
#     \item \[P+\frac{Q_{in}}{A}+\frac{G_{in}}{A}-E -\frac{Q_{out}}{A}-\frac{G_{out}}{A}= \frac{\Delta S}{A \Delta t}\,\,\, \text{[L T\tsp{-1}]}\] 
#     \end{itemize}
# \end{frame}
# 
# \begin{frame}[t]
#     \frametitle{\bf Watershed Water Budget} \footnotesize
# 	\begin{itemize} 
#        \item One crucial step in hydrologic mass balance analysis is defining the boundary or control volume of the system such as a small pond, a large dam or a watershed. 
#        \item A watershed is defined as a locus of all points (pixels of a digital elevation model) on the earth's surface that drain precipitation water to a single point called the "{\bf watershed outlet}". The boundary of a watershed is called the "{\bf divide}". Watersheds can be delineated either manually or automatically using digital elevation models (DEM) and computational algorithms. The size of a watershed can range from a few acres  to millions of square miles (Amazon River Basin) depending on the geomorphologic characteristics of land surfaces and location of the outlet. 
#     	\end{itemize}
#    	\begin{figure}[p] 
# 	\includemedia[
# 		label=water_cycle,
# 		width=0.56\textwidth,height=0.35\textwidth,
# 		activate=pageopen,
# 		addresource=watershed_anim.mp4,
# 		flashvars={
# 		src=watershed_anim.mp4
# 		&volume=0.5
# 		&loop=false}
# 				]{}{StrobeMediaPlayback.swf}
# 	\hspace{2mm}
#         	 \includegraphics[height=0.35\textwidth]{nested_watersheds}
# 	\caption{ A schematic of a watershed and its divide (left, credit: \href{http://fergusonfoundation.org/btw-students/what-is-a-watershed/}{Alice Ferguson Foundation}). A schematic of how watersheds are nested (right, credit: Marsh, 1998, p. 170)}
# 	\end{figure}	 
# \end{frame}
# 
# \begin{frame}[t]
#  \frametitle{\bf Watershed Water Budget} \footnotesize
# \begin{itemize}
# \item {\bf At a global scale}, as earth is a close thermodynamic system, water mass balance at the earth's surface is $\frac{dS}{dt}=P-ET$. In a steady state condition this mass balance leads to $P=ET$. 
# \item Note that the steady state assumption is a function of the time-scale. The above global steady state assumption is valid for sufficiently long period of time such as a year, because evapotranspiration and precipitation are highly dynamic processes that vary significantly in a shorter time scale. However, based on the law of conservation of mass it is easy to conclude that on an annual basis the steady state assumption is reasonable and precipitation and ET are equal. As the time scale increases the accuracy of this mass balance also increase. Observational evidence suggests that the annual rate of both precipitation and ET is approximately 1000 [mm yr\textsuperscript{-1}]. 
# 
# \item {\bf At a watershed scale}, each basin may exchange water mass with its surrounding basins through the underlying groundwater systems. A watershed mass balance can be written as follows: \vspace{-2mm}
# \item \[\frac{dS}{Adt}=P+\frac{G_{in}}{A}-\left(ET+\frac{Q}{A}+\frac{G_{out}}{A}\right)\,\,\, \text{[L\,T\tsp{-1}]}.\]
# \end{itemize}
# \vspace{-4mm}
# \begin{itemize}
# \item After averaging over sufficiently long period of time, for a steady state condition, we have 
# \end{itemize}
# \vspace{-4mm}
# \begin{columns}
# \begin{column}{0.5\textwidth}
# \begin{itemize}
# \item \[P+G_{in}/A=ET+Q/A+G_{out}/A.\]
# \item Long resident time of groundwater implies $G_{in}\approx G_{out}\rightarrow 0$: \vspace{-2mm}
# \item \[ P\approx Q/A+ET \Rightarrow ET\approx P-Q/A.\]
# \item When a storm is occurring, the air humidity is relatively high, which reduces the ET significantly. Assuming  ($\overline{ET}\approx0$), the watershed mass balance can be reduced to \vspace{-2mm}
# \item \[ P\approx Q/A.\]
# \end{itemize}
# \end{column}
# \begin{column}{0.4\textwidth}
# \begin{center} \includegraphics[width=0.55\textwidth]{watershed_mass_bal}\end{center}
# \end{column}
# \end{columns}
# \end{frame}
# 
# 
# \begin{frame}[t]
#     \frametitle{\bf Hydrologic Cycle and Satellites} \footnotesize
#     \begin{itemize}
#     \item Remote sensing has provided new insights for deeper understanding of hydrologic cycle in the past few decades. \href{https://www.youtube.com/watch?v=oaDkph9yQBs}{Satellites}, including those launched by NASA, have provided invaluable information about global land and sea surface temperatures (e.g., Advanced Very High Resolution Radiometer, AVHRR), atmospheric moisture (e.g., Atmospheric Infrared Sounder, AIRS), precipitation (e.g., Global Precipitation Measuring, GPM), snow (e.g., Special Sensor Microwave Imager/Sounder, SSMI/S), soil moisture (e.g., Soil Moisture Active Passive satellite, SMAP), vegetation coverage (e.g., Moderate-Resolution Imaging Spectroradiometer, MODIS ), and even changes in ground water elevation (e.g., Gravity Recovery and Climate Experiment, GRACE).
#     \end{itemize}
# 
# %	\begin{figure}[c]
# %	\includemedia[
# %		width=0.75\linewidth,height=0.4218\linewidth, % 16:9
# %		activate=pageopen,
# %		flashvars={
# %		modestbranding=1 % no YT logo in control bar
# %		&autohide=1 % controlbar autohide
# %		&showinfo=0 % no title and other info before start
# %		&rel=0         % no related videos after end
# %				}
# %				]{}{https://www.youtube.com/watch?v=oaDkph9yQBs?rel=0}
# %		\caption{A sophisticated explanation of hydrologic water cycle: insights from space-based remote sensing (credit: NASA Goddard).}
# %	\end{figure}
#       \begin{figure}
# 	\includegraphics[width=0.8\columnwidth]{NASA_Earth-Missions}
# 	\caption{\tiny NASA Earth Science Division Operating Missions -- 2019.}
# 	\end{figure}
# \end{frame}
# 
# 
# 
# 
#  \section{Hydrologic Hazards}   
#  \begin{frame}[t]
#     \frametitle{\bf Hydrologic Hazards} \footnotesize
#         \begin{itemize}
#     \item {\bf Floods:}  Flood prediction and management is an important topic in hydrologic engineering. A flood is an overflow of water that submerges land surfaces that are usually dry. Flooding may occur as an overflow of water from water bodies, such as  rivers, lakes, or oceans.
#     \end{itemize}
#     	\begin{figure}
# 	\includegraphics[width=0.7\textwidth]{Cambodia-flooding}
# 	\caption{\tiny These images on 17 May and 24 October 2013, show the impact of Typhoon Nari and heavy seasonal rainfall on Cambodia's Mekong and Tonle Sap Rivers. More than half a million people were affected by the flood and more than 300,000 hectares of rice fields were destroyed.}
# 	\end{figure}
# \end{frame}
#  
#   \begin{frame}[t]
#     \frametitle{\bf Floods in U.S.} \footnotesize
#         \begin{itemize} 
#     \item[\bf o] California Flooding - February 2017: Heavy, persistent rainfall across northern and central California created substantial property and
# infrastructure damage from flooding, landslides and erosion. Notable impacts include severe damage to the Oroville Dam spillway, which caused a
# multi-day evacuation of 188,000 residents downstream. Excessive rainfall also caused flood damage in the city of San Jose, as Coyote Creek
# overflowed its banks and inundated neighborhoods forcing 14,000 residents to evacuate. Total Estimated Costs: \$1.5 Billion; 5 Deaths
# \item[\bf o] Louisiana Flooding - August 2016: A historic flood devastated a large area of southern Louisiana resulting from 20 to 30 inches of rainfall over
# several days. Watson, Louisiana received an astounding 31.39 inches of rain from the storm. Two-day rainfall totals in the hardest hit areas have a
# 0.2\% chance of occurring in any given year: a 1 in 500 year event. More than 30,000 people were rescued from the floodwaters that damaged or
# destroyed over 50,000 homes, 100,000 vehicles and 20,000 businesses. This is the most damaging U.S. flood event since Superstorm Sandy
# impacted the Northeast in 2012. Total Estimated Costs: \$10.0 (\$10.3) Billion; 13 Deaths
# \item[\bf o] Texas and Oklahoma Flooding and Severe Weather - May 2015: A slow-moving system caused tremendous rainfall and subsequent flooding to
# occur in Texas and Oklahoma. The Blanco river in Texas swelled from 5 feet to a crest of more than 40 feet over several hours causing considerable
# property damage and loss of life. The city of Houston also experienced flooding which resulted in hundreds of high-water rescues. The damage in
# Texas alone exceeded 1.0 (1.1) billion. There was also damage in other states (KS, CO, AR, OH, LA, GA, SC) from associated severe storms. Total
# Estimated Costs: \$2.5 (\$2.6) Billion; 31 Deaths
# \item[\bf o] Northern Plains Flooding - Spring 1997: Severe flooding in North Dakota, South Dakota and Minnesota due to heavy spring snow melt. This
# flooding caused widespread damage to agriculture, infrastructure, homes and businesses. Total Estimated Costs: \$3.7 (\$5.7) Billion; 11 Deaths
# \item source: \url{https://www.ncdc.noaa.gov/billions/events.pdf}
#     \end{itemize}
# \end{frame}
# 
# 
#  \begin{frame}[t]
#     \frametitle{\bf Hydrologic Hazards} \footnotesize
#         \begin{itemize}
#     \item {\bf Droughts:} Droughts continue to be one of the most severe weather-related problems in the world.
#     \begin{itemize}
#     \item[-] Meteorological droughts -- lack of precipitation 
#     \item[-] Agricultural droughts -- lack of soil moisture
#     \item[-] Hydrological droughts -- reduced stream flow and groundwater levels
#     \end{itemize}
#     \end{itemize}
#     	\begin{figure}
# 	\includegraphics[width=0.7\textwidth]{drought_sat}
# 	\caption{\tiny California Drought: left image is on Jan 2014 and right image is on Jan 2017}
# 	\end{figure}
# \end{frame}
# 
#  \begin{frame}[t]
#     \frametitle{\bf Hydrologic Hazards} \footnotesize
#         \begin{itemize}
#     \item {\bf Droughts:} Droughts continue to be one of the most severe weather-related problem around the world.
#     \begin{itemize}
#     \item[-] Meteorological droughts -- lack of precipitation 
#     \item[-] Agricultural droughts -- lack of soil moisture
#     \item[-] Hydrological droughts -- reduced stream flow and groundwater levels
#     \end{itemize}
#     \end{itemize}
#     	\begin{figure}
# 	\includegraphics[width=0.7\textwidth]{ca_drought}
# 	\caption{\tiny California Drought in 2014---a closer look.}
# 	\end{figure}
# \end{frame}
#  
#  
#    \begin{frame}[t]
#     \frametitle{\bf Droughts in U.S.} \footnotesize
#         \begin{itemize} 
#         
#     \item[\bf o] Western Drought - 2014: Historic drought conditions affected the majority of California for all of 2014 making it the worst drought on record for the
# state. Surrounding states and parts of Texas, Oklahoma and Kansas also experienced continued severe drought conditions. This is a continuation of
# drought conditions that have persisted for several years. Total Estimated Costs: \$4.0 (\$4.2) Billion; 0 Deaths
#     
#     \item[\bf o] U.S. Drought/Heatwave - 2012: The 2012 drought is the most extensive drought to affect the U.S. since the 1930s. Moderate to extreme drought
# conditions affected more than half the country for a majority of 2012. The following states were affected: CA, NV, ID, MT, WY, UT, CO, AZ, NM, TX,
# ND, SD, NE, KS, OK, AR, MO, IA, MN, IL, IN, GA. Costly drought impacts occurred across the central agriculture states resulting in widespread
# harvest failure for corn, sorghum and soybean crops, among others. The associated summer heatwave also caused 123 direct deaths, but an estimate
# of the excess mortality due to heat stress is still unknown. Total Estimated Costs: \$30.0 (\$32.4) Billion; 123 Deaths
# \item[\bf o] Southern Plains/Southwest Drought \& Heat Wave - Spring-Summer 2011: Drought and heat wave conditions created major impacts across
# Texas, Oklahoma, New Mexico, Arizona, southern Kansas, and western Louisiana. In Texas and Oklahoma, a majority of range and pastures were
# classified in "very poor" condition for much of the 2011 crop growing season. Total Estimated Costs: \$12.0 (\$13.3) Billion; 95 Deaths
# 
# \item source: \url{https://www.ncdc.noaa.gov/billions/events.pdf}
# \item \url{http://droughtmonitor.unl.edu/MapsAndData/MapArchive.aspx}
#     \end{itemize}
# \end{frame}
# 
# \section{Hydrologic Sustainability}  
#  \begin{frame}[t]
#     \frametitle{\bf Hydrologic Sustainability} \footnotesize
#         \begin{itemize}
#     \item {\bf Sustainable development} is the development that can meet the needs for the present generation without compromising the ability of future generation to meet their own needs. 
#     \item {\bf Hydrologic sustainability} refers to engineering and management practices that enable us and ecosystem to have access to water in sufficient quantity and quality at present without compromising the ability of future generation to meet their own needs to freshwater resources. \vspace{5mm}
#     \item \centering {\bf {\normalsize Challenges to sustainability:}}
#     \begin{columns}
#     \begin{column}{0.50\textwidth}
#     \begin{itemize} \scriptsize
#     \item {\bf Urbanization:} By 2050 more than 9 billion people will live on the Earth. Now we have more than 22 cities with more than 10 million inhabitants. The challenges are related to water supply, drainage, waste and storm water collection and treatment. The excessive demand exerts immense pressure on our natural water resources systems. 
#     \item {\bf Climate Change:} A change in the state of climate that can be identified by changes in the mean and/or variability of its properties that can persist for an extended period of time -- typically decades or longer (IPCC). The climate system consists of five major components: the atmosphere, the hydrosphere, the cryosphere, the land surface, and the biosphere. These subsystems are influenced largely by the human activity and extraterrestrial sources such as the Sun. \url{https://www.esrl.noaa.gov/gmd/ccgg/trends/full.html} 
#     \end{itemize}
#     \end{column}
#     \begin{column}{0.5\textwidth}
#       \begin{figure}
# 	\includegraphics[width=1.1\columnwidth]{clim_pacific}
# 	%\caption{\tiny California Drought: zoom in!!}
# 	\end{figure}
# 	\end{column}
# 	\end{columns} \vspace{5 mm}
# 	\item \bf Sustainability of hydrologic systems can be quantified in terms of their water mass balance.
#     \end{itemize}
# \end{frame}
# 
# 
# 
# \begin{frame}[t]
#     \frametitle{\bf Lack of the Hydrologic Mass Balance} \footnotesize
#     \begin{itemize}
#     \item Lake Urmia is a prime example of a water body with an imbalanced water budget. The Urmia lake, once was the sixth largest saltwater lake on earth has shrunk to 10\% of its original size in recent decade, mainly due to damming (less inflow) and excessive groundwater withdrawals (more outflow) for agricultural water use. The following animation shows shrinkage of the lake surface from 1984-2014. We can see that how a simple mass balance problem can have significant unforeseen ramifications for regional ecology and human population. 
#     \end{itemize}
# 	\begin{figure}[c]
# 	\includemedia[
# 		label=water_cycle,
# 		width=0.8\linewidth,height=0.45\linewidth,
# 		activate=pageopen,
# 		addresource=Urmia_lake_drought.mp4,
# 		flashvars={
# 		src=Urmia_lake_drought.mp4
# 		&volume=0.5
# 		&loop=true}
# 				]{}{StrobeMediaPlayback.swf}
# 	\caption{Lake Urmia (area: 5200 km\tsp{2}) in north west of Iran has been shrinking in the past decades due unsustainable regional water resource management (credit: NASA).}
# 	\end{figure}
# \end{frame}
# 
# \begin{frame}[t]
#     \frametitle{\bf Lack of the Hydrologic Mass Balance} \footnotesize
#     \begin{itemize}
#     \item Formerly one of the four largest lakes in the world with an area of 68,000 km2 (26,300 sq mi), the \href{https://www.youtube.com/watch?v=FzvEW1FHc60}{Aral Sea} has been steadily shrinking since the 1960s after the rivers that fed it were diverted by Soviet irrigation projects. By 1997, it had declined to 10\% of its original size.
#     \end{itemize}
# %	\begin{figure}[c]
# %	\includemedia[
# %		width=0.75\linewidth,height=0.4218\linewidth, % 16:9
# %		activate=pageopen,
# %		flashvars={
# %		modestbranding=1 % no YT logo in control bar
# %		&autohide=1 % controlbar autohide
# %		&showinfo=0 % no title and other info before start
# %		&rel=0         % no related videos after end
# %				}    % https://www.youtube.com/v/oaDkph9yQBs?rel=0
# %				]{}{https://www.youtube.com/v/FzvEW1FHc60?rel=0}
# %		\caption{Aral Sea: Man-made environmental disaster - BBC News}
# %	\end{figure}
#     	\begin{figure}
# 	\includegraphics[width=0.9\textwidth]{Aral_Sea}
# 	\caption{\tiny Shrinkage of the Aral Sean from 1960 to 2014. }
# 	\end{figure}
# 
# \end{frame}
# 
# 
# 
# \end{document}

# In[ ]:




