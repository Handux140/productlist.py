products = []

while True:
    print("\nMenu:")
    print("1. List Products")
    print("2. Add Product")
    print("3. Delete Product")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        if products:
            print("Products:")
            for product in products:
                print(product)
        else:
            print("No products available.")
    elif choice == '2':
        product = input("Enter product name: ")
        products.append(product)
        print("Product added successfully.")
    elif choice == '3':
        if products:
            print("Products:")
            for index, product in enumerate(products):
                print(f"{index}: {product}")
            index_to_delete = int(input("Enter the index of the product you want to delete: "))
            if index_to_delete >= 0 and index_to_delete < len(products):
                del products[index_to_delete]
                print("Product deleted successfully.")
            else:
                print("Invalid index.")
        else:
            print("No products available to delete.")
    elif choice == '4':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")
