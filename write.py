import pandas as pd
import pickle

csv_list=["名詞","代名詞","冠詞","形容詞","動詞","副詞","前置詞","接続詞","疑問詞","助動詞","間投詞"]
Words=[]
for i in csv_list:
    Words.append(pd.read_csv(f'~/Documents/translation/csv/{i}.csv',header=None,index_col=0,squeeze=True).to_dict())
with open('Words.pickle','wb') as f:
    pickle.dump(Words,f)