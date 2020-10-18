from tensorflow.keras.models import model_from_json
import numpy as np
import tensorflow as tf


class FacialExpressionModel(object):
    EXPRESSIONS = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']

    def __init__(self, model_json_file, model_weight_file):
        with open(model_json_file, 'r') as json_file:
            loaded_model = json_file.read()
            self.loaded_model = model_from_json(loaded_model)
        self.loaded_model.load_weights(model_weight_file)
        # self.loaded_model._make_predict_function()

    def predict_emotion(self, img):
        self.preds = self.loaded_model.predict(img)
        return FacialExpressionModel.EXPRESSIONS[np.argmax(self.preds)]


