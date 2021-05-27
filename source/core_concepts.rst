Core Concepts in OpenAg
========================

The OpenAg Model
-----------------
The OpenAg application utilizes Positive Mathematical Programming (Howitt et al. 2012) to model
changes in land use, applied irrigation water, and gross revenue based on user-provided fine-grained
adjustments to land and water availability, crop prices and yields, and crop land-use constraints.

.. _RegionConceptSection:
Regions
--------
Each distinct model hosted in OpenAg will contain multiple regions. Regions represent real landscape areas,
typically some meaningful unit where land-use decisions may involve some coordination. The application
stores land use data for each region and other economic values that are used in the PMP model. OpenAg optimizes regions
independently, meaning that decisions in one region do not affect decisions in other regions, though users can simulate
activities such as water transfers through specifically crafted inputs to the model.

Crops
------
OpenAg groups multiple crops into groups that it refers to as "crops", so in many cases data on individual crops,
e.g. strawberries may be aggregated into a larger group, such as "berries", for modeling. OpenAg's input data
ties crops to regions along with information on prices, yields, and costs that allow for economic modeling of each crop
in each region.

Model Runs (Scenarios)
----------------------
.. todo:: This item should be updated/rewritten to be clearer - I'm not sure the language used clarifies the model significantly.

OpenAg's web application is principally designed for scenario analysis and decision support, in addition to viewing the
raw economic input data. A scenario can be thought of as answering a "what if" question you have, such as
"what if crop yields are reduced in a set of regions due to climate change?" OpenAg helps you answer these questions through
:code:`Model Runs`, which allows you to define changes to data and the model, then run the model and see the results as
compared with a scenario with no modifications.

.. seealso:: :ref:`ModelRunDoc`


Modifications
--------------
When creating a model run, you will create a set of modifications to the model that come in two forms: modifications
to region-level data, such as irrigated water availability, rainfall, and cropped land area, and modifications to crop-level
data, such as price yield, and minimum/maximum land area.

.. seealso:: :ref:`MakeModelRunsDoc`

.. _CardsConceptSection:

Cards
-----
