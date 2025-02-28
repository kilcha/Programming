from abc import ABC, abstractmethod
from copy import deepcopy

# Синглтон
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

# Фабричный метод
class Product(ABC):
    @abstractmethod
    def operation(self):
        pass

class ConcreteProductA(Product):
    def operation(self):
        return "ConcreteProductA"

class ConcreteProductB(Product):
    def operation(self):
        return "ConcreteProductB"

class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self):
        product = self.factory_method()
        return f"Creator: {product.operation()}"

class ConcreteCreatorA(Creator):
    def factory_method(self):
        return ConcreteProductA()

class ConcreteCreatorB(Creator):
    def factory_method(self):
        return ConcreteProductB()

# Фабрика
class SimpleFactory:
    @staticmethod
    def create_product(product_type):
        if product_type == "A":
            return ConcreteProductA()
        elif product_type == "B":
            return ConcreteProductB()
        else:
            raise ValueError("Unknown product type")

# Билдер
class Builder:
    def __init__(self):
        self.reset()

    def reset(self):
        self._product = Product()

    @property
    def product(self):
        product = self._product
        self.reset()
        return product

    def produce_part_a(self):
        self._product.add("PartA")

    def produce_part_b(self):
        self._product.add("PartB")

class Product:
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def list_parts(self):
        return f"Product parts: {', '.join(self.parts)}"

# Абстрактная фабрика
class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self):
        pass

    @abstractmethod
    def create_product_b(self):
        pass

class ConcreteFactory1(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA()

    def create_product_b(self):
        return ConcreteProductB()

class ConcreteFactory2(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA()

    def create_product_b(self):
        return ConcreteProductB()

# Прототип
class Prototype:
    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        self._objects[name] = obj

    def unregister_object(self, name):
        del self._objects[name]

    def clone(self, name, **attrs):
        obj = deepcopy(self._objects.get(name))
        obj.__dict__.update(attrs)
        return obj

# Пример использования
if __name__ == "__main__":
    # Синглтон
    singleton1 = Singleton()
    singleton2 = Singleton()
    print(singleton1 is singleton2)  # True

    # Фабричный метод
    creator_a = ConcreteCreatorA()
    print(creator_a.some_operation())  # Creator: ConcreteProductA

    creator_b = ConcreteCreatorB()
    print(creator_b.some_operation())  # Creator: ConcreteProductB

    # Фабрика
    factory = SimpleFactory()
    product_a = factory.create_product("A")
    print(product_a.operation())  # ConcreteProductA

    product_b = factory.create_product("B")
    print(product_b.operation())  # ConcreteProductB

    # Билдер
    builder = Builder()
    builder.produce_part_a()
    builder.produce_part_b()
    print(builder.product.list_parts())  # Product parts: PartA, PartB

    # Абстрактная фабрика
    factory1 = ConcreteFactory1()
    product_a1 = factory1.create_product_a()
    product_b1 = factory1.create_product_b()
    print(product_a1.operation())  # ConcreteProductA
    print(product_b1.operation())  # ConcreteProductB

    factory2 = ConcreteFactory2()
    product_a2 = factory2.create_product_a()
    product_b2 = factory2.create_product_b()
    print(product_a2.operation())  # ConcreteProductA
    print(product_b2.operation())  # ConcreteProductB

    # Прототип
    prototype = Prototype()
    prototype.register_object("ConcreteProductA", ConcreteProductA())
    cloned_product = prototype.clone("ConcreteProductA")
    print(cloned_product.operation())  # ConcreteProductA