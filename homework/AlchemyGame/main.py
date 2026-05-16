class Element:
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return self.name

    def __add__(self, other: 'Element'):
        pass


class Recipe:
    def __init__(self, element1_name: str, element2_name: str, result_name: str):
        self.element1_name = element1_name
        self.element2_name = element2_name
        self.result_name = result_name

    def check(self, element1_name: str, element2_name: str) -> bool:
        return ((element1_name == self.element1_name and element2_name == self.element2_name) or
                (element1_name == self.element2_name and element2_name == self.element1_name))

class AlchemyGame:
    def __init__(self):
        self.elements = {}
        self.recipes = []
        self.discovered_elements = set()
        self._initialize_base_elements()
        self._initialize_recipes()
    def _initialize_base_elements(self):
        base_elements = [
            "огонь", "вода", "земля", "воздух",
            "песок", "камень", "грязь", "пар",
            "лава", "энергия", "жизнь", "человек",
            "дерево", "металл", "стекло", "пыль",
            "растение", "инструмент", "доска", "оружие",
            "парогенератор"
        ]

        for element_name in base_elements:
            self.elements[element_name] = Element(element_name)

        self.discovered_elements = {"огонь", "вода", "земля", "воздух"}

    def _initialize_recipes(self):
        recipes_data = [
            ("огонь", "вода", "пар"),
            ("огонь", "земля", "лава"),
            ("вода", "земля", "грязь"),
            ("воздух", "вода", "пар"),
            ("воздух", "земля", "пыль"),
            ("огонь", "воздух", "энергия"),
            ("земля", "энергия", "жизнь"),
            ("вода", "жизнь", "растение"),
            ("земля", "жизнь", "человек"),
            ("огонь", "песок", "стекло"),
            ("огонь", "камень", "металл"),
            ("человек", "металл", "инструмент"),
            ("инструмент", "дерево", "доска"),
            ("инструмент", "камень", "оружие"),
            ("энергия", "пар", "парогенератор"),
            ("песок", "грязь", "глина"),
            ("вода", "песок", "пляж"),
            ("огонь", "дерево", "пепел"),
            ("воздух", "пепел", "пыль"),
            ("человек", "энергия", "маг"),
        ]

        for e1_name, e2_name, result_name in recipes_data:
            self.recipes.append(Recipe(e1_name, e2_name, result_name))

    def get_element(self, name: str):
        return self.elements.get(name)

    def discover_element(self, element_name: str):
        if element_name not in self.discovered_elements and element_name in self.elements:
            self.discovered_elements.add(element_name)
            print(f"\n Иследован новый элемент {element_name}")
            return True
        return False

    def combine(self, element1_name: str, element2_name: str):
        if element1_name not in self.elements:
            print(f"Элемента '{element1_name}' не существует в игре!")
            return None

        if element2_name not in self.elements:
            print(f"Элемента '{element2_name}' не существует в игре!")
            return None

        if element1_name not in self.discovered_elements:
            print(f"Вы ещё не открыли элемент '{element1_name}'!")
            return None

        if element2_name not in self.discovered_elements:
            print(f"Вы ещё не открыли элемент '{element2_name}'!")
            return None

        for recipe in self.recipes:
            if recipe.check(element1_name, element2_name):
                result_name = recipe.result_name

                if result_name in self.discovered_elements:
                    print(f"{element1_name} + {element2_name} = {result_name} (уже есть)")
                else:
                    print(f"{element1_name} + {element2_name} = {result_name}!")
                    self.discover_element(result_name)

                return self.get_element(result_name)

        print(f"{element1_name} + {element2_name} = ничего не дало... Попробуйте другую комбинацию!")
        return None

    def show_inventory(self):
        if not self.discovered_elements:
            print("У вас пока нет элементов!")
            return

        print("\n" + "=" * 50)
        print("Открытые элементы")
        print("=" * 50)

        sorted_elements = sorted(self.discovered_elements)

        elements_per_row = 4
        for i in range(0, len(sorted_elements), elements_per_row):
            row = sorted_elements[i:i + elements_per_row]
            print("  " + " | ".join(f"{elem:^12}" for elem in row))

        print(f"\nВсего открыто элементов: {len(self.discovered_elements)}")
        print("=" * 50)

    def show_hint(self):
        possible_recipes = []

        for recipe in self.recipes:
            if (recipe.element1_name in self.discovered_elements and
                    recipe.element2_name in self.discovered_elements and
                    recipe.result_name not in self.discovered_elements):
                possible_recipes.append(recipe)

        if possible_recipes:
            import random
            hint_recipe = random.choice(possible_recipes)
            print(
                f"\nПопробуйте соединить '{hint_recipe.element1_name}' и '{hint_recipe.element2_name}'")
        else:
            print("\nВсе возможные комбинации уже открыты")

    def show_all_elements(self):
        print("\n" + "=" * 50)
        print("Все элементы:")
        print("=" * 50)

        all_elements = sorted(self.elements.keys())
        elements_per_row = 4
        for i in range(0, len(all_elements), elements_per_row):
            row = all_elements[i:i + elements_per_row]
            print("  " + " | ".join(f"{elem:^12}" for elem in row))

        print(f"\nВсего элементов в игре: {len(all_elements)}")
        print("=" * 50)


def main():
    game = AlchemyGame()

    print("\n Игра алхимия")
    print("Комбинируйте элементы, чтобы создавать новые")
    print("Введите два элемента через пробел (например: 'огонь вода')")
    print("\nДоступные команды:")
    print("   'список' - показать ваши открытые элементы")
    print("   'все' - показать все возможные элементы в игре")
    print("   'подсказка' - получить подсказку")
    print("   'выход' - выйти из игры")
    print("\n Начальные элементы: огонь, вода, земля, воздух")
    print("-" * 60)

    while True:
        print("\nЧто вы хотите скомбинировать?")
        command = input("> ").strip().lower()

        if command == "выход":
            print("\nСпасибо за игру! До свидания!")
            break
        elif command == "список":
            game.show_inventory()
        elif command == "все":
            game.show_all_elements()
        elif command == "подсказка":
            game.show_hint()
        else:
            parts = command.split()
            if len(parts) == 2:
                elem1, elem2 = parts
                game.combine(elem1, elem2)
            else:
                print("Неверная команда!")
                print("Введите два элемента через пробел (например: 'огонь вода')")
                print("Или используйте одну из команд: список, все, подсказка, выход")


if __name__ == "__main__":
    e1 = Element(123)
    e2 = Element(223)
    e3 = e1 + e2
    main()