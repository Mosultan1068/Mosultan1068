from operator import truediv

from sklearn.utils import check_array

# Simple Python array (list)
numbers = [10, 20, 30, 40, 50]
days = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
mix_numbers = ["2","3","Test"]

# Access elements
print("First element:", numbers[0])      # Output: 10
print("Last element:", numbers[-1])      # Output: 50

print("All Elements:", days)

print("First element:", numbers[0])
# Add an element
numbers.append(60)
numbers.append(70)
print("After adding:", numbers)          # Output: [10, 20, 30, 40, 50, 60]

# Remove an element
numbers.remove(30)
print("After removing 30:", numbers)     # Output: [10, 20, 40, 50, 60]

# Update an element
numbers[1] = 25
numbers[0] = 100
print("After updating second element:", numbers)  # Output: [10, 25, 40, 50, 60]

print(len(numbers))

sorted_array = sorted(numbers)
print(sorted_array)
print(min(mix_numbers))
print(max(mix_numbers))





for i in range(len(sorted_array)):
    print(f"Index {i}: {sorted_array[i]}")




x = (i**2 for i in range(3))
print(list(x))

