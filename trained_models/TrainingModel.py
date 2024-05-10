import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
import joblib
# Load the dataset
data = pd.read_csv('./dataset/training.csv')
# Extract features (symptoms) and target variable (disease)
X = data.drop('prognosis', axis=1)  # Assuming 'prognosis' is the target variable
y = data['prognosis']
# Initialize the decision tree classifier
clf_DT = DecisionTreeClassifier()
clf_knn=KNeighborsClassifier()
clf_RF=RandomForestClassifier()
clf_SVM=SVC()
clf_NB=GaussianNB()

# Train the model
clf_DT.fit(X, y)
clf_knn.fit(X, y)
clf_RF.fit(X, y)
clf_SVM.fit(X, y)
clf_NB.fit(X, y)
# Save the trained model to a file
joblib.dump(clf_DT, 'trained_models/DTmodel.pkl')
joblib.dump(clf_knn, 'trained_models/KNNmodel.pkl')
joblib.dump(clf_RF, 'trained_models/RFmodel.pkl')
joblib.dump(clf_SVM, 'trained_models/SVMmodel.pkl')
joblib.dump(clf_NB, 'trained_models/NBmodel.pkl')
print("Model trained and saved successfully")
