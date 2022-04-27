.. _WashingtonModelInputsDoc:

Input Data and Processing
===================================

.. contents::
    :local:

Summary of Data Inputs
--------------------------
The following table summarizes data sources used for defining model inputs for the Washington State :ref:`model area <ModelAreasDoc>`.

.. csv-table::
    :header: "Data", Spatial Resolution, Temporal Resolution, Source

    Land use, Parcel, Annual, `Washington State Department of Agriculture <https://agr.wa.gov/departments/land-and-water/natural-resources/agricultural-land-use>`_
    Crop water demand, Station, Monthly, `Washington State University <http://irrigation.wsu.edu/Content/ET_IWR_For_WA.php>`_
    Precipitation and temperature, Gridded 4 km\ :superscript:`2`, Monthly, `PRISM Climate Group <https://prism.oregonstate.edu/>`_
    Surface water deliveries, State and/or Water district, Monthly, "Water Right Tracking System (WRTS), US Bureau of Reclamation [#usbrnote]_ "
    Crop price, "State, regional", Annual, "`US Department of Agriculture NASS <https://www.nass.usda.gov/Statistics_by_State/Washington/index.php>`_, `Washington State University Crop Enterprise Budgets <http://ses.wsu.edu/enterprise_budgets/>`_"
    Crop yield, "State, county", Annual, "`US Department of Agriculture NASS <https://www.nass.usda.gov/Statistics_by_State/Washington/index.php>`_, `Washington State University Crop Enterprise Budgets <http://ses.wsu.edu/enterprise_budgets/>`_"
    Crop production costs, Regional, Annual, `Washington State University Crop Enterprise Budgets <http://ses.wsu.edu/enterprise_budgets/>`_
    Supply elasticities, , Annual,


Land Use and Crop Groups
---------------------------
Parcel-level land use data used in the model comes from the Washington State Department of Agriculture. The model excludes
semi-agricultural or fishery categories such as nursery plants, shellfish, and horticulture.
Spatial data for each year is first clipped to model designated regions. Then, crop commodities are grouped into the 14 crop
categories in the table below. Each category is assessed to determine the most significant
crop commodities considering a combination of both acreage and revenue, with the most significant made an economic and water
use proxy for other commodities in the same category. The proxy commodity's economic and water use data are used in place
of data for other commodities in the same category and all data are grouped together as one crop.

Spatial cropping data contains metadata pertaining to the type of irrigation of each parcel. This information
is used to split data between the :ref:`irrigated <IrrigatedPMPDoc>` and :ref:`non-irrigated <NonIrrigatedDoc>` models by
region. See :ref:`IrrigatedDataSplitDoc` for more information on how OpenAg splits data between the two models.

The following table shows the crops included in each crop group in OpenAg for the Washington model.
The pipe character :code:`|` splits separate commodities, so, for example in the "Bean" row, the first
commodity included as a bean is "Bean, Dry" and the second is "Bean, Garbanzo", etc. Any commodity not shown
in the table is not included in the model.

..
    comment
    This data came from Box\OpenAGWA\Task1_Database\Databases\Stepwise Databases\Other\Database_New_Regions_05042021\OpenAgWA_cropcodebridge_10172020.csv
    Reaggregated in Notepad++ with CsvQuery using the query

    SELECT Col1 as OpenAg_Crop, group_concat(Col2, "  |  ") as WSDA_Level_1 FROM THIS GROUP BY Col1

    Then dropped the wheat fallow, fallow, other, and the header row that was inserted

.. csv-table::
    :header: OpenAg_Crop, WSDA_Level_1
    :widths: 30, 70

    APPLE, Apple
    BEAN, "Bean, Dry  |  Bean, Garbanzo  |  Bean, Green  |  Chickpea  |  Legume Cover  |  Lentil  |  Pea, Dry  |  Pea, Green  |  Pea/Vetch  |  Soybean"
    BLUEBERRY, Blueberry
    CANEBERRY, "Berry, Unknown  |  Caneberry  |  Cranberry  |  Currant  |  Strawberry"
    CHERRY, Cherry
    CORN, "Corn, Field  |  Corn, Sweet  |  Corn, Unknown"
    GRAIN, "Alfalfa Seed  |  Alfalfa, Seed  |  Barley  |  Bean Seed  |  Bean, Seed  |  Beet Seed  |  Beet, Seed  |  Bluegrass Seed  |  Bluegrass, Seed  |  Broccoli Seed  |  Broccoli, Seed  |  Bromegrass Seed  |  Bromegrass, Seed  |  Brussels Sprouts Seed  |  Brussels Sprouts, Seed  |  Buckwheat  |  Burnet Seed  |  Burnet, Seed  |  Cabbage Seed  |  Cabbage, Seed  |  Camelina  |  Canola  |  Carrot Seed  |  Carrot, Seed  |  Cauliflower, Seed  |  Cereal Grain, Unknown  |  Cilantro Seed  |  Cilantro, Seed  |  Clover Seed  |  Clover, Seed  |  Conifer Seed  |  Conifer, Seed  |  Corn Seed  |  Corn, Seed  |  Fescue Seed  |  Fescue, Seed  |  Flax  |  Flax Seed  |  Grass Seed  |  Grass Seed, Other  |  Grass, Seed  |  Misc. Grass Seed  |  Mustard  |  Mustard Seed  |  Mustard, Seed  |  Oat  |  Onion Seed  |  Onion, Seed  |  Pea Seed  |  Pea, Seed  |  Pepper  |  Potato Seed  |  Potato, Seed  |  Quinoa  |  Radish Seed  |  Radish, Seed  |  Reclamation Seed  |  Rye  |  Ryegrass Seed  |  Ryegrass, Seed  |  Safflower Seed  |  Safflower, Seed  |  Seed, Other  |  Seed, Unknown  |  Sorghum  |  Spinach Seed  |  Spinach, Seed  |  Sugar Beet Seed  |  Sugar Beet, Seed  |  Sunflower  |  Sunflower Seed  |  Sunflower, Seed  |  Swiss Chard Seed  |  Swiss Chard, Seed  |  Triticale  |  Wheat  |  Wildlife Feed  |  Yarrow Seed  |  Yarrow, Seed  |  Yellow Mustard"
    GRAPE, "Grape, Concord  |  Grape, Juice  |  Grape, Table  |  Grape, Unknown  |  Grape, Wine"
    HAY, "Alfalfa Hay  |  Alfalfa, Hay  |  Alfalfa/Grass Hay  |  Alfalfa/Grass, Hay  |  Barley Hay  |  Clover Hay  |  Clover, Hay  |  Clover/Grass Hay  |  Grass Hay  |  Grass, Hay  |  Hay/Silage , Unknown  |  Hay/Silage, Unknown  |  Oat Hay  |  Rye Hay  |  Sudangrass  |  Timothy  |  Triticale Hay"
    HOPS, Hops
    PASTURE, Pasture
    PEAR, Pear
    POTATO, Potato
    VEGETABLE, "Artichoke  |  Asparagus  |  Beet  |  Broccoli  |  Brussels Sprouts  |  Cabbage  |  Cantaloupe  |  Carrot  |  Cauliflower  |  Cucumber  |  Garlic  |  Kale  |  Kiwi  |  Leek  |  Lettuce  |  Market Crops  |  Melon, Unknown  |  Onion  |  Peanut  |  Pumpkin  |  Radish  |  Rhubarb  |  Rutabaga  |  Spinach  |  Squash  |  Sugar Beet  |  Tomato  |  Vegetable, Unknown  |  Watermelon"


