
# Statsmodels exercises

Instructions...for breakout & in-class **teams**

* One person create a shared Colab notebook to share with your breakout team
  * One person should manage the Colab notebook
  * One person should be prepared to be present results and lead discussion when we return from breakout
  * Each group should make sure they have an accurate notebook at the end of class
  * Note: there will be 3 sets of exercises (12 total)
* Share the Colab notebook with me and give me a copy of the URL when I visit your breakout room
  * I'll use these notebooks to monitor progress
  * Students can use these to discuss what's going on
* Presentations
  * When you're done each set of exercises, one person in the breakout should let me know
  * Contact me by chat or by returning to the main session.

# Exercises -- Set 1

* Exercise 1
  * Reproduce the Table 3.1 (p68): univariate sales on TV (coeff, stderr of coef, t-statistic, p-value)
  * Adapt the statsmodels OLS-estimation demo to reproduce the content of Table 3.1 (p68) of ISL
  * [OLS-estimation](https://www.statsmodels.org/stable/examples/notebooks/generated/ols.html#OLS-estimation)
* Exercise 2
  * Reproduce the content of Table 3.2 (p69): performance metrics for model (Resid std err, R^2, F-statistic)
  * Look at API Reference docs and adapt the example
  * [OLS API reference](https://www.statsmodels.org/stable/generated/statsmodels.regression.linear_model.OLS.html)
* Exercise 3
  * Reproduce Figure 3.1 (p62): plot univariate model: sales on TV
  * Use matplotlib only (not seaborn)
  * This involves extracting the parameters from the model and applying Eqn 3.5 (p63)
* Exercise 4
  * Plot the residuals from the univariate model with TV
  * A solution for this exercise is not in the book -- it's a simple modification of the previous exercise
* Exercise 5
  * Plot the distribution of the residuals Sales vs TV
* Discuss the results in after reconvening with the entire class

# Exercises -- Set 2

* Exercise 6 -- other univariate models
  * Solve this exercise by applying DRY programming principles
  * Reproduce Table 3.3 (p72)
* Exercise 7 -- multivariate model
  * Reproduce Table 3.4 (p74)
* Exercise 8 -- correlation matrix
  * Recreate Table 3.5 (p75)
  * With numpy (from statsmodels example): [plot_corr](https://www.statsmodels.org/dev/generated/statsmodels.graphics.correlation.plot_corr.html) example
  * With pandas [DataFrame.corr()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html)
* Discuss the results in after reconvening with the entire class

# Exercises -- Set 3

* Exercise 9
  * Plot residuals from multivariate linear model -- not in book
* Exercise 10
  * Plot residuals vs cross-term -- not in book
* Exercise 11 -- removing additive (linear) assumption
  * Reproduce Table 3.9 (p89)
* Exercise 12 -- Residual with cross term vs cross term
  * Plot residuals from the multivariate model that includes the cross-term vs the cross-term
* Discuss the results in after reconvening with the entire class
