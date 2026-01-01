import streamlit as st
import requests

API_URL='http://127.0.0.1:8000/predict'
st.title('House Price Prediction Model')

st.markdown('enter the following details')

#input all the details required by the model
area=st.number_input('area',min_value=500,max_value=2000)
bedrooms=st.number_input('no of bedrooms in the house',min_value=1,max_value=5)
available_locations=['cityA','cityB','cityC']
location=st.selectbox('location of the house',available_locations)
age=st.number_input('age of the house',min_value=5,max_value=30)

if st.button('predict the home price'):
    input_data={
        'area':area,
        'bedrooms':bedrooms,
        'location':location,
        'age':age
    }

    try:
        response=requests.post(API_URL,json=input_data)
        if response.status_code == 200 :
            result=response.json()
            st.success(f'the price is predicted successfully and the predicetd price is {result}')
        else:
            st.error(f'API error : {response.status_code} - {response.text}')
    
    except requests.exceptions.ConnectionError:
        st.error("could not connect to the fastAPI server, Make sure its running on the port 8000")
