s1 = "Doremon"
s2 = """Shinchan"""

print(s1)
print(s2)

# s = "Mississippi"
# print(s)
# print(s[0])
# print(s[5])
# print(s[-4])
# print(s[0:8])
# print(s[3:])
# print(s[:9])
# print(s[:])
# print(s[1:8:2])
# print(s[0:9:5])
# print(s[-2:-8])
# print(s[-8:-2])
# print(s[-2:-8:-1])
# print(s[::-1])
# print(s[4:-2])


# s = "Mississippi"
# print(s)
# print(s.find("i"))
# print(s.find("i", 3))
# print(s.find("i", 3, 6))

# print(s.endswith("pi"))
# print(s.endswith("ip"))

# print("   Hello  ".strip())
# print("   Hello  ".lstrip())
# print("   Hello  ".rstrip())

# print("Hello".replace("l", "v"))

# t = "I am Java"
# print(t.split())

# e = "demo@gmail.com"
# print(e.split("@"))


# x = "a-b-c-d-e"
# print(x.split("-"))
# print(x.split("-", 2))

# y = x.split("-")

# print("$".join(y))

# print("²".isdigit())
# print("²".isdecimal())

# print("hi".center(6, "-"))
# print("hi".ljust(6, "-"))
# print("hi".rjust(6, "-"))
# print("42".zfill(1))

# print("My name is {}".format("Ansh"))


name = "Ram"
age = 22

print("My name is", name, " age is", age)
print("My Name is " + name + " age is " + str(age))
print(f"My name is {name} and age is {age}")
print("My name is {} and age is {}".format(name, age))

print("\101")

import string

a_string = "!hi. wh?at is the weat[h]er lik?e."
new_string = a_string.translate(str.maketrans("", "", string.punctuation))
print(new_string)


s = "Mississippi"

for i in s:
    print(i, end="")

for i in range(0, len(s)):
    print(s[i])


t = "Hello Pyth@n is 100% easy"
