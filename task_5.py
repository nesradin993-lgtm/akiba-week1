


customer_name = input("Enter customer name: ")


product_name = input("Enter product name: ")
price = float(input("Enter price (ETB): "))
quantity = int(input("Enter quantity: "))


total = price * quantity


print("\n========================================")
print("              RECEIPT")
print("========================================")

print(f"Customer: {customer_name}")
print()
print("Product        Price       Qty")
print("----------------------------------------")
print(f"{product_name:<15} {price:<10.2f} {quantity}")

print()
print(f"Total: {total:.2f} ETB")
print()
print("Thank you for shopping!")
print("========================================")