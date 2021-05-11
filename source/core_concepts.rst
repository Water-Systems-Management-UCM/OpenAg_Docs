Core Concepts in OpenAg
========================

The OpenAg Model
-----------------
The OpenAg application utilizes Positive Mathematical Programming (Howitt et al. 2012) to model
changes in land use, applied irrigation water, and gross revenue based on user-provided fine-grained
adjustments to land and water availability, crop prices and yields, and crop land use constraints.

Regions
--------
Each distinct model hosted in OpenAg will contain multiple regions. Regions represent real landcape areas,
typically some meaningful unit where land use decisions may involve some coordination. The application
stores land use data for each region and other economic values that are used in the PMP model. OpenAg optimizes regions
independently, meaning that decisions in one region do not effect decisions in other regions, though users can simulate
activities such as water transfers through specifically crafted inputs to the model.

Crops
------

Model Runs (Scenarios)
----------------------

Modifications
--------------

Cards
-----
