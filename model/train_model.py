import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score,mean_squared_error
from sklearn.pipeline import make_pipeline
import pickle

data=pd.read_csv("SMSSpamCollection",sep='\t',names=['label','message'])
data['label']=data['label'].map({'ham':0,'spam':1})

X_train,X_test,y_train,y_test=train_test_split(data['message'],data['label'],test_size=0.2,random_state=42)

model=make_pipeline(TfidfVectorizer(stop_words='english'),MultinomialNB())
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
print("Accuracy:",accuracy_score(y_test,y_pred))
print("Mean Squared Error:",mean_squared_error(y_test,y_pred))

vectorizer=model.named_steps['tfidfvectorizer']
pickle.dump(model,open('model/spam_model.pkl','wb'))