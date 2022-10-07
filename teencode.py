import time
with open('teencode.txt','r',encoding='utf8') as file:
    data=file.read()

teencode=[]
OriWord=[]
l=data.split('\n')
AllWord=[l[i].split("\t") for i in range(len(l))]

#teen ori list
teen_dict={}
for teen,w in AllWord:
    teencode.append(teen)
    OriWord.append(w)



def TeenConverToOriWord(word):
    if len(word)==0:
        return 
    for idx,w in enumerate(teencode):
        if w==word:
            word=OriWord[idx]
    return word

def TeenConverToOriSentence(sentence):
    w=[]
    for s in sentence.split():
        w.append(TeenConverToOriWord(s))
    return " ".join(w)
        


def main():
    start=time.time()
    s='b'
    a=TeenConverToOriWord(s)
    print(a)
    end=time.time()
    print(end-start)
    
    
    return



if __name__=="__main__":
    main()