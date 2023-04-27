import tensorflow as tf
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input
import numpy as np

# Load the pre-trained ResNet50 model with imagenet weights
model = ResNet50(weights='imagenet', include_top=False)

# Define a function to generate image embeddings
def generate_image_embedding(img_path):
    # Load the image and resize it to 224x224 pixels
    img = image.load_img(img_path, target_size=(224, 224))
    # Convert the image to an array of shape (224, 224, 3)
    x = image.img_to_array(img)
    # Preprocess the image array for the ResNet50 model
    x = preprocess_input(x)
    # Expand the image array to shape (1, 224, 224, 3)
    x = np.expand_dims(x, axis=0)
    # Generate the CNN output for the image
    features = model.predict(x)
    # Flatten the features to a 1D vector
    features = features.flatten()
    # Normalize the features to have unit length
    features = features / np.linalg.norm(features)
    return features
# Example usage
img_path = 'path/to/image.jpg'
img_embedding = generate_image_embedding(img_path)
