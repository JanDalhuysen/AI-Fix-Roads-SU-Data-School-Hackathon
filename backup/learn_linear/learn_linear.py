import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

import joblib

import matplotlib.pyplot as plt
from micromlgen import port

data = pd.read_csv("learn_linear.csv")

X = data.drop(columns=['output'])
y = data['output']

model = LinearRegression()
model.fit(X, y)

predictions = model.predict([ [1.05] ])
print(predictions)

code = open("learn_linear_to_c_1.h", mode="w+")
code.write(port(model))

joblib.dump(model, 'learn_linear.pkl')
