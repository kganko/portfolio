import csv
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from tensorflow import keras
from sklearn.preprocessing import StandardScaler
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve


# add data to the model
data = pd.read_csv (r'C:\Users\kinga\Desktop\projekt\projekt.csv')

def remove_duplicates(data2):
    for item in data2:
        if item not in data2:
            data2.append(item)
    return data2

data.head(11)

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# heatmap
sns.set_style("whitegrid")

# correlation matrix
corr = data.corr()
f, ax = plt.subplots(figsize=(12, 9))
sns.heatmap(corr, vmax=.3, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})


data.head()

data2 = data.drop(columns=['industry','profession', 'traffic','coach','way'])

#zamiana wartosci
yesno_map = {'f': 1, 'm': 0}
truefalse_map = {'white': 1, 'grey': 0}
data2['gender'] = data2['gender'].map(yesno_map)
data2['head_gender'] = data2['head_gender'].map(yesno_map)
data2['greywage'] = data2['greywage'].map(truefalse_map)

data2

data2[['event','gender','head_gender']]

# create churn and rest
cols = ['stag','age', 'gender','head_gender', 'greywage', 'extraversion','independ','selfcontrol', 'anxiety', 'novator']
x = data2[cols].values
y = data2.event.values

sc = StandardScaler()
x = sc.fit_transform(x)

print(x)

# create train and test
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2, random_state=1)

model = keras.models.Sequential()
model.add(keras.layers.Dense(7, activation=keras.activations.relu, input_shape=(10,)))
model.add(keras.layers.Dense(5, activation=keras.activations.relu))
model.add(keras.layers.Dense(3, activation=keras.activations.relu))
model.add(keras.layers.Dense(1, activation=keras.activations.sigmoid))
model.summary()

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.compile(loss='binary_crossentropy',optimizer='adam',
              metrics=[keras.metrics.AUC(),
                  keras.metrics.Precision(),
                  keras.metrics.Recall(),
                  keras.metrics.TruePositives(),
                  keras.metrics.TrueNegatives(),
                  keras.metrics.FalsePositives(),
                  keras.metrics.FalseNegatives(),
                  'accuracy'])

results = model.evaluate(x_test, y_test, batch_size=64)
result_dict = dict(zip(model.metrics_names, results))

print(result_dict)

print(f'Results: {result_dict}')

# predictions
y_pred = model.predict(x_test).ravel()
y_pred_train = model.predict(x_train).ravel()

cm = np.array([[result_dict['true_negatives'],result_dict['false_positives']],
              [result_dict['false_negatives'],result_dict['true_positives']]]).astype(int)

print(cm)

# confusion matrix

sns.heatmap(cm,annot=True, fmt='d')
plt.title('Confusion Matrix', fontsize = 15) # title with fontsize 20
plt.xlabel('Predicted label', fontsize = 12) # x-axis label with fontsize 15
plt.ylabel('Actual label', fontsize = 12) # y-axis label with fontsize 15

plt.show()

model2 = keras.models.Sequential()
model2.add(keras.layers.Dense(11, activation=keras.activations.relu, input_shape=(10,)))
model2.add(keras.layers.Dense(7, activation=keras.activations.relu))

model2.add(keras.layers.Dense(2, activation=keras.activations.sigmoid))
model2.add(keras.layers.Dense(1, activation=keras.activations.sigmoid))
model2.summary()

model2.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

history = model2.fit(x_train,
 y_train,
 epochs=10,
 batch_size=32,
 validation_data=(x_test, y_test))

# ROC curve
class ModelOutputs():
    def __init__(self, fpr, tpr):
        self.fpr = fpr
        self.tpr = tpr
    def accuracy_count(self):
        self.accuracy = metrics.auc(self.fpr,self.tpr)
        return self.accuracy

fpr_model, tpr_model, thresholds = roc_curve(y_test,y_pred)
outputs_model = ModelOutputs(fpr_model,tpr_model)
auc_model = outputs_model.accuracy_count()
fpr_model_train, tpr_model_train, thresholds_train = roc_curve(y_train,y_pred_train)
outputs_train = ModelOutputs(fpr_model_train,tpr_model_train)
auc_model_train = outputs_train.accuracy_count()

# plot
plt.figure(1)
plt.plot([0, 1], [0, 1], 'k--')
plt.plot(fpr_model, tpr_model, label='Test (auc = {:.3f})'.format(auc_model))
plt.plot(fpr_model_train, tpr_model_train, label='Train (auc = {:.3f})'.format(auc_model_train))
plt.xlabel('False positive rate')
plt.ylabel('True positive rate')
plt.title('ROC curve')
plt.legend(loc='best')
plt.show()

accuracy1 = auc_model
accuracy2 = auc_model_train

# text analysus
text_analysis = 'This project is the summary of two neuron network. Accuracy for the test set is: ', accuracy1, 'and for train set:', accuracy2

print(text_analysis)

if accuracy1 > 0.6:
    print('Accuracy is higher than assumed. Success!')
else:
    print('Maybe try another paramaters?')

