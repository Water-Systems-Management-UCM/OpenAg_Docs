.. _ModelsAvailableDoc:

Models Available in OpenAg
==============================

OpenAg includes two models that run side by side - one for irrigated lands and one for nonirrigated lands.
By default, it uses a Positive Mathematical Programming (PMP) (`Howitt et al. 2012 <https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1002/2016WR019639>`_)
model for irrigated lands and it uses a statistical
regression model for nonirrigated (rainfall or dryland) agriculture. You may also choose to run a simple linear version
of the model for irrigated lands in place of the PMP model. OpenAg runs
each model separately for each region where data are available supporting both models and then pools the
results together in the application.

Where the PMP model focuses on decisions of land use and water allocation with user-provided price and yield modifications, for nonirrigated lands OpenAg estimates yields while assuming constant land use. Both models output revenues as their primary output, but only the PMP model estimates land use changes. Each model’s capabilities are summarized in the following table:

.. list-table::
    :header-rows: 1

    * - Model
      - User inputs
      - Outputs
    * - :ref:`Irrigated Lands PMP (Full) Model <IrrigatedPMPDoc>`
      - Irrigated water availability, land availability, crop price, crop yield, crop area constraints
      - Land allocation, water allocation, gross revenue
    * - :ref:`Irrigated Lands Linear (Simple) Model <SimpleModelingDoc>`
      - Irrigated water availability, land availability, crop price, crop yield
      - Land allocation, water allocation, gross revenue
    * - :ref:`Nonirrigated Lands Regression Model <NonIrrigatedDoc>`
      - Rainfall, crop price
      - Crop yield, gross revenue

The nonirrigated lands model is not included for all regions or all model areas - you will know a region includes rainfall data if the region has a slider to adjust rainfall in the web application.
