def calculate_discount_price(price: float, discount: int) -> float:
    return price * (1 - discount / 100)
print(calculate_discount_price(1000, 10))


def filter_adults(ages: list[int]) -> list[int]:
    return [age for age in ages if age >= 18]
print(filter_adults([15, 18, 21, 10, 30]))



def get_user_data() -> tuple[str, int, bool]:
    name = "Олександр"
    age = 17
    is_active = True
    return name, age, is_active

user = get_user_data()
print(user)


