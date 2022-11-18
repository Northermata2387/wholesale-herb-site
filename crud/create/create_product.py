from model import Product


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