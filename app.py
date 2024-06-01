import streamlit as st
import os
import pickle
import numpy as np
from PIL import Image
from predict_breed import predict

# Direct URL to the image hosted online
image_url = "https://t3.ftcdn.net/jpg/06/71/53/70/360_F_671537078_UOjhRBtGStc0Jhn95JcqkroycvYgugJW.jpg"


# Custom CSS to set the background image with a gradient overlay and title
page_bg_img = f"""
<style>
  .container {{
      position: relative;
      width: 100%;
      height: 30vh;
      display: flex;
      justify-content: flex-end;
      align-items: flex-start;
      background: linear-gradient(to right,  #694E4E 60%, transparent 70%);
  }}
  .image {{
      position: relative;
      height: 30vh;
      width: auto;
      mask-image: linear-gradient(to right, rgba(0, 0, 0, 0), rgba(0, 0, 0, 1) 50%);
      -webkit-mask-image: linear-gradient(to right, rgba(0, 0, 0, 0), rgba(0, 0, 0, 1) 50%);
      z-index: 2;
  }}
  .title {{
      position: absolute;
      top: 25%;
      width: 35%;
      left: 8%;
      color: white;
      font-size: 2em;
      font-weight: normal;
      z-index: 3;
  }}
</style>
<div class="container">
    <div class="title">Dog and Cat Breed Classifier</div>
    <img src="{image_url}" class="image">
</div>
"""

# Inject the custom CSS and HTML into the Streamlit app
st.markdown(page_bg_img, unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "Upload your pet's image here", type=['png', 'jpg', 'jpeg'])


# # Load the pre-trained model
# model_path = "pet_breed_model.pkl"
# with open(model_path, 'rb') as file:
#     model = pickle.load(file)


# Function to preprocess the image
def preprocess_image(image):
    # Resize the image to match the input size of the model
    image = image.resize((224, 224))
    # Convert the image to numpy array and normalize the pixel values
    image = np.array(image) / 255.0
    # Expand the dimensions to match the input shape expected by the model
    image = np.expand_dims(image, axis=0)
    return image


# Function to make predictions
def predict_breed(image):
    # Preprocess the image
    # image = preprocess_image(image)
    # Make predictions using the model
    prediction = predict(image)
    return prediction


if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True, width=100)

    # Predict the breed
    prediction = predict_breed(image)

    # Display the predicted breed
    st.write(prediction)
