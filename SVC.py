# 1. Importing Libraries
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

# 2. Importing Dataset
dataset = pd.read_csv('Social_Network_Ads.csv')
features =dataset.iloc[:,2:4].values
labels= dataset.iloc[:,-1].values



# 5. Splitting data into training and testing dataset
from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test = train_test_split(features,labels,test_size=0.25,random_state=0)


# 6.  feature Scaling 
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features_train =sc.fit_transform(features_train)
features_test = sc.fit_transform(features_test)

#SVC
from sklearn.svm import SVC
classifier=SVC(kernel = "linear" , random_state=0)
classifier.fit(features_train,labels_train)

##Predicting the class labels 
labels_pred =classifier.predict(features_test)

#Making the confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test,labels_pred)

#Accuracy Score
from sklearn.metrics import accuracy_score
ac = accuracy_score(labels_test,labels_pred)



# Evaluating the training set results
from matplotlib.colors import ListedColormap
x_set,y_set=features_train,labels_train
x1,x2 = np.meshgrid(np.arange(start=x_set[:,0].min()-1,stop=x_set[:,0].max() +1,step=0.01),
                    np.arange(start=x_set[:,1].min()-1,stop=x_set[:,1].max() +1,step=0.01))

plt.contour(x1,x2,classifier.predict(np.array([x1.ravel(),x2.ravel()]).T).reshape(x1.shape),
            alpha=0.75, cmap=ListedColormap(('red','green')))
plt.xlim(x1.min(),x1.max())
plt.xlim(x2.min(),x2.max())

for i,j in enumerate(np.unique(y_set)):
    plt.scatter(x_set[y_set==j,0],x_set[y_set==j,1],
                c=ListedColormap(('red','green'))(i),label=j)
plt.title("SVC (Training set)")    
plt.xlabel("age")
plt.ylabel("salary")
plt.legend()
plt.show()



# Evaluating the test set results
from matplotlib.colors import ListedColormap
x_set,y_set=features_test,labels_test
x1,x2 = np.meshgrid(np.arange(start=x_set[:,0].min()-1,stop=x_set[:,0].max() +1,step=0.01),
                    np.arange(start=x_set[:,1].min()-1,stop=x_set[:,1].max() +1,step=0.01))

plt.contour(x1,x2,classifier.predict(np.array([x1.ravel(),x2.ravel()]).T).reshape(x1.shape),
            alpha=0.75, cmap=ListedColormap(('red','green')))
plt.xlim(x1.min(),x1.max())
plt.xlim(x2.min(),x2.max())

for i,j in enumerate(np.unique(y_set)):
    plt.scatter(x_set[y_set==j,0],x_set[y_set==j,1],
                c=ListedColormap(('red','green'))(i),label=j)
plt.title("KNN (Test set)")    
plt.xlabel("age")
plt.ylabel("salary")
plt.legend()
plt.show()
