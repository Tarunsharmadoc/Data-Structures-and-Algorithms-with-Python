def Selection_Sort(arr):
    length=len(arr)
    for i in range(length):
        """Intitially taking min_index as equal to i at every iteration of i"""
        min_index=i
        for j in range(i+1,length):
            if (arr[j]<arr[min_index]):
                """Here we are comparing min_index element of array to j element of array 
                and if j element of array is less then min_index of array then the new min_index is j"""
                min_index=j
        """At every iteration of i we are changing the arr[i] with arr[min_index] and if both are equal then values are not changed"""
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr
if __name__ == '__main__':
    arr=[2,8,4,16,11,99,88,56,23,47,35,98,15,68,78]
    # arr=[i for i in range(200,0,-1)]
    print(Selection_Sort(arr))

"""In this algorithm we take the min_index at every i(th) iteration and compare it with the every element from
i+1 to length of that array and if any element from j to length of array is less then the element present at min_index
then the new min_index is equal to j and j is the index that is lesser then the previous min_index"""