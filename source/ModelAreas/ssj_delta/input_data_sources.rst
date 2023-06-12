.. _SSJDeltaModelInputsDoc:

SSJ Delta Input Data and Processing
======================================

.. contents::
    :local:

Summary of Data
-------------------
The Open Delta Agricultural Production Model employs data on land use, cost of production, price, yield and applied water to estimate profit-maximizing patterns of Delta crops under varying conditions (Medellin-Azuara et al., 2018). Data for these inputs are available in tabular and shapefile formats from various state and federal agencies and University of California crop Cost and Return studies. The model uses GIS crop acreage shapefiles to generate a tabular dataset of 2014-2017 crop acreages in defined Delta regions. Analysis of raw model input data yields results which may indicate needs for additional quality control. For example, some widely planted commodities such as corn, alfalfa, and pasture crops may produce borderline or negative net returns on farming, whereas some vegetable crops such as cucurbits (gourds) and potatoes show higher marginal profits, yet these represent a relatively small proportion of the total irrigated area in the Delta. These wide ranges in expected returns may be explained by factors not captured by model, such as market behavior or impacts of resolving commodity level data to crop groups. The model is best served for determining economically optimal solutions to cropping distributions, while utilizing observed patterns as a constraint on adaptation to prevent overspecialization. Model outputs include land allocation, water use, net revenues and estimated agricultural land value.

Results show that corn, pasture and alfalfa are the top crop commodities grown in the Delta by irrigated area. Yet these top crops (corn, alfalfa and pasture) make up a relatively small portion of overall value despite dominating the available cropping area. Additionally, these crops consume over 50% of the agricultural water used in the Delta while high value crops yield high returns with a much lower water footprint. Vineyards and tomatoes provide the highest gross revenues, combining to constitute roughly 30-40% of overall value.

Summary of Inputs
--------------------------
The following table summarizes data sources used for defining model inputs for the Washington State :ref:`model area <ModelAreasDoc>`.

.. csv-table::
    :header: "Data", Spatial Resolution, Temporal Resolution, Source

    Land use, Field, Annual, "LandIQ and DWR `View all years <https://gis.water.ca.gov/app/CADWRLandUseViewer/?page=home>`_, `Statewide downloads 2014 and 2016 <https://data.cnra.ca.gov/dataset/statewide-crop-mapping>`_"
    Crop water demand, Detailed Analysis Unit (DAU), Annual, `DWR Land & Water Use Estimates <https://water.ca.gov/Programs/Water-Use-And-Efficiency/Land-And-Water-Use/Agricultural-Land-And-Water-Use-Estimates>`_
    Crop price, County, Annual, `USDA National Agricultural Statistics Service (NASS) <https://www.nass.usda.gov/>`_ and `CDFA Agricultural Statistics Review <https://www.cdfa.ca.gov/statistics/>`_
    Crop yield,
    Crop production costs,
    Supply elasticities, , Annual,
