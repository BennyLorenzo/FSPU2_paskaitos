months_str = "sausis vasaris kovas"

# .split() - padalina stringą į listą pagal nurodytą skirtuką

months_list = months_str.split(" ")
print(months_list)

# literalams galima naudoti metodus pagal tipą
print("sausis".upper())

# .join() - sujungia stringų dalis į vieną stringą naudodamas skirtuką
print(" ".join(months_list))