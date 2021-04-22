from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
import itertools

import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix
from tqdm import trange
import matplotlib.pyplot as plt
import csv
import math

def evaluate(y_pred,y_true,result_dir,labels):
        def plot_confusion_matrix(cm, classes, output_file,
                                  normalize=False,
                                  title='Confusion matrix',
                                  cmap=plt.cm.Blues):
            """
            This function prints and plots the confusion matrix.
            Normalization can be applied by setting `normalize=True`.
            """
            if normalize:
                cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
                print("Normalized confusion matrix")
            else:
                print('Confusion matrix, without normalization')
 
            print(cm)
 
            plt.imshow(cm, interpolation='nearest', cmap=cmap)
            plt.title(title)
            plt.colorbar()
            tick_marks = np.arange(len(classes))
            plt.xticks(tick_marks, classes,rotation=45)
            plt.yticks(tick_marks, classes)
 
            fmt = '.2f' if normalize else 'd'
            thresh = cm.max() / 2.
            for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
                plt.text(j, i, format(cm[i, j], fmt),
                         horizontalalignment="center",
                         color="white" if cm[i, j] > thresh else "black")
 
            plt.tight_layout()
            plt.ylabel('true')
            #plt.xlabel('pre')
            plt.savefig(output_file)
            
        # 有効桁数を下2桁とする
        np.set_printoptions(precision=2)
        
        # accuracyの計算
        accuracy=accuracy_score(y_true,y_pred)
        print("accuracy_score_finish")
        
        # confusion matrixの作成
        cnf_matrix=confusion_matrix(y_true,y_pred)#,labels=labels
        print("cnf_finish")
        
        # report(各種スコア)の作成と保存
        report=classification_report(y_true,y_pred)#,labels=labels
        report_file=open(result_dir+"/report.txt","w")
        report_file.write(report)
        report_file.close()
        print(report)
        print("report_finish")
        
        # confusion matrixのプロット、保存、表示
        title="overall accuracy:"+str(accuracy)
        plt.title(title)
        plt.figure()
        plot_confusion_matrix(cnf_matrix, classes=labels,output_file=result_dir+"/CM_without_normalize.png",title='pre')
        plt.figure()
        plot_confusion_matrix(cnf_matrix, classes=labels,output_file=result_dir+"/CM_normalized.png", normalize=True,title='pre')
        plt.show()


df1 = pd.read_csv('confusion_matrix_true_label.csv')# true_label get
df2 = pd.read_csv('confusion_matrix_pre_label.csv') # pre_label get
df3 = pd.concat([df1, df2], axis=1)# [true_label,pre_label] get
df3.to_csv('combine.dat',index = None)# [true_label,pre_label] no index save

with open('combine.dat') as f:
    d = [v for v in csv.reader(f)]

data = []

for i in trange(1, len(d)):

    data.append([int(d[i][0]), int(d[i][1])])# [[7,7],[7,7],[7,7]]

data = np.array(data)

y_true = data.T[0] # [[7,7,7]]

y_pred = data.T[1] # [[7,7,7]]



result_dir = '../confusion_matrix'

labels = ['water', 'bareground', 'grass', 'tree', 'bamboo', 'road', 'clutter', 'background']#[0,1,2,3,4,5,6,7] 

evaluate(y_pred,y_true,result_dir,labels)
print("完成")
