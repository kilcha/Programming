from abc import ABC, abstractmethod
import copy

# Prototype
class AircraftComponent(ABC):
    @abstractmethod
    def clone(self):
        pass

class Engine(AircraftComponent):
    def __init__(self, model, thrust):
        self.model = model
        self.thrust = thrust

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"{self.model} ({self.thrust} kN)"

class Wing(AircraftComponent):
    def __init__(self, length, material):
        self.length = length
        self.material = material

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"{self.length}m {self.material} wings"

class Aircraft:
    def __init__(self, components):
        self.engines = [c for c in components if isinstance(c, Engine)]
        self.wings = [c for c in components if isinstance(c, Wing)]
    
    def describe(self):
        print("Aircraft components:")
        print(f"Engines: {', '.join(str(e) for e in self.engines)}")
        print(f"Wings: {self.wings[0] if self.wings else 'None'}")

# Singleton
class ComponentManager:
    _instance = None
    
    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance._prototypes = {}
        return cls._instance
    
    def register_prototype(self, name, component):
        self._prototypes[name] = component
        
    def get_prototype(self, name):
        return self._prototypes[name].clone()

# Abstract Factory
class AircraftFactory(ABC):
    @abstractmethod
    def create_engine(self):
        pass
    
    @abstractmethod
    def create_wing(self):
        pass

# Concrete Factories
class PassengerJetFactory(AircraftFactory):
    def create_engine(self):
        return ComponentManager().get_prototype("jet_engine")
    
    def create_wing(self):
        return ComponentManager().get_prototype("jet_wing")

class CargoPlaneFactory(AircraftFactory):
    def create_engine(self):
        return ComponentManager().get_prototype("prop_engine")
    
    def create_wing(self):
        return ComponentManager().get_prototype("cargo_wing")

# Builder
class AircraftBuilder:
    def __init__(self, factory):
        self.factory = factory
        self.components = []
    
    def add_engine(self, count=1):
        for _ in range(count):
            self.components.append(self.factory.create_engine())
        return self
    
    def add_wings(self):
        self.components.append(self.factory.create_wing())
        return self
    
    def build(self):
        return Aircraft(self.components)

# Check
b = AircraftBuilder(CargoPlaneFactory())
b.build()

# Factory Method
class AircraftDirector:
    @staticmethod
    def construct_passenger_jet():
        builder = AircraftBuilder(PassengerJetFactory())
        return builder.add_engine(2).add_wings().build()
    
    @staticmethod
    def construct_cargo_plane():
        builder = AircraftBuilder(CargoPlaneFactory())
        return builder.add_engine(4).add_wings().build()

# Usage
if __name__ == "__main__":
    ComponentManager().register_prototype("jet_engine", Engine("CFM56", 120))
    ComponentManager().register_prototype("jet_wing", Wing(30, "Carbon composite"))
    ComponentManager().register_prototype("prop_engine", Engine("PW150", 50))
    ComponentManager().register_prototype("cargo_wing", Wing(40, "Aluminum"))

    print("Building passenger jet:")
    passenger_jet = AircraftDirector.construct_passenger_jet()
    passenger_jet.describe()

    print("\nBuilding cargo plane:")
    cargo_plane = AircraftDirector.construct_cargo_plane()
    cargo_plane.describe()

    print("\nBuilding custom aircraft:")
    custom_builder = AircraftBuilder(PassengerJetFactory())
    custom_plane = custom_builder.add_engine(4).add_wings().build()
    custom_plane.describe()
