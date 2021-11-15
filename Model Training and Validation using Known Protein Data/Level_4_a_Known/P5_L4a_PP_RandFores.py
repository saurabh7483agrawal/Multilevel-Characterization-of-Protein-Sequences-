# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 17:46:57 2021

@author: lenovo
"""

import pandas as pd  
import numpy as np  
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from collections import Counter
from imblearn.over_sampling import SMOTE 


#Importing Dataset
#Preparing Data For Training
df = pd.read_csv("Level_4_a_Path_StaAu_PSL_1_2_3.csv")
X=df.iloc[:,1:311]
y=df.iloc[:,311]

lda = LinearDiscriminantAnalysis(n_components=10)
Z = lda.fit(X, y).transform(X)

sm = SMOTE(random_state=50)
Z_res, Y_res = sm.fit_resample(Z, y)
print('Resampled dataset shape %s' % Counter(Y_res))

df.head()
Z_res_train, Z_res_test, Y_res_train, Y_res_test = train_test_split(Z_res, Y_res, test_size=0.2, random_state=0)  


# Feature Scaling
sc = StandardScaler()  
Z_res_train = sc.fit_transform(Z_res_train)  
Z_res_test = sc.transform(Z_res_test)


#Training the Algorithm
rfs = RandomForestClassifier(n_estimators=10, random_state=0)  
rfs.fit(Z_res_train, Y_res_train)  
Y_res_pred = rfs.predict(Z_res_test)
prob_Pred = rfs.predict_proba(Z_res_test)

#Evaluating the Algorithm
print('Mean Absolute Error:', metrics.mean_absolute_error(Y_res_test, Y_res_pred))  
print('Mean Squared Error:', metrics.mean_squared_error(Y_res_test, Y_res_pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(Y_res_test, Y_res_pred))) 
print('Confusion Matrix::', confusion_matrix(Y_res_test,Y_res_pred))  
print('Classification Report::', classification_report(Y_res_test,Y_res_pred))  
print('Accuracy Score::', accuracy_score(Y_res_test, Y_res_pred))  