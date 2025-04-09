from functools import wraps

# Базовый класс, который мы будем декорировать
class Coffee:
    def cost(self):
        return 5  # Базовая стоимость кофе

# Декоратор для добавления молока
class MilkDecorator:
    def __init__(self, coffee):
        self._coffee = coffee  # Храним ссылку на объект Coffee

    def cost(self):
        return self._coffee.cost() + 1  # Добавляем стоимость молока

# Декоратор для добавления сахара
class SugarDecorator:
    def __init__(self, coffee):
        self._coffee = coffee  # Храним ссылку на объект Coffee

    def cost(self):
        return self._coffee.cost() + 0.5  # Добавляем стоимость сахара

# Использование декораторов
if __name__ == "__main__":
    # Создаем обычный кофе
    my_coffee = Coffee()
    print(f"Стоимость обычного кофе: {my_coffee.cost()}")

    # Добавляем молоко
    my_coffee_with_milk = MilkDecorator(my_coffee)
    print(f"Стоимость кофе с молоком: {my_coffee_with_milk.cost()}")

    # Добавляем сахар
    my_coffee_with_milk_and_sugar = SugarDecorator(my_coffee_with_milk)
    print(f"Стоимость кофе с молоком и сахаром: {my_coffee_with_milk_and_sugar.cost()}")
