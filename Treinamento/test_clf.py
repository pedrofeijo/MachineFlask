import joblib

loaded_model= joblib.load("classifier.pkl")
result= loaded_model(y_test)
print(result)