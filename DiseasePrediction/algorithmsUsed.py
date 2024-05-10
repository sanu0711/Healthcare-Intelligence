import random
import joblib
# from algoModels import modelAlgos
from forms import modelAlgos
class DiseasePredictor:
    def __init__(self):
        self.model = self.load_model()
    def load_model(self):
        model_path = 'trained_models\DTmodel.pkl'
        model = joblib.load(model_path)
        return model
    def predict_disease(self, symptoms):
        predicted_disease = self.model.predict([symptoms])
        return predicted_disease[0]
# Usage
# predict_disease= DiseasePredictor().predict_disease
random_symptoms = [random.randint(0, 1) for _ in range(132)]
# predicted_disease = predict_disease(random_symptoms)
# print("Predicted Disease:", predicted_disease)
m=modelAlgos().decisionTree([random_symptoms])[0]
print(m)
