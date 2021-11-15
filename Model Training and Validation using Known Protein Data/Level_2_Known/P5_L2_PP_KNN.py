# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 11:42:44 2021

@author: Indian
"""
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from collections import Counter
from imblearn.over_sampling import SMOTE 



# dataload
data = pd.read_csv("Level_2_Path_NonPath_GP.csv") 
X=data.iloc[:,1:311]
Y=data.iloc[:,311]
plt.figure()

lda = LinearDiscriminantAnalysis(n_components=10)
Z = lda.fit(X, Y).transform(X)

sm = SMOTE(random_state=42)
Z_res, Y_res = sm.fit_resample(Z, Y)
print('Resampled dataset shape %s' % Counter(Y_res))


validation_size = 0.10
seed = 7
Z_res_train, Z_res_validation, Y_res_train, Y_res_validation = train_test_split(Z_res, Y_res, test_size=validation_size, random_state=seed)                    ## shuffle and split training and test sets
scoring = 'accuracy'

knn=KNeighborsClassifier()
knn.fit(Z_res_train, Y_res_train)
predictions = knn.predict(Z_res_validation)
print(accuracy_score(Y_res_validation, predictions))
print(confusion_matrix(Y_res_validation, predictions))
print(classification_report(Y_res_validation, predictions))