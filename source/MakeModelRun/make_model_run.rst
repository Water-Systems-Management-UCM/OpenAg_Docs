.. index::
    pair: model run; create

.. _MakeModelRunsDoc:

Creating Model Runs
==================================
By default, running the OpenAg model with no modifications will produce the output that most
closely aligns with observed conditions, called the "Base Case". The OpenAg application
is designed to allow you to create your own model runs, or scenarios, where you specify
deviations or changes in conditions compared with the base case. You provide these in the form
of two separate types of modifications to the model inputs and constraints: region modifications
and crop modifications.

.. todo:: This page needs some restructuring once everything is written - the adding cards section is redundant,
    and maybe those kinds of details go on another page

.. toctree::
    :maxdepth: 2
    :caption: In this section:

    model_run_creation_overview.rst
    region_modifications.rst
    crop_modifications.rst
    model_input_hierarchy.rst
    translating_common_scenarios.rst



