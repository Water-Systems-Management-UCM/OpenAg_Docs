.. _IrrigatedPMPDoc:

The Irrigated Land Crop Choice Model
======================================

The irrigated agriculture crop choice model employs positive mathematical programming (PMP), a deductive method
developed by `Howitt (1995) <https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1477-9552.1995.tb00762.x>`_
which calibrates exactly to base production input use (land, water, labor, and other)
and crop selection subject to limiting resource constraints on land and water. The approach captures
non-linearities associated to agricultural production that prevent overspecialization
in crop selection through the
parameters of a cost function. The approach is consistent with profit maximizing behavior in agricultural production and has
served as the backbone for economic impact assessment of droughts (`Medellin-Azuara et al. 2015 <https://link.springer.com/article/10.1007/s10040-015-1283-9>`_
, `Lund et al. 2017 <https://ascelibrary.org/doi/full/10.1061/%28ASCE%29WR.1943-5452.0000984>`_),
climate change (`Medellin-Azuara et al. 2011 <https://link.springer.com/article/10.1007/s10584-011-0314-3>`_),
and groundwater regulation (`Hanak et al. 2019 <https://www.ppic.org/wp-content/uploads/water-and-the-future-of-the-san-joaquin-valley-overview.pdf>`_), among other applications.

.. contents::
    :local:

Profit Maximizing Behavior
----------------------------
The PMP approach maximizes net returns to land and management from producing crops in an irrigated agriculture region
by selecting total land and water use, the selection of crops, and the intensity in production input use
(e.g., applied water per unit area) given a set of limited resource constraints. A calibrated PMP model allows simulation
of various economic, land use policy, climate, technology, or water management scenarios by allowing the user to alter
land and/or water availability, crop prices, or yields. For example, if there is a curtailment of water for irrigation due
to drought, the model will likely cultivate first those crops that provide the highest net returns and are less water
intensive.

.. _WaterExchangeSection:

Water Exchange
----------------
In addition to the resource-constrained profit maximizing behavior, the PMP crop choice model assumes water trading
within the region of analysis is allowed. Inter-regional water transfers are also possible with appropriate modifications
to the governing water balance and resource equations. Statewide profit maximization is also possible.

Total Land and Water Use
--------------------------
Both land and water are the limiting factors in the model. In the current setting, it is assumed that access to farm
labor and crop production supplies (such as fertilizer and agrochemicals) are unlimited. There is an implicit
assumption of no irrigated area expansion in the current setting, yet this constraint can be changed to some plausible
extent (e.g., 10 percent) within the model calibration range.

.. _CropPriceYieldSection:

Crop Prices and Yields
-------------------------
The calibrated model considers average base yields per crop and irrigated area, as well as commodity prices. Technological
change and improved crop management can increase yields, yet in some cases warmer climate conditions, deficit irrigation,
and other processes such as soil salinization may reduce average crop yields. The bundled crop price and yield provides
the marginal gross revenue per unit of land, yet it is possible to change it with respect to base conditions and the
model will provide a new cropping pattern based such that net returns are maximized.

Crop Area Constraints
------------------------
The calibrated model in the absence of changes to land and water availability as well as crop production economics
(price, yields, costs) will reproduce exactly the base calibration cropping patterns. Water shortages will likely affect
the lower value and high water use crops, however forages such as alfalfa, irrigated pasture and some silage crops are
required for downstream agricultural sectors such as dairies and beef cattle. Hence there are some constraints on minimum
silage requirements that must be added to avoid unrealistic fallowing of feed crops that cannot be hauled long distances
to the point of use. The same constraint can be employed for other crop categories.

Deficit Irrigation
-----------------------
The calibrated model allocates water based on average observed water use per unit area. However, under water scarcity
conditions, many irrigated areas around the world practice deficit irrigation, where growers apply less water than
necessary to achieve ideal yields in order to grow a larger acreage with limited water. This practice extends a
limited amount of water to more crop acreage, but with some sacrifice of crop yields. The OpenAg model settings
allow up to 1% deficit irrigation, meaning that any significant reductions in water
availability will lead to changes in crop acreage rather than reducing crop yields.

Mathematical Model Formulation
--------------------------------
The calibrated model predicts farmer’s crop decisions including on irrigated cropland use and use of inputs including
water within an area assuming profit maximizing behavior considering expected prices, subsidies, yields, and costs,
as well as restrictions on land, water and crop specific constraints. This is undertaken by solving the non-linear
program described by equations :math:numref:`eq1` to :math:numref:`eq3` below for each region *g*:

.. math:: Max Z= \sum_{i}{p_{i}Y_{gi}(X_{gij})} - \sum_{i}{\delta_{gi}X_{gi,land}} - \sum_{i}{}\sum_{j}{\omega_{gij}X_{gij}}
    :label: eq1

.. math:: \sum_{i}{X_{i,land} \le B_{g,land}}
    :label: eq2

.. math:: \sum_{i}{X_{i,water} \le B_{g,water}}
    :label: eq3

Individual regions *g* are assumed to freely trade water. Details on the full program are described in `Howitt et al. (2012) <https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1002/2016WR019639>`_.

References
--------------

* Hanak, Ellen, Alvar Escriva-Bou, Brian Gray, Sarge Green, Thomas Harter, Jelena Jezdimirovic, Jay Lund, Josué Medellín-Azuara, Peter Moyle, and Nathaniel Seavy. 2019. "`Water and the Future of the San Joaquin Valley: Overview <https://www.ppic.org/wp-content/uploads/water-and-the-future-of-the-san-joaquin-valley-overview.pdf>`_," February, 16.
* Howitt, Richard E. 1995. "`A Calibration Method for Agricultural Economic Production Models <https://doi.org/10.1111/j.1477-9552.1995.tb00762.x>`_." Journal of Agricultural Economics 46 (2): 147–59.
* Howitt, Richard E., Josué Medellín-Azuara, Duncan MacEwan, and Jay R. Lund. 2012. "`Calibrating Disaggregate Economic Models of Agricultural Production and Water Management <https://doi.org/10.1016/j.envsoft.2012.06.013>`_." Environmental Modelling & Software 38 (December): 244–58.
* Lund, Jay, Dist M Asce, Josué Medellín-Azuara, M Asce, John Durand, and Kathleen Stone. 2018. "`Lessons from California’s 2012 – 2016 Drought <https://doi.org/10.1061/(ASCE)WR.1943-5452.0000984>`_" 144 (10): 1–13.
* Medellín-Azuara, Josué, Richard E. Howitt, Duncan J. MacEwan, and Jay R. Lund. 2011. "`Economic Impacts of Climate-Related Changes to California Agriculture <https://doi.org/10.1007/s10584-011-0314-3>`_." Climatic Change 109 (1): 387–405.
* Medellín-Azuara, Josué, Duncan MacEwan, Richard E. Howitt, George Koruakos, Emin C. Dogrul, Charles F. Brush, Tariq N. Kadir, Thomas Harter, Forrest Melton, and Jay R. Lund. 2015. "`Hydro-Economic Analysis of Groundwater Pumping for Irrigated Agriculture in California’s Central Valley, USA <https://doi.org/10.1007/s10040-015-1283-9>`_." Hydrogeology Journal 23 (6): 1205–16.

