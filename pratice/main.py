arr=[1,2,3,4,5,5,5,5,6,6,6,6,6,6];
def vote(arr):
    for i in range(len(arr)):
        n=len(arr)
        index=0;
        if arr[i]==arr[n-i-1]:
            index+=1
            i+=1
            n-+1
        elif index > 2:
            return arr;
        else:
            pass
    return arr
print(vote(arr))
