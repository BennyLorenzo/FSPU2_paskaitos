text1 = "ABCDE"
text2 = "Hello World"

# atomic variables (etc. int) cannot be divided in array

print(text1[0])
print(text1[-1])

print(text1[1:4])
print(text1[1:-1])
print(text1[1:])

# World
print(text2[6:])
# Hello W
print(text2[:7])
# ello W
print(text2[1:7])

# slice su žingsniu
print(text2[1:10:1])
print(text2[1:10:2])
print(text2[::2]) # HloWrd
print(text2[::-1]) # dlroW olleH

