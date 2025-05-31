def get_sum_and_product(a, b):
    sum = a + b
    product = a * b
    return sum, product

a = int(input("first value: "))
b = int(input("second value: "))

#Calling the function
result_sum, result_product = get_sum_and_product(a, b)

print("Sum:", result_sum)
print("Product:", result_product)
