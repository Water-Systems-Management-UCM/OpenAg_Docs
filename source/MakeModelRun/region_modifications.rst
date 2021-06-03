.. _RegionModificationsDoc:

Region Modifications
=====================
.. contents::
    :local:

.. _RegionModificationsOverviewSection:

Overview
----------

.. _RegionModificationsParametersSection:

Parameters
----------------

.. seealso::
    :ref:`See how region parameters are used in the irrigated land model <WaterExchangeSection>`

Creating Region Modification Cards
------------------------------------
1. Search for region by name
2. Click on map

Map Capabilities
-------------------

.. _AdvancedRegionOptionsSection:

Advanced Region Options
------------------------
When working with region cards, you have the option to change advanced settings by clicking on the
"Advanced" expansion panel at the bottom of the card. The advanced settings give you three options
that adjust how the region is modeled. Since each region is modeled independently, you can change these settings for any
given region without affecting the output of another region.

#. Modeled:
    The default behavior - the region will be run through the PMP model and, when applicable, through the nonirrigated agricultural yield model.
#. Hold to Base Case:
    In some cases, you may want to hold specific region's values as "static" - in this case, holding
    them to the base case prevents them from being modeled, and assumes that they won't change from the base
    conditions. The model run will provide the same outputs for the region as those in the base case.
#. No Production:
    Use this if you want to model the region as if it produced nothing over the model time period. In the
    San Francisco Bay Delta, for example, this can be useful for scenarios where an island floods and produces
    no agricultural output. An alternative is to model the region normally, but filter results in the output
    to remove the region, in case you want to assess results both with and without the region.

Note that these are high priority settings in that they take first precedence. A region held to base case will not
be affected by the crop modification settings you choose. Results will appear exactly as in the base case for that region,
while other regions will apply crop modifications as normal.

.. image:: region_card_advanced.png


.. _AdditionalReadingRegionModifications:

Additional Reading on Modifications
-------------------------------------------
* :ref:`ModificationsOverviewSection`
* :ref:`ModelInputHierarchyDoc`
* :ref:`CropModificationsDoc`