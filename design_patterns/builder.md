The Builder Pattern is a creational design pattern used to construct complex objects step by step. It allows the construction of different representations of an object using the same construction process. This pattern separates the construction of a complex object from its representation, allowing the same construction process to create different representations.

Here's how the Builder Pattern works:

1. A Builder interface declares product construction steps.
2. Concrete builders provide implementations for the steps defined in the Builder interface.
3. A Director class constructs the object using a Builder object.

Here are five popular system design examples where the Builder Pattern can be used:

1. **Document Generation System**: A system that generates documents in various formats (e.g., PDF, Word, HTML) using a builder pattern to construct documents with different structures and formatting.

2. **Meal Ordering System**: A system that allows users to customize their meals by selecting different ingredients and options. The Builder Pattern can be used to construct meals with various combinations of ingredients.

3. **Vehicle Configuration System**: A system that lets users configure their vehicles by selecting different options (e.g., color, engine type, interior features). The Builder Pattern can be used to construct vehicles with different configurations.

4. **Email Message Builder**: A system that constructs email messages with different formats and attachments. The Builder Pattern can be used to construct email messages with varying content and attachments.

5. **Graphical User Interface (GUI) Builder**: A system that constructs graphical user interfaces with different layouts and components. The Builder Pattern can be used to construct GUIs with different structures and styles.

Here's a Python code example demonstrating the Builder Pattern for constructing different types of meals:

```python
from abc import ABC, abstractmethod

# Product
class Meal:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_cost(self):
        return sum(item.price for item in self.items)

    def show_items(self):
        for item in self.items:
            print(f"Item: {item.name}, Packing: {item.packing().pack()}, Price: {item.price}")


# Item
class Item(ABC):
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def packing(self):
        pass

    @abstractmethod
    def price(self):
        pass


# Concrete Items
class Burger(Item):
    def name(self):
        return "Burger"

    def packing(self):
        return Wrapper()

    def price(self):
        return 2.50


class Drink(Item):
    def name(self):
        return "Drink"

    def packing(self):
        return Bottle()

    def price(self):
        return 1.00


# Packing
class Packing(ABC):
    @abstractmethod
    def pack(self):
        pass


class Wrapper(Packing):
    def pack(self):
        return "Wrapper"


class Bottle(Packing):
    def pack(self):
        return "Bottle"


# Builder
class MealBuilder:
    def prepare_veg_meal(self):
        meal = Meal()
        meal.add_item(Burger())
        meal.add_item(Drink())
        return meal

    def prepare_non_veg_meal(self):
        meal = Meal()
        meal.add_item(Burger())
        meal.add_item(Burger())
        meal.add_item(Drink())
        return meal


# Client
if __name__ == "__main__":
    meal_builder = MealBuilder()

    veg_meal = meal_builder.prepare_veg_meal()
    print("Veg Meal:")
    veg_meal.show_items()
    print("Total Cost:", veg_meal.get_cost())

    non_veg_meal = meal_builder.prepare_non_veg_meal()
    print("\nNon-Veg Meal:")
    non_veg_meal.show_items()
    print("Total Cost:", non_veg_meal.get_cost())
```

In this example:

- The `Meal` class represents the product being constructed.
- The `Item` class represents the components of the meal (e.g., burger, drink).
- The `Packing` interface represents the packaging of the items.
- Concrete implementations of `Item` and `Packing` are provided.
- The `MealBuilder` class constructs different types of meals.
- The client code demonstrates how to use the builder to construct veg and non-veg meals with different combinations of items.
