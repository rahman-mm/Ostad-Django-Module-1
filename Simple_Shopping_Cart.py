name= input("Give me the customer name: ")


product_1= input("First product name: ")
product_1_price= float(input("Price of first product: "))

product_2= input("Second product name: ")
product_2_price= float(input("Price of second product: "))

product_3= input("Third product name: ")
product_3_price= float(input("Price of third product: "))


subtotal= product_1_price + product_2_price + product_3_price


if subtotal >= 5000:
    discount= subtotal*(20/100)

elif subtotal >= 3000:
    discount= subtotal*(10/100)

elif subtotal >= 1000:
    discount= subtotal*(5/100)

else:
    discount= 0


total= subtotal-discount


print(f"Customer Name: {name}")
print()

print(f"Product 1: {product_1}")
print(f"Price: {product_1_price}")
print()

print(f"Product 2: {product_2}")
print(f"Price: {product_2_price}")
print()

print(f"Product 2: {product_3}")
print(f"Price: {product_3_price}")
print()

print(f"Subtotal: {subtotal}")
print(f"Discount: {discount}")
print(f"Final Total: {total}")
