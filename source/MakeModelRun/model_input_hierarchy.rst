.. _ModelInputHierarchyDoc:

The Model Input Hierarchy: Prioritizing Overlapping Inputs
=============================================================
OpenAg allows for inputs that can overlap each other, such as setting irrigation water availability for
all regions and setting the same value for a specific region. In each case, only a single parameter will
apply - no merging is done between overlapping parameters, and the model applies the most specific input parameters
and discards less specific parameters.

.. note::
    It is important to note that, while the web interface makes it appear as if one set of settings
    can apply across the whole model, OpenAg applies parameters individually to each crop and region
    combination present in a :ref:`model area <ModelAreasDoc>`. The web interface simply provides a way
    to apply settings quickly across the whole model. A single value will always apply for each parameter
    for each region/crop combination, though they can have the same value.

Priority Orders
-----------------

Highest priority items are first, and lowest priority items are last for each list

Region Modification Hierarchy
_______________________________
#. No Production regions:
    Regions that are set to :ref:`"No Production" <AdvancedRegionOptionsSection>` override *all* other settings that would apply to that region, including settings
    from crop cards. OpenAg drops the data for No Productions regions before running the model and the data for a removed
    region is not included in the model run.
#. Hold to Base Case regions:
    :ref:`"Hold to Base Case" <AdvancedRegionOptionsSection>` behave the same way as No Production regions. Setting a region as
    Hold to Base Case overrides all the other settings for
    the region for the model run, including crop modifications that would apply to the region. OpenAg drops the data
    for regions set to Hold to Base Case from the model and re-adds the base case results back for the region after modeling the non-fixed and non-removed regions.
#. Specific region settings:
    Input parameters on a specific region are the highest priority way to specific a single input, such as irrigation water
    availability. If the region is not fixed or removed and a value is set on a specific region modification card, then
    that value will apply.
#. Region group settings (when available):
    If region groups are available, then parameters provided for a region group will apply for all regions within the
    region group unless a card is added to the model run for a region within the group, in which case the region-specific
    card's settings would take precedence for that region, with the region group card applying to all remaining regions
    in the group.
#. All Regions:
    The All Regions card is the fallback card - it applies when a more specific setting from the items above has not been provided.

Crop Modification Hierarchy
____________________________________
#. Region-linked crop value:
    Specific crop cards that have been linked to a single region take the highest priority for crop parameters and will
    be used when present.
#. Specific crop value:
    Similar to region cards, a modification card for a single crop is used for crop parameters in each region
    the crop is present in, except in the case where a region-linked crop card is present for the same crop, in which case
    the region-linked crop card would supply the parameters for that single crop and region and the crop-specific card
    without a region-link would supply the parameters for the crop in all other regions it is present within.
#. All Crops:
    The All Crops card is the fallback card - it applies when a more specific setting from the items above has not been provided.

.. warning::
    Crop adjustments never apply to regions that are set to "Removed" or "Fixed". These regions are not modeled directly
    and so will not include crop modifications, regardless of region-linking.