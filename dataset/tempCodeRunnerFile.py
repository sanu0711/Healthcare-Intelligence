import pandas as pd

med=pd.read_csv(r"C:\Users\Abhishek Yadav\OneDrive - rgipt.ac.in\Desktop\DiseasePrediction\dataset\Medication.csv")
precaution=pd.read_csv(r"C:\Users\Abhishek Yadav\OneDrive - rgipt.ac.in\Desktop\DiseasePrediction\dataset\symptom_precaution.csv")
print(med[med['Disease']=='Allergy']['Medication'].values[0])
