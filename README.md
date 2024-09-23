# Monte-Carlo-Risk-Assessment


Value at Risk (VaR) and Conditional Value at Risk (CVaR) are two metrics used in quantative finance to assess the risk of a portfolio. VaR determines, to a given degree of certainity, what the maximum loss of a portfolio would be over a given time period. Similarly, CVaR forecasts what the average loss would be for a portfolio in the case where the true loss of that portfolio exceeded the maximum loss that VaR estimated. Both VaR and CVaR are equally informative and are often used in conjunction. 

With the rise of data science, researchers in finance have begun to use Monte Carlo simulations as a tool to simulate a fraction of the many different combinations of how the compounded returns of a portfolio could unfold over a given period of time. Oftentimes, in these simulations, researchers assume that the assets within these portfolios are normally distributed. Sometimes this assumption is true, but in equally as many cases, this assumption is false. In this study, I assumed that all assets *were* normally distributed. If one wanted to assume a different distribution, they would need to change the following line: 

`random_vals = np.random.normal(loc = 0, scale = 1, size=(len(weights), period))`

to sample values from the distribution of their choice. 

This work was part of an independent project to learn. As part of this project, I used the following links: 

[1] "Monte Carlo Simulation of a Stock Portfolio with Python" : https://www.youtube.com/watch?v=6-dhdMDiYWQ&t=0s 

[2] "Measuring Portfolio risk using Monte Carlo simulation in python — Part 1" : https://medium.com/codex/measuring-portfolio-risk-using-monte-carlo-simulation-in-python-part-1-ac69ea9802f 

[3] "Monte Carlo Simulation with value at risk (VaR) and conditional value at risk (CVaR) in Python" : https://www.youtube.com/watch?v=f9MAFvP5-pA 

[4] "Magic of Log Returns: Concept – Part 1" : https://www.allquant.co/post/magic-of-log-returns-concept-part-1#:~:text=When%20you%20add%20log%20returns%2C%20you%20compound.%20Across,the%20same%20time%20period%2C%20use%20simple%20returns%20instead.

[5] "Cholesky Decomposition: Take your Backtesting to the Next Level" : https://www.youtube.com/watch?v=4OunaCjm2YM

[6] "The Multivariate Normal Distribution" : https://stats.libretexts.org/Bookshelves/Probability_Theory/Probability_Mathematical_Statistics_and_Stochastic_Processes_(Siegrist)/05%3A_Special_Distributions/5.07%3A_The_Multivariate_Normal_Distribution

[7] "Bivariate Normal Distribution" : https://online.stat.psu.edu/stat505/lesson/4/4.2 




