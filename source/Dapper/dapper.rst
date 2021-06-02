How the Model Works
====================
OpenAg is composed of two separate models for irrigated and nonirrigated
lands. Each of these models operates on distinct Model Areas, which provide
the suite of inputs, region definitions, crop data, and more required to
run OpenAg's models. This section provides information on how the models
in OpenAg work and the Model Areas that they work with.

.. figure:: ModelArea_Diagram.png

    A diagram of OpenAg's input data and model relationships. Each model area has many regions with independent data.
    Each region runs as an independent model, but all regions are run through both models simultaneously.


.. todo:: Describe model and data relationships briefly in text


.. toctree::
    :maxdepth: 2
    :caption: Contents

    available_models.rst
    ../ModelAreas/model_areas.rst
    input_data.rst
    irrigated_pmp.rst
    nonirrigated.rst
    outputs.rst
    irrigated_nonirrigated_data_split.rst
