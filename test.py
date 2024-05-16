import importlib
import datasets
import regression

X,Y = datasets.load_linear_example1()
model = regression.LinearRegression()
importlib.reload(regression)
model = regression.LinearRegression()
model.fit(X,Y)
print(model.theta)
