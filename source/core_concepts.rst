Core Concepts in |project_name|
=================================

.. index::
    single: overview

The |project_name| Model
---------------------------
The |project_name| application models
changes in land use, applied irrigation water, and gross revenue based on user-provided fine-grained
adjustments to land and water availability, crop prices and yields, and crop land-use constraints. It uses three
separate models, including Positive Mathematical Programming (`Howitt et al. 2012 <https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1002/2016WR019639>`_),
a linear model, and a rainfall regression model to account for multiple types of agriculture and assumptions.


.. index::
    double: concept; model area

.. _ModelAreaConceptSection:

Model Areas
-------------
Each distinct model in |project_name| is called a :code:`Model Area`, encompassing
regions, crop groups, and calibrated input data for the model. Model Areas are the top units of organization
for everything else within |project_name|.

.. index::
    double: concept; region

.. _RegionConceptSection:

Regions
--------
Each distinct model hosted in |project_name| will contain multiple regions. Regions represent real landscape areas,
typically some meaningful unit where land-use decisions may involve some coordination. The application
stores land use data for each region and other economic values that are used in the PMP model. |project_name| optimizes regions
independently, meaning that decisions in one region do not affect decisions in other regions, though users can simulate
activities such as water transfers through specifically crafted inputs to the model.

.. index::
    double: concept; crop

Crops
------
|project_name| groups multiple crops into groups that it refers to as "crops", so in many cases data on individual crops,
e.g. strawberries may be aggregated into a larger group, such as "berries", for modeling. |project_name|'s input data
ties crops to regions along with information on prices, yields, and costs that allow for economic modeling of each crop
in each region.

.. index::
    double: concept; model run
    double: concept; scenario

Model Runs (Scenarios)
----------------------

|project_name|'s web application is principally designed for scenario analysis and decision support, in addition to viewing
raw economic input data. A scenario can be thought of as answering a "what if" question you have, such as
"what if water deliveries are reduced in a set of regions due to climate change?" |project_name| helps you answer these questions through
:code:`Model Runs`, which allows you to define changes to input parameters then run the model and see the results as
compared to a scenario with no modifications or other scenarios you create.

.. seealso:: :ref:`ModelRunDoc`

.. index::
    double: concept; modification
    double: concept; region modification
    double: concept; crop modification

Modifications
--------------
When creating a model run, you will create a set of modifications to the model that come in two forms: modifications
to region-level data, such as irrigated water availability, rainfall, and cropped land area, and modifications to crop-level
data, such as price yield, and minimum/maximum land area.

.. seealso::
    * :ref:`MakeModelRunsDoc`
    * :ref:`RegionModificationsDoc`
    * :ref:`CropModificationsDoc`


.. index::
    double: concept; card

.. _CardsConceptSection:

Cards
-------
Some parts of the application and documentation will refer to "cards" - these will be boxes in the application with
sets of parameters that refer to a specific item - typically a crop or region's parameters.