import os
from random import choice, randint

import model
import server

import json
import csv

import crud

os.system("dropdb rising-sun-herbs")
os.system("createdb rising-sun-herbs")


model.connect_to_db(server.app, echo=False)


with server.app.app_context():
    model.db.create_all()
    
    
    products_in_db = []
    
    with open("data/products.json") as products_json:
        product_data = json.loads(products_json.read())
        
        for product in product_data:
            name, part, grade, size, unit, price, botanical_name, origin, desc, sku, image = (
                product["name"],
                product["part"],
                product["grade"],
                product["size"],
                product["unit"],
                product["price"],
                product["botanical_name"],
                product["origin"],
                product["desc"],
                product["sku"],
                product["image"]
            )

            db_product = crud.create_product(name, part, grade, size, unit, price, botanical_name, origin, desc, sku, image)
            products_in_db.append(db_product)

    model.db.session.add_all(products_in_db)
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

            db_user = crud.create_user(email, password, first_name, last_name, image)
            users_in_db.append(db_user)
    
    model.db.session.add_all(users_in_db)
    model.db.session.commit()


    reviews_in_db = []
    
    with open("data/reviews.json") as reviews_json:
        review_data = json.loads(reviews_json.read())
        
        for review in review_data:
            product_id, user_id, date, title, comment = (
                review["product_id"],
                review["user_id"],
                review["date"],
                review["title"],
                review["comment"]
            )

            db_review = crud.create_review(product_id, user_id, date, title, comment)
            reviews_in_db.append(db_review)

    model.db.session.add_all(reviews_in_db)
    model.db.session.commit()
    
    
    rating_count = 60

    for _ in range(rating_count):
        user_id = choice(users_in_db).id
        product_id = choice(products_in_db).id
        score = randint(1, 5)

        rating = crud.create_rating(user_id, product_id, score)
        model.db.session.add(rating)

    model.db.session.commit()