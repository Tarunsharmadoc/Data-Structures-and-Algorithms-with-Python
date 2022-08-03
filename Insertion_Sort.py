def Insertion_Sort(arr):
    length=len(arr)
    for i in range(1,length):
        """Here we are taking j=i-1 because we are starting from i-1 every i(th) iteration"""
        j=i-1
        """Here we are taking arr[i] value to temp because we dont want to lose that value after iteration"""
        temp=arr[i]
        while(j>=0 and arr[j]>temp):
            """Here in this step if i is greater then 0 and the arr[j] element is greater then arr[i] element
            then we are changing the arr[j+1] with arr[j] till the j reach to -1 or the arr[j]>temp
            and when the condition is not satisfied then we are just stopping the loop and then change the arr[j+1] with temp"""
            arr[j+1]=arr[j]
            j=j-1
        """Below condition will run if the j reach to -1 or the arr[j] is less them temp and then we just change the value
        of arr[j+1] with the temp value"""
        arr[j+1]=temp
    return arr
if __name__ == '__main__':
    arr = [2, 8, 4, 16, 11, 99, 88, 56, 23, 47, 35, 98, 15, 68, 78]
    print(Insertion_Sort(arr))