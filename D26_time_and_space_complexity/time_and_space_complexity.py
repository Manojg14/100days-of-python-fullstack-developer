
# Constant Time - O(1) Time
# Constant Time - O(1) Space

def get_first_element(arr):
    return arr[0]  # Accessing the first element takes constant time and no extra space

# Linear Time - O(n) Time
# Linear Time - O(1) Space

def print_all_elements(arr):
    for element in arr:  # Loop runs n times
        print(element)   # Each print is O(1)

# Quadratic Time - O(n²) Time
# Quadratic Time - O(1) Space

def print_all_pairs(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i], arr[j])  # Each pair is printed, total n*n times

arr = [1,2,3,4]

print("O(1) Example:", get_first_element(arr))
print("O(n) Example:", print_all_elements(arr))
print("O(n^2) Example:", print_all_pairs(arr))