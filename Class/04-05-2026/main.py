"""
ООП RPG: перевантаження операторів у Python
===========================================

Тема заняття:
- класи та об'єкти;
- magic-методи;
- перевантаження операторів;
- інкапсуляція;
- проста RPG-система бою.

Ідея прикладу:
Ми створимо невелику RPG-модель:
- Character — персонаж;
- Weapon — зброя;
- Inventory — інвентар;
- Battle — простий бій.

У прикладі будуть використані такі magic-методи:
- __str__      — красивий текстовий опис об'єкта;
- __repr__     — технічне представлення об'єкта;
- __add__      — додавання предметів / посилення зброї;
- __sub__      — атака персонажа по іншому персонажу;
- __mul__      — множення сили атаки;
- __lt__       — порівняння персонажів за рівнем;
- __eq__       — перевірка рівності персонажів;
- __len__      — кількість предметів в інвентарі;
- __contains__ — перевірка наявності предмета в інвентарі;
- __getitem__  — доступ до предмета за індексом;
- __bool__     — перевірка, чи живий персонаж.
"""


# ============================================================
# 1. КЛАС WEAPON — ЗБРОЯ
# ============================================================

class Weapon:
    """
    Клас Weapon описує зброю персонажа.

    Поля:
    - name: назва зброї;
    - damage: базова шкода;
    - rarity: рідкість зброї.
    """

    def __init__(self, name: str, damage: int, rarity: str = "common"):
        self.name = name
        self.damage = damage
        self.rarity = rarity

    def __str__(self):
        """
        Викликається, коли ми робимо print(weapon).
        """
        return f"{self.name} [{self.rarity}] — damage: {self.damage}"

    def __repr__(self):
        """
        Технічне представлення об'єкта.
        Часто використовується для дебагу.
        """
        return f"Weapon(name={self.name!r}, damage={self.damage}, rarity={self.rarity!r})"

    def __add__(self, other):
        """
        Перевантаження оператора +

        Логіка:
        weapon1 + weapon2 = нова покращена зброя

        Наприклад:
        sword + gem
        """
        if isinstance(other, Weapon):
            new_name = f"{self.name} + {other.name}"
            new_damage = self.damage + other.damage
            return Weapon(new_name, new_damage, "upgraded")

        raise TypeError("Weapon can be added only to another Weapon")

    def __mul__(self, multiplier):
        """
        Перевантаження оператора *

        Логіка:
        weapon * 2 = зброя з подвоєною шкодою
        """
        if isinstance(multiplier, int):
            return Weapon(self.name, self.damage * multiplier, self.rarity)

        raise TypeError("Weapon can be multiplied only by integer")


class Armor:
    def __init__(self, name, defense, rarity: str = 'common'):
        self.name = name
        self.defense = defense
        self.rarity = rarity

    def __str__(self):
        return f"Name: {self.name}, Defense: {self.defense}"

    def __repr__(self):
        return f"Armor(name={self.name!r}, defense={self.defense}, rarity={self.rarity!r})"


# ЗАВДАННЯ 1
# ----------
# Додайте клас Armor.
#
# Поля:
# - name
# - defense
#
# Зробіть так, щоб персонаж мав броню.
# Під час атаки шкода має зменшуватися на defense броні.
#
# Приклад:
# damage = attacker.strength + attacker.weapon.damage - defender.armor.defense
#
# Мінімальна шкода має бути не менше 1.

# ============================================================
# 2. КЛАС INVENTORY — ІНВЕНТАР
# ============================================================

class Inventory:
    """
    Клас Inventory зберігає предмети персонажа.

    Тут ми покажемо перевантаження:
    - len(inventory)
    - item in inventory
    - inventory[index]
    - inventory + item
    """

    def __init__(self):
        self._items = []

    def __str__(self):
        if not self._items:
            return "Inventory is empty"

        result = "Inventory:\n"
        for index, item in enumerate(self._items, start=1):
            result += f"  {index}. {item}\n"
        return result.strip()


    def __len__(self):
        """
        Дозволяє використовувати len(inventory).
        """
        return len(self._items)

    def __contains__(self, item_name):
        """
        Дозволяє використовувати:
        "Sword" in inventory
        """
        for item in self._items:
            if item.name == item_name:
                return True
        return False

    def __getitem__(self, index):
        """
        Дозволяє отримати предмет за індексом:
        inventory[0]
        """
        return self._items[index]

    def __add__(self, item):
        """
        Перевантаження оператора +

        inventory + item додає предмет в інвентар.
        """
        self._items.append(item)
        return self


