import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# import the excel file.
df=pd.read_excel(r'E:\task5.xlsx')
df.head() # print the top 5 row

#initializing variables
x=df.iloc[:,0:-1].values
y=df.iloc[:,1].values
#create single dimendion
x=x[:,np.newaxis]
y=y[:,np.newaxis]
#sort x values and get index
inds=x.ravel().argsort()
x=x.ravel()[inds].reshape(-1,1)
#sort y according to x sorted index
y= y[inds]
print(x.shape)
print(y.shape)

#plotting the Polynomial function
fig, ax = plt.subplots(figsize=(15, 8))
plt.scatter(x,y, color='red')
plt.xlabel('y-value', fontsize='12')
plt.ylabel('x-value', fontsize='12')
plt.title("PDF",fontsize=12)
plt.show()

#OLS Regression Model
import statsmodels.api as sm
model =sm.OLS(y,x).fit()
#predected variable
ypred=model.predict(x)
fig, ax = plt.subplots(figsize=(15, 8))
plt.scatter(x,y,color='red')
plt.plot(x,ypred,color='green')
plt.xlabel('y-value', fontsize='12')
plt.ylabel('x-value', fontsize='12')
plt.title("Linear Model",fontsize=12)
plt.show()

#genrate polynomial
from sklearn.preprocessing import PolynomialFeatures
polynomial_features= PolynomialFeatures (degree=10)
xp=polynomial_features.fit_transform(x)
xp.shape

#running regression on polynomials using statsmodels ols
model= sm.OLS(y,xp).fit()
ypred=model.predict(xp)

#plot the predection model
fig, ax = plt.subplots(figsize=(15, 8))
plt.scatter(x,y,color='red')
plt.plot(x,ypred,color='green')
plt.xlabel('y-value', fontsize='12')
plt.ylabel('x-value', fontsize='12')
plt.title("Prediction model",fontsize=12)
plt.show()


#Plotting lower and upper confidance intervals
from statsmodels.sandbox.regression.predstd import wls_prediction_std
_, upper,lower = wls_prediction_std(model)
fig, ax = plt.subplots(figsize=(15, 8))
plt.scatter(x,y,label='data',color='red')
plt.plot(x,ypred,label='Predicted Plot',color='green')
plt.plot(x,upper,'--',label="Upper",color='black') # confid. intrvl
plt.plot(x,lower,':',label="lower",color='orange')
plt.legend(loc='upper left')
plt.xlabel('y-value', fontsize='12')
plt.ylabel('x-value', fontsize='12')
plt.title("Plotting lower and upper confidence intervals",fontsize=12)
plt.show()

model.summary()
# Apply ridge regularization with alpha = 0.1
from sklearn.linear_model import Ridge
reg = Ridge(alpha=0.1)
reg.fit(x, y)
# Print the coefficients of the model
print(reg.coef_)

