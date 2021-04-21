import pandas as pd
from sklearn.ensemble import RandomForestClassifier

import pickle
data = pd.read_csv('C:/Users/athar/OneDrive/Documents/Data.csv')

data = data.drop(['Unnamed: 32','id'],axis = 1)
data = data.drop(data.iloc[:,11:], axis =1)


x = data.iloc[:,1:].values
y = data['diagnosis'].copy()
y = y.map({'B':0,'M':1})


RF_clf = RandomForestClassifier()

RF_clf.fit(x, y)
pickle.dump(RF_clf, open('Cancer_model.pkl', 'wb'))
