.. _WashingtonModelDoc:

The Washington State Model
===========================

.. _WashingtonModelOverviewSection:

Model Overview
------------------
Data collected for use in the model includes a variety of types and spans a decade (2008-2018), although only a selected
subset (2016-2018) is used in model calibration at this time. Spatial coverage of the model is nearly the entire state, with the
exception of some regions which lack the agricultural complexity to effectively model (see :ref:`FixedRegionsSection` for more information),
and the spatial scale of the model is a modified version of Washington's `Water Resource Inventory Areas (WRIA) <https://waecy.maps.arcgis.com/apps/webappviewer/index.html?id=996e6b21ae394cc3a3b63c6da0c3aa0a>`_.
Models are run at an annual scale, as sub-annual planting decisions cannot be captured using available data.

Model input data utilizes a crop grouping structure to retain sufficient resolution in outputs while
reducing data dependency. Initial land use surveys contain approximately 200 commodities that OpenAg groups into 14
categories for modeling. Each category is then assigned a proxy commodity to represent the economics and water needs
of the group. Proxies are assigned based on a combination of data availability and prominence in the overall land portfolio.

.. toctree::
    :maxdepth: 2

    input_data_sources.rst

.. contents::
    :local:
    :depth: 2



Supported Capabilities
------------------------
The Washington model supports both the :ref:`irrigated lands model <IrrigatedPMPDoc>` and the :ref:`nonirrigated lands
rainfall model <NonIrrigatedDoc>`. The nonirrigated lands model is not used for all regions or crops. Most modeled regions
include rainfall modeling but only four crops are used in rainfall modeling: grain, bean, hay, and corn.