import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

input_data=pd.read_csv("C:/Users/nithi/Documents/Iris_new.csv")
print(input_data.isna().sum())
input_data=input_data.fillna('')
print(input_data.shape)

x=input_data[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']]
y=input_data['Species']
print(x,y)

xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2,random_state=3)

print(xtrain.shape,ytrain.shape,xtest.shape,ytest.shape)

model=svm.SVC()
model.fit(xtrain,ytrain)

prediction=model.predict(xtrain)
accuracyofmodel=accuracy_score(ytrain,prediction)

print(accuracyofmodel)

import pickle


with open('model_nithin.pkl', 'wb') as m:
    pickle.dump(model, m)

import joblib
# Load your trained model
with open('model_nithin.pkl', 'rb') as m:
    model = pickle.load(m)

st.title("Species identification")

import numpy as np
prediction=np.array([0,1,2])

def predict():
   pass

def main():
   input_feature=st.text_input("Enter your data : ")
   if st.button("check",on_click=predict):
      predict()
if np.any(prediction == 0):
   st.write('The Species is Iris-Setosa')
elif np.any(prediction == 1):
   st.write('The Species is Iris-Versicolor')
else:
   st.write('The Species is Iris-Virginica')






