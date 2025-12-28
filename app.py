import streamlit as st
from tensorflow.keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

# Cargar modelo
model = load_model("mnist_cnn_model.h5")

st.title("Reconocimiento de Dígitos Manuscritos (MNIST)")
st.write("Dibuja o sube una imagen de un dígito (28x28 px)")

uploaded_file = st.file_uploader("Sube tu imagen", type=["png","jpg","jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file).convert('L')
    st.image(image, caption="Imagen subida", use_column_width=True)
    
    # Preprocesamiento
    image = ImageOps.invert(image)
    image = image.resize((28,28))
    image_array = np.array(image)/255.0
    image_array = image_array.reshape(1,28,28,1)
    
    # Predicción
    prediction = model.predict(image_array)
    predicted_digit = np.argmax(prediction)
    st.success(f"El dígito predicho es: {predicted_digit}")
