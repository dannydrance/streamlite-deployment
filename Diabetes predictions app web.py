# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 07:29:27 2024

@author: cococe ltd
"""

import numpy as np
import pickle
import streamlit as st

#loading the saved model
loaded_model=pickle.load(open('C:/Users/user/Desktop/Anaconda Courses/ML deployment/ML deployment/ML deployment/trained_model.sav','rb'))

# Creating a function for prediction
def diabetes_prediction(input_data):
    
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    
    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    
    if (prediction[0] == 0):
      return 'The person is not diabetic'
    else:
      return 'The person is diabetic'  
      
  # create a main function
def main():
    # A title of a user interface
    st.title('Diabetes predictions Web Apllication')
    # Getting the input from the user
        
    Pregnancies=st.text_input('Number of pregnancies')
    Glucose=st.text_input('Glucose level')
    BloodPressure=st.text_input('BloodPressure value')
    SkinThickness=st.text_input('SkinThickness value')
    Insulin=st.text_input('Insulin level')
    BMI=st.text_input('BMI value')
    DiabetesPedigreeFunction=st.text_input('DiabetesPedigreeFunction value')
    Age=st.text_input('number of age')
    
    # Codes for prediction
    diagnosis = ''
    # Creating a button for prediction  
    if st.button('Diabetes Test Result'):
        diagnosis= diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
    
    st.success(diagnosis)
    
if __name__ == '__main__':
    main()
    
    