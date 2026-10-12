# s = input("Enter a string : ")
# print(s)
# print(s.swapcase())

# # x = chr(97)
# # print(x)

# # y = ord("A")
# # print(y)

# s2 = ""

# for i in s:
#     if i >= "A" and i <= "Z":
#         s2 += chr(ord(i) + 32)
#     elif i >= "a" and i <= "z":
#         s2 += chr(ord(i) - 32)
#     else:
#         s2 += i

# print(s2)


# no = int(input("Enter a number : "))
# shift = int(input("Enter a shift : "))
# s = str(no)
# lenOfS = len(s)


# if shift > lenOfS:
#     print(s[::-1])
# else:
#     print(s[shift:] + s[:shift])


# s = input("Enter a string : ")

# cipher = ""

# for i in s:
#     if i != " ":
#         cipher += chr(ord(i) + 3)
#     else:
#         cipher += " "

# print(cipher)


# def add(a, b):
#     return a + b


# print(add(10, 20))

# add2 = lambda a, b: a + b
# print(add2(20, 50))


# li = []

# for i in range(1, 11):
#     n = int(input("Enter a number : "))
#     li.append(n)

# print(li)


# l2 = [int(input("Enter a number : ")) for i in range(1, 11)]
# print(l2)


even = []
odd = []
for i in range(1, 21):
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)

# even2 = [i for i in range(1, 21) if i % 2 == 0]
# print(even2)

evenOdd = ["Even" if i % 2 == 0 else "Odd" for i in range(1, 21)]
print(evenOdd)


marks = [89, 56, 78, 34, 95]

grade = ["A" if m >= 90 else "B" if m >= 80 else "F" for m in marks]
print(grade)
