from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[2008,16],[2009,14],[2010,16],[2011,16],[2012,19],[2013,18],[2014,16],[2015,17],[2016,15]])
y = np.array([421,434,520,438,441,548,523,374,399])

x1 = np.array([[2008,15],[2009,14],[2010,14],[2011,14],[2013,13],[2014,14],[2015,14],[2016,10]])
y1 = np.array([299,340,255,343,238,375,248,236])

model = LinearRegression(fit_intercept=True)

model.fit(X, y)
import warnings
warnings.filterwarnings("ignore")
pred = np.array([2017,12])
y_predict = model.predict(pred)
print("Suresh Raina 2017 Predicted score\n" + str(y_predict))

model.fit(x1,y1)
import warnings
warnings.filterwarnings("ignore")
pred = np.array([2017,10])
y_predict = model.predict(pred)
print("Yuvraj Singh 2017 Predicted score\n" + str(y_predict))

