import joblib
# load classifier

loaded_model= joblib.load("classifier.pkl")
a1 = float(input('Digite sepal_length = '))
a2 = float(input('Digite sepal_width =  '))
a3 = float(input('Digite pental_length = '))
a4 = float(input('Digite petal_width = '))
result= loaded_model.predict([[a1,a2, a3, a4]])
# result= loaded_model.predict([[6.3,2.7,4.9,1.8]])
print(result)