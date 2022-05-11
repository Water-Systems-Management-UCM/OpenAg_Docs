Model Limitations
=====================
As with every model, the drought assessment tool team considers the following limitations are present and may benefit
from further development in future releases of the tool.

* Nonirrigated land soil moisture (or precedent soil conditions) are not accounted for. The workaround at this point is to change price of the commodity to emulate gross revenue reductions in the crop. In the future, precedent soil conditions yield impact to be explicitly in a single or composite yield impact slider.
* Limited lifespan of calibration data is an area of improvement yet will remain appropriate for another 5 years. While current calibration represents the most recent land use available and costs of production, future upload of datasets and recalibration needs further development.
* Irrigated land model does not show maintenance costs of perennial crops if they are not grown for production in a dry year, but are kept alive using reduced irrigation for the following year. There is also an associated lingering effect of deficit irrigation in most perennials that is not factored in dynamically.
* Irrigated land model does not scale back yields when water availability is reduced (i.e. stress irrigation). Instead, it assumes that if a crop’s water needs cannot be met, it cannot grow that crop and removes enough acreage from production for that crop or another crop in order to balance water needs for in-production crops.
* Input data has a significant influence in model results. Curating the input data to better represent baseline production conditions benefits from documentation of sources and model assumptions.
* Baseline conditions calibration point. The more an scenario moves from the calibration point (baseline scenario), the less reliable become the results
* For the non-irrigated model: although we obtain regression coefficients using seasonal temp and precip for the same year (winter, spring and summer), we run the scenarios with precip adjustments that result in equal changes in precipitation across seasons, which might not be realistic (different seasons might have different amount of precipitation and different results in final yield)
* To simplify the scenario development, the modeler only uses the same year seasonal precipitation and temperature (winter, spring and summer), yet there might be significant impacts on yields from antecedent conditions (previous year precipitation and temperature) that the model is not considering
* Increases in production costs from increases in groundwater pumping or water trading costs are not factored in.


.. todo:: refine, flesh out, and incorporate in a more digestible format

.. seealso::

    * :ref:`NetRevenueLimitsDoc`
