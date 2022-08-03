def Bubble_Sort(arr):
    length=len(arr)
    for i in range(length):
        """The reason for taking the length-i-1 is that after every i(th) iteration we have largest element at end of the array(last element of array)
        so why need to compare them"""
        for j in range(0,length-i-1):
            """Here with every i(th) iteration we compare the arr[j] and arr[j+1] and if arr[j] is greater then arr[j+1]
            then we just interchange these value with each other
            At every i(th) iteration we have the largest value at the end of the array(last element of array)"""
            if (arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
if __name__ == '__main__':
    arr=[2,8,4,16,11,99,88,56,23,47,35,98,15,68,78]
    print(Bubble_Sort(arr))