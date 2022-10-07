import json
from re import X
from utils import WordTokenize,BagOfWord
import numpy as np
from sklearn.linear_model import LogisticRegression
import pickle
import joblib


with open('contentVn.json','r',encoding='utf8') as file:
    data=json.load(file)
with open('test_contentVn.json','r',encoding='utf8') as test_file:
    Testdata=json.load(test_file)


# preparing training data:
word=[]
xy=[]
label=[]

for intents in data['intents']:
    for patter in intents['patterns']:
        w=WordTokenize(patter)
        word.extend(w)
        xy.append((w,intents['tag']))
    label.append(intents['tag'])
word=[w.lower() for w in word]
word=sorted(list(set(word)))

# preparing test data:

xytest=[]
for intent in Testdata['intents']:
    for patter in intent['patterns']:
        w=WordTokenize(patter)
        xytest.append((w,intent['tag']))


# training data:

X_train=[]
y_train=[]
# training data:
for val,lab in xy:
    X_train.append(BagOfWord(val,word))
    y_train.append(label.index(lab))
X_train=np.array(X_train)
y_train=np.array(y_train)

# test data:
# test data:
X_test=[]
y_test=[]
for val,lab in xytest:
    X_test.append(BagOfWord(val,word))
    y_test.append(label.index(lab))

X_test=np.array(X_test)
y_test=np.array(y_test)


#model:
model=LogisticRegression(solver='lbfgs',multi_class = 'multinomial',penalty='l2',C=1)
#training:
model.fit(X_train,y_train)
#score:
print(model.score(X_train,y_train))
print(model.score(X_test,y_test))


# saving data:
# data={
#     "model":model.predict,
#     "prob":model.predict_proba,
# }
# filename="data2.joblib"
# with open(filename, 'wb') as file:
#     joblib.dump(data,filename)

