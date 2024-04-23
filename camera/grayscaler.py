import streamlit as st
from PIL import Image 

with st.expander("Start camera"):
    # Start the camera
    camera_image = st.camera_input("Camera")

if camera_image:
    # Create a Pillow image instance
    img = Image.open(camera_image)

    # Convert the Pillow instance to grayscale
    gray_img = img.convert("L")

    # Render the grayscale image on the web page
    st.image(gray_img)
else:
    st.write("Capture the Image to generate grayscale picture")