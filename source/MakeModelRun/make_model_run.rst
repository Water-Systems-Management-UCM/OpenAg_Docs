.. _MakeModelRunsDoc:

Creating Model Runs (Scenarios)
==================================
By default, running the OpenAg model with no modifications will produce the output that most
closely aligns with observed conditions, called the "Base Case". The OpenAg application
is designed to allow you to create your own model runs, or scenarios, where you specify
deviations or changes in conditions compared with the base case. You provide these in the form
of two separate types of modifications to the model inputs and constraints: region modifications
and crop modifications.

.. contents::
    :depth: 2
    :local:
    :backlinks: none

An Overview of Model Run Creation
-----------------------------------
Within the application, creating a model run has three steps:

#. Add Region Modifications:
    Add adjustmetns to region-wide parameters either across the model or for specific regions in the :ref:`model area <ModelAreasDoc>`.
    Modifications for regions will always include irrigated water availability and total cropped land availability and may
    include rainfall, depending on the model area and available data.
#. Add Crop Modifications:



.. seealso::
    :ref:`ModelInputHierarchyDoc` for more information on how OpenAg determines which values to use when inputs overlap.

Capabilities in the Application
---------------------------------
Though we have attempted to make the application as straightforward and user-friendly as possible, before creating a model run it is important
to spend time considering how to translate your scenario of interest into adjustments that the model accepts.

e.g. what can we actually change or control in the application

.. seealso::
    :ref:`TranslatingCommonScenariosDoc`

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

Region Modifications
______________________


.. seealso::
    :ref:`RegionModificationsDoc`

Crop Modifications
_____________________

.. seealso::
    :ref:`CropModificationsDoc`

All Regions and All Crops
___________________________

Resources not pooled - instead behaves as if an individual card was set up for each region or crop - optimization always
happens per region, so changing water availability in all regions card will not produce water transfers between regions.

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





