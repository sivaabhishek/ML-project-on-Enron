#!/usr/bin/python

import operator
def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    tuple_list = []
    for i in range(len(ages)):
        a = ages[i][0]  # ages are an array, so need to take the element out
        b = net_worths[i][0]
        c = abs(net_worths[i][0] - predictions[i][0])
        tuple_list.append((a, b, c))
    new_tuple_list = sorted(tuple_list, key=operator.itemgetter(2), reverse=True)

    cleaned_data = new_tuple_list[len(ages) // 10:]

    
    return cleaned_data

