import streamlit as st
import pandas as pd
import numpy as np
import requests


API_KEY = '052c760f40df01f6dd06f47aa9236660' 


# with open('C:/Users/nisha/OneDrive/Desktop/c_st/learn_streamlit/style.css') as f:
#     st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)





def convert_to_celcius(temp_in_kelvin):
    return temp_in_kelvin -273.15

def find_current_weather_city(city):
    base_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    weather_data=requests.get(base_url).json()
   
    try:
         general = weather_data['weather'][0]['main']
         icon_id = weather_data['weather'][0]['icon']
         temperature = round(convert_to_celcius(weather_data['main']['temp']))
         temp_min = round(convert_to_celcius(weather_data['main']['temp_min']))
         icon = f"http://openweathermap.org/img/wn/{icon_id}@2x.png"
    except KeyError:
        st.error("City Not Find")
        st.stop()
    return general,temperature,temp_min,icon


def find_current_weather_city_id(city_id):
    base_url = f"https://api.openweathermap.org/data/2.5/weather?id={city_id}&appid={API_KEY}"
    weather_data=requests.get(base_url).json()

    try:
         general = weather_data['weather'][0]['main']
         icon_id = weather_data['weather'][0]['icon']
         temperature = round(convert_to_celcius(weather_data['main']['temp']))
         temp_min = round(convert_to_celcius(weather_data['main']['temp_min']))
         icon = f"http://openweathermap.org/img/wn/{icon_id}@2x.png"
    except KeyError:
        st.error("City ID Find")
        st.stop()
    return general,temperature,temp_min,icon


def find_current_weather_geo(lat,lon):
    base_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"
    weather_data=requests.get(base_url).json()

    try:
         general = weather_data['weather'][0]['main']
         icon_id = weather_data['weather'][0]['icon']
         temperature = round(convert_to_celcius(weather_data['main']['temp']))
         temp_min = round(convert_to_celcius(weather_data['main']['temp_min']))
         icon = f"http://openweathermap.org/img/wn/{icon_id}@2x.png"
    except KeyError:
        st.error("City ID Find")
        st.stop()
    return general,temperature,temp_min,icon


def find_current_weather_zip(zip_code,country):
    base_url = f"https://api.openweathermap.org/data/2.5/weather?zip={zip_code},{country}&appid={API_KEY}"
    weather_data=requests.get(base_url).json()

    try:
         general = weather_data['weather'][0]['main']
         icon_id = weather_data['weather'][0]['icon']
         temperature = round(convert_to_celcius(weather_data['main']['temp']))
         temp_min = round(convert_to_celcius(weather_data['main']['temp_min']))
         icon = f"http://openweathermap.org/img/wn/{icon_id}@2x.png"
    except KeyError:
        st.error("City ID Find")
        st.stop()
    return general,temperature,temp_min,icon


def find_current_weather_histo(lat,lon):
    base_url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}"
    weather_data=requests.get(base_url).json()

    try:
         general = weather_data['weather'][0]['main']
         icon_id = weather_data['weather'][0]['icon']
         temperature = round(convert_to_celcius(weather_data['main']['temp']))
         temp_min = round(convert_to_celcius(weather_data['main']['temp_min']))
         icon = f"http://openweathermap.org/img/wn/{icon_id}@2x.png"
    except KeyError:
        st.error("City ID Find")
        st.stop()
    return general,temperature,temp_min,icon





def find_current_weather_hour(lat,lon,start,cnt):
    base_url = f"https://history.openweathermap.org/data/2.5/history/city?lat={lat}&lon={lon}&type=hour&start={start}&cnt={cnt}&appid={API_KEY}"
    weather_data=requests.get(base_url).json()

    try:
         general = weather_data['weather'][0]['main']
         icon_id = weather_data['weather'][0]['icon']
         temperature = round(convert_to_celcius(weather_data['main']['temp']))
         temp_min = round(convert_to_celcius(weather_data['main']['temp_min']))
         icon = f"http://openweathermap.org/img/wn/{icon_id}@2x.png"
    except KeyError:
        st.error("City ID Find")
        st.stop()
    return general,temperature,temp_min,icon




    
def main():
    #with open("style.css") as source_design:
    st.header('Check Weather')
    option = st.selectbox(
    'Select Method',options = 
    ['City Name', 'City ID', 'ZIP Code','Geographical Coordinates','Historical Data','Previous Data'])
    if option=='City Name':
        city = st.text_input("Enter City Name").lower()
        if st.button('Find'):
            general,temperature,temp_min,icon = find_current_weather_city(city)
            col_1,col_2 = st.columns(2)
            with col_1:
                st.metric(label ="Temperature",value = f"{temperature}°C",delta=f"{temperature - temp_min}°C")
                with col_2:
                    st.write(general)
                    st.image(icon)

    elif option == "City ID":
        city_id = st.text_input("Enter City ID").lower()
        if st.button('Find'):
            general,temperature,temp_min,icon = find_current_weather_city_id(city_id)
            col_1,col_2 = st.columns(2)
            with col_1:
                st.metric(label ="Temperature",value = f"{temperature}°C",delta=f"{temperature - temp_min}°C")
                with col_2:
                    st.write(general)
                    st.image(icon)

    elif option == "Historical Data":
        lat = st.number_input("Enter Latitude")
        lon = st.number_input("Enter Longitude")
        if st.button('Find'):
            general,temperature,temp_min,icon = find_current_weather_histo(lat,lon)
            col_1,col_2 = st.columns(2)
            with col_1:
                st.metric(label ="Temperature",value = f"{temperature}°C",delta=f"{temperature - temp_min}°C")
                with col_2:
                    st.write(general)
                    st.image(icon)
            st.map(pd.DataFrame(np.array([[lat,lon]]),columns=['lat','lon']),zoom=3)


    elif option == "Geographical Coordinates":
        lat = st.number_input("Enter Latitude")
        lon = st.number_input("Enter Longitude")
        if st.button('Find'):
            general,temperature,temp_min,icon = find_current_weather_geo(lat,lon)
            col_1,col_2 = st.columns(2)
            with col_1:
                st.metric(label ="Temperature",value = f"{temperature}°C",delta=f"{temperature - temp_min}°C")
                with col_2:
                    st.write(general)
                    st.image(icon)
            st.map(pd.DataFrame(np.array([[lat,lon]]),columns=['lat','lon']),zoom=3)




    elif option == "ZIP Code":
        zip_code = st.text_input("Enter Zip code")
        country = st.text_input("Enter Country").lower()
        if st.button('Find'):
            general,temperature,temp_min,icon = find_current_weather_zip(zip_code,country)
            col_1,col_2 = st.columns(2)
            with col_1:
                st.metric(label ="Temperature",value = f"{temperature}°C",delta=f"{temperature - temp_min}°C")
                with col_2:
                    st.write(general)
                    st.image(icon)



    elif option == "Previous Data":
        lat = st.number_input("Enter Latitude")
        lon = st.number_input("Enter Longitude")
        start = st.text_input("Enter Start time ")
        cnt = st.text_input("Enter Count")
        if st.button('Find'):
            general,temperature,temp_min,icon = find_current_weather_hour(lat,lon,start,cnt)
            col_1,col_2 = st.columns(2)
            with col_1:
                st.metric(label ="Temperature",value = f"{temperature}°C",delta=f"{temperature - temp_min}°C")
                with col_2:
                    st.write(general)
                    st.image(icon)



        
    
    
    



if __name__ == "__main__":
    main()

