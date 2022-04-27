.. _SacramentoSanJoaquinModelDoc:

The Sacramento-San Joaquin Delta Model
========================================

The Sacramento-San Joaquin Delta (Delta) occurs at the confluence of the two
eponymous rivers and is a crucial cornerstone of water resource management in
California. While important in supporting agriculture throughout the state by conveying
water to key regions, the Delta itself hosts significant production of select crops, namely
alfalfa, corn, pasture, and tomatoes, among others. Challenges facing the Delta align
with anticipated climate change impacts rising sea level, saline intrusion, and increasing
hydrological variability. The OpenDAP model was developed as a tool to assess
economic impacts of changing economic, biophysical, water management and land
management conditions in the Delta. It is assumed that changes in these systemwide
conditions will likely affect production decisions including total area planted and
production factors use, intensity in production factors use, and choice of crops such that
returns to farm and management are maximized. The OpenDAP model was embedded
in a user friendly web application which runs an economic optimization model in
response to user-provided scenarios of land use and water management such that crop
profitability is maintained.


The OpenAg/DAP Model
----------------------
The OpenDAP Beta Version model was developed using economic and
production input data for 2014, 2015, 2016, and 2017, and is calibrated based on
average conditions from these four baseline years. Unit of analysis consists of Delta
Islands and other agricultural clustered areas within the Legal Delta. The model is
calibrated using the economic principles of Positive Mathematical Programming for
disaggregate models (Howitt et al. 2012) and its architecture is based on the DAP
model employed to study salinity effects in the Delta Agriculture (Medellin-Azuara et al.
2014). The calibrated model predicts decisions of farmers on cropland use and use of
inputs including water within an island assuming profit maximizing behavior considering
expected prices, subsidies, yields, and costs, as well as restrictions on land, water and
crop specific restrictions. This is undertaken by solving the non-linear program
described by equations 1 to 5 below.

Commodity Groupings
-----------------------

..
    comment
    This data came from a spreadsheet from Spencer Cole via Teams on 4/26/2022
    Reaggregated in Notepad++ with CsvQuery using the query

    SELECT Col1 as Category, group_concat(Col2, "  |  ") as Commodities FROM THIS GROUP BY Col1

    Then reformatted the line for Not Included and removed some extra quotes and an extra header row that's inserted


.. csv-table::
    :header: Category, Commodities
    :widths: 30, 70

    Alfalfa, Alfalfa and Alfalfa Mixtures | Alfalfa
    Almonds and Pistachios, Almonds | Pistachios
    Corn, Corn | Sorghum and Sudan | Corn | Sorghum | Sudan Grass
    Cucurbits, Melons | Squash and Cucumbers | Cucurbit
    Deciduous, Apples | Cherries | Miscellaneous Deciduous | Peaches/Nectarines | Pears | Plums | Prunes and Apricots | Pomegranates | Walnuts | Young Perennials | N/A Deciduous
    Dry Beans, Beans (Dry)
    Field Crops, Miscellaneous Field Crops | Sunflowers | Sunflower
    Grain, Miscellaneous Grain and Hay | Wheat
    Onions and Garlic, Onions and Garlic
    Pasture, Miscellaneous Grasses | Mixed Pasture | Forage Grass | Pasture | Turf
    Potatoes, Potatoes and Sweet Potatoes | Potatoes
    Processing Tomatoes, Tomatoes
    Rice, Rice
    Safflower, Safflower
    Subtropical, Citrus | Kiwis | Olives
    Vegetables, Bush Berries | Carrots | Cole Crops | Lettuce/Leafy Greens | Miscellaneous Truck Crops | Peppers | Strawberries | Asparagus | Truck Crops
    Vineyards, Grapes | Vineyards
    Not Included, Fallow | Flowers | Nursery and Christmas Tree Farms | Idle | Managed Wetland | Urban | Wild Rice | Floating Vegetation | Riparian | Semi-agricultural/ROW | Upland Herbaceous | Water | Wet herbaceous/sub irrigated pasture

Getting Access
----------------
The web platform is available now as a beta version at https://openag.ucmerced.edu.
To get access for additional staff, please `contact Nick Santos <https://nicksantos.com/about-and-contact/>`_.