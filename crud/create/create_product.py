from model import Product, connect_to_db


def create_product(name, part, grade, botanical_name, origin, desc, sku, image):

    return Product(
        name=name,
        part=part,
        grade=grade,
        botanical_name=botanical_name,
        origin=origin,
        desc=desc,
        sku=sku,
        image=image
    )


if __name__ == '__main__':
    from server import app
    connect_to_db(app)