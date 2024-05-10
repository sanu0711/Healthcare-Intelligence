import pandas as pd
class modelAlgos:
    def __init__(self):
        data = pd.read_csv('./dataset/training.csv')
        self.X = data.drop('prognosis', axis=1)  # Assuming 'prognosis' is the target variable
        self.y = data['prognosis']

    def decisionTree(self, X_test):
        # Decision Tree
        from sklearn.tree import DecisionTreeClassifier
        dtree = DecisionTreeClassifier()
        dtree.fit(self.X, self.y)
        y_pred = dtree.predict(X_test)
        return y_pred

    def randomForest(self,  X_test):
        # Random Forest
        from sklearn.ensemble import RandomForestClassifier
        rfc = RandomForestClassifier(n_estimators=200)
        rfc.fit(self.X, self.y)
        y_pred = rfc.predict(X_test)
        return y_pred

    def knn(self, X_test):
        # KNN
        from sklearn.neighbors import KNeighborsClassifier
        knn = KNeighborsClassifier(n_neighbors=3)
        knn.fit(self.X, self.y)
        y_pred = knn.predict(X_test)
        return y_pred

    def svm(self, X_test):
        # SVM
        from sklearn.svm import SVC
        svc = SVC()
        svc.fit(self.X, self.y)
        y_pred = svc.predict(X_test)
        return y_pred

    def naiveBayes(self, X_test):
        # Naive Bayes
        from sklearn.naive_bayes import GaussianNB
        gaussian = GaussianNB()
        gaussian.fit(self.X, self.y)
        y_pred = gaussian.predict(X_test)
        return y_pred

