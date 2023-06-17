import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pickle

from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn import metrics
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV

data = pd.read_csv('m31.csv')

X = data[['ra','dec','u', 'b', 'v', 'r', 'i', 'j', 'h', 'k', 'Vr']]
y = data[['classification']]

ohenc1 = OneHotEncoder(sparse=False)
m1=ohenc1.fit_transform(data[['classification']])

X_train, X_test , y_train, y_test = train_test_split(X,y,
                                                     test_size=0.2,
                                                     random_state=8)

model = GradientBoostingClassifier(n_estimators=100,max_features= None)
model.fit(X_train, y_train)


with open('old.pkl','wb') as file :
    pickle.dump(model, file)
