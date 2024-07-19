auto = {}

auto['make'] = 'Audi'
print(auto)

auto['model'] = 'A8'
print(auto)

auto['colors'] = ['red', 'black', 'blue']
print(auto)

bonus_info = {
    'drive':'2-wheel',
    'power':'430 HP'
}

auto.update(bonus_info)
print(auto)
auto.update({
    'year':'2020',
    'type':'sedan'
})
print(auto)
del auto['type']
print(auto)
auto.pop('power') # returns the value
print(auto)

auto['wheel-drive'] = auto.pop('drive')
print(auto)

auto['model'] = 'Quattro'
print(auto)

auto['colors'].append('yellow')
print(auto['colors'])
