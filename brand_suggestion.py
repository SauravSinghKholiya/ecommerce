import numpy as np
import pandas as pd


#importing csv files
dataset1=pd.read_csv("brands.csv")

#getting the different categories of brands
dataset1['brand'].unique()

#extracting required columns
dataset = dataset1.iloc[:,[0,1,2,3]]

#counting categorical data values
dataset['brand'].value_counts()
dataset['gender'].value_counts()

#now to map categorical data into numbers
cleanup_nums = {"gender":     {"male": 0, "female": 1}, "brand": {"vans": 11, "puma": 12, "calvin-klein": 13, "woodland": 14, "reebok": 15, "nike": 16, "converse": 17, "asics": 18, "skechers": 19, "lotto": 20 }}
dataset.replace(cleanup_nums, inplace=True)

X = dataset.iloc[:,[0,1,2]].values
y = dataset.iloc[:,[3]].values


# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

#applying random forest classifier
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators=100)
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

#calculating accuracy score
from sklearn.metrics import accuracy_score
accuracy_score(y_pred,y_test)

#converting back the y predict values to brand names
df = pd.DataFrame(y_pred)
df = df.replace({11: "vans", 12: "puma", 13: "calvin-klein", 14: "woodland", 15: "reebok", 16: "nike", 17: "converse", 18: "asics", 19: "skechers", 20: "lotto"})
