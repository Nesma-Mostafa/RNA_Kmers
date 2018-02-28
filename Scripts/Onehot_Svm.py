import numpy as np
from sklearn import svm
from sklearn.feature_selection import VarianceThreshold
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.svm import LinearSVC
from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_selection import SelectFromModel

Y1=[]
data=[]
with open ("dataset.txt") as f:
	data =f.read().splitlines()
        for i in range(1,len(data),1):
			Y1.append(data[i].split(' ')[1])

 
 
seqs = data

CHARS = 'ACGT'
CHARS_COUNT = len(CHARS)

maxlen = max(map(len, seqs))
res = np.zeros((len(seqs), CHARS_COUNT * maxlen), dtype=np.uint8)

for si, seq in enumerate(seqs):
    seqlen = len(seq)
    arr = np.chararray((seqlen,), buffer=seq)
    for ii, char in enumerate(CHARS):
        res[si][ii*seqlen:(ii+1)*seqlen][arr == char] = 1

print("Start SVM")

X1 = res
print(len(res))
Y1.append('1')
print(Y1)
#Y1 = [0,1]

clf = svm.SVC()
print("SVM done")
clf.fit(X1, Y1).predict(X1)
print("done")
