import pickle
import numpy as np
import random
from teencode import TeenConverToOriSentence
import json
from utils import WordTokenize,BagOfWord
import sklearn.externals 
import joblib

with open("data2.joblib",'rb') as f:
    data=joblib.load(f)

model_predict=data['model']
model_prob=data['prob']
    

with open('data.pkl', 'rb') as file:
    pickle_model = pickle.load(file)

label=pickle_model['label']
word=pickle_model['word']
data=pickle_model['data']

def GetResponse(msg):
    result=WordTokenize(TeenConverToOriSentence(msg))
    result=BagOfWord(result,word)
    result=np.array(result).reshape(1,-1)
    y_prob=float(np.max(model_prob(result),axis=1))
    if(y_prob>0.6):
        y_pred=model_predict(result)
        for intent in data['intents']:
            if intent['tag']==label[int(y_pred)]:
                respons=intent['responses']
                return random.choice(respons)
                
    
    return "Xin lỗi mình không hiểu ý bạn. Bạn có thể thử lại."


def main():
    s=GetResponse("cho mih hỏi này chút đc kh ?")
    print(s)
    
    return

if __name__ =="__main__":
    main()