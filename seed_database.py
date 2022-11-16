import os
from random import choice, randint

import json
import crud
import model
import server

os.system("dropdb rising-sun-herbs")
os.system("createdb rising-sun-herbs")


model.connect_to_db(server.app)


with server.app.app_context():
    model.db.create_all()
    
    with open("data/products.json") as f:
        product_data = json.loads(f.read())
        
    products_in_db = []
    for product in product_data:
        name, botanical_name, origin, desc, image = (
            product["name"],
            product["botanical_name"],
            product["origin"],
            product["desc"],
            product["image"],
        )

        db_product = crud.create_product(name, botanical_name, origin, desc, image)
        products_in_db.append(db_product)

    model.db.session.add_all(products_in_db)
    model.db.session.commit()
    
    user_count = 10

    for n in range(user_count):
        email = f"user{n}@test.com"
        password = "test"

        user = crud.create_user(email, password)
        model.db.session.add(user)

        for _ in range(10):
            random_product = choice(products_in_db)
            score = randint(1, 5)

            rating = crud.create_rating(user, random_product, score)
            model.db.session.add(rating)

    model.db.session.commit()