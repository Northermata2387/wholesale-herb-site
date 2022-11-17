import os

import model
import server

import json
import csv

import crud

os.system("dropdb rising-sun-herbs")
os.system("createdb rising-sun-herbs")


model.connect_to_db(server.app)


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

            db_product = crud.create_product(name, part, grade, botanical_name, origin, desc, sku, image)
            products_in_db.append(db_product)

    model.db.session.add_all(products_in_db)
    model.db.session.commit()
    
    
    users_in_db = []
    
    with open("data/users.csv", "r") as users_csv:
        user_data = csv.DictReader(users_csv)
        
        for user in user_data:
            email, password, first_name, last_name= (
                user["email"],
                user["password"],
                user["first_name"],
                user["last_name"]
            )

            db_user = crud.create_user(email, password, first_name, last_name)
            users_in_db.append(db_user)
    
    model.db.session.add_all(users_in_db)
    model.db.session.commit()