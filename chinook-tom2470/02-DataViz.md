
# 02-DataViz

## Goals

* Introduce data viz in python
* Manipulation of data types
* (Re)Introduce NumPy and Pandas

## Links

* repo for class notes: https://github.com/ds5110/spring-2023
* [02-income.ipynb](https://colab.research.google.com/drive/17UVJ9aMVFQzt3vNDcnFxRlwEQ_GszzIP)
* [02-central-exercises.ipynb](https://colab.research.google.com/drive/1KrQr0qPTE-nAREGzBZeQgXvfu6AKbpMn)
* polleverywhere: https://PollEv.com/pbogden
* [scratch notebook](https://colab.research.google.com/drive/1H4sj-XdST_PqBXQTrkutsamSFrOs2wNG) -- shared

## Homework

* Homework #1 is posted in Canvas
* Submit by the due date for full credit
* Remember that there's a resubmission policy!
* Max grade on resubmissions is 9/10
* Remember all the code must run from the command line -- [git-intro](http://github.com/ds5110/git-intro)

## Projects

...as of 16 May (a couple more coming)

* [project list](project-list-16May23.md)
* [projects](projects-16May23.md) -- guidance for first few milestones

## Reading -- for next week

* [Data structures accepted by Seaborn](https://seaborn.pydata.org/tutorial/data_structure.html)
  * describes "tidy" data -- long-form and wide-form
* VanderPlas -- Chapters 2 & 3, and especially...
  * [03.06-Concat-and-Append.ipynb](https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/03.06-Concat-And-Append.ipynb)
  * [03.07-Merge-and-Join.ipynb](https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/03.07-Merge-and-Join.ipynb)
* McKinney
  * [8 Data Wrangling: Join, Combine and Reshape](https://wesmckinney.com/book/data-wrangling.html)
  * [10 Data Aggregation & Group Operations](https://wesmckinney.com/book/data-aggregation.html)

## Resources -- overview

* McKinney, 3rd Edition
  * [Chapter 3: Built-in data structures, functions, and files](https://wesmckinney.com/book/python-builtin.html)
  * [Chapter 4: Numpy basics: arrays and vectorized computation](https://wesmckinney.com/book/numpy-basics.html)
  * [Chapter 5: Getting started with pandas](https://wesmckinney.com/book/pandas-basics.html)
    * Series (1-D)
    * DataFrames (2-D)
  * [Chapter 9: Plotting and visualization](https://wesmckinney.com/book/plotting-and-visualization.html)
    * matlotlib
    * seaborn
* [Data Science Handbook](https://github.com/jakevdp/PythonDataScienceHandbook) (2022) by Jake VanderPlas
  * Chapter 2 -- Introduction to Numpy
  * Chapter 3 -- Introduction to Pandas
  * Chapter 4 -- Introduction to Matplotlib

## Read the docs (wisely)...

* API reference docs
  * [numpy](https://numpy.org/doc/stable/reference/index.html)
  * [pandas](https://pandas.pydata.org/docs/reference/index.html#api)
  * [matplotlib](https://matplotlib.org/stable/api/pyplot_summary.html)
    * [matplotlib.pyplot](https://matplotlib.org/stable/api/pyplot_summary.html)
  * [seaborn](https://seaborn.pydata.org/api.html)
* How to search the reference docs
  * stackoverflow can be a great path to the documentation -- if used wisely!
  * google your error message (colab offers a search of stackoverflow for you)
  * it helps if you know [How to ask a question](https://stackoverflow.com/help/how-to-ask) -- stackoverflow.com
* How to use the reference docs
  * Look at the examples in the reference docs!
  * Avoid random blogs and kaggle examples -- there's a lot of highly ranked junk out there.

## Visualize your data

...before you do anything else!!!

* [Anscombe's quartet](https://seaborn.pydata.org/examples/anscombes_quartet.html) -- seaborn.pydata.org
* [Datasaurus](https://cran.r-project.org/web/packages/datasauRus/vignettes/Datasaurus.html) -- R community version
* Is there structure in your data?
* Is there random noise in your data -- how much?
  * Are your data [IID](https://en.wikipedia.org/wiki/Independent_and_identically_distributed_random_variables)(independent and identically distributed)?
  * Are they normally distributed (Gaussian)?

## Income vs education

Distinguishing signal and noise

* [02-income.ipynb](https://colab.research.google.com/drive/17UVJ9aMVFQzt3vNDcnFxRlwEQ_GszzIP#scrollTo=uUVnW1JZGudi)
* Reproduce Figure 2.2 of ISL
* Investigate the order of the polynomial fit
* Visualize the residual -- with the goal of distinguishing signal and noise
* [income.md](income.md) -- instructor only

## Random number generators

* [random](random.md)

## GIL

* [GIL](gil.md) -- Global Interpreter Lock

## Histogram vs PDF

* [histogram-pdf](histogram-pdf.md)

## Central limit theorem

If your data includes a predictable signal plus random noise, then averaging may help distinguish them.

* [Central Limit Theorem](https://en.wikipedia.org/wiki/Central_limit_theorem) 
  * the sum of independent random variables tends toward a normal distribution
  * ...regardless of their distribution!
  * it can provide a baseline for understanding your data
  * it helps explain the prevalence of the "bell curve"
* The standard error of the mean of $n$ identically distributed random variables with standard deviation $\sigma$ is $\sigma / \sqrt{n}$.
* If the data are not independent or normally distributed, then you should know why
  * there may be something interesting going on
  * there may be some underlying predictable signal or process in your data
  * your visualization and analysis could provide insight
* [Central Limit Theorem](https://observablehq.com/d/fdba46dcce67b508) -- observable notebook
