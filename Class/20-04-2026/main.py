from typing import Optional, Union, Callable, Any

def sum_only_ints(items: list[Any]) -> int:
    return sum(item for item in items if type(item) is int)

def parse_score(value: str) -> Optional[int]:
    try:
        return int(value)
    except (ValueError, TypeError):
        return None

def get_top_student(students: list[dict[str, Union[str, int, float]]]) -> Optional[str]:
    if not students:
        return None
    top_student = max(students, key=lambda s: s.get("score", 0))
    return str(top_student["name"])

def find_user_by_id(users: list[dict[str, Any]], user_id: int) -> Optional[dict[str, Any]]:
    for user in users:
        if user.get("id") == user_id:
            return user
    return None

def normalize(data: Union[float, int, list[Union[int, float]]]) -> Union[float, list[float]]:
    if isinstance(data, (int, float)):
        return float(data)
    return [float(x) for x in data]

def greet_user(name: str, prefix: Optional[str] = None) -> str:
    if prefix:
        return f"{prefix} {name}"
    return name

product: dict[str, Union[str, float, bool, list[str]]] = {
    "name": "Смартфон",
    "price": 15000.50,
    "in_stock": True,
    "tags": ["tech", "sale"]
}

def format_product(p: dict[str, Any]) -> str:
    return f"Товар: {p['name']}, Ціна: {p['price']}, В наявності: {p['in_stock']}"

def extract_strings(items: list[Any]) -> list[str]:
    return [item for item in items if isinstance(item, str)]

def is_valid_student(data: dict[str, Any]) -> bool:
    is_name_ok = isinstance(data.get("name"), str)
    is_age_ok = isinstance(data.get("age"), int)
    is_grade_ok = isinstance(data.get("grade"), (int, float))
    return is_name_ok and is_age_ok and is_grade_ok

def get_min_max(numbers: list[Union[int, float]]) -> Optional[tuple[Union[int, float], Union[int, float]]]:
    if not numbers:
        return None
    return min(numbers), max(numbers)

def count_total_scores(data: dict[str, list[int]]) -> dict[str, int]:
    return {name: sum(scores) for name, scores in data.items()}

def to_int(value: Union[int, float, str]) -> Optional[int]:
    try:
        return int(float(value))
    except (ValueError, TypeError):
        return None

config: dict[str, Union[str, int, bool, list[str]]] = {
    "host": "localhost",
    "port": 8080,
    "debug": True,
    "allowed_users": ["admin", "user1"]
}

def print_config(cfg: dict[str, Any]) -> None:
    for key, val in cfg.items():
        print(f"{key}: {val}")

def apply_operation(a: float, b: float, operation: Callable[[float, float], float]) -> float:
    return operation(a, b)

def sort_users(users: list[dict[str, Any]], key_name: str) -> list[dict[str, Any]]:
    try:
        return sorted(users, key=lambda x: x[key_name])
    except KeyError:
        return users

def print_report(data: str) -> None:
    print(f"REPORT: {data}")

def unique_words(words: list[str]) -> set[str]:
    return set(words)

def char_count(text: str) -> dict[str, int]:
    result: dict[str, int] = {}
    for char in text:
        result[char] = result.get(char, 0) + 1
    return result

def repeat_value(value: Union[str, int], times: int) -> list[Union[str, int]]:
    return [value] * times

def analyze_grades(grades: list[float]) -> Optional[dict[str, float]]:
    if not grades:
        return None
    return {
        "min": min(grades),
        "max": max(grades),
        "average": sum(grades) / len(grades)
    }

def get_order_total(order: dict[str, Any]) -> float:
    items = order.get("items", [])
    total = 0.0
    for item in items:
        total += item.get("price", 0.0)
    return total

def safe_divide(a: Union[int, float], b: Union[int, float]) -> Optional[float]:
    return a / b if b != 0 else None

def find_first_string(items: list[Any]) -> Optional[str]:
    for item in items:
        if isinstance(item, str):
            return item
    return None

def transform_list(items: list[int], transformer: Callable[[int], int]) -> list[int]:
    return [transformer(x) for x in items]

def validate_settings(settings: dict[str, Any]) -> bool:
    checks = [
        isinstance(settings.get("theme"), str),
        isinstance(settings.get("font_size"), int),
        isinstance(settings.get("notifications"), bool)
    ]
    return all(checks)

def merge_tags(tags1: list[str], tags2: list[str]) -> list[str]:
    return sorted(list(set(tags1 + tags2)))

def filter_by_age(users: list[dict[str, Any]], min_age: int) -> list[dict[str, Any]]:
    return [u for u in users if u.get("age", 0) >= min_age]

def get_average_price(products: list[dict[str, Any]]) -> Optional[float]:
    if not products:
        return None
    prices = [p["price"] for p in products if "price" in p]
    return sum(prices) / len(prices) if prices else None

def group_by_first_letter(words: list[str]) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for word in words:
        if not word: continue
        letter = word[0].upper()
        if letter not in result:
            result[letter] = []
        result[letter].append(word)
    return result

def apply_discount(price: float, discount: Optional[float]) -> float:
    if discount is None:
        return price
    return price * (1 - discount / 100)




def get_user_data() -> tuple[str, int, bool]:
    name = "Олександр"
    age = 25
    is_active = True
    return name, age, is_active

# Приклад використання:
# user = get_user_data()
# print(user)  # Результат: ('Олександр', 25, True)
