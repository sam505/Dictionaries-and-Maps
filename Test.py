n = int(input ("Enter a number here: "))
phonebook = {}
for m in range (0,n):
    a = input("Enter key and value: ").split()
    phonebook[a[0]] = a[1]

for i in range(0, n):
    name = input("Enter a name: ")
    if name in phonebook:
        print(name + "=" + str(phonebook[name]))
    else:
        print("Not found")
    i += 1