# Natural Language Processing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def func1(s):
    d = {'Review Text':s, 'Recommended IND':0}
    inp = pd.DataFrame(d,index=[0])
    # Importing the dataset
    dataset1 = pd.read_csv('womens.csv')

    dataset2 = dataset1.iloc[0:100,[4,6]]

    dataset2['Review Text'].fillna(value="good", inplace=True)
    
    dataset = dataset2.append(inp,ignore_index=True)
    
    print(dataset)

    # Cleaning the texts
    import re
    import nltk
    #nltk.download('stopwords')
    from nltk.corpus import stopwords
    from nltk.stem.porter import PorterStemmer
    corpus = []
    for i in range(0,101):
        review = re.sub('[^a-zA-Z]', ' ', dataset['Review Text'][i])
        review = review.lower()
        review = review.split()
        ps = PorterStemmer()
        review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
        review = ' '.join(review)
        corpus.append(review)

    print("data filtered")
    
    # Creating the Bag of Words model
    from sklearn.feature_extraction.text import CountVectorizer
    cv = CountVectorizer(max_features = 3000)
    X = cv.fit_transform(corpus).toarray()
    y = dataset.iloc[:, 1].values
    
    print("Split begin")
    
    # Splitting the dataset into the Training set and Test set
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)
    
    print("model training")
    
    # Fitting Naive Bayes to the Training set
    from sklearn.ensemble import RandomForestClassifier
    classifier = RandomForestClassifier(n_estimators=100)
    classifier.fit(X_train, y_train)

    # Predicting the Test set results
    y_pred = classifier.predict(X_test)

    # Making the Confusion Matrix
    from sklearn.metrics import confusion_matrix
    cm = confusion_matrix(y_test, y_pred)
    print("confusion matrix is:")
    print(cm)

    #calculating accuracy score
    from sklearn.metrics import accuracy_score
    ascore = accuracy_score(y_pred,y_test)
    print("accuracy is:")
    print(ascore)
    
    output = y_pred[-1]
    print("output is:")
    print(output)

    return output


