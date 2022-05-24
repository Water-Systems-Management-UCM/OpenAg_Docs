.. _NetRevenueLimitsDoc:

Explanation and Limitations of Net Revenue Estimates
======================================================
OpenAg is an optimization model that maximizes net returns to land and management using
Positive Mathematical Programming (Howitt et al. 2012), a self calibrating method that
assumes non-linearities exist in agricultural crop production costs, and that the observed
input land use satisfies that marginal revenues equal marginal costs. Usually, baseline
conditions give net returns close to the difference between gross revenues and average
production costs. However, as scenarios created in OpenAg depart from the baseline conditions
through the addition of :ref:`user modifications <ModificationsOverviewSection>`, the net returns on individual crops or regions
resulting from the model objective function, which is comprised of all gross revenues and
all production costs (average and non-linear), may also depart from the baseline net returns,
and the net revenues may be reflective of assumptions on production outcomes and farmer
behavior which are hard to fully capture.

In the optimization process, OpenAg considers crop profitability, and under scarcity less
profitable crops are usually allocated less land area and irrigation water in comparison
with more profitable crops. OpenAg can be set to avoid unprofitability by scaling down
production costs in response to lower yields or crop prices, as farmers usually manage
production to avoid net losses. In addition, the objective function maximizes total net
returns to land and management from all crops or total producer surplus using input allocation
(land, water, labor and other) by crop and region. Given non-linearities in the objective
function, the total net returns might not coincide with those under baseline conditions,
which assume average costs are in place despite user modifications to land, water, price,
or yield.

It is possible to create scenarios that diverge from the baseline, even though scenario optimized
results may suggest negative net returns for individual crops since
the aggregate of all crops is maximized. The disparity in net returns explained above is solved
by postprocessing land use allocation from the optimized model, using gross revenues and average
costs to obtain net returns by crop for each modeled scenario. OpenAg assumes the resulting
cropping patterns will maintain crop profitability by using
the average costs. Growers typically take action to prevent losses by, for instance, cutting
back on variable costs for the year, such as supplies and labor. OpenAg may adjust costs in
net revenue estimates to account for such potential cost downscaling by scaling variable costs
such as supplies and labor by the price and yield modifications input by users when creating
model runs.

Though the adjusted costs in OpenAg’s postprocessing should provide a more accurate estimate
of net revenues than if average costs were assumed, postprocessed net revenue values should
be used with caution and only when comparing gross revenues to the base case or to other
scenarios/model runs cannot provide an appropriate metric of the economic impacts of land
and water use scarcity, changes in commodity prices, yield response to salinity, water stress,
or climate or higher production costs.


Net Revenue Calculation
------------------------

.. math:: area_{crop} * ((yield * adjustment_{yield} * price * adjustment_{price}) -
        (cost_{water} * water use) - cost_{land} - (adjustment_{yield} * adjustment_{price} * (cost_{labor} + cost_{supplies})))

