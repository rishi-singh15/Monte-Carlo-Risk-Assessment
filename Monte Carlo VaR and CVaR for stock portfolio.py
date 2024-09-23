#Monte Carlo Var and CVar
#
#Rishabh Singh
#September 18th, 2024
#Independent, Educational Project. 
#
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import datetime as dt
import yfinance as yf
# 
#Creating and Assessing Porfolio
#
# Import data
def get_data(tickers, start_date, end_date):
    stocks = yf.download(tickers,  start = start_date, end = end_date)
    stocks = stocks['Close'] #Because we are only concerned with closing prices.  
    #
    #Simple Returns 
    simple_returns  = stocks.pct_change().dropna() #Drops first row
    return simple_returns
#
#Defining Arguments
portfolio_stocks = ['AAPL', 'GOOG', 'FDX', 'WM', 'JNJ', 'TMO']
end_date = dt.datetime.now() #Today
start_date = end_date - dt.timedelta(days = 300) 
weights = [0.3, 0.3, 0.2, 0.1, 0.05, 0.05] #Tech-Heavy Portfolio. All weights must add to 1. 
#
#Historical Characteristics
returns = get_data(portfolio_stocks, start_date = start_date, end_date=end_date) 
mean_returns = np.mean(returns.values, axis=0)
sd_returns = np.std(returns.values, axis=0)
covMatrix = returns.cov() #Variance-Covariance Matrix
#
#Are returns normally distributed for our portfolio? Is it okay to make this assumption? 
pd.DataFrame.hist(returns)
plt.suptitle("Distribution of Returns for all assets")
plt.show()
#
#One Simulation: Daily Returns are assumed to be a normal random variable.  
#
#Defining Arguments
period = 100
#
#Random Values and Cholesky Decomposition 
#
random_vals = np.random.normal(loc = 0, scale = 1, size=(len(weights), period)) #Chosen values are elements in the set [0.0, 1.0)
#
simulated_returns = np.matmul(np.linalg.cholesky(covMatrix), mean_returns[:,np.newaxis] + sd_returns[:, np.newaxis] * random_vals) #Further realism: added covariances to
#denormalized variables. 
#
#Simulated Returns: One combination of how daily returns for our portfolio could have 
#played out over the given time period. 
pd.DataFrame(data = simulated_returns, index = portfolio_stocks).T.plot()
plt.ylabel('Simple Returns')
plt.suptitle('Simulated Returns for a ' + str(period) + ' period')
plt.show()
#
#Cash value of our portfolio over this time period 
initial_cash = 10000
simulated_cashVal = np.cumprod(np.inner(simulated_returns.T, weights) + 1) * initial_cash #Compounded Returns on any given day. 
#
plt.plot(simulated_cashVal)
plt.ylabel('Cumulative Returns')
plt.suptitle('Cumulative returns for our portfolio given a $' + str(initial_cash) + ' initial cash value')
plt.show()
#
#
#Multiple simulations
#
n = 1000 #Number of simulations. 
multiple_simulations = [] #For each simulation of cumulative stores. 
#
for i in range(n):
    randomVals = np.random.normal(loc=0, scale=1, size = (len(weights), period)) #Random values 
    denormalized_returns= np.matmul(np.linalg.cholesky(covMatrix), mean_returns[:,np.newaxis] + sd_returns[:, np.newaxis] * randomVals) #With covariances introduced.
    cashVal =  np.cumprod(np.inner(denormalized_returns.T, weights) + 1) * initial_cash
    multiple_simulations.append(cashVal)
multiple_simulations = np.array(multiple_simulations)
#
plt.plot(multiple_simulations.T)
plt.xlabel('Days')
plt.ylabel('Cumulative Returns')
plt.suptitle(str(n) + ' Monte Carlo simulations of Cumulative Returns given $' + str(initial_cash))
plt.show()
#
#VaR and CVaR with alpha = 0.01.
#
lowest_returns = np.percentile(multiple_simulations[:, -1], q= 1) #Lowest possible returns with (1-q)% confidence on the last generated day from "period". 
#
VaR = initial_cash - lowest_returns #Because the initial cash value constitues the mean. 
#All divergence in returns occured from the initial cash value. 
#
CVaR = initial_cash - np.mean(multiple_simulations[:, -1][multiple_simulations[:, -1] <= lowest_returns]) #Average (expected) loss in the q% case. 
#
print("Value at Risk on the " + str(period) + "-th day for our portfolio:", VaR)
print("Conditional Value at Risk on the " + str(period) + "-th day for our portfolio:", CVaR)
