.. index::
    triple: delta; model area; data sources

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
    Supply elasticities, , Annual, County Ag Commissioner Reports


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


Region Boundaries and Land Use
---------------------------------
Adaptation of Delta Region Boundary Layers
____________________________________________
The original Delta island boundaries shapefile provided by the Delta Stewardship Council contained some empty space within the DWR Legal Delta Boundary, in which sections of the Delta not considered “islands” were not covered by polygons. To ensure inclusion of these areas in the agricultural model, polygons are created in each of the blank spaces and aggregated into three separate polygons for southern, middle and northern regions.

Intersecting Delta Regions with Cropped Polygons
_________________________________________________
The land use shapefiles for each year (sourced from DWR/Land IQ) are clipped to fit within the DWR Legal Delta Boundary. The resulting layer subset is then intersected with the Delta Island Boundaries layer to yield the observed cropping pattern by island. In order to process the data, the area was then calculated via the geoprocessing tool to calculate geometry for each individual polygon. The final shapefile for each year is then exported from a GIS program to a comma separated value (.csv) file for postprocessing.

Land Use
____________
Land use data is obtained by bridging commodities to crop groups and assigning each region in the study area a unique Delta region code. The “ACRES” attribute in the employed Land IQ dataset is then cross-referenced with the calculated area of each polygon to ensure acreage data is not over-projected; if the calculated polygon area is less than the attribute area, then the polygon area is used to prevent discrepancies in the physical land available for farming. Final acres by crop group are aggregated for each region and exported for use as model inputs.
When assigning crop groups, care was taken to ensure that crops with prominent acreages and/or revenue were separated into their own respective groups. Turf, eucalyptus and nursery trees were excluded from the totals as they are not considered traditional agricultural products and prove challenging to accurately model (see section 3.3). Double cropping was included in total acreage and revenue, consisting primarily of small grains grown on fields that are typically fallowed.

Costs of Production
______________________
Production costs are broken into five major cost categories: land rental, labor, supplies, establishment (if applicable), and water. Proxy crops are assigned to each crop group and costs are obtained from UC Davis Cost and Return studies pertinent to that proxy group (see Table A3 of the appendix). Costs are inflated or deflated from the study year to 2015 dollars using Equation :math:numref:`eq1`:

.. math:: C_{2015} = C_n(1-I_n)
    :label: eq1

where :math:`C_{2015}` is the cost in 2015 dollars, :math:`C_n` is the nominal cost in the study year, n, and :math:`I_n` is the cumulative inflation rate between year n and 2015.

Costs in the current model version draw information from several studies and employ an average cost for each major cost type based on the post-inflation value across all studies utilized (see Table A3 of the appendix for a full list of all studies by crop group). Water is assumed to cost $10/AF as a baseline. Current cost assessments do not include annualized establishment costs; however, data is available to include this category in future economic modeling that considers annualized capital costs.

Crop Prices and Yields
________________________
Price and yield information for the selection of crops in the model are obtained by bridging commodities to crop groups and bridging from island to county. County level data for price and yield by year from the National Agricultural Statistics Service (NASS) is then assigned to each crop by island based on the bridging procedures. In cases where county-specific data was unavailable for the proxy crop, an average value for other counties intersecting the study region was substituted. For complex crop groups such as deciduous fruits and truck crops, a proxy crop is chosen to represent the group (see Table A2 of the Appendix). Prices are shown in 2015 dollars following methods analogous to those used for costs (:math:numref:`eq1`).

For crop categories for which the sum of all costs exceeds the gross crop revenues, price is assumed to have an implicit subsidy such that net returns are roughly 5 percent above the total costs. While negative net returns are sometimes a reality for farmers, it is assumed that in the average most farms operate within the aforesaid profit margin. The adjustment is shown in :math:numref:`eq2` below:

.. math:: p = 1.05(\frac{\omega_{land} + \omega_{supply} + x_{water}\omega_{water}}{y})
    :label: eq2

