def Binary_Search(arr,element):
    start=0
    end=len(arr)-1
    while(start<=end):
        mid=(start+end)//2
        if (arr[mid]==element):
            return mid
        elif (arr[mid]>element):
            """if mid element is greater then element to be found just reduce the mid by 1 and then mid will be mid-1 and start remains same"""
            end=mid-1
        else:
            """Here if the mid element id less then the element to be found then increment the start to mid+1, now the start is mid+1 and end will remains same"""
            start=mid+1
    return -1
arr=[1,3,5,9,13,15,19,24,26,29,35,39,42,46]
element=39
if __name__=='__main__':
    print(Binary_Search(arr,element))

"""This is the demo for Binary search to check the steps it taken to find that element just simply use a step_count variable
in the elif and else section and return it to get how many steps are done in that algorithm"""