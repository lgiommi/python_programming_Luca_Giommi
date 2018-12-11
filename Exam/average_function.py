#average_function.py
'''
This script allows to compute the average of the components of a vector.
First of all a function that loads from the keyboard the components of the vector
is called, it creates a list that represent the vector itself and then returns this
list. In the main code, after loaded the vector, its content is printed and, after this,
is printed the average (computed by an appropriate function).
'''

def load_vector():
    '''
    This function creates a vector and loads the values from the keyboard.
    '''
    v=[]
    for i in range(0,10):
        v.append(input("Insert the component %d of the vector " %i))
    return v

def average(v):
    '''
    This function returns the average of the components of a vector.
    '''
    mean=(float(sum(v))/len(v))
    return mean

v=load_vector()
print("The input vector is {0}".format(v))
print("The average of the vector components is {0:1.3f}".format(float(average(v))))