# ============================================================
# 3. КЛАС CHARACTER — ПЕРСОНАЖ
# ============================================================

class Character:
    """
    Клас Character описує RPG-персонажа.

    Поля:
    - name: ім'я;
    - level: рівень;
    - health: здоров'я;
    - strength: сила;
    - weapon: зброя;
    - inventory: інвентар.
    """

    def __init__(self, name: str, level: int, health: int, strength: int, weapon: Weapon, armor: Armor):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength
        self.weapon = weapon
        self.inventory = Inventory()
        self.armor = armor

    def __str__(self):
        return (
            f"{self.name} | "
            f"Level: {self.level} | "
            f"HP: {self.health} | "
            f"STR: {self.strength} | "
            f"Weapon: {self.weapon.name} | "
            f"Armor: {self.armor.name}"
        )

    def __repr__(self):
        return (
            f"Character(name={self.name!r}, level={self.level}, "
            f"health={self.health}, strength={self.strength})"
        )

    def __bool__(self):
        """
        Дозволяє писати:

        if hero:
            print("Hero is alive")

        Якщо health > 0, персонаж вважається живим.
        """
        return self.health > 0

    def __lt__(self, other):
        """
        Перевантаження оператора <

        Порівнюємо персонажів за рівнем.
        """
        if isinstance(other, Character):
            return self.level < other.level

        raise TypeError("Character can be compared only with another Character")

    def __eq__(self, other):
        """
        Перевантаження оператора ==

        Два персонажі вважаються однаковими,
        якщо мають однакове ім'я та рівень.
        """
        if isinstance(other, Character):
            return self.name == other.name and self.level == other.level
        return False

    def __sub__(self, other):
        """
        Перевантаження оператора -

        Логіка:
        hero - monster означає, що hero атакує monster.

        Це не математичне віднімання, а ігрова дія.
        """
        if not isinstance(other, Character):
            raise TypeError("Character can attack only another Character")

        damage = self.strength + self.weapon.damage - other.armor.defense
        if damage > 1:
            other.health -= damage
        else:
            other.health -= 1

        if other.health < 0:
            other.health = 0

        print(f"{self.name} attacks {other.name} and deals {damage} damage")
        print(f"{other.name} HP: {other.health}")

        return other.health

    def __add__(self, value):
        """
        Перевантаження оператора +

        Логіка:
        hero + 20 означає лікування героя на 20 HP.
        """
        if isinstance(value, int):
            self.health += value
            print(f"{self.name} restores {value} HP")
            return self

        raise TypeError("Character can be healed only by integer value")

    def level_up(self):
        """
        Звичайний метод підвищення рівня.
        """
        self.level += 1
        self.health += 20
        self.strength += 5
        print(f"{self.name} reached level {self.level}!")


# ============================================================
# 4. КЛАС BATTLE — ПРОСТИЙ БІЙ
# ============================================================

class Battle:
    """
    Клас Battle відповідає за простий покроковий бій.
    """

    def __init__(self, hero: Character, enemy: Character):
        self.hero = hero
        self.enemy = enemy

    def start(self):
        print("\nBATTLE STARTED")
        print("-" * 50)
        print(self.hero)
        print(self.enemy)
        print("-" * 50)

        round_number = 1

        while self.hero and self.enemy:
            print(f"\nRound {round_number}")

            self.hero - self.enemy

            if not self.enemy:
                print(f"{self.enemy.name} is defeated!")
                self.hero.level_up()
                break

            self.enemy - self.hero

            if not self.hero:
                print(f"{self.hero.name} is defeated!")
                break

            round_number += 1

        print("\nBATTLE ENDED")
        print("-" * 50)
        print(self.hero)
        print(self.enemy)