Crop Water Demand
-------------------
Monthly point estimates of reference evapotranspiration were made by `Peters et al. (2012) <http://irrigation.wsu.edu/Content/Fact-Sheets/IrrigationWaterRequirements4WA.pdf>`_ at weather stations
throughout Washington state using approximately 30 years of data and serve as the primary source of crop water
demand data for the model inputs. Peters et al. used the ASCE Penman-Monteith method for calculating reference
evapotranspiration and subsequently applied crop coefficients to estimate crop evapotranspiration (2012).
Station coordinates were used to create `Thiessen polygons <https://pro.arcgis.com/en/pro-app/latest/tool-reference/analysis/create-thiessen-polygons.htm>`_ which define regions of influence which are closer
to that station than any other station. Thiessen polygons surrounding stations were then intersected with model
regions and area-weighted averaging was used to approximate monthly crop water demands by crop type and model region.

Precipitation and Temperature
-------------------------------
Rainfall data were obtained from PRISM's monthly 4km gridded normals. Monthly data were summed into seasons (summer, fall, winter,
and spring) and the mean grid value within each region was extracted as the region's rainfall value for each time period.

Surface Water Deliveries
---------------------------
Surface water delivery data were obtained from the US Bureau of Reclamation via a Freedom of Information Act request.

Crop Price and Yield
-------------------------
For most crop categories in the model, price and yield data are estimated from Washington State University Crop
Enterprise Budgets pertaining to proxy crops. Crops with only fresh or processing production use their respective
price and yield. Crops surveyed to produce both fresh and processing products use fresh prices and adjust yield to
reflect the combined revenue from both pathways. Some crop categories are represented by information taken from a
single crop budget if data is scarce, while crops with more data take prices and yields averaged from several studies.

Primarily non-irrigated crop categories (e.g. grain, hay, beans, corn) instead take a time series of county-level yields
from USDA NASS. County boundaries are intersected with WRIAs and county-level yield for relevant crops are averaged across
intersecting counties where data is available. This is done to reflect variation in yield in response to precipitation
for crops whose main source of water supply is rainfall. Non-irrigated agriculture is modeled separately from irrigated
crops, as discussed in :ref:`NonIrrigatedDoc`.

All crop prices are adjusted to 2018 dollars using a cumulative inflation index as reported by the US Bureau of Labor
Statistics.

Crop Production Costs
-------------------------
Production costs for crop categories are taken from Washington State University Crop Enterprise Budgets for relevant
proxy commodities. Information for some crops are also taken from Oregon State University or University of California,
Davis crop budgets when not available for Washington state. For perennial crops with significant establishment periods
(e.g. apples, berries, grapes, pears), annual costs are estimated over their estimated lifetime using both establishment
and production costs. Costs are divided into variable costs and fixed costs, of which 30% of variable costs are assumed
to go towards labor and the remaining 70% go towards supplies and miscellaneous costs. Some crop categories are
represented by information taken from a single crop budget if data is scarce, while crops with more data take costs
averaged from several studies.

All crop costs are adjusted to 2018 dollars using a cumulative inflation index as reported by the US Bureau of Labor
Statistics.

Supply elasticities
----------------------
Own-price supply elasticities are used for the calibration of the exponential cost function parameter gamma,
which defines the shape of the cost function curvature and the concavity of the model. Own-price supply elasticities
represent the response in produced land for a crop to a change in crop price by farmers. Crop-specific values are available
at a regional or state level and are usually obtained from econometric studies, however the literature for specific crops
and specific agricultural regions is Washington is limited. For this reason we assume that these values respond similarly
for specific crops in other agricultural regions like California.


.. rubric:: Footnotes
.. [#usbrnote] Requested through the Freedom of Information Act