where :math:`\omega` refers to the cost associated with each input ($/ac), :math:`x_{water}` is the applied water requirement per acre of land (AF/ac) and y is the yield (ton/ac). This correction allows for a 5% profit margin in final production calculations, yet it can be adjusted or eliminated or updated as better production cost information becomes available. Prices and derivative values (such as gross returns and profits) represented here reflect base values prior to corrections to the subset of crops.

Applied Water
_______________
Applied water data is provided at the detailed analysis unit and county level (DAU-Co) and is aggregated to individual island regions by applying a weighted average using Equations :math:numref:`eq3` and :math:numref:`eq4` below:

.. math:: AW_{ik} = \frac{\sum_{w=1}^{n}l_{iw}AW_{iw}}{\sum_{w=1}^{n}l_{iw}}
    :label: eq3


.. math:: AW_{ij} = \sum_{k=1}^{n}f_{jk}AW_{ik}
    :label: eq4

where :math:`i` is the crop index, :math:`k` is the DAU index, :math:`w` is the county index for each DAU, :math:`j` is the district index, :math:`l` is irrigated acreage and :math:`f` represents the vector of area fractions of DAU’s for a given island. Prior to integrating data at the island level, missing data for individual DAU’s by crop group are patched with the average applied water value for all other DAU’s across the study area. Applied water data for 2015 is used for all model years (2014-2017) due to a relatively low inter-annual variability across the study region.


Additional Tables
--------------------
Region names and associated IDs
_______________________________________

