.. _NetRevenueLimitsDoc:

Explanation and Limitations of Net Revenue Estimates
======================================================
OpenAg is designed and calibrated to optimize gross revenues for comparison to a base case, where
the absolute values of revenues may deviate from actual values, but the values relative to the base case should
accurately represent the impacts of model inputs.

In the course of estimating gross revenues, the model does take into account a measure of profitability for each crop -
it is part of how it chooses land area allocations for crops in a region. Less profitable, or unprofitable, crops
are assigned less land area. However, the model avoids the assumption that a crop has become truly unprofitable, even with
user inputs that may trigger unprofitability, in part because it is an unlikely outcome. Growers typically
take action to prevent losses by avoiding plantings and cutting back on variable costs for the year such as supplies and
labor. Additionally, the model inputs explicitly indicate that each crop is grown in each region, so the model avoids
completely removing production for a crop, even if it becomes unprofitable given inputs. Instead, it may still show up,
but with very small land areas, and with some fixed costs per acre.

The model objective function that balances these concerns cannot provide gross or net revenues, however. Instead,
it chooses the crop allocation that is then used to estimate gross and net revenues after the fact. Because the model
is calibrated for gross revenues and the calculation is simpler, those values are reliable. Net revenues, in contrast, require
a linear function that includes costs. This linear function estimates profitability in a different manner
from the objective function. When combined with user input changes to the model that make it deviate significantly from
its calibration point, it can produce profitability estimates that are *different from*
the objective function that balanced the crop allocation in the region, resulting in unreliable net
revenue values. In some cases, these values may indicate unprofitability via negative net revenue values.

OpenAg takes steps to better align the net revenue calculation of the objective function with the post-calculated net revenue.
Primarily, it does this by scaling the variable costs of labor and supplies using the price and yield adjustments,
under the assumption that as prices and yields decrease, growers may put fewer inputs into a parcel of land. The net
revenue values that result from this scaling appear to include fewer artifacts, but have not undergone comprehensive review
or calibration. Net revenue values should be used with caution and *only* when comparing gross revenues to the base case
or to other scenarios/model runs cannot provide a necessary answer.

Net Revenue Calculation
------------------------


Limitations
-------------




.. todo::

    Fill in