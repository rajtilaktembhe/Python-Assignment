car = {
    "brand": "Toyota",
    "model": "Camry",
    "year": 2022,
    "color": "blue"
}
del car["color"]
print("Key-value pairs:")
for key, value in car.items():
    print(key, ":", value)
key_to_check = "model"
if key_to_check in car:
    print("\nKey", key_to_check, "exists in the dictionary.")
else:
    print("\nKey", key_to_check, "does not exist in the dictionary.")
