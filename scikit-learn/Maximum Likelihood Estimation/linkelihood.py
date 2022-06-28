#%%
# import libraries
import numpy as np, pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from scipy.optimize import minimize
import scipy.stats as stats
import pymc3 as pm3
import numdifftools as ndt
import statsmodels.api as sm
from statsmodels.base.model import GenericLikelihoodModel

# generate data
N = 100
x = np.linspace(0,20,N)
ϵ = np.random.normal(loc = 0.0, scale = 5.0, size = N)
y = 3*x + ϵ
df = pd.DataFrame({'y':y, 'x':x})
df['constant'] = 1
# plot
sns.regplot(df.x, df.y);

# define likelihood function
def MLERegression(params):
    intercept, beta, sd = params[0], params[1], params[2] # inputs are guesses at our parameters
    yhat = intercept + beta*x # predictions
# next, we flip the Bayesian question
# compute PDF of observed values normally distributed around mean (yhat)
# with a standard deviation of sd
    negLL = -np.sum( stats.norm.logpdf(y, loc=yhat, scale=sd) )
# return negative LL
    return(negLL)
 

# let’s start with some random coefficient guesses and optimize
guess = np.array([5,5,2])
results = minimize(MLERegression, guess, method = 'Nelder-Mead', 
options={'disp': True})
# --------------------------------------------------------------------
# Optimization terminated successfully.
#          Current function value: 311.060386
#          Iterations: 111
#          Function evaluations: 195

results # this gives us verbosity around our minimization
# notice our final key and associated values…
#--------------------------------------------------------------------
# final_simplex: (array([[0.45115297, 3.03667376, 4.86925122],
#        [0.45123459, 3.03666955, 4.86924261],
#        [0.45116379, 3.03667852, 4.86921688],
#        [0.45119056, 3.03666796, 4.8692127 ]]), array([300.18758478, 300.18758478, 300.18758478, 300.18758479]))
#            fun: 300.18758477994425
#        message: 'Optimization terminated successfully.'
#           nfev: 148
#            nit: 80
#         status: 0
#        success: True
#              x: array([0.45115297, 3.03667376, 4.86925122])

# drop results into df and round to match statsmodels
resultsdf = pd.DataFrame({'coef':results['x']})
resultsdf.index=['constant','x','sigma']   
np.round(resultsdf.head(2), 4)
# do our numbers match the OLS model?

# %%
