# Data Scientist Marathon

## First part: Excel ✅
### Completed in 22-26 September.
Here the key aspect I learnt

* Cleaning Data
* Making Chart
* Making pivot table
* Handling Special cases of if-else
* scrap out information using left,right,middle
* Concatenating data
* VLookup table: to smartly describe the abbreviation or something like that
* Cell referencing:
    * Relative referencing 
        * C12
    * Absolute referencing
        * $C12 - Column C is absolute
        * C$12 - Row 12 is absolute

## Second part: Statistics 🚧
### Standard Deviation

**For a Population:**
Standard deviation, denoted as sigma (σ), is calculated using the formula:

    σ = sqrt( Σ (xi - μ)² / N )

Where:
- σ (sigma): Population standard deviation
- N: Size of the population
- xi: Each value from the population
- μ (mu): The population mean

**For a Sample:**
Sample standard deviation, denoted as s, is calculated as:

    s = sqrt( Σ (xi - x̄)² / (n - 1) )

Where:
- s: Sample standard deviation
- n: Size of the sample
- xi: Each value from the sample
- x̄ (x-bar): The sample mean


### Covariance

Covariance between two variables X and Y is calculated using the formula:

    cov(X, Y) = Σ ((xi - x̄) * (yi - ȳ)) / (n - 1)

Where:
- cov(X, Y): Represents the covariance between X and Y
- xi, yi: Are the individual data points
- x̄, ȳ: Are the means of X and Y respectively
- n: Is the number of data points.


### Correlation

The Pearson correlation coefficient, denoted as r, between two variables X and Y is calculated using the formula:

    r = (n * Σ(xy) - Σx * Σy) / sqrt( [n * Σx² - (Σx)²] * [n * Σy² - (Σy)²] )
    r = cov(X, Y) / (σx * σy)

Where:
- r: Is the correlation coefficient, representing the strength and direction of the linear relationship between X and Y.
- n: Is the number of paired data points.
- Σxy: Is the sum of the product of each pair of values.
- Σx and Σy: Are the sums of the X and Y values, respectively.
- Σx² and Σy²: Are the sums of the squared X and Y values, respectively.

This coefficient r ranges from -1 to 1, inclusive:
- r = 1 implies a perfect positive linear relationship.
- r = -1 implies a perfect negative linear relationship.
- r = 0 implies no linear relationship.

### Bayes' Theorem

Bayes' Theorem is used to find the probability of a hypothesis given the prior knowledge. It is articulated as:

    P(A|B) = (P(B|A) * P(A)) / P(B)

Where:
- \( P(A|B) \): is the probability of hypothesis \( A \) given the data \( B \).
- \( P(B|A) \): is the probability of the data \( B \) given that the hypothesis \( A \) was true.
- \( P(A) \) and \( P(B) \): are the probabilities of hypothesis \( A \) and data \( B \) respectively.

