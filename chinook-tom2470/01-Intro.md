
# 01 -- Intro

## Goals

* Course overview
* Introductions
* Setup

## links

* Repo for class notes: https://github.com/ds5110/summer-2023
* Polleverywhere: https://PollEv.com/pbogden
* [01-numpy.ipynb](https://colab.research.google.com/drive/1QJeh2ELgp5eqwHCYQ0VeyNXXI1KYGUKv)
* [03.02-Data-Indexing-and-Selection.ipynb](https://drive.google.com/file/d/1y0ieAm2_1g3SWHS5cLAmWC5ulZYXxW5z) by Jake Vanderplas
* [Scratch notebook](https://colab.research.google.com/drive/1H4sj-XdST_PqBXQTrkutsamSFrOs2wNG) -- shared

## Course overview

* See Canvas for the syllabus
* Homework & project timelines are coming

## Introductions

Brief introductions.

## Reading and exercises (for next week)

* ISL
  * Ch 1: [ISL](https://www.statlearning.com/) -- Background and notation
    * Bring any questions if you have on this chapter to class.
  * Ch 2: [ISL](https://www.statlearning.com/) -- Intro/overview
    * We'll review Section 2.1 in class, so bring any questions you have on this section.
    * We'll implement some of the material in Python.
    * Skim Section 2.2 -- the material is important and we'll get to it at some point.
    * We won't cover Sections 2.3 and 2.4, which depend on R.
* PDS -- matplotlib
  * We'll start working with seaborn and matplotlib next week to visualize and work with tidy data.
  * PDS github repo: https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/
  * Read the following notebooks, and experiment by running the code in Colab...
    * 04.00-Introduction-To-Matplotlib.ipynb
    * 04.01-Simple-Line-Plots.ipynb
    * 04.02-Simple-Scatter-Plots.ipynb
  * These notebooks use numpy and pandas -- make sure you understand what's going on.
    * If numpy is new to you, then look at relevant notebooks in Chapter 2 of PDS
    * If pandas is new to you, then look at relevant notebooks in Chapter 3 of PDS
* [Seaborn data structures](https://seaborn.pydata.org/tutorial/data_structure.html) -- pydata.org
  * This section in the Seaborn documentation describes "tidy" data
  * You can experiment with Seaborn by running the code from the seaborn documentation in Colab.
* [How to ask a good question](https://stackoverflow.com/help/how-to-ask) -- stackoverflow.com
  * It's important to know how to ask a good question, even if you're asking google.
  * Stackoverflow can be a great resource for answering good questions and debugging, provided it's used well.
  * Be careful about how you use google and stackoverflow. And be super careful about random blogs.
* For awareness...
  * [Ch 12: R4DS](https://r4ds.had.co.nz/tidy-data.html)
    * "Tidy data" is a adopted from the R community
  * [Introduction to licenses](https://observablehq.com/@observablehq/licenses) -- observablehq.com
    * Attribution and licenses are important when using published work.
    * Remember [Northeastern's academic integrity policy](https://osccr.sites.northeastern.edu/academic-integrity-policy/)
    * Copy and paste could have legal implications that extend beyond academic integrity (unlikely for us right now).

## Projects

* [projects.md](projects.md)
* An example...
  * [5110 stinky2](https://ds5110.github.io/stinky2/)
  * [7290 stinky](https://cs7290.github.io/stinky/)

## Data science environment

* [git-intro](https://github.com/ds5110/git-intro)
  * including [setup.md](https://github.com/ds5110/git-intro/blob/main/setup.md)
  * and [git.md](https://github.com/ds5110/git-intro/blob/main/git.md)
* Make sure you can clone a repo, make local changes, and push them back to github.
* If you have difficulty or connect during office hours.
* Additional resources: [Github Quickstart](https://docs.github.com/en/get-started/quickstart) -- github
* Command line -- Really!?
  * The following excerpts come from [this Nature article](../resources/nature_observable.pdf)
  * "Reactive, reproducible, collaborative: computational notebooks evolve" by Jeffrey Perkel, Nature, p156, Vol 593, 6 May 2021
  * "A 2019 study found that just 24% of 863,878 publicly available Jupyter notebooks on GitHub could be successfully re-executed, and only 4% produced the same results."
  * "Notebooks are messy. You write stuff, keep old crusty code behind, and it's hard to kind of figure out which cells to execute in the right order because you're trying different things."
* For these and other reasons...
  * Colab for prototyping & class interactions
  * GitHub for assignments & projects

## Q: R or Python?

* R or Python or...?
  * [Berkeley](https://bootcamp.berkeley.edu/blog/most-in-demand-programming-languages/)
  * [Northeastern](https://www.northeastern.edu/graduate/blog/most-popular-programming-languages/)
  * [Tiobe index](https://www.tiobe.com/tiobe-index/)
* R perspective
  * Data science overview -- [Hadley Wickham's perspective](https://r4ds.had.co.nz/explore-intro.html)
  * [ISL online course](https://www.statlearning.com/online-course)
  * [Lecture 1](https://youtu.be/5N9V07EIfIg) -- youtube
* Python perspective
  * [NumPy.org](https://numpy.org/)
    * The feature gallery on the home page is worth reviewing
    * The core of NumPy is well-optimized C code
    * [Black Hole case study](https://numpy.org/case-studies/blackhole-image/)
    * Note [the data-processing pipeline](https://numpy.org/case-studies/blackhole-image/#the-challenges)
  * [Python for data analysis](https://wesmckinney.com/) (2022) by Wes McKinney
    * McKinney's book focusses on "structured data" -- tidy/tabular
    * [1. Preliminaries](https://wesmckinney.com/book/preliminaries.html)
    * [Why Python?](Reviews the core packages)

## Colab intro

* [Colab intro](https://youtu.be/inN8seMm7UI) (video) by Jake VanderPlas
  * Jake VanderPlas introduces colab and mentions seedbank...
  * [aihub (formerly research.google.com/seedbank)](https://aihub.cloud.google.com/s?category=notebook)
* [Data Science Handbook](https://github.com/jakevdp/PythonDataScienceHandbook) by Jake VanderPlas -- github
  * These used to have automatic links to open in Colab
* Colab -- https://colab.research.google.com/
  * Colab is Jupyter as a service (container in the cloud)
  * Colab has some nice GUI improvements & GPU access (and a business model)
  * Authenticate with your "husky.neu.edu" email -- just replace "northeastern.edu" with "husky.neu.edu"
  * Colab and Jupyter are great for prototyping and in-class exercises, but NOT for code submission.
  * You can share Colab notebooks, but editing is not synchronous.  You need to "save" explicitly.
* Accessing the iris dataset from Colab
  * Look here: https://github.com/mwaskom/seaborn-data/blob/master/iris.csv
  * Use the "raw" link
  * `!curl -O "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"`
* EXERCISES
  * [colab.md](colab.md) -- instructor only

## EXERCISES

* [numpy.md](numpy.md)
* [central.md](central.md) -- instructor only
