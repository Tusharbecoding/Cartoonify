#By - Tushar Chopra
#Branch - COBS
#Roll No. - 102118056


import cv2
import streamlit as st
import numpy as np 
from PIL import Image


def cartoonization (img, cartoon):

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

    if cartoon == "Pencil Sketch":
        
        value = st.sidebar.slider('Tune the brightness of your sketch (the higher the value, the brighter your sketch)', 0.0, 300.0, 250.0)
        kernel = st.sidebar.slider('Tune the boldness of the edges of your sketch (the higher the value, the bolder the edges)', 1, 99, 25, step=2)


        gray_blur = cv2.GaussianBlur(gray, (kernel, kernel), 0)

        cartoon = cv2.divide(gray, gray_blur, scale=value)

    if cartoon == "Detail Enhancement":
        
       
        smooth = st.sidebar.slider('Tune the smoothness level of the image (the higher the value, the smoother the image)', 3, 99, 5, step=2)
        kernel = st.sidebar.slider('Tune the sharpness of the image (the lower the value, the sharper it is)', 1, 21, 3, step =2)
        edge_preserve = st.sidebar.slider('Tune the color averaging effects (low: only similar colors will be smoothed, high: dissimilar color will be smoothed)', 0.0, 1.0, 0.5)
        
        gray = cv2.medianBlur(gray, kernel) 
        edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
 										cv2.THRESH_BINARY, 9, 9) 
    
        color = cv2.detailEnhance(img, sigma_s=smooth, sigma_r=edge_preserve)
        cartoon = cv2.bitwise_and(color, color, mask=edges) 

        

    if cartoon == "Bilateral Filter":
        
        
       
        smooth = st.sidebar.slider('Tune the smoothness level of the image (the higher the value, the smoother the image)', 3, 99, 5, step=2)
        kernel = st.sidebar.slider('Tune the sharpness of the image (the lower the value, the sharper it is)', 1, 21, 3, step =2)
        edge_preserve = st.sidebar.slider('Tune the color averaging effects (low: only similar colors will be smoothed, high: dissimilar color will be smoothed)', 1, 100, 50)
       
        gray = cv2.medianBlur(gray, kernel) 
        edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
 										cv2.THRESH_BINARY, 9, 9)
    
        color = cv2.bilateralFilter(img, smooth, edge_preserve, smooth) 
        cartoon = cv2.bitwise_and(color, color, mask=edges) 

    return cartoon

###############################################################################
    
st.write("""
          # Cartoonize Your Image!
          """
          )

st.write("This is an app to turn your photos into cartoon")
file = st.sidebar.file_uploader("Please upload an image file", type=["jpg", "png"])

if file is None:
    st.text("You haven't uploaded an image file")
    st.text("JPG, JPEG and PNG formats accepted.")
    st.text("")
    st.text("")
    st.text("")
    st.text("By - Tushar Chopra")
    st.text("Branch - COBS")
    st.text("Roll No. - 102118056")
    st.text("Year - 2nd")
else:
    image = Image.open(file)
    img = np.array(image)
    
    option = st.sidebar.selectbox(
    'Which cartoon filters would you like to apply?',
    ('Pencil Sketch', 'Detail Enhancement', 'Bilateral Filter'))
    
    st.text("Your original image")
    st.image(image, use_column_width=True)
    
    st.text("Your cartoonized image")
    cartoon = cartoonization(img, option)
    
    st.image(cartoon, use_column_width=True)
