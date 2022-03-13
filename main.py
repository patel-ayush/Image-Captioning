import cv2
import streamlit as st
from helper import extract_features,generate_desc,word_for_id,predict
from PIL import Image
import numpy as np

st.markdown("<center><b style='text-align: center;font-family:Brush Script MT, cursive;font-size: 40px;'>Lets caption the image</b><br></center>", unsafe_allow_html=True)
st.text("")
st.text("")
uploaded_file = st.file_uploader("Upload an image...", type="jpg")

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    opencv_image = cv2.imdecode(file_bytes, 1)
    opencv_image=cv2.cvtColor(opencv_image,cv2.COLOR_BGR2RGB)
    col1, col2 = st.columns(2)
    with col1:
        st.image(opencv_image, caption='Uploaded Image.', use_column_width=True,clamp=True,)
    with col2:
        st.markdown(f"<center><b style='text-align: center;font-family:Brush Script MT, cursive;font-size: 25px;'>Here in your caption :</b></center>", unsafe_allow_html=True)
        gif_runner = st.image("ic_load_1.gif")
        st.markdown(f"<center><b style='text-align: center;font-family:Brush Script MT, cursive;font-size: 25px;color:MediumSeaGreen'>\"{predict(opencv_image)}\" </b><br></center>", unsafe_allow_html=True)
        gif_runner.empty()

#66ff66
