#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "rb") )
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

print(data_dict)

names = []
for i in data_dict.keys():
    # be careful with null values; zeros haven't been removed from the data_dict
    if data_dict[i]['bonus'] != 'NaN' and data_dict[i]['bonus'] > 5000000:
        if data_dict[i]['salary'] != 'NaN' and data_dict[i]['salary'] > 1000000:
            names.append(i)
print(names)