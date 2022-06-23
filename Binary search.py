def binarysearch(items,x):
    start = 0
    end = len(items)

    while True:

        if start <=end:
            mid = int((start + end)/2)
        else:
            return
        
        if items[mid]==x:
            return mid+1

        print(items[mid])

        if items[mid]<x:
            start = mid + 1
        else: end = mid-1

def binarysearch1(items,x)->str:
    start = 0
    end = len(items)

    while True:
        if start <= end:
            mid = int((start+end)/2)
        else: return

        if items[mid]==x:
            return f"Item Found At {mid}"
            
        elif items[mid]<x:
            start = mid + 1
        else: end = mid-1

if __name__ == '__main__':
    print(binarysearch1([1,12,12,13,20],12))
