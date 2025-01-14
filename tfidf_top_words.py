# tfidf top words

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
tf = TfidfVectorizer(decode_error='ignore',lowercase=False,max_features=11)
x_traintf=tf.fit_transform(x_train.values.astype('U'))
top_sum=x_traintf.toarray().sum(axis=0)
top_sum_tf=[top_sum]#to let pandas know that these are rows
columns_tf = tf.get_feature_names()
x_traintfdf = pd.DataFrame(top_sum_tf,columns=columns_tf)


import operator
dic = {}
for i in range(len(top_sum_tf[0])):
    dic[columns_tf[i]]=top_sum_tf[0][i]
sorted_dic=sorted(dic.items(),reverse=True,key=operator.itemgetter(1))
print(sorted_dic[1:])
bins = [w for w,v in sorted_dic][1:]#slicing to delete the first swachh bharat
freq = [v for w,v in sorted_dic][1:]
from matplotlib import pyplot as plt

plt.figure(figsize=(8,6))
plt.bar(bins,freq)
plt.xlabel('Words')
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.title('Top words - Tfidf Vectorizer')
plt.show()
