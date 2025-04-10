# Базовый класс
class Coffee:
    def cost(self):
        return 5  # базовая цена кофе

    def ingredients(self):
        return "Coffee"


# Декоратор для добавления молока
class MilkDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 1.5  # добавляем стоимость молока

    def ingredients(self):
        return self._coffee.ingredients() + ", Milk"


# Декоратор для добавления сахара
class SugarDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 0.5  # добавляем стоимость сахара

    def ingredients(self):
        return self._coffee.ingredients() + ", Sugar"


# Клиентский код
def client_code(coffee):
    print(f"Ingredients: {coffee.ingredients()}")
    print(f"Total cost: ${coffee.cost():.2f}")


# Использование
if __name__ == "__main__":
    # Создаем базовый кофе
    my_coffee = Coffee()

    # Добавляем молоко
    my_coffee_with_milk = MilkDecorator(my_coffee)

    # Добавляем сахар
    my_coffee_with_milk_and_sugar = SugarDecorator(my_coffee_with_milk)

    # Выводим информацию о кофе
    client_code(my_coffee_with_milk_and_sugar)
