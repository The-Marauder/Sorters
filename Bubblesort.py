
arr = [2,7,3,5,6,8,9,10,1,4]
def bubblesort(arr) :
    for i  in range(len(arr)) :
        for i in range(0,len(arr)-1) :
            if arr[i+1] < arr[i] :
                arr[i],arr[i+1] = arr[i+1],arr[i]

bubblesort(arr)
print(arr)