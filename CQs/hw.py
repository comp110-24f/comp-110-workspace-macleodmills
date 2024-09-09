def get_tax(price: int, tax_rate: float) -> float:
    return price * tax_rate


def total_cost(cost: int, tax: float) -> float:
    return cost + get_tax(price=cost, tax_rate=tax)


print(total_cost(cost=100, tax=0.07))
