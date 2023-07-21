#Linear Search 
#Using Function
arr = [1,2,3,4,5,6,7,76,45,33] 
def linearsearch(target):
    if len(arr)==0:
        print("Array is empty")
    for i in range(len (arr)):
        element = arr[i]
        if element == target:
            return i
    return -1
result = linearsearch(33)
print (result)  

#Using Class 
class LinearSearch():
    def __init__(self):
        self.element = None
    def linaersearch(self,target):
        arr = [1,2,3,4,5,6,7,88,55,44,33,22]
        if len(arr)==0:
            print("Array is Empty")
        for i in range(len(arr)):
            self.element = arr[i]
            if self.element == target:
                return i
        return -1
obj = LinearSearch()
result = obj.linaersearch(3) 
print(result)           
        
        
            