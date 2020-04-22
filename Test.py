import sys
sys.stdin = open('input01.txt','r')

n = int(input ())
phonebook = {}
for m in range (n):
    name = input().split()
    phonebook[name[0]] = name[1]

for i in range(n):
    name = input()
    if name in phonebook:
        print(name + "=" + str(phonebook[name]))
    else:
        print("Not found")
        
