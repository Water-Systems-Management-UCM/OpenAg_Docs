.. _ModelsAvailableDoc:

Models Available in OpenAg
==============================

OpenAg includes two models that run side by side. It uses a Positive Mathematical Programming (PMP) [CITE] model for irrigated lands and it uses a statistical regression model for nonirrigated (rainfall or dryland) agriculture. OpenAg runs each model separately for each region where data are available supporting both models and then pools the results together in the application.

Where the PMP model focuses on decisions of land use and water allocation with user-provided price and yield modifications, for nonirrigated lands OpenAg estimates yields while assuming constant land use. Both models output revenues as their primary output, but only the PMP model estimates land use changes. Each model’s capabilities are summarized in the following table:

.. list-table::
    :header-rows: 1

    * - Model
      - User inputs
      - Outputs
    * - Irrigated Lands PMP Model
      - Irrigated water availability, Land availability, crop price, crop yield, crop area constraints
      - Land allocation, water allocation, gross revenue
    * - Nonirrigated Lands Regression Model
      - Rainfall, crop price
      - Crop yield, gross revenue

The nonirrigated lands model is not included for all regions or all model areas - you will know a region includes rainfall data if the region has a slider to adjust rainfall in the web application.
