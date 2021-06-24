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

#. Full:
    The default behavior - the region will be run through the :ref:`full PMP model <IrrigatedPMPDoc>` and, when applicable, through the nonirrigated agricultural yield model.
#. Simple:
    In some cases, you may not want to make the assumptions that the full PMP model makes - in this case, the "simple"
    option prevents them from being modeled in the PMP formulation, and instead assumes a linear scaling of values based
    upon modifications in the input. See :ref:`SimpleModelingDoc` for more information on how the region will be modeled
    when choosing this option.
#. No Production:
    Use this if you want to model the region as if it produced nothing over the model time period. In the
    San Francisco Bay Delta, for example, this can be useful for scenarios where an island floods and produces
    no agricultural output. An alternative is to model the region normally, but filter results in the output
    to remove the region, in case you want to assess results both with and without the region.

Note that these are high priority settings in that they take first precedence. A region held to base case will not
be affected by the crop modification settings you choose. Results will appear exactly as in the base case for that region,
while other regions will apply crop modifications as normal.

.. image:: region_card_advanced.png

.. _DefaultAdvancedRegionOptionsSection:
Default Advanced Region Options
__________________________________
In some cases, when choosing a region, one of the advanced region options may show up as chosen by default for that region.
This occurs because some regions may have default modeling behaviors other than the full PMP model, based primarily on
data availability. Regions with very small acreages of agriculture are very sensitive to fluctuations in inputs and regions
with only one or two crop groups cannot be modeled with a PMP. In these cases, the region may show up with the :ref:`Simple
modeling option <SimpleModelingDoc>` chosen by default. You may change these values, but note that it may make the results
less reliable or result in an infeasible model run.

.. warning::
    It is important to note that these default behaviors apply to the regions even if you do not choose them for
    modifications. If a region has a default modeling behavior and you do not create a region modification card
    for it, then the default behavior will apply.

.. _AdditionalReadingRegionModifications:

Additional Reading on Modifications
-------------------------------------------
* :ref:`ModificationsOverviewSection`
* :ref:`ModelInputHierarchyDoc`
* :ref:`CropModificationsDoc`