# ============================================================
# 5. ДЕМОНСТРАЦІЯ РОБОТИ ПРОГРАМИ
# ============================================================
print(__name__)
if __name__ == "__main__":
    print(__name__)
    # --------------------------------------------------------
    # Створюємо зброю
    # --------------------------------------------------------

    sword = Weapon("Iron Sword", 15)
    fire_gem = Weapon("Fire Gem", 10, "magic")
    KnightArmor = Armor('Knight Armor', 20, 'Rare')
    axe = Weapon("Orc Axe", 12)
    LeatherArmor = Armor('Leather Armor', 10)

    print("WEAPONS")
    print("-" * 50)
    print(sword)
    print(fire_gem)
    print(axe)

    # --------------------------------------------------------
    # Перевантаження оператора + для зброї
    # --------------------------------------------------------

    fire_sword = sword + fire_gem

    print("\nUPGRADED WEAPON")
    print("-" * 50)
    print(fire_sword)

    # --------------------------------------------------------
    # Перевантаження оператора * для зброї
    # --------------------------------------------------------

    legendary_sword = fire_sword * 2

    print("\nLEGENDARY WEAPON")
    print("-" * 50)
    print(legendary_sword)

    # --------------------------------------------------------
    # Створюємо персонажів
    # --------------------------------------------------------

    hero = Character("Artemis", 3, 120, 18, legendary_sword, KnightArmor)
    orc = Character("Orc Warrior", 2, 90, 14, axe, LeatherArmor)

    print("\nCHARACTERS")
    print("-" * 50)
    print(hero)
    print(orc)

    # --------------------------------------------------------
    # Робота з інвентарем
    # --------------------------------------------------------

    potion = Weapon("Health Potion", 0, "consumable")
    dagger = Weapon("Small Dagger", 5)

    hero.inventory + potion
    hero.inventory + dagger

    print("\nHERO INVENTORY")
    print("-" * 50)
    print(hero.inventory)

    print("\nInventory length:", len(hero.inventory))
    print("Has Health Potion:", "Health Potion" in hero.inventory)
    print("First item:", hero.inventory[0])

    # --------------------------------------------------------
    # Порівняння персонажів
    # --------------------------------------------------------

    print("\nCOMPARISON")
    print("-" * 50)
    print("Hero level lower than orc level:", hero < orc)
    print("Hero equals orc:", hero == orc)

    # --------------------------------------------------------
    # Лікування через оператор +
    # --------------------------------------------------------

    print("\nHEALING")
    print("-" * 50)
    hero + 20
    print(hero)

    # --------------------------------------------------------
    # Бій
    # --------------------------------------------------------

    battle = Battle(hero, orc)
    battle.start()


# ============================================================
# 6. ЗАВДАННЯ ДЛЯ СТУДЕНТІВ
# ============================================================

"""
ЗАВДАННЯ 1
----------
Додайте клас Armor.

Поля:
- name
- defense

Зробіть так, щоб персонаж мав броню.
Під час атаки шкода має зменшуватися на defense броні.

Приклад:
damage = attacker.strength + attacker.weapon.damage - defender.armor.defense

Мінімальна шкода має бути не менше 1.


ЗАВДАННЯ 2
----------
Додайте перевантаження оператора > для Character.

Логіка:
hero > enemy має повертати True, якщо сила героя більша за силу ворога.

Сила персонажа:
strength + weapon.damage


ЗАВДАННЯ 3
----------
Додайте клас Potion.

Поля:
- name
- heal_amount

Зробіть метод use_potion(potion), який лікує персонажа.


ЗАВДАННЯ 4
----------
Зробіть обмеження максимального здоров'я.

Наприклад:
- max_health = 150
- health не може бути більше max_health


ЗАВДАННЯ 5
----------
Додайте перевантаження оператора -= для атаки.

Приклад:
orc -= hero

Це має означати:
orc отримує шкоду від hero.

Підказка:
використайте magic-метод __isub__.
"""

# ============================================================
# 7. ПРИКЛАД РІШЕННЯ ДЛЯ ЗАВДАННЯ 2
# ============================================================

"""
class Character:
    ...

    def __gt__(self, other):
        if isinstance(other, Character):
            self_power = self.strength + self.weapon.damage
            other_power = other.strength + other.weapon.damage
            return self_power > other_power

        raise TypeError("Character can be compared only with another Character")
"""

# ============================================================
# 8. КОРОТКИЙ ПІДСУМОК
# ============================================================

"""
Що важливо запам'ятати:

1. Magic-методи дозволяють змінювати поведінку стандартних операторів.

2. Перевантаження операторів не означає створення нових операторів.
   Ми лише змінюємо поведінку вже існуючих операторів:
   +, -, *, ==, <, >, len(), in тощо.

3. Перевантаження має бути логічним.
   Наприклад:
   - weapon1 + weapon2 — покращення зброї;
   - hero - enemy — атака;
   - hero + 20 — лікування.

4. Не треба зловживати перевантаженням операторів.
   Код має залишатися зрозумілим.

5. RPG — зручна тема для пояснення ООП,
   бо в ній є багато природних об'єктів:
   персонажі, зброя, броня, інвентар, бій, рівні, навички.
"""
