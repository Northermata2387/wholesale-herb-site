from os import environ
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_email = db.Column(db.String(255), unique = True, nullable = False)
    user_password = db.Column(db.text, nullable = False)

    def __repr__(self):
        return f"<User user_id={self.user_id} email={self.user_email}>"
    
    
class Address(db.Model):

    __tablename__ = "addresses"
    
    address_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    address_street = db.Column(db.String(255), unique = True, nullable = False)
    address_city = db.Column(db.String(255), nullable = False)
    address_zip_code = db.Column(db.Integer(5), nullable = False)
    address_state = db.Column(db.String(2), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))

    user = db.relationship("User", backref="addresses")

    def __repr__(self):
        return f"<Address address_id={self.address_id} address_street={self.address_street} address_city={self.address_city} address_zip_code={self.address_zip_code} address_state={self.address_state}>"


class Product(db.Model):

    __tablename__ = "products"
    
    product_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    product_title = db.Column(db.String(255), unique = True, nullable = False)
    product_botanical_name = db.Column(db.String(255), unique = True, nullable = False)
    product_origin = db.Column(db.String(255), nullable = False)
    product_description = db.Column(db.String(255), nullable = False)
    product_image = db.Column(db.String(255), nullable = False)
    
    def __repr__(self):
        return f"<Product product_id={self.product_id} product_title={self.product_title} product_botanical_name={self.product_botanical_name} product_origin={self.product_origin} product_description={self.product_description} title={self.product_image} title={self.product_image}>"


class Option(db.Model):

    __tablename__ = "options"
    
    option_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    option_size = db.Column(db.Integer, nullable = False)
    option_price = db.Column(db.Float, nullable = False)
    product_id = db.Column(db.Integer, db.ForeignKey("products.product_id"))
    
    product= db.relationship("Product", backref="options")
    
    def __repr__(self):
        return f"<Option option_id={self.option_id} option_size={self.option_size} option_price={self.option_price}>"
    

class Rating(db.Model):

    __tablename__ = "ratings"

    rating_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    rating_stars = db.Column(db.Integer)
    product_id = db.Column(db.Integer, db.ForeignKey("products.product_id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    
    product= db.relationship("Product", backref="ratings")
    user = db.relationship("User", backref="ratings")
    
    def __repr__(self):
        return f"<Rating rating_id={self.rating_id} rating_stars={self.rating_stars}>"


class Review(db.Model):

    __tablename__ = "reviews"

    review_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    review_comment = db.Column(db.String(255))
    product_id = db.Column(db.Integer, db.ForeignKey("products.product_id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))

    product= db.relationship("Product", backref="ratings")
    user = db.relationship("User", backref="ratings")

    def __repr__(self):
        return f"<Review review_id ={self.review_id } review_comment={self.review_comment}>"
    
    
class Order(db.Model):

    __tablename__ = "orders"

    orders_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("products.product_id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    
    product= db.relationship("Product", backref="ratings")
    user = db.relationship("User", backref="ratings")

    def __repr__(self):
        return f"Order orders_id={self.orders_id}>"



def connect_to_db(flask_app, db_uri=environ["POSTGRES_URI"], echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")
    

if __name__ == "__main__":
    from server import app
    connect_to_db(app, echo=False)