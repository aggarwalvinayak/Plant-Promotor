# from collections import Counter
# import tensorflow as tf
# from sklearn.metrics import make_scorer, accuracy_score, precision_recall_fscore_support,classification_report
import numpy as np
import pandas as pd
# from sklearn.metrics import f1_score
# from sklearn.utils import shuffle
from tensorflow import keras
# from sklearn.metrics import confusion_matrix

def stringToIarr(s):
    arr = []
    for i in s:
        if (i=='a'):
            arr.append(1.0)
        elif (i=='t'):
            arr.append(2.0)
        elif (i=='g'):
            arr.append(-1.0)
        else :
            arr.append(-2.0)
    return arr

def plantPromClassifier(text):

    model = keras.models.load_model('./90.092.h5')
    inputText = stringToIarr(text.lower())
    while(len(inputText)<1000):
        inputText.append(0.0)

    Xtest = np.array([inputText])
    Xtest.reshape(1,-1)
    Xtest = Xtest.reshape(len(Xtest),1,1000)

    pred = np.argmax(model.predict(Xtest),axis=1)
    if(pred == 1):
        return "Up-Regulated"
    elif(pred == 2):
        return "Down-Regulated"
    elif(pred == 0):
        return "Neutral"


