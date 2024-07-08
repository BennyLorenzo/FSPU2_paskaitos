text = "hello world"

# "." - taško operatorius, naudojam kviesdami string metodus

# .upper() - all-caps string
print(text.upper())

text_u = text.upper()
print(text_u)

print(text.count("l"))
print(text.count("ll"))

print(text_u.count("L"))

print(text.index("e"))
# print(text_u.index("e")) # crashes if nothing found

print(text.find("e"))
print(text_u.find("e")) # -1 if not found

text_w = text.replace("l", "w")
print(text_w)
text_w = text_w.replace("w", "")
print(text_w)

text_w = text_w = text_w.replace(" ", "")
print(text_w)

text2 = "   Welcome, class!    "
print(text2.strip())


