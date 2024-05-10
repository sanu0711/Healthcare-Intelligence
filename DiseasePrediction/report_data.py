import pandas as pd

def get_disease_data(name,algo,disease):
    df1=pd.read_csv('./dataset/symptom_Description.csv')
    df2=pd.read_csv('./dataset/symptom_precaution.csv')
    disc=df1[df1["Disease"]==disease]
    pre=df2[df2["Disease"]==disease]
    data={
            "Name":name,
            "algo":algo,
            "prediction":disease,
           "discription":disc["Description"].values[0],
            "pre1":pre["Precaution_1"].values[0],
            "pre2":pre["Precaution_2"].values[0],
            "pre3":pre["Precaution_3"].values[0],
            "pre4":pre["Precaution_4"].values[0],
          }
    return data