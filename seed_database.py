import os
from random import choice, randint

import model
import server
from crud import create

import json
import csv


os.system("dropdb rising-sun-herbs")
os.system("createdb rising-sun-herbs")

model.connect_to_db(server.app, echo=False)


with server.app.app_context():
    model.db.create_all()
    
    
    products_in_db = []
    
    with open("data/products.json") as products_json:
        product_data = json.loads(products_json.read())
        
        for product in product_data:
            name, part, grade, botanical_name, origin, desc, sku, image = (
                product["name"],
                product["part"],
                product["grade"],
                product["botanical_name"],
                product["origin"],
                product["desc"],
                product["sku"],
                product["image"]
            )

            db_product = create.create_product(name, part, grade, botanical_name, origin, desc, sku, image)
            products_in_db.append(db_product)

    model.db.session.add_all(products_in_db)
    model.db.session.commit()
    
    
    product_options_in_db = []
    
    with open("data/product_options.json") as product_options_json:
        product_option_data = json.loads(product_options_json.read())
        
        for product_option in product_option_data:
            product_id, size, unit, price = (
                product_option["product_id"],
                product_option["size"],
                product_option["unit"],
                product_option["price"]
            )

            db_product_option = create.create_product_option(product_id, size, unit, price)
            product_options_in_db.append(db_product_option)

    model.db.session.add_all(product_options_in_db)
    model.db.session.commit()
    
    
    users_in_db = []
    
    with open("data/users.csv", "r") as users_csv:
        user_data = csv.DictReader(users_csv)
        
        for user in user_data:
            email, password, first_name, last_name, image= (
                user["email"],
                user["password"],
                user["first_name"],
                user["last_name"],
                user["image"]
            )

            db_user = create.create_user(email, password, first_name, last_name, image)
            users_in_db.append(db_user)
    
    model.db.session.add_all(users_in_db)
    model.db.session.commit()
    
    
    addresses_in_db = []
    
    with open("data/address.csv", "r") as address_csv:
        address_data = csv.DictReader(address_csv)
        
        for address in address_data:
            user_id, street, city, state, postal_code, country, telephone= (
                address["user_id"],
                address["street"],
                address["city"],
                address["state"],
                address["postal_code"],
                address["country"],
                address["telephone"]
            )

            db_address = create.create_address(user_id, street, city, state, postal_code, country, telephone)
            addresses_in_db.append(db_address)
    
    model.db.session.add_all(addresses_in_db)
    model.db.session.commit()


    reviews_in_db = []
    
    with open("data/reviews.json") as reviews_json:
        review_data = json.loads(reviews_json.read())
        
        for review in review_data:
            product_id, user_id, comment = (
                review["product_id"],
                review["user_id"],
                review["comment"]
            )

            db_review = create.create_review(product_id, user_id, comment)
            reviews_in_db.append(db_review)

    model.db.session.add_all(reviews_in_db)
    model.db.session.commit()
    
    
    rating_count = 60

    for _ in range(rating_count):
        user_id = choice(users_in_db).id
        product_id = choice(products_in_db).id
        score = randint(1, 5)

        rating = create.create_rating(user_id, product_id, score)
        model.db.session.add(rating)

    model.db.session.commit()