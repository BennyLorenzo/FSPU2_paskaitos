# tuple - duomenų tipas list, kuriam negalimi pakeitimai

months = ('sausis', 'vasaris', 'kovas', 'balandis', 'gegužė', 'birželis')

print(type(months))

for month in months:
    print(month)

print(months[0])

# keitimo operacijos negalimos
# del months[0]
# months[0] = "gruodis"

# galimi tik 2 metodai, kurie veikia su tuple
# .index() - grąžina elemento indeksą
print(months.index("sausis"))

# .count() - skaičiuoja, kiek kartų elementas pasikartoja
print(months.count("sausis"))

# galima pridėti elementus prie kintamojo
months += ("lapkritis", "gruodis")
print(months)

months = ('sausis', 'vasaris', 'kovas', 'balandis', 'gegužė', 'birželis', 'sausis')
months = months[:-1] + ('liepa', 'rugpjūtis', 'rugsėjis', 'spalis', 'lapkritis', 'gruodis')

print(months)
