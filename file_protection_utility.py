import base64

choice = input("Choose:\n1. Protect File\n2. Restore File\nEnter choice: ")

if choice == "1":
    text = input("Enter text to protect: ")

    encoded = base64.b64encode(text.encode()).decode()

    print("\nProtected Content:")
    print(encoded)

elif choice == "2":
    encoded_text = input("Enter protected content: ")

    decoded = base64.b64decode(encoded_text.encode()).decode()

    print("\nRestored Content:")
    print(decoded)

else:
    print("Invalid Choice")