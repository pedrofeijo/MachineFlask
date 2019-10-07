import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, confusion_matrix
import joblib

data = pd.read_csv('/home/feijo/Documents/MachineFlask/Treinamento/iris.csv', names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])
data.head()

# class 1 = setosa
# print(data)

le = LabelEncoder()
data['class'] = le.fit_transform(data['class'])
data.head()

X = np.array(data.drop(['class'], axis=1))
y = np.array(data['class'])

clf = LogisticRegression()
clf.fit(X, y)

y_test = clf.predict(X)
print(accuracy_score(y, y_test))
print(confusion_matrix(y, y_test))

# save classifier

joblib.dump(clf, 'classifier.pkl')

# load classifier

loaded_model= joblib.load("classifier.pkl")
a1 = float(input('Digite sepal_length = '))
a2 = float(input('Digite sepal_width =  '))
a3 = float(input('Digite pental_length = '))
a4 = float(input('Digite petal_width = '))
result= loaded_model.predict([[a1,a2, a3, a4]])
# result= loaded_model.predict([[6.3,2.7,4.9,1.8]])
print(result)


