import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
st.set_page_config(page_title='Prediction of Disease Outbreaks',
                   layout='wide',
                   page_icon=":male-doctor:")
heart_model=pickle.load(open(r"D:\SAP disease\training files\heart_model.sav",'rb'))
diabetes_model=pickle.load(open(r"D:\SAP disease\training files\diabetes_model.sav",'rb'))
parkinsons_model=pickle.load(open(r"D:\SAP disease\training files\parkinsons_model.sav",'rb'))
with st.sidebar:
    selected = option_menu('Prediction of Diseases Outbreak Systems', ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Disease Prediction']
                           ,menu_icon='hospital-fill', icons=['activity','heart','person'],default_index=0)

if selected == 'Diabetes Prediction':
    st.title("Diabetes Prediction using Machine Learning")
    col1,col2,col3=st.columns(3)
    with col1:
        Pregnancies=st.text_input("No. of Pregnancies")
        SkinThickness=st.text_input("Skin-Thickness Value")
        DiabetesPedigreeFunction=st.text_input("Diabetes Pedigree Function Value")
    with col2:
        Glucose=st.text_input("Glucose Level")
        Insulin=st.text_input("Insulin Level")
        Age=st.text_input("Age")
    with col3:
        BloodPressure=st.text_input("Blood Pressure")
        BMI=st.text_input('BMI Value')
    
    x=''
    if st.button("Diabetes Test"):
     user_input=[Pregnancies,BloodPressure,BMI,Glucose,Insulin,Age,DiabetesPedigreeFunction,SkinThickness]
     user_input=[float(x) for x in user_input]
     diab_prediction=diabetes_model.predict([user_input])
     if diab_prediction==1:
        x="You are likely to have Diabetes"
     else:
        x="You are not likely to have Diabetes"
    st.success(x)
 



if selected == 'Heart Disease Prediction':
    st.title("Heart Disease Prediction using Machine Learning")
    col1,col2,col3=st.columns(3)
    with col1:
        cp=st.text_input("Chest Pain Type")
        trestbps=st.text_input("Resting Blood Pressure")
        fbs=st.text_input("Fasting Blood Sugar Value")
        restecg=st.text_input("Resting Electrocardiogram Results")
        ca=st.text_input("No. of Major Vessels")
    with col2:
        chol=st.text_input("Cholestrol Value")
        sex=st.text_input("Sex")
        age=st.text_input("Age")
        thalach=st.text_input("Maximum Heart Rate Achieved")
    with col3:
        exang=st.text_input("Exercise Induced Angina")
        oldpeak=st.text_input("ST Depression Value")
        slope=st.text_input("Slope of ST Segment")
        thal=st.text_input("Thalassemia")

    heart_diagnosis=''
    if st.button("Heart Disease Test"):
     user_input1=[cp,trestbps,fbs,restecg,chol,sex,age,thalach,exang,oldpeak,slope,thal,ca]
     user_input1=[float(x) for x in user_input1]
     heart_prediction=heart_model.predict([user_input1])
     if heart_prediction==1:
        heart_diagnosis="You are likely to have any Heart Diseases"
     else:
        heart_diagnosis="You are not likely to have any Heart Diseases"
    st.success(heart_diagnosis)


if selected == 'Parkinsons Disease Prediction':
    st.title("Parkinsons Disease Prediction using Machine Learning")
    col1,col2,col3=st.columns(3)
    with col1:
        MDVPFo=st.text_input("Average vocal fundamental frequency")
        MDVPFhi=st.text_input("Maximum vocal fundamental frequency")
        MDVPFlo=st.text_input("Minimum vocal fundamental frequency")
        MDVPJi=st.text_input("Variation in fundamental frequency1")
        MDVPJa=st.text_input("Variation in fundamental frequency2")
        MDVPRAP=st.text_input("Variation in fundamental frequency3")
        MDVPPPQ=st.text_input("Variation in fundamental frequency4")
        Jitter=st.text_input("Variation in fundamental frequency5")
    with col2:
        MDVPShi=st.text_input("Variation in amplitude1")
        MDVPShiD=st.text_input("Variation in amplitude2")
        ShimAP=st.text_input("Variation in amplitude3")
        ShimAP5=st.text_input("Variation in amplitude4")
        MDVPAP=st.text_input("Variation in amplitude5")
        ShimDD=st.text_input("Variation in amplitude6")
        NHR=st.text_input("Ratio  of  noise  to  tonal components in the voice1")
    with col3:
        HNR=st.text_input("Ratio  of  noise  to  tonal components in the voice2")
        RPDE=st.text_input("Nonl-inear dynamical complexity measures1")
        DFA=st.text_input("Signal fractal scaling exponent")
        spread1=st.text_input("Non-linear  measures  of fundamental frequency variation1")
        spread2=st.text_input("Non-linear  measures  of fundamental frequency variation2")
        D2=st.text_input("Non-linear dynamical complexity measures2")
        PPE=st.text_input("Non-linear  measures  of fundamental frequency variation3")

    park_diagnosis=''
    if st.button("Parkinsons Disease Test"):
     user_input2=[MDVPFo,MDVPFhi,MDVPFlo,MDVPJi,MDVPJa,MDVPRAP,MDVPPPQ,Jitter,MDVPShi,MDVPShiD,ShimAP,ShimAP5,MDVPAP,ShimDD,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]
     user_input2=[float(x) for x in user_input2]
     park_prediction=parkinsons_model.predict([user_input2])
     if park_prediction==1:
      park_diagnosis="You are likely to have Parkinsons Diseases"
     else:
      park_diagnosis_diagnosis="You are not likely to have Parkinsons Diseases"
    st.success(park_diagnosis)

