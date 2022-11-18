from model import Option, connect_to_db


def create_product_option(product_id, size, unit, price):

    return Option(
        product_id=product_id,
        size=size,
        unit=unit,
        price=price
    )


if __name__ == '__main__':
    from server import app
    connect_to_db(app)