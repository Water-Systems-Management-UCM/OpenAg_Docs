The Washington State Model
===========================
The model for Washington State is based primarily on the state's water resource
inventory areas as regions, with minor modifications.

.. contents::
    :local:
    :depth: 2

Crop Groups
---------------
The following table shows the crops included in each crop group in OpenAg for the Washington model.
The pipe character :code:`|` splits separate commodities, so, for example in the "Bean" row, the first
commodity included as a bean is "Bean, Dry" and the second is "Bean, Garbanzo", etc.

..
    comment
    This data came from Box\OpenAGWA\Task1_Database\Databases\Stepwise Databases\Other\Database_New_Regions_05042021\OpenAgWA_cropcodebridge_10172020.csv
    Reaggregated in Notepad++ with CsvQuery using the query

    SELECT Col1 as OpenAg_Crop, group_concat(Col2, "  |  ") as WSDA_Level_1 FROM THIS GROUP BY Col1

    Then dropped the wheat fallow and the header row that was inserted

.. csv-table::
    :header: OpenAg_Crop,WSDA_Level_1

    APPLE,Apple
    BEAN,"Bean, Dry  |  Bean, Garbanzo  |  Bean, Green  |  Chickpea  |  Legume Cover  |  Lentil  |  Pea, Dry  |  Pea, Green  |  Pea/Vetch  |  Soybean"
    BLUEBERRY,Blueberry
    CANEBERRY,"Berry, Unknown  |  Caneberry  |  Cranberry  |  Currant  |  Strawberry"
    CHERRY,Cherry
    CORN,"Corn, Field  |  Corn, Sweet  |  Corn, Unknown"
    FALLOW,"Fallow  |  Fallow, Idle  |  Fallow, Tilled"
    GRAIN,"Alfalfa Seed  |  Alfalfa, Seed  |  Barley  |  Bean Seed  |  Bean, Seed  |  Beet Seed  |  Beet, Seed  |  Bluegrass Seed  |  Bluegrass, Seed  |  Broccoli Seed  |  Broccoli, Seed  |  Bromegrass Seed  |  Bromegrass, Seed  |  Brussels Sprouts Seed  |  Brussels Sprouts, Seed  |  Buckwheat  |  Burnet Seed  |  Burnet, Seed  |  Cabbage Seed  |  Cabbage, Seed  |  Camelina  |  Canola  |  Carrot Seed  |  Carrot, Seed  |  Cauliflower, Seed  |  Cereal Grain, Unknown  |  Cilantro Seed  |  Cilantro, Seed  |  Clover Seed  |  Clover, Seed  |  Conifer Seed  |  Conifer, Seed  |  Corn Seed  |  Corn, Seed  |  Fescue Seed  |  Fescue, Seed  |  Flax  |  Flax Seed  |  Grass Seed  |  Grass Seed, Other  |  Grass, Seed  |  Misc. Grass Seed  |  Mustard  |  Mustard Seed  |  Mustard, Seed  |  Oat  |  Onion Seed  |  Onion, Seed  |  Pea Seed  |  Pea, Seed  |  Pepper  |  Potato Seed  |  Potato, Seed  |  Quinoa  |  Radish Seed  |  Radish, Seed  |  Reclamation Seed  |  Rye  |  Ryegrass Seed  |  Ryegrass, Seed  |  Safflower Seed  |  Safflower, Seed  |  Seed, Other  |  Seed, Unknown  |  Sorghum  |  Spinach Seed  |  Spinach, Seed  |  Sugar Beet Seed  |  Sugar Beet, Seed  |  Sunflower  |  Sunflower Seed  |  Sunflower, Seed  |  Swiss Chard Seed  |  Swiss Chard, Seed  |  Triticale  |  Wheat  |  Wildlife Feed  |  Yarrow Seed  |  Yarrow, Seed  |  Yellow Mustard"
    GRAPE,"Grape, Concord  |  Grape, Juice  |  Grape, Table  |  Grape, Unknown  |  Grape, Wine"
    HAY,"Alfalfa Hay  |  Alfalfa, Hay  |  Alfalfa/Grass Hay  |  Alfalfa/Grass, Hay  |  Barley Hay  |  Clover Hay  |  Clover, Hay  |  Clover/Grass Hay  |  Grass Hay  |  Grass, Hay  |  Hay/Silage , Unknown  |  Hay/Silage, Unknown  |  Oat Hay  |  Rye Hay  |  Sudangrass  |  Timothy  |  Triticale Hay"
    HOPS,Hops
    OTHER,"Alkali Bee Bed  |  Allium  |  Almond  |  Apricot  |  Bulb, Allium  |  Bulb, Daffodil  |  Bulb, Dahlia  |  Bulb, Iris  |  Bulb, Peony  |  Bulb, Tulip  |  Chestnut  |  Christmas Tree  |  CRP  |  CRP/Conservation  |  Daffodil  |  Dahlia  |  Dandelion  |  Developed  |  Dill  |  Douglas Fir  |  Driving Range  |  Filbert  |  Golf Course  |  Green Manure  |  Hemp  |  Herb, Medicinal  |  Herb, Unknown  |  Iris  |  Marijuana  |  Medicinal Herb  |  Mint  |  Nectarine/Peach  |  Nursery, Caneberry  |  Nursery, Greenhouse  |  Nursery, Holly  |  Nursery, Lavender  |  Nursery, Lilac  |  Nursery, Orchard/Vineyard  |  Nursery, Ornamental  |  Nursery, Silvaculture  |  Nursery, Silviculture  |  Orchard, Unknown  |  Parsley  |  Peony  |  Plum  |  Poplar  |  Poplar, Hybrid  |  Research Station  |  Rosemary  |  Sage  |  Shellfish  |  Silvaculture  |  Silviculture  |  Sod Farm  |  Tarragon  |  Tea  |  Tobacco  |  Tulip  |  Unknown  |  Walnut  |  Yew  |  Yew, Pacific"
    PASTURE,Pasture
    PEAR,Pear
    POTATO,Potato
    VEGETABLE,"Artichoke  |  Asparagus  |  Beet  |  Broccoli  |  Brussels Sprouts  |  Cabbage  |  Cantaloupe  |  Carrot  |  Cauliflower  |  Cucumber  |  Garlic  |  Kale  |  Kiwi  |  Leek  |  Lettuce  |  Market Crops  |  Melon, Unknown  |  Onion  |  Peanut  |  Pumpkin  |  Radish  |  Rhubarb  |  Rutabaga  |  Spinach  |  Squash  |  Sugar Beet  |  Tomato  |  Vegetable, Unknown  |  Watermelon"





Supported Capabilities
------------------------
The Washington model supports both the :ref:`irrigated lands model <IrrigatedPMPDoc>` and the :ref:`nonirrigated lands
rainfall model <NonIrrigatedDoc>`. The nonirrigated lands model is not used for all regions or crops. Most modeled regions
include rainfall modeling but only four crops are used in rainfall modeling: grain, bean, hay, and corn.