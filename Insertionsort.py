arr = [55,61,136,6113,122,685,987,551,864,1277,34,2,6]

def sortingarray(arr) :
    for i in range(1,len(arr)) :
        smalltemp = arr[i]
        n = i-1
        while(n>=0 and smalltemp<arr[n]) :
            arr[n+1] = arr[n]
            n-=1
        arr[n+1] = smalltemp



sortingarray(arr)
print(arr)
