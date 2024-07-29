# 2
class CoffeeShop:

    def __init__(self, name, meniu):
        self.name = name
        self.meniu = meniu
        self.orders = []

    def add_order(self, item):
        if item in self.meniu.keys():
            self.orders.append(item)
        else:
            print("Šiuo metu šios prekės nėra!")

    def fulfill_order(self):
        if len(self.orders) > 0:
            del self.orders[0]
        else:
            print("Visi užsakymai įvykdyti!")

    def list_orders(self):
        return self.orders

    def due_amount(self):
        sum = 0
        for item in self.orders:
            for key, value in self.meniu.items():
                if item == key:
                    sum += value['price']
        print(sum)

    def cheapest_item(self):
        prices = []
        for key, value in self.meniu.items():
            prices.append(value['price'])
        return min(prices)

    def drinks_only(self):
        drinks = []
        for key, value in self.meniu.items():
            if value['type'] == 'drink':
                drinks.append(key)
        return drinks

    def food_only(self):
        food = []
        for key, value in self.meniu.items():
            if value['type'] == 'food':
                food.append(key)
        return food


cafe1 = CoffeeShop("La Chikita", {
    'cola':
        {
            'type': 'drink',
            'price': 2.2},
    'fanta':
        {
            'type': 'drink',
            'price': 2},
    'burger':
        {
            'type': 'food',
            'price': 4.5},
    'pizza':
        {
            'type': 'food',
            'price': 12}
})

cafe1.add_order('cola')
cafe1.add_order('burger')
cafe1.add_order('burger')
# cafe1.fulfill_order()
# print(cafe1.orders)
print(cafe1.list_orders())

print(cafe1.cheapest_item())
cafe1.due_amount()
print(cafe1.drinks_only())
print(cafe1.food_only())