.. csv-table::
    :header: Region Name, ID, County
    :widths: auto

    Atlas Tract, DAP001, San Joaquin
    Bacon Island, DAP002, San Joaquin
    Bethel Island, DAP003, Contra Costa
    Big Break, DAP004, Contra Costa
    Bishop Tract/Dlis-14, DAP005, San Joaquin
    Bixler Tract, DAP006, Contra Costa
    Bouldin Island, DAP007, San Joaquin
    Brack Tract, DAP008, San Joaquin
    Bradford Island, DAP009, Contra Costa
    Brannan-Andrus, DAP010, Sacramento
    Browns Island, DAP011, Contra Costa
    Byron Tract, DAP012, Contra Costa
    Cache Haas Area, DAP013, Solano
    Canal Ranch Tract, DAP014, San Joaquin
    Central Stockton, DAP015, San Joaquin
    Chipps Island South, DAP016, Solano
    Clifton Court Forebay, DAP017, Contra Costa
    Coney Island, DAP018, Contra Costa
    Dead Horse Island, DAP019, Sacramento
    Decker Island, DAP020, Solano
    Dlis-01 (Pittsburg Area), DAP021, Contra Costa
    Dlis-02 (Antioch Area), DAP022, Contra Costa
    Dlis-03 (Lower Sherman Island), DAP023, Sacramento
    Dlis-04 (West Island), DAP024, Sacramento
    Dlis-05 (Donlon Island), DAP025, Sacramento
    Dlis-06 (Oakley Area), DAP026, Contra Costa
    Dlis-07 (Knightsen Area), DAP027, Contra Costa
    Dlis-08 (Discovery Bay Area), DAP028, Contra Costa
    Dlis-09 (Byron Area), DAP029, Contra Costa
    Dlis-10, DAP030, Contra Costa
    Dlis-12 (Paradise Cut), DAP031, San Joaquin
    Dlis-15, DAP032, San Joaquin
    Dlis-16 (Lodi), DAP033, San Joaquin
    Dlis-17, DAP034, San Joaquin
    Dlis-18, DAP035, San Joaquin
    Dlis-19 (Grizzly Slough Area), DAP036, Sacramento
    Dlis-20 (Yolo Bypass), DAP037, Yolo
    Dlis-21, DAP038, Solano
    Dlis-22 (Rio Vista), DAP039, Solano
    Dlis-23 (Georgiana Oxbow), DAP040, Sacramento
    Dlis-62, DAP042, Solano
    Dlis-63 (Grizzly Island Area), DAP043, Solano
    Dlis-64, DAP044, Contra Costa
    Drexler Pocket, DAP045, San Joaquin
    Drexler Tract, DAP046, San Joaquin
    Dutch Slough, DAP047, Contra Costa
    Egbert Tract, DAP048, Solano
    Ehrheardt Club, DAP049, Sacramento
    Empire Tract, DAP050, San Joaquin
    Fabian Tract, DAP051, San Joaquin
    Fay Island, DAP052, San Joaquin
    Franks Tract, DAP053, Contra Costa
    Glanville, DAP054, Sacramento
    Glide District, DAP055, Yolo
    Grand Island, DAP056, Sacramento
    Hastings Tract, DAP057, Solano
    Holland Tract, DAP058, Contra Costa
    Holt Station, DAP059, San Joaquin
    Honker Lake Tract, DAP060, San Joaquin
    Hotchkiss Tract, DAP061, Contra Costa
    Ida Island, DAP062, Sacramento
    Jersey Island, DAP063, Contra Costa
    Jones Tract (Lower And Upper), DAP064, San Joaquin
    Kasson District, DAP065, San Joaquin
    King Island, DAP066, San Joaquin
    Kings Island, DAP067, San Joaquin
    Libby Mcneil, DAP068, Sacramento
    Liberty Island, DAP069, Solano
    Lisbon District, DAP070, Yolo
    Little Egbert Tract, DAP071, Solano
    Little Franks Tract, DAP072, Contra Costa
    Little Mandeville Island, DAP073, San Joaquin
    Long Island, DAP074, Sacramento
    Lower Roberts Island, DAP075, San Joaquin
    Maintenance Area 9 North, DAP076, Sacramento
    Maintenance Area 9 South, DAP077, Sacramento
    Mandeville Island, DAP078, San Joaquin
    Mccormack-Williamson Tract, DAP079, Sacramento
    Mcdonald Island, DAP080, San Joaquin
    Mcmullin Ranch, DAP081, San Joaquin
    Medford Island, DAP082, San Joaquin
    Merritt Island, DAP083, Yolo
    Middle & Upper Roberts Island, DAP084, San Joaquin
    Middle Delta Extra, DAP085, Contra Costa
    Mildred Island, DAP086, San Joaquin
    Mossdale Island, DAP087, San Joaquin
    Netherlands, DAP088, Yolo
    New Hope Tract, DAP089, San Joaquin
    North Delta Extra, DAP090, Solano
    North Stockton, DAP091, San Joaquin
    Palm-Orwood, DAP092, Contra Costa
    Paradise Junction, DAP093, San Joaquin
    Pearson District, DAP094, Sacramento
    Pescadero District, DAP095, San Joaquin
    Peters Pocket, DAP096, Solano
    Pico-Naglee, DAP097, San Joaquin
    Prospect Island, DAP098, Solano
    Quimby Island, DAP099, Contra Costa
    Randall Island, DAP100, Sacramento
    Reclamation District 17, DAP101, San Joaquin
    Rindge Tract, DAP102, San Joaquin
    Rio Blanco Tract, DAP103, San Joaquin
    River Junction, DAP104, San Joaquin
    Rough And Ready Island, DAP105, San Joaquin
    Ryer Island, DAP106, Solano
    Sherman Island, DAP107, Sacramento
    Shima Tract, DAP108, San Joaquin
    Shin Kee Tract, DAP109, San Joaquin
    South Delta Extra, DAP110, San Joaquin
    Stark Tract, DAP111, San Joaquin
    Staten Island, DAP112, San Joaquin
    Stewart Tract, DAP113, San Joaquin
    Sutter Island, DAP114, Sacramento
    Terminous Tract, DAP115, San Joaquin
    Twitchell Island, DAP116, Sacramento
    Tyler Island, DAP117, Sacramento
    Union Island East, DAP118, San Joaquin
    Union Island West, DAP119, San Joaquin
    Upper Andrus Island, DAP120, Sacramento
    Veale Tract, DAP121, Contra Costa
    Venice Island, DAP122, San Joaquin
    Victoria Island, DAP123, San Joaquin
    Walnut Grove, DAP124, Sacramento
    Walthall, DAP125, San Joaquin
    Webb Tract, DAP126, Contra Costa
    West Sacramento, DAP127, Yolo
    Wetherbee Lake, DAP128, San Joaquin
    Winter Island, DAP129, Contra Costa
    Woodward Island, DAP130, San Joaquin
    Wright-Elmwood Tract, DAP131, San Joaquin
    Yolano, DAP132, Solano


