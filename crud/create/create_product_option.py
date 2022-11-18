from model import Option


def create_product_option(product_id, size, unit, price):

    return Option(
        product_id=product_id,
        size=size,
        unit=unit,
        price=price
    )