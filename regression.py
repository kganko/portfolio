
#linear regression

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

df = pd.read_csv('ds_salaries.csv')
df.dropna(inplace = True)
# df['remote_ratio'] = pd.to_numeric(df['remote_ratio'])
# df.plot("salary_in_usd")
plt.plot(df, linestyle = 'dashed',color = 'r')
plt.title("Salary in USD")
plt.show()

# Features
X = df.drop(['remote_ratio'], axis = 1)
y = df['remote_ratio']

# Create a model
lr = LinearRegression()
# Fit the model
lr.fit(X, y)
# make predictions
pred = lr.predict(X)

coeff_df = pd.DataFrame(lr.coef_, X.columns, columns=['Coefficient'])
coeff_df

print('Intercept:', lr.intercept_)
print('Mean Absolute Error:', metrics.mean_absolute_error(y, pred))
print('Mean Squared Error:', metrics.mean_squared_error(y, pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y, pred)))
print('R2:', np.sqrt(metrics.r2_score(y, pred)))

#model evaluation


model = LogisticRegression(solver='liblinear', C=0.5, random_state=0)
model.fit(X, y)

p_pred = model.predict_proba(X)
y_pred = model.predict(X)
score_ = model.score(X, y)
conf_m = confusion_matrix(y, y_pred)
report = classification_report(y, y_pred)