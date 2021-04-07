# Soil Resistivity Prediction in South Africa: 
## Using Decision Trees for Improving The Design Process of Overhead Power Line Tower Earth Electrodes
> Read the full report [here](https://github.com/ruankie/soil-resistivity-prediction/blob/main/report.pdf).


## Project Overview
Soil resistivity measurements are required for the
earth electrode design of many structures like telecommunication
towers, photovoltaic power plants, and overhead power lines to
comply with design standards. For long lines of high voltage
overhead power lines, this may require the laborious task of soil
resistivity measurement at every tower site as well as a multistep
iterative design and construction process. As part of the
initial design phase, time and money can be saved by having a
model that predicts the soil resistivity based on freely available
geospatial data. 

In this study, the feasibility of this soil resistivity
prediction was investigated. This was done using descision trees
trained on geospacial data such as bedrock depth, runoff, relief
index, and biome type. The accuracy of the models produced
in this study were between 48% and 54%. 

The lack of accuracy was likely due to the limited size of the
data set used. This led to the hypothesis space becoming too
restricted for the decision trees to make accurate predictions
and a need to reduce the amount of predictor variables used
to train them. 

To improve on this study, the most important aspect is
to increase the data set size used for training and testing
the decision trees. This would allow the addition of more
predictor variables to the models which might lead to increased
discrimination power and more accurate predictions.
Alternatively, other machine learning methods that might
be better suited for use in restricted hypothesis spaces can be
tested on this data set.


## Backgroud
Soil resistivity is an electrical property of soil which describes
to what extent it resists electric current flowing through
it [1]. The earth electrode design of many structures like
telecommunication towers [2], photovoltaic power plants [3],
and overhead power lines [4], [5] are dependent on the soil
resistivity at the location where they will be constructed.

In the case of high voltage overhead power transmission
lines for example, the tower foot resistance must be below
a specific value to comply with design standards. In South
Africa the towers of a 400 kV power line must have a tower
foot resisance of below 40 Ω [4]. This tower foot resistance
depends highly on the local soil resistivity at the tower. Due
to high soil resistivity at the location of construction of some
of these towers, this design value is sometimes not met after
the first design iteration [2], [4].

Towers that are found not to comply with the design
standard have to be modified or retrofitted after the initial
setup and construction to reduce the tower foot resistance to a
satisfactory level. This requires a lot of extra time and money
to fix. In some cases the towers need to be addressed on an
individual basis and a unique re-design or updated design is
required for each one [4].

The iterative design process just described includes many
stages: These include the initial design and construction of
the towers; the measurement of tower foot resistances for
each tower after initial construction to see if it is below the
design requirement; the re-design and modification of some
of the towers that did not meet the requirement; and finally,
after modifications are made, follow-up tower foot resistance
measurements to see if the modifications were adequate [2], [4].

This process can be improved and the number of steps
in this process can be reduced if reliable soil resistivity
information was available without having to do physical measurements.
The focus of this paper is to evaluate the feasibility
of soil resistivity prediction in South Africa for this purpose.
If the soil resistivity can be reliably predicted, the initial route
layout and design of overhead power transmission lines can be
adjusted so that no re-design and modification is required later
on which will save time and money. For this study, prediction
of soil resistivity was done by using freely available geospaial data.

The machine learning method selected for relating this
geospatial data (input features) to soil resistivity (target variable)
was the decision tree. Decision trees were used for this
purpose mainly because of the human readability of their
output. The hypothesis of a decision tree is represented as
a series of if-then rules [6]. This is advantageous from an
engineering design point of view since design decisions need
to be transparent and clearly supported.
At the time of writing, no other methods were found in
literature that attempted soil resistivity prediction with machine
learning methods. Especially for imporving the design
process of overhead power lines.


## Acknowledgement
This work was funded by the DSI-NICIS National e-Science
Postgraduate Teaching and Training Platform (NEPTTP).
Some of the soil resistivity data which the CDEGS soil models
were constructed from was kindly shared by: Barry Reid from
Royal Haskoning DHV; Gary Thoresson from The Testing
Guys; Ivan Grobbelaar from DEHN Africa; Johann Rossouw
from EPCM Solutions; Dr. Pieter Pretorius from Terratech;
Theunus Marais from Eskom; and Trevor Manas from LP
Concepts.


## References
### Literature
* [1] M. Kizlo, A. Kanbergs, ''The Causes of the Parameters Changes of Soil Resistivity, the causes of the parameters changes of soil resistivity.''
	Electrical, Control and Communication Engineering 25.25, 2009, pp. 43-46.

* [2] L. W. Choun, C. Gomes, M. Z. A. Ab Kadir, W. F. Wan Ahmad, ''Analysis of earth resistance of electrodes and soil resistivity at different environments,'' 	
	2012 International Conference on Lightning Protection (ICLP), Vienna, 2012, pp. 1-9, doi: 10.1109/ICLP.2012.6344314.

* [3] P. H. Pretorius, ''Loss of equipotential during lightning ground potential rise on large earthing systems,'' 
	2018 IEEE International Symposium on Electromagnetic Compatibility and 2018 IEEE Asia-Pacific Symposium on Electromagnetic Compatibility (EMC/APEMC), Singapore, 2018, pp. 793-797, doi: 10.1109/ISEMC.2018.8393890.

* [4] P. H. Pretorius, B. Ntshuntsha, S. Ramadhin, ''Application of counterpoise in the reduction of tower footing resistance - low frequency design and case study,'' 
	Cigre Symposium Cape Town - 2015, South Africa, Session 9 – Paper 7, 2015.

* [5] Jinxi Ma, F. P. Dawalibi and W. Ruan, ''Design Considerations of HVDC Grounding Electrodes,'' 
	2005 IEEE/PES Transmission & Distribution Conference & Exposition: Asia and Pacific, Dalian, 2005, pp. 1-6, doi: 10.1109/TDC.2005.1546811.

* [6] T. M. Mitchell, ''Machine learning,'' Singapore: McGraw-Hill, 1997, pp. 52-80.

* [7] IEEE Guide for Measuring Earth Resistivity, Ground Impedance, and Earth Surface Potentials of a Grounding System, 
	in IEEE Std 81-2012 (Revision of IEEE Std 81-1983), vol., no., pp.1-86, 28 Dec. 2012, doi: 10.1109/IEEESTD.2012.6392181.

### Data Sets
* Department of Agriculture, Fisheries and Forestry - South African Environmental GIS Data, ''Soil and Terrain Database (SOTER) for South Africa,'' 
	March 17, 2020, Distributed by Open Africa.
	https://africaopendata.org/dataset/department-of-agriculture-fisheriesand-forestry-south-african-environmental-gis-data

* International Soil Reference and Information Centre (ISRIC) - Soil and Terrain (SOTER) database programme, ''Environmental GIS Data,'' 
	November 17, 2015, Distributed by ISRIC Data Hub.
	https://data.isric.org/geonetwork/srv/eng/catalog.search#/metadata/c3f7cfd5-1f25-4da1-bce9-cdcdd8c1a9a9