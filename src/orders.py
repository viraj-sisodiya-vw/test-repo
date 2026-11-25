def calculate_total(items):
    subtotal = sum(
        item["price"] * item["quantity"]
        for item in items
    )
    return round(subtotal, 2)
