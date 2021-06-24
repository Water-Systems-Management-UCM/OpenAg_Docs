.. _SimpleModelingDoc:
"Simple" Modeling and Linear Scaling
=======================================

|project_name| includes a simplified modeling mode for regions where

1. Sufficient data to support PMP modeling are unavailable
2. Data are available, but the region contains a small acreage of agriculture
3. The region supports only one or two crop commodity groups
4. You wish to run a version of the model that makes a more limited set of assumptions
5. For running "worst case scenario" modeling

Where the Full model assumes that within regions, resources can be freely traded, allowing multiple independent farmers
to find optimal economic outcomes as resource availability changes, the simplified version assumes that changes
to resource availability apply evenly to everyone, and they are unable to take steps to further improve their outcomes
as their resource availability changes. We sometimes think of this as a "worst case scenario" outcome in that, when using
the model to reduce resource availability, the Simple model gives us a reasonable lower bound on gross revenues and can
be used with the Full PMP-modeled version of the same data to estimate a range of outcomes.

In the first three cases above, |project_name| may be unable to adequately run the Full PMP model, so it will default to using
the Simple model - this behavior :ref:`will show up when adding crop cards <DefaultAdvancedRegionOptionsSection>`, but will also apply to the affected regions whether
or not a card is explicitly added for the region.

Simple Model Formulation
--------------------------
For each crop in the region, revenue is calculated using the following equations. The adjustments provided in the web
interface are noted as :code:`adj` with a subscript and are used as proportions relative to the original value.

.. math:: land scaling factor = Min(adj_{land}, adj_{irrigatedwater})

.. math:: gross revenue = price * adj_{price} * yield * adj_{yield} * acreage * land scaling factor

The Simple model makes an assumption similar to the Full PMP model that deficit irrigation is not allowed. Thus, a proportional
reduction in water can be thought of as proportional reduction in land because, without deficit irrigation, water will
not be available to farm additional land as water is reduced. However, land and water reductions do not stack, and instead,
the Simple model uses the smallest of the two adjustments as the limiting factor that determines how much land is in production.