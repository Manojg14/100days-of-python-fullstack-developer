def recursive_binary_search(names_list, search_name,low, high):
    if low > high:
        return False

    mid = (low + high) // 2

    if names_list[mid] == search_name:
        return True
    elif names_list[mid] > search_name:
        return recursive_binary_search(names_list, search_name, low, mid - 1)
    else:
        return recursive_binary_search(names_list, search_name, mid + 1, high)

contacts = {
    "Manojkumar": {"age": 25, "phone": "9876543210", "relationship": "Friend"},
    "Ganesh": {"age": 45, "phone": "9876542310", "relationship": "Father"},
    "Latha": {"age": 40, "phone": "9876534210", "relationship": "Mother"},
    "Priya": {"age": 19, "phone": "9123456780", "relationship": "Sister"},
    "Vikram": {"age": 35, "phone": "9812345678", "relationship": "Colleague"},
    "Pooja": {"age": 21, "phone": "8887654321", "relationship": "Friend"},
    "Mohan": {"age": 24, "phone": "9345678123", "relationship": "Friend"},
    "Kiruthika": {"age": 22, "phone": "7890123456", "relationship": "Cousin"},
    "Deepak": {"age": 19, "phone": "9001234567", "relationship": "Brother"}
}

names = sorted(contacts.keys())

search_name = input("Enter the contact name to search: ").capitalize()

found = recursive_binary_search(names, search_name, 0, len(names) - 1)

if found:
    info = contacts[search_name]
    print(f"Contact Details for {search_name}")
    print(f"Name: {search_name}")
    print(f"Age: {info['age']}")
    print(f"Phone: {info['phone']}")
    print(f"Relationship: {info['relationship']}")
else:
    print(f"\nContact '{search_name}' not found.")
