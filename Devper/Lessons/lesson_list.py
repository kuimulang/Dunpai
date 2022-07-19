mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0]) # prints 1
print(mylist[1]) # prints 2
print(mylist[2]) # prints 3

# prints out 1,2,3
for x in mylist:
    print(x)

# print(mylist[10]) #IndexError: list index out of range

print("=======================================")
numbers = []
strings = []
names = ["John", "Eric", "Jessica"]
# write your code here
second_name = None
count = 0
while count < len(names):
    print(names[count])
    count += 1  # This is the same as count = count + 1
# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)

for x in names:
    print("The names list is %s" % x)
print("names contains %d objects" % len(names))

print("=======================================")