UC Davis cost and return studies utilized in characterizing costs of production
______________________________________________________________________________________

.. csv-table::
    :header: Crop Group, Study Commodity, Study Year, Study Region, Study Link
    :widths: auto

    Alfalfa, Alfalfa hay, 2014, Sacramento Valley, `link <https://web.archive.org/web/20200726023226/https://coststudyfiles.ucdavis.edu/uploads/cs_public/69/ed/69ed1c05-999e-4c06-b59f-ebe6dbcecc8a/alfalfa-drip-sv-delta-2014.pdf>`_
    Alfalfa, Alfalfa hay, 2015, Sacramento Valley, `link <https://web.archive.org/web/20200726023219/https://coststudyfiles.ucdavis.edu/uploads/cs_public/39/f2/39f29aa5-b991-4a13-816e-c695ed243249/alfalfa-flood-sv-2015.pdf>`_
    Alfalfa, Alfalfa hay, 2008, Sacramento Valley, `link <https://web.archive.org/web/20200209221230/https://coststudyfiles.ucdavis.edu/uploads/cs_public/f2/0e/f20ea94b-1cf4-4364-bf51-79dc5ad44790/alfalfasv08.pdf>`_
    Almonds, Almond, 2016, Sacramento Valley, `link <https://web.archive.org/web/20201112022001/https://coststudyfiles.ucdavis.edu/uploads/cs_public/57/1c/571c5eea-78fe-4dd2-a950-cd886bc7b5cb/16almondsacvalfinaldraft81216.pdf>`_
    Almonds, Almond, 2019, Sacramento Valley, `link <https://web.archive.org/web/20200726023255/https://coststudyfiles.ucdavis.edu/uploads/cs_public/67/b7/67b72c81-5ce0-4462-a396-fbb62ce8564e/2019sacvalleyalmonds.pdf>`_
    Almonds, Almond, 2012, Sacramento Valley, `link <https://web.archive.org/web/20200210073320/https://coststudyfiles.ucdavis.edu/uploads/cs_public/cb/be/cbbe6906-0b85-499c-98a5-c100c468fd6f/almondsprinklesv2012.pdf>`_
    Corn, Field corn, 2008, Sacramento Valley, `link <https://web.archive.org/web/20200209221148/https://coststudyfiles.ucdavis.edu/uploads/cs_public/35/1a/351a40bc-aa3b-45c1-9c0f-0c9e4bf688a2/cornsv2008.pdf>`_
    Corn, Field corn, 2015, North/South San Joaquin Valley, `link <https://web.archive.org/web/20200726023321/https://coststudyfiles.ucdavis.edu/uploads/cs_public/03/dc/03dc4496-32af-47c6-b479-38e1d27c134e/15cornsacramentovalleyfinaldraftjuly20.pdf>`_
    Cotton, Cotton, 2012, North/South San Joaquin Valley, `link <https://web.archive.org/web/20211206082818/https://coststudyfiles.ucdavis.edu/uploads/cs_public/e0/15/e0152943-7158-4e13-8ca9-f95260582a2d/cotton2012acala.pdf>`_
    Cucurbits, Watermelon, 2003, Imperial County, `link <https://web.archive.org/web/20200209221059/https://coststudyfiles.ucdavis.edu/uploads/cs_public/a7/02/a70224a1-88de-4b9f-a314-cf3199341378/watermelon03.pdf>`_
    Cucurbits, Watermelon, 2000, Imperial County, `link <https://coststudyfiles.ucdavis.edu/uploads/cs_public/0f/ea/0fead9bf-49b1-4187-afc1-346d3ed6187b/watermelon.pdf>`_
    Dry Beans, Dry bean, 2014, Sacramento Valley, `link <https://web.archive.org/web/20200726023237/https://coststudyfiles.ucdavis.edu/uploads/cs_public/a2/fe/a2fec200-2ff7-4166-9ff9-59b47bb28a70/beans_double-cropped_sv_2014.pdf>`_
    Dry Beans, Dry bean, 2014, Sacramento Valley, `link <https://web.archive.org/web/20200726023313/https://coststudyfiles.ucdavis.edu/uploads/cs_public/de/d6/ded6333c-02e2-4a1c-9efb-b0b96a1fc713/beans_singlecropped_sv_2014.pdf>`_
    Fresh Tomato, Fresh tomato, 2007, North/South San Joaquin Valley, `link <https://web.archive.org/web/20200209202102/https://coststudyfiles.ucdavis.edu/uploads/cs_public/2e/2a/2e2a411e-73e1-469c-9eae-8458c3badedf/tomatofrmktsj07.pdf>`_
    Grain, Wheat, 2016, Sacramento Valley, `link <https://web.archive.org/web/20220119185854/https://coststudyfiles.ucdavis.edu/uploads/cs_public/dc/15/dc158210-055c-494c-9c2f-54083fbf0323/2016wheatsacvalleyfinaldraft122116.pdf>`_
    Grain, Wheat, 2009, Sacramento Valley, `link <https://web.archive.org/web/20200209223257/https://coststudyfiles.ucdavis.edu/uploads/cs_public/64/d9/64d94b28-ba10-4e00-b879-88a1b1e81afc/wheatsv09.pdf>`_
    Onions, Onion, 2006, South San Joaquin Valley, `link <https://web.archive.org/web/20230430175021/https://coststudyfiles.ucdavis.edu//uploads/cs_public/37/c8/37c88af8-b52e-45eb-bc21-2acd754b0c0a/onionredvs06.pdf>`_
    Orchards, Walnut, 2018, Sacramento Valley, `link <https://web.archive.org/web/20200726023633/https://coststudyfiles.ucdavis.edu/uploads/cs_public/3c/ef/3cefc943-ffea-407a-8281-240241efe5d5/18walnutssacval-final_draft-11518.pdf>`_
    Orchards, Walnut, 2015, Sacramento Valley, `link <https://web.archive.org/web/20200209220812/https://coststudyfiles.ucdavis.edu/uploads/cs_public/78/a7/78a775e3-6488-49d4-b234-b3eaf9171a55/15walnutssacvalleyfinaldraftjan4.pdf>`_
    Orchards, Bartlett pear, 2010, Sacramento Valley, `link <https://web.archive.org/web/20210926040213/https://coststudyfiles.ucdavis.edu/uploads/cs_public/3d/89/3d892a7b-b898-466c-9024-2d8d3efc04c3/pearsv2010.pdf>`_
    Field, Grain silage, 2013, South San Joaquin Valley, `link <https://web.archive.org/web/20160607033952/http://coststudyfiles.ucdavis.edu/uploads/cs_public/1a/d8/1ad8788d-8db4-4c43-9a84-19d48916311f/smallgrainsilagevs2013.pdf>`_
    Vegetables, Asparagus, 2013, North San Joaquin Valley, `link <https://web.archive.org/web/20191022193321/https://coststudyfiles.ucdavis.edu/uploads/cs_public/91/0b/910b6b2a-1f01-4697-be7f-0ae88f5ee11b/asparagusvn2013.pdf>`_
    Pasture, Pasture, 2015, Sacramento Valley, `link <https://web.archive.org/web/20200726023504/https://coststudyfiles.ucdavis.edu/uploads/cs_public/0e/23/0e230982-8610-42a4-8a26-32a0b10a4c5c/pasture_sv_2015.pdf>`_
    Pasture, Pasture, 2015, Sacramento Valley, `link <https://web.archive.org/web/20230430171158/https://coststudyfiles.ucdavis.edu//uploads/cs_public/b2/a9/b2a91349-8ef5-4ed3-8b99-37eccbbdd272/pastureep_sv_2015.pdf>`_
    Pasture, Pasture, 2003, Sacramento Valley, `link <https://web.archive.org/web/20200210071853/https://coststudyfiles.ucdavis.edu/uploads/cs_public/3e/0f/3e0f1a8c-75b2-437e-8370-1cdfed476664/pasturesv03.pdf>`_
    Potato, Potato, 2015, Klamath Basin, `link <https://web.archive.org/web/20200726023445/https://coststudyfiles.ucdavis.edu/uploads/cs_public/3c/5c/3c5cf640-be4b-42bd-8a4c-af337c15d09d/15potatochipperklamathfinaldraftdec10.pdf>`_
    Potato, Potato, 2008, Klamath Basin, `link <https://web.archive.org/web/20200209221235/https://coststudyfiles.ucdavis.edu/uploads/cs_public/81/84/8184c2a2-28a1-4d07-9e4c-0f3543306e03/potatoeschipir2008.pdf>`_
    Processing Tomatoes, Processing tomato, 2017, Sacramento Valley, `link <https://web.archive.org/web/20200726023522/https://coststudyfiles.ucdavis.edu/uploads/cs_public/d7/b2/d7b2ee5f-8961-417d-b9d1-216d41fb47d8/2017processtomssacvalfinaldraft32817.pdf>`_
    Processing Tomatoes, Processing tomato, 2014, Sacramento Valley, `link <https://web.archive.org/web/20200209230853/https://coststudyfiles.ucdavis.edu/uploads/cs_public/3e/62/3e625c07-cf86-4591-a51d-6609fdd1f89f/process-tomato-drip.pdf>`_
    Processing Tomatoes, Processing tomato, 2014, Sacramento Valley, `link <https://web.archive.org/web/20200209231201/https://coststudyfiles.ucdavis.edu/uploads/cs_public/46/9d/469d2b35-4c6f-4c19-b3d1-633ef72043c3/process-tomato-furrow.pdf>`_
    Rice, Rice, 2015, Sacramento Valley, `link <https://web.archive.org/web/20200726023458/https://coststudyfiles.ucdavis.edu/uploads/cs_public/e8/9c/e89c1d86-f3fd-47bf-8e9a-02714e1e046e/2015_rice_2016_amendedfinaldraft7516-1.pdf>`_
    Safflower, Safflower, 2011, Sacramento Valley, `link <https://web.archive.org/web/20200209223731/https://coststudyfiles.ucdavis.edu/uploads/cs_public/63/a9/63a948b0-8cef-4843-b66c-ac27006f726f/safflowersv2011.pdf>`_
    Sugar Beets, Sugar beet, 2003, Southeast Interior, `link <https://web.archive.org/web/20200210034717/https://coststudyfiles.ucdavis.edu/uploads/cs_public/64/68/6468f81c-241a-44ea-923d-37c38de8feba/sugarbeetim03.pdf>`_
    Subtropical, Olive, 2016, Sacramento Valley, `link <https://web.archive.org/web/20200726023451/https://coststudyfiles.ucdavis.edu/uploads/cs_public/ad/97/ad9753c5-0cdc-4d82-b358-31157d6e6061/2016tableolivessacramentovalleyfinaldraftmar17.pdf>`_
    Subtropical, Olive, 2011, Sacramento Valley, `link <https://web.archive.org/web/20200210065430/https://coststudyfiles.ucdavis.edu/uploads/cs_public/54/26/54269a47-2bdb-4a22-84dd-567556d934d4/olivetablesv2011.pdf>`_
    Vineyards, Wine grape, 2013, Sacramento Valley, `link <https://web.archive.org/web/20191022193355/https://coststudyfiles.ucdavis.edu/uploads/cs_public/42/a7/42a7ee28-6775-426d-9e93-e621128aeb5d/grapewinesv2013.pdf>`_
    Vineyards, Wine grape, 2008, Sacramento Valley, `link <https://web.archive.org/web/20200209221308/https://coststudyfiles.ucdavis.edu/uploads/cs_public/13/46/134617e9-c64b-4cd3-919a-fd43634ed198/grapewinesv2008.pdf>`_
    Vineyards, Wine grape, 2016, North San Joaquin Valley, `link <https://web.archive.org/web/20200726023426/https://coststudyfiles.ucdavis.edu/uploads/cs_public/a8/4a/a84a16ba-4971-4348-8a55-5f2f6f372134/2016grapewinelodifinaldraftmay192019.pdf>`_


