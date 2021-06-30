.. _NonIrrigatedDoc:

The Nonirrigated Lands Regression Model
=========================================

The nonirrigated land model operates in two phases. In its first phase a regression model estimates coefficients per-region
crop yield response based on winter, spring, and summer temperatures and precipitation using region-level monthly input
data for a recent period of record depending on the application at hand.

Regression coefficients obtained in the first phase are employed in modeling scenarios runs. Model outputs
provide estimated levels of crop production and gross revenues resulting from temperature and changes in precipitation.
This phase is run twice: first without precipitation adjustments and then run again with them. The yield change is calculated as the
difference between these to remove artifacts introduced by the regression itself.

OpenAg calculates gross revenues based on the new yield estimates in a similar manner to the PMP model’s revenue
calculation: :code:`crop area (acres) * estimated yield (tons/acre) * adjusted price ($/ton)`

The regression model uses a more limited dataset than the PMP model, depending on how much agriculture is irrigated
or nonirrigated. In order to reduce effects from small samples, it is limited to crops with large amounts of nonirrigated
area, and it is only used in regions where nonirrigated agriculture accounts for more than 5% of total agriculture.

Considerations
-----------------
The regression model can occasionally show *higher* yields in response to *less* rainfall if the data for the calibration
period had that response. In the Washington model area, this is rare, but has been noted as occurring.
