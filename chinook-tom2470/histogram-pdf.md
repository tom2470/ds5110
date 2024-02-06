
# Histogram vs PDF

There are four related concepts: 

1. histogram, 
2. probability **distribution** function,
3. probability **density** function (PDF) and
4. probability **mass** function

### histogram & probability

To relate a histogram to a probability, divide bin count (# of samples in a bin) by the total number of samples, $N$.

$$
P_{\mathrm{bin}} \approx \frac{\mathrm{bin\ count}}{N}
$$

$P_{\mathrm{bin}}$ is the probability that a sample at $x$ lies within the bin defined by 
$\mathrm{bin\ start} < x < \mathrm{bin\ end}$

### distribution vs density

* $P_{\mathrm{bin}}$ is the probability **distribution** function;
  it is a function of the range of values of $x$ that define the bin.
* The probability **density** function $\mathrm{PDF}(x)$ is related to probability distribution function.
  * The probability distribution is the integral of the probability density function $PDF(x)$ over the bin.

$$
\int_{\mathrm{bin\ start}}^{\mathrm{bin\ end}} \mathrm{PDF}(x) dx = P_{\mathrm{bin}}
\approx \mathrm{pdf}(x_{ \mathrm{bin} }) d_{\mathrm{bin}}
= \frac{\mathrm{bin\ count}}{N}
$$

* A probability density doesn't tell you about the probability of occurrence until you perform the integral.
* Likewise, the density of water (1 kg per cubic meter) doesn't tell you how much water you have until you
  define a volume of water.
  You multiply the density of water by its volume to get the total mass.
* Since the probability of getting any value is 1 whenever you take a measurement, 
  then a continuous probability density function integrates to 1 for the entire range of possible measurements:

$$
\int_{- \infty}^{\infty} \mathrm{PDF}(x) dx = 1
$$

### histogram vs density

If the range of $x$ in in bin is small, then

$$
P_{\mathrm{bin}}
\approx \mathrm{PDF}(x_{ \mathrm{bin} }) d_{\mathrm{bin}}
\approx \frac{\mathrm{bin\ count}}{N}
$$

where $d_{\mathrm{bin}}$ is the bin size. So...

$$
\mathrm{PDF}(x_{ \mathrm{bin} }) \approx \frac{\mathrm{bin\ count}}{N\ \mathrm{bin\ size}}
$$

### distribution vs mass

The probability **mass** function gives the probability that a discrete random variable is exactly equal to some value.
In the sense that it determines a probability, it's like a probability distribution function.
However, the [probability **mass** function](https://en.wikipedia.org/wiki/Probability_mass_function) applies to 
discrete processes, whereas distribution and density functions apply to continuous processes.
