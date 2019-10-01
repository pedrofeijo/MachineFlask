import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv('/home/feijo/Documents/MachineFlask/Treinamento/iris.csv', names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])
data.head()

# class 1 = setosa

le = LabelEncoder()
data['class'] = le.fit_transform(data['class'])
data.head()

X = np.array(data.drop(['class'], axis=1))
y = np.array(data['class'])

clf = LogisticRegression()
clf.fit(X, y)

clf = LogisticRegression()
clf.fit(X, y)
accuracy = clf.score(X, y)

print(accuracy)
