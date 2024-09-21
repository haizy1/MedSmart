# import os
# from django.conf import settings
# #from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing import image
# import numpy as np


# # Chargement du modèle
# #model_path = os.path.join(settings.BASE_DIR, 'rayapp', 'cnn_model.h5')
# model = 'cnn_model.h5'

# def predict_image(image_file):
#     img = image.load_img(image_file, target_size=(64, 64))
#     img_array = image.img_to_array(img)
#     img_array = np.expand_dims(img_array, axis=0) / 255.0
#     prediction = model.predict(img_array)
#     if prediction[0][0] > 0.5:
#         return 'Pneumonia'
#     else:
#         return 'Normal'
import numpy as np
from PIL import Image
from tensorflow import keras
# #model = 'cnn_model.h5'
def load_and_preprocess_image(image_path):
    # Charger l'image avec PIL
    image = Image.open(image_path)
    
    # Redimensionner l'image à la taille attendue par le modèle (64x64 dans votre cas)
    image = image.resize((64, 64))
    
    # Convertir l'image en niveaux de gris
    image = image.convert('L')
    
    # Convertir l'image PIL en tableau NumPy
    image_array = np.array(image)
    
    # Normaliser les valeurs des pixels entre 0 et 1
    image_array = image_array / 255.0
    
    # Ajouter une dimension supplémentaire pour représenter les canaux (1 pour les images en niveaux de gris)
    image_array = np.expand_dims(image_array, axis=2)
    
    # Ajouter une dimension supplémentaire pour représenter les échantillons (1 car une seule image est prédite à la fois)
    image_array = np.expand_dims(image_array, axis=0)
    
    return image_array




def predict_image(image_path, model_path):
    # Charger le modèle pré-entraîné
    model = keras.models.load_model(model_path)
    
    # Charger et prétraiter l'image
    image_array = load_and_preprocess_image(image_path)
    
    # Effectuer la prédiction avec le modèle
    prediction = model.predict(image_array)
    
    # Interpréter la prédiction
    if prediction[0][0] > 0.5:
        label = 'Pneumonia'
    else:
        label = 'Normal'
    
    return label

############################## Tubersculosis


# from tensorflow.keras.models import load_model








def predict_image_tuberculosis(image_path, model_path):
    # Load the model
    model = keras.models.load_model(model_path)

    # Load and preprocess the image (using the existing preprocess_image function)
    preprocessed_image = load_and_preprocess_image(image_path)

    # Make the prediction using the preprocessed image
    prediction = model.predict(preprocessed_image)
    predicted_class = np.argmax(prediction)

    # Map the predicted class index to its corresponding label
    class_labels = {0: 'Normal', 1: 'Tuberculosis'}
    predicted_label = class_labels[predicted_class]

    return predicted_label


