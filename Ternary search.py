def ternary_search(arr, target):
    low = 0
    high =  len(arr) - 1

    while low <= high:
        
        mid1 = low + (high - low) // 3
        mid2 = high - (high - low) // 3
        
        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2

        if target < arr[mid1]:
            high = mid1 - 1

        
        elif target > arr[mid2]:
            low = mid2 + 1

        
        else:
            low = mid1 + 1
            high = mid2 - 1

    return -1 


arr = [3, 6, 9, 12, 15, 18, 21, 24, 27]
target = 18

result = ternary_search(arr, target)
if result != -1:
    print(f"Target {target} found at index: {result}")
else:
    print("Target not found!")

#Ternary Search Implementation in OOP

class TernarySearch:
    def __init__(self, arr):
        # Store sorted array
        self.arr = arr

    def search(self, target):
        low, high = 0, len(self.arr) - 1

        while low <= high:
            # Divide the range into 3 parts
            mid1 = low + (high - low) // 3
            mid2 = high - (high - low) // 3

            # Check if target is at mid1 or mid2
            if self.arr[mid1] == target:
                return mid1
            if self.arr[mid2] == target:
                return mid2

            # If target lies in first part
            if target < self.arr[mid1]:
                high = mid1 - 1

            # If target lies in third part
            elif target > self.arr[mid2]:
                low = mid2 + 1

            # If target lies in middle part
            else:
                low = mid1 + 1
                high = mid2 - 1

        return -1  # Target not found

arr = [3, 6, 9, 12, 15, 18, 21, 24, 27]
searcher = TernarySearch(arr)
target = 18
result = searcher.search(target)

if result != -1:
    print(f"Target {target} found at index: {result}")
else:
    print("Target not found!")
