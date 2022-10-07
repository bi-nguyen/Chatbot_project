import re
import numpy as np
patter=re.compile(r'(?i)\b[a-záàảãạăắằẳẵặâấầẩẫậéèẻẽẹêếềểễệóòỏõọôốồổỗởỡợíìỉĩịúùủũụưứừửữựýỳỷỹỵộơớờđ]+\b')

def WordTokenize(word):
    w=patter.findall(word)
    return w

def BagOfWord(word,ListWord):
    bag=np.zeros(len(ListWord))
    w=[i.lower() for i in word]
    for idx,val in enumerate(ListWord):
        if val in w:
            bag[idx]=1
    return bag



def main():
    s="xin chào mọi người"
    s=WordTokenize(s)
    listword=["chào","chiều","ngườI","xin"]
    print(np.array(BagOfWord(s,listword)))
    return


if __name__=="__main__":
    main()
