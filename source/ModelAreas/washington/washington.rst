.. _WashingtonModelDoc:

The Washington State Model
===========================

.. _WashingtonModelOverviewSection:

Model Overview
------------------
Data collected for use in the model includes a variety of types and spans a decade (2008-2018), although only a selected
subset (2016-2018) is used in model calibration at this time. Spatial coverage of the model is nearly the entire state, with the
exception of some regions which lack the agricultural complexity to effectively model (see :ref:`FixedRegionsSection` for more information),
and the spatial scale of the model is a modified version of Washington's `Water Resource Inventory Areas (WRIA) <https://waecy.maps.arcgis.com/apps/webappviewer/index.html?id=996e6b21ae394cc3a3b63c6da0c3aa0a>`_.
Models are run at an annual scale, as sub-annual planting decisions cannot be captured using available data.

Model input data utilizes a crop grouping structure to retain sufficient resolution in outputs while
reducing data dependency. Initial land use surveys contain approximately 200 commodities that OpenAg groups into 14
categories for modeling. Each category is then assigned a proxy commodity to represent the economics and water needs
of the group. Proxies are assigned based on a combination of data availability and prominence in the overall land portfolio.
For example, imagine a category "vegetable" that includes onions, carrots, and tomato. If carrot is by far the most prominent
of the three (90% acreage) then we treat that entire category of land use as though it was carrots for the price,
yield, costs, and water demand. This approach is necessary because with so many commodities data and time are not available
to model every individual crop.

.. toctree::
    :maxdepth: 2

    input_data_sources.rst

.. contents::
    :local:
    :depth: 2


.. _WashingtonModelRegionsSection:

Regions
----------
.. figure:: WA_map_fixed_regions.jpg

    Regions used in the Washington model along with how they are handled, as modeled regions, or
    fixed regions that are scaled linearly by default rather than modeled.

.. csv-table::
    :header: "Region Name", "WRIA Region ID"

    "Alkali - Squilchuck", "40",
    "Cedar - Sammamish", "8",
    "Chambers - Clover", "12",
    "Chelan", "47",
    "Colville", "59",
    "Cowlitz", "26",
    "Deschutes", "13",
    "Duwamish - Green", "9",
    "Elwha - Dungeness", "18",
    "Entiat", "46",
    "Esquatzel Coulee", "36",
    "Foster", "50",
    "Grand Coulee", "42",
    "Grays - Elochoman", "25",
    "Hangman", "56",
    "Island", "6",
    "Kennedy - Goldsborough", "14",
    "Kettle", "60",
    "Kitsap", "15",
    "Klickitat", "30",
    "Lewis", "27",
    "Little Spokane", "55",
    "Lower Chehalis", "22",
    "Lower Crab", "41",
    "Lower Lake Roosevelt", "53",
    "Lower Skagit - Samish", "3",
    "Lower Snake", "33",
    "Lower Spokane", "54",
    "Lower Yakima (Kennewick ID)", "37-KID",
    "Lower Yakima (Roza ID)", "37-RID",
    "Lower Yakima (Sunnyside Valley ID)", "37-SVID",
    "Lower Yakima (Wapato Irrigation Project)", "37-WIP",
    "Lyre - Hoko", "19",
    "Methow", "48",
    "Middle Lake Roosevelt", "58",
    "Middle Snake", "35",
    "Middle Spokane", "57",
    "Moses Coulee", "44",
    "Naches (Yakima-Tieton ID)", "38-YTID",
    "Nespelem", "51",
    "Nisqually", "11",
    "Nooksack", "1",
    "Okanogan", "49",
    "Palouse", "34",
    "Pend Oreille", "62",
    "Puyallup - White", "10",
    "Queets - Quinault", "21",
    "Quilcene - Snow", "17",
    "Rock - Glade", "31",
    "Salmon - Washougal", "28",
    "San Juan", "2",
    "Sanpoil", "52",
    "Skokomish - Dosewallips", "16",
    "Snohomish", "7",
    "Soleduc", "20",
    "Stillaguamish", "5",
    "Upper Chehalis", "23",
    "Upper Crab-Wilson", "43",
    "Upper Lake Roosevelt", "61",
    "Upper Skagit", "4",
    "Upper Yakima (Ellensberg Area)", "39-EW",
    "Upper Yakima (Kittitas RD)", "39-KRD",
    "Walla Walla", "32",
    "Wenatchee", "45",
    "Willapa", "24",
    "Wind - White Salmon", "29"

.. _FixedRegionsSection:

Fixed Regions
_________________

.. todo:: fill in

Supported Capabilities
------------------------
The Washington model supports both the :ref:`irrigated lands model <IrrigatedPMPDoc>` and the :ref:`nonirrigated lands
rainfall model <NonIrrigatedDoc>`. The nonirrigated lands model is not used for all regions or crops. Most modeled regions
include rainfall modeling but only four crops are used in rainfall modeling: grain, bean, hay, and corn.