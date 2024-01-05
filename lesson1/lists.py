users=  ['Dave','John','Sara', 'Kamil']
data = ['Dave', 42, True]

emptylist = []

# print('Dave' in emptylist)

# print(users[0])
# print(users[-1])
print(users[-3:4])


print(users.index('Sara'))

print(len(data))

users.append('Elsa')
# print(users)

users.extend(['Robert','Jimmy'])
print(users)
# users.extend(data)
# print(users)

users.insert(0, 'Bob')
# print(users)

users[2:2]= ['Eddie','Alex']
# print(users)


users.remove('Bob')
print(users)

del data
users.sort()
print(users)

nums = [4,42,78,1,5]
# # nums.sort(reverse=True)
# print(nums)
# nums.reverse()

# # print(sorted(nums, reverse=True))
# x=sorted(nums, reverse=True)
# print(nums)
# print(x)
# print(nums)
# nums.reverse()
# # print(nums)
# print(nums)


mycopy= nums.copy()
print(mycopy)
mycopy.sort()
print(mycopy)
mycopy.sort(reverse=True)
print(mycopy)  
mylist = list([1,"Neil", True])
print(mylist)
mylist.append("Ilona")
print(mylist)


mytuple = tuple(('dave',42,True))

anothertuple = (1, 4, 2, 8, 2, 2)

print(type(anothertuple))

newlist = list(mytuple)
newlist.append('Neil')
print(newlist)
newtuple = tuple(newlist)
print(newtuple)

(one,two,*hey) = anothertuple
print(one)
print(two)
print(hey)
print(anothertuple.count(2))














