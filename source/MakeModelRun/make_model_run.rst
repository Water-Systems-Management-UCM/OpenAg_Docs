.. _MakeModelRunsDoc:

Creating Model Runs
==================================
By default, running the OpenAg model with no modifications will produce the output that most
closely aligns with observed conditions, called the "Base Case". The OpenAg application
is designed to allow you to create your own model runs, or scenarios, where you specify
deviations or changes in conditions compared with the base case. You provide these in the form
of two separate types of modifications to the model inputs and constraints: region modifications
and crop modifications.

On this page:

.. contents::
    :depth: 2
    :local:
    :backlinks: none

An Overview of Model Run Creation
-----------------------------------
Within the application, creating a model run has three steps:

#. Add :ref:`Region Modifications <RegionModificationsDoc>`:
    Add adjustments to region-wide parameters either across the model or for specific regions in the :ref:`model area <ModelAreasDoc>`.
    Modifications for regions will always include irrigated water availability and total cropped land availability and may
    include rainfall, depending on the model area and available data.
#. Add :ref:`Crop Modifications <CropModificationsDoc>`:
    Add adjustments to crop-specific parameters, such as prices, yields, and crop area constraints. The crop parameters will apply to the crop
    in all region it is grown in, by default, though it is possible to :ref:`tie crop parameters to a specific region <RegionLinkedCropsSection>`.
#. Add Metadata and Review:
    The final step of creating a model run allows you to add a name, descriptive text, and to review a summary of inputs.

.. seealso::
    :ref:`ModelInputHierarchyDoc` for more information on how OpenAg determines which values to use when inputs overlap.

Overview of Modifications
---------------------------
When creating a new model run, most inputs are expressed as modifications relative to the base case. You can express
these modifications for all regions or all crops, or provide modifications for specific regions or specific crops.

By default, OpenAg preserves the base case, so a model run with no modifications will produce identical results to the
base case model run for the model area. All modification options default to 100%, meaning the application will keep
the value exactly as in the base case. Adjusting the value then means making an adjustment relative to that item's normal value,
rather than inputting an absolute value for the parameter. If you wish to input a specific quantity of a resource (e.g.
irrigation water availability), then you need to first convert it to a percentage by comparing it to the amount available
in the base case for the same unit of analysis, such as the individual region it applies to or all regions.

As a consequence of using relative values, for some scenarios, you will need to carefully consider your inputs. For example,
if you want to simulate a water transfer between two regions, it would be incorrect to increase one region by 10% and
decrease the other by 10% unless they both have the same amount of total available irrigation water. Instead, you would
need to determine how much water is available in each region, using either the Input Data Viewer or viewing the base case,
and then determine what percentage values for each region would indicate the same amount of water.

All Regions and All Crops
___________________________

.. figure:: all_regions.png

    The All Regions card with model parameters showing for all regions in the model

The most straightforward inputs in OpenAg are displayed by default in the form of the "All Regions" and "All Crops"
cards. The controls on these cards adjust the associated parameter for every region in the model area. Conceptually,
the All Regions and All Crops can be thought of as making an adjustment across the entire model domain. So adjusting
"irrigation availability" to 90% would produce a 10% cutback of irrigation water in every region within the model.

When setting values via the All Regions or All Crops cards, resources are not pooled between regions or crops and there
is no implicit trading between regions, though you can replicate that scenario. Instead, when you adjust values
on the All Regions or All Crops cards,
the model behaves as if an individual card was set up for each region or crop. In other words, optimization always
happens per region and the values are set explicitly for each region and crop combination, so changing water
availability in the all regions card, for example, will not produce water transfers between regions.

Adding Cards
-----------------
For more granular adjustments, OpenAg allows you to create modification cards for each region or crop in the model area.
Modification cards provide the same parameters as are on the All Regions or All Crops card, but they are specific to
the region or crop selected when creating the card.

.. figure:: adding_region_cards.png

    Cards can be added either by searching the Add Modifications dropdown or clicking on the map (regions only)

You may create cards in two ways:

1.
    From the dropdown menu under the Add Region Modifications or Add Crop Modifications heading. You may select one or
    deselect one or more regions from the list shown in alphabetical order. You may also type in the dropdown to search
    or filter the regions to one whose name you know.
2.
    For region modifications you may also click on the map to create a region modification card for the corresponding
    region. Since crop modification cards apply to the crop in all regions, there is no map to add crop modification cards.


Overview of Region Modifications
___________________________________

..
    .. image:: RegionModifications.png

.. seealso::
    :ref:`RegionModificationsDoc`

Overview of Crop Modifications
_________________________________

..
    .. image:: cropimage.png

.. seealso::
    :ref:`CropModificationsDoc`

.. _AllRegionsAndAllCropsOverviewSection:

.. seealso::
    :ref:`ModelInputHierarchyDoc`


Capabilities in the Application
---------------------------------
Though we have attempted to make the application as straightforward and user-friendly as possible, before creating a model run it is important
to spend time considering how to translate your scenario of interest into adjustments that the model accepts.

.. todo:: flesh out section stub

e.g. what can we actually change or control in the application

.. seealso::
    :ref:`TranslatingCommonScenariosDoc`


.. _ModificationsOverviewSection:

Summary and Review
--------------------

Additional Reading on Model Run Creation
-------------------------------------------
.. toctree::
    :maxdepth: 2

    region_modifications.rst
    crop_modifications.rst
    model_input_hierarchy.rst
    translating_common_scenarios.rst

