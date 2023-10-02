#to find minimum and maximum 
#first we can simply find it by sorting the array and then getting first and last elements 
#-------CODE---------# using classes 
#first we initiated a class named pair 
#it have 2 objects min and max and the function minmax access this class to initialize the pair of minum and maximum. 
arr=[2,45,67,22,31,12]
class pair:
    def __init__(self):
        self.min=0
        self.max=0
def getMinMax(arr:list, n:int) -> pair:
    minmax= pair()
    if n==1:
        minmax.max=arr[0]
        minmax.min=arr[0]
    if arr[0]>arr[1]:
        minmax.min=arr[1]
        minmax.max=arr[0]
    else:
        minmax.min=arr[0]
        minmax.max=arr[1]
    for i in range(2,n):
        if arr[i]>minmax.max:
            minmax.max= arr[i]
        if arr[i]<minmax.min:
            minmax.min= arr[i]
    return minmax()