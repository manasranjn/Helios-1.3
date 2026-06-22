l1 = ['Hi', 'Hello', 'Good', 'bye', 'Morning', 'bye']

# print(l1[2])
# print(l1[2:5])
# print(l1[2:])
# print(l1[:5])
# print(l1[:])
# print(l1[-2])
# print(l1[-2:])

# l1.append(10)
# l1.insert(3, 10)
# l1.extend([10, 20, 30])
# l1.remove('bye')
# elem = l1.pop(2)
# print(elem)
# l1.clear()
# print(l1)
# print(l1.index('bye'))
# print(l1.count('Hii'))

l2 = [30,20,40,60,10,50]
# l2.sort()
# l2.sort(reverse=True)
# l2.reverse()
# print(l2)

# l3 = l2.copy()
# print(l3)

# WAP to check if two strings are anagrams

s1 = 'listens'
s2 = 'silent'

if sorted(s1) == sorted(s2):
    print("Anagrams")
else:
    print("Not Anagrams")

# Take a list of strings  and short them  based on string length