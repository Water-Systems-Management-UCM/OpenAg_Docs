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

    Land use, Field, Annual (limited), "LandIQ and DWR `View all years <https://gis.water.ca.gov/app/CADWRLandUseViewer/?page=home>`_, `Statewide downloads 2014 and 2016 <https://data.cnra.ca.gov/dataset/statewide-crop-mapping>`_"
    Crop water demand, Detailed Analysis Unit (DAU), Annual, `DWR Land & Water Use Estimates <https://water.ca.gov/Programs/Water-Use-And-Efficiency/Land-And-Water-Use/Agricultural-Land-And-Water-Use-Estimates>`_
    Crop price, County, Annual, `USDA National Agricultural Statistics Service (NASS) <https://www.nass.usda.gov/>`_ and `CDFA Agricultural Statistics Review <https://www.cdfa.ca.gov/statistics/>`_
    Crop yield, County, Annual, `USDA National Agricultural Statistics Service (NASS) <https://www.nass.usda.gov/>`_ and `CDFA Agricultural Statistics Review <https://www.cdfa.ca.gov/statistics/>`_
    Crop production costs, County/macro-region, Sparse, `UC Davis Cooperative Extension Cost and Return Studies <https://coststudies.ucdavis.edu/en/>`_
    Supply elasticities, , Annual,


Land Use and Crop Groups
-----------------------------
Whereas Delta agriculture contains many commodities, modeling crops individually can pose many challenges in data
availability and overall performance when evaluating cropping patterns. Especially for crops which are grown in low
amounts (small acreage crops), data for prices, yields, production costs and water requirements are often not available.
Information for crop water requirements are derived from crop-specific evapotranspiration coefficients which are rarely
calculated for uncommon commodities, while data for prices and yields from NASS are reported only for crops with enough
production to verify reliability. To reduce the scale of the model and circumnavigate these issues, OpenDAP utilizes a
set of 20 crop categories employed by the Department of Water Resources (DWR) in water efficiency and planning documents
and datasets. Crops are grouped based on several factors – these include crop biophysics (water requirements, family of
crop, etc.), harvest characteristics (how harvest occurs, seasonality considerations, etc.) and most importantly,
expected marginal returns (price multiplied by yield).

After grouping crops by category, each category is assigned a proxy commodity which represents the production economics
of the crop group. The same proxy is used for price and yield information as well as for production costs. Applied water
requirements are reported by DWR at the same category grouping level. The table below summarizes
all categories employed along with the included commodities and proxies. For most cases, the assigned proxy represents
well the overall economics of the crop group because many of the groups are almost exclusively dominated by a single
commodity within the Delta. For example, the “Corn” group contains only a single commodity, and while the “Almonds”
group contains also pistachios, pistachios have very few acres grown in the Delta. The most complex groups are “Orchards”
and “Vegetables”, each of which contain many commodities and are not overly dominated by a single crop by acreage.
In these cases, typically the most dominant crop by acreage is used as a proxy, with the expectation that considerations
taken in grouping reduce the variance in production costs and marginal returns between commodities within groups. Use
of proxies in these complex categories can lead to over- or under-estimation of total value of crop agriculture in the
Delta from all commodities, which should be considered when analyzing economic results from the model. While modeling
all commodities individually would theoretically provide the most accurate representation of the system, this poses
challenges in data availability and model scale along with introducing new solver infeasibilities where crop groups are
too small to effectively allocate land between.

.. csv-table::
    :header: |project_name| Crop, Commodities Included, Proxy Crop
    :widths: 25, 50, 25

    Alfalfa, Alfalfa, Alfalfa hay
    Almonds & Pistachios, "Almond | Pistachio", Almond
    Corn, Corn, Field Corn
    Cotton, Cotton, Cotton
    Cucurbits, "Cucumber | Eggplant | Squash | Gourd | Zucchini | Pumpkin | Melon (various)", Watermelon
    Dry Beans, "Garbanzo Bean | Fava Bean | Pea | Bean (dried)", Dry Bean
    Fresh Tomatoes, Tomato (fresh), Fresh Tomato
    Grain, "Barley | Oat | Triticale | Wheat", Wheat
    Onions & Garlic, "Garlic | Onion", Onion
    Deciduous, "Apple | Apricot | Pear | Cashew | Cherry | Jujube | Nectarine | Peach | Pecan | Persimmon | Plum | Pomegranate | Pomelo | Prune | Quince | Walnut | Stonefruit (various)", Walnut
    Field Crops, "Oilseed | Sorghum | Sudangrass | Sugarcane | Sunflower", Grain silage
    Vegetables, "Arugula | Artichoke | Asparagus | Basil | Blackberry | Blueberry | Bok Choy | Boysenberry | Broccoli | Brussel Sprout | Berry (other) | Cabbage | Cactus | Carrot | Cauliflower | Celery | Chestnut | Chive | Cilantro | Collard | Daikon | Dill | Fennel | Herb (other) | Kale | Leek | Lettuce | Mustard | Okra | Parsley | Parsnip | Pepper | Radish | Rutabaga | Spinach | Strawberry | Turnip | Vegetable (other) | Yam", Asparagus
    Pasture, "Pasture (mixed) | pastureland | rangeland | rye", Pasture
    Potatoes, "Potato | Sweet Potato", Potato
    Processing Tomatoes, Tomato (processing), Processing Tomato
    Rice, Rice, Rice
    Safflower, Safflower, Safflower
    Sugar Beets, Sugarbeet, Sugar beet
    Subtropical, "Avocado | Citrus (other) | Fig | Grapefruit | Kiwi | Kumquat | Lemon | Olive | Orange | Papaya | Tangelo | Tangerine", Olive
    Vineyards, Grape (various), Wine Grapes
