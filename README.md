# MNIST Handwritten Digit Recognition with CNN

Este proyecto implementa un **Clasificador de Dígitos Manuscritos** usando una **Red Neuronal Convolucional (CNN)** entrenada sobre el dataset **MNIST**. Además, incluye un prototipo de **aplicación web con Streamlit** para predecir dígitos a partir de imágenes.

## 📋 Tabla de Contenidos

- [Estructura del Proyecto](#estructura-del-proyecto)
- [Descripción](#descripción)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Resultados](#resultados)
- [Demo en Vivo](#demo-en-vivo)
- [Referencias](#referencias)
- [Autor](#autor)

---

## 📁 Estructura del Proyecto

```
MNIST/
│
├── app.py                      # Aplicación Streamlit para predicción
├── mnist_cnn_model.h5          # Modelo entrenado en Keras
├── proyecto-mnist.ipynb        # Notebook con el análisis completo
├── requeriment.txt             # Dependencias de Python
├── Dockerfile                  # Contenedor para ejecutar la app
```

---

## 📖 Descripción

El proyecto sigue la **metodología IBM Data Science**:

1. **Analytic Approach:** Clasificar imágenes de dígitos manuscritos (0–9)
2. **Data Requirements & Collection:** Dataset MNIST en formato IDX
3. **Data Understanding:** Exploración de muestras y distribución de clases
4. **Data Preparation:** Normalización, reshaping y one-hot encoding
5. **Modeling:** CNN con bloques de convolución y pooling, seguido de capas densas y dropout
6. **Evaluation:** Métricas de precisión, matriz de confusión y visualización de resultados
7. **Deployment:** Modelo guardado en `.h5` y prototipo de app Streamlit

### 🧠 Arquitectura del Modelo

La CNN implementada incluye:
- **Capas convolucionales** para extracción de características
- **Capas de pooling** para reducción dimensional
- **Capas densas** para clasificación
- **Dropout** para prevenir overfitting
- **Activación softmax** en la capa de salida (10 clases)

---

## 🛠️ Requisitos

- Python 3.10
- TensorFlow 2.13.0
- Streamlit 1.52.2
- Pillow
- Numpy

> ⚠️ **Nota:** Se recomienda usar el contenedor Docker proporcionado para evitar problemas de compatibilidad.

---

## 📦 Instalación

### Opción 1: Instalación Local

```bash
# Clonar el repositorio
git clone <url-del-repositorio>
cd MNIST

# Crear entorno virtual (opcional pero recomendado)
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requeriment.txt
```

### Opción 2: Usando Docker (Recomendado)

```bash
# Construir la imagen
docker build -t mnist-streamlit .

# Ejecutar el contenedor
docker run -p 8501:8501 mnist-streamlit
```

---

## 🚀 Uso

### Ejecutar la Aplicación Web

#### Con Python local:
```bash
streamlit run app.py
```

#### Con Docker:
```bash
docker run -p 8501:8501 mnist-streamlit
```

Luego abrir en el navegador: **http://localhost:8501**

### Explorar el Notebook

```bash
jupyter notebook proyecto-mnist.ipynb
```

---

## 🎯 Funcionamiento de la App

1. **Subir imagen:** Permite cargar imágenes de dígitos manuscritos (PNG, JPG, JPEG)
2. **Preprocesamiento:** Convierte la imagen a escala de grises y normaliza los valores
3. **Predicción:** Utiliza la CNN entrenada para clasificar el dígito
4. **Visualización:** Muestra la predicción y la imagen procesada en la interfaz web

### 💡 Características

- ✅ Interfaz intuitiva y fácil de usar
- ✅ Preprocesamiento automático de imágenes
- ✅ Predicción en tiempo real
- ✅ Visualización de resultados

---

## 📊 Resultados

- **Precisión en conjunto de prueba:** ~99%
- **Loss:** Convergencia efectiva durante el entrenamiento
- **Generalización:** Pocas confusiones entre dígitos similares
- **Rendimiento:** Modelo capaz de generalizar sobre nuevas imágenes manuscritas de 28×28 píxeles

### Métricas Destacadas

| Métrica | Valor |
|---------|-------|
| Accuracy | ~99% |
| Precision | ~99% |
| Recall | ~99% |
| F1-Score | ~99% |

---

## 🌐 Demo en Vivo

Prueba la aplicación desplegada en:

**🔗 [https://mnistproject-gtddipu8hv4wxpfd2amzbs.streamlit.app/](https://mnistproject-gtddipu8hv4wxpfd2amzbs.streamlit.app/)**

---

## 📚 Referencias

- [MNIST Dataset](http://yann.lecun.com/exdb/mnist/)
- Chollet, F. *Deep Learning with Python*, Manning, 2017
- [Streamlit Documentation](https://docs.streamlit.io/)
- [TensorFlow Documentation](https://www.tensorflow.org/)
- [Keras CNN Tutorial](https://keras.io/examples/vision/)

---

## 👤 Autor

**NOE ULISES MACHACA CHAMBILLA**

---

## 📄 Licencia

Este proyecto es de código abierto y está disponible para fines educativos.

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

---

## 📞 Contacto

Para preguntas o sugerencias, por favor abre un issue en el repositorio.

---

**⭐ Si este proyecto te fue útil, considera darle una estrella!**
