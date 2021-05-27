.. _IrrigatedDataSplitDoc:

How OpenAg Splits Data Between Irrigated and Nonirrigated Lands
================================================================
By default, OpenAg uses the input data for each region to determine what data goes into the
:ref:`irrigated land model <IrrigatedPMPDoc>` and what data goes into the :ref:`nonirrigated land model <NonIrrigatedDoc>`.
The input data contain values for the irrigated acreage and the nonirrigated acreage for each crop within each region.

When either irrigated or nonirrigated acreage is small for a crop in a region, the model changes its behavior in order to
avoid the effects of optimizing small values, which could produce incorrect results. Before splitting data between the
irrigated and nonirrigated models, it checks the irrigated and nonirrigated acreages for each crop to make sure that they're
more than 5% of the total value for the crop. If the nonirrigated acreage is less than 5% of the total within the region,
it will merge the acreage for the nonirrigated acreage with the irrigated acreage and run it through the PMP model. Similarly, if the irrigated
acreage is less than 5% of the total acreage for the crop in the region, it will merge the irrigated acreage into the nonirrigaged
acreage and run it through the regression model.

For example if we had the following crops and acreages in a region, we would send the outputs as shown in the table

.. list-table:: Example Crop Acreage in a Single Region
    :header-rows: 1

    * - Crop
      - Irrigated Acreage
      - Nonirrigated Acreage
      - Acreage sent to PMP model
      - Acreage sent to Regression model
    * - Corn
      - 80 acres
      - 20 acres
      - 80 acres
      - 20 acres
    * - Grain
      - 4 acres
      - 96 acres
      - 0 acres
      - 100 acres
    * - Beans
      - 97.5 acres
      - 2.5 acres
      - 100 acres
      - 0 acres

So, a crop like corn, which has a split of acres at 80% irrigated and 20% nonirrigated is sent to the models exactly as
the inputs provide, with 80 acres used in the PMP model and 20 acres used in the regression model. But the other two crops
in the region are modified slightly. Grain, with 96 nonirrigated acres and 4 irrigated acres has all 100 acres sent to the
nonirrigated regression model. Beans, see the reverse, with 97.5 acres of irrigated land and 2.5 acres of nonirrigated land,
it sees all 100 acres of its cropped area sent to the irrigated PMP model. These numbers add up to 100 for ease of percentages,
but in reality, the area for each crop within a region would not match between crops.

These calculations are conducted for each crop and each region, so even though all grain acreage is sent to the regression
model for this example region, in other regions it may still use the PMP model or a combination of the PMP and regression
models, based on the acreages for each specific region.