from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[2008,3],[2009,13],[2010,15],[2011,15],[2012,17],[2013,19],[2014,14],[2015,15],[2016,14]])
y = np.array([5,12,17,14,6,24,14,18,9])

x1 = np.array([[2008,11],[2009,6],[2010,14],[2011,15],[2012,16], [2013,2],[2014,6],[2015,7],[2016,12]])
y1 = np.array([13,6,15,14,17,5,5,7,10])

model = LinearRegression(fit_intercept=True)

model.fit(X, y)
import warnings
warnings.filterwarnings("ignore")
pred = np.array([2017,9])
y_predict = model.predict(pred)
print("Harbajan Singh 2017 Predicted wickets\n" + str(round(float(y_predict))))


model.fit(x1,y1)
import warnings
warnings.filterwarnings("ignore")
pred = np.array([2017,10])
y_predict = model.predict(pred)
print("Zaheer Khan 2017 Predicted Wickets\n" + str(round(float(y_predict))))

