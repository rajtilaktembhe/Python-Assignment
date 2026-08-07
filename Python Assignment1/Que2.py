numbers = [100, 50, 400, 500]
numbers[1] = 200
print("After changing:", numbers)
numbers.append(600)
print("After appending:", numbers)
numbers.insert(2, 300)
print("After inserting:", numbers)
numbers.remove(600)
print("After removing 600:", numbers)
numbers.pop(0)
print("After removing index 0:", numbers)