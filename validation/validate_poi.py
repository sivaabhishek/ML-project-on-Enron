#!/usr/bin/python


"""
    Starter code for the validation mini-project.
    The first step toward building your POI identifier!

    Start by loading/formatting the data

    After that, it's not our code anymore--it's yours!
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "rb") )

### first element is our labels, any added elements are predictor
### features. Keep this the same for the mini-project, but you'll
### have a different feature list when you do the final project.
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### it's all yours from here forward!

from sklearn import tree

clf=tree.DecisionTreeClassifier()
clf=clf.fit(features,labels)
clf.predict(features)
print(clf.score(features,labels))

from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test = train_test_split(features,labels,test_size=0.3,random_state=42)


clf=tree.DecisionTreeClassifier()
clf=clf.fit(features_train,labels_train)
print(clf.score(features_test,labels_test)) # 0.72413793103448276
print(len(features_test))

from sklearn.metrics import *
print(precision_score(labels_test,clf.predict(features_test)))
print(recall_score(labels_test,clf.predict(features_test)))

predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]
true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]
print(precision_score(true_labels, predictions))
print(recall_score(true_labels, predictions))
print(confusion_matrix(true_labels, predictions))