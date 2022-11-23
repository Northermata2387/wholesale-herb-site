from os import environ
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(255), unique = True, nullable = False)
    password = db.Column(db.Text, nullable = False)
    first_name = db.Column(db.String(24), nullable = True)
    last_name = db.Column(db.String(48), nullable = True)
    image = db.Column(db.String(255), nullable = True)

    def __repr__(self):
        return f"<User user_id={self.user_id} email={self.email} first_name={self.first_name} last_name ={self.last_name} image={self.image}>"
    
    
class Address(db.Model):

    __tablename__ = "addresses"
    
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    street = db.Column(db.String(72), unique = True, nullable = True)
    city = db.Column(db.String(72), nullable = True)
    state = db.Column(db.String(2), nullable = True)
    postal_code = db.Column(db.String(24), nullable = True)
    country = db.Column(db.String(24), nullable = True)
    telephone = db.Column(db.String(24), nullable = True)
    
    user = db.relationship("User", backref="addresses")

    def __init__(self, user_id, street, city, state, postal_code, country, telephone):
        self.user_id=user_id
        self.street = street
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.country = country
        self.telephone = telephone
        
    def __repr__(self):
        return f"<Address address_id={self.address_id} street={self.street} city={self.city} state={self.state} postal_code={self.postal_code} country={self.country} telephone={self.telephone}>"


class Product(db.Model):

    __tablename__ = "products"
    
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(255), nullable = False)
    part = db.Column(db.String(255))
    grade = db.Column(db.String(255))
    size = db.Column(db.Integer, nullable = False)
    unit = db.Column(db.String(24), nullable = False)
    price = db.Column(db.Float, nullable = False)
    botanical_name = db.Column(db.String(255), nullable = False)
    origin = db.Column(db.String(255), nullable = False)
    desc = db.Column(db.Text, nullable = False)
    sku = db.Column(db.String(255), unique = True, nullable = False)
    image = db.Column(db.String(255), nullable = False)
    
    def __init__(self, name, part, grade, size, unit, price, botanical_name, origin, desc, sku, image):
        self.name = name
        self.part = part
        self.grade = grade
        self.size = size
        self.unit = unit
        self.price = price
        self.botanical_name = botanical_name
        self.origin = origin
        self.desc = desc
        self.sku = sku
        self.image = image
        
    def __repr__(self):
        return f"<Product product_id={self.product_id} name={self.name} part={self.part} grade={self.grade} size={self.size} unit={self.unit} price={self.price} botanical_name={self.botanical_name} origin={self.origin} desc={self.desc} sku={self.sku} image={self.image}>"



class Rating(db.Model):

    __tablename__ = "ratings"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"))
    score = db.Column(db.Integer)
    
    user = db.relationship("User", backref="ratings")
    product = db.relationship("Product", backref="ratings")
    
    def __init__(self, user_id, product_id, score):
        self.user_id= user_id,
        self.product_id =product_id,
        self.score = score
    
    def __repr__(self):
        return f"<Rating rating_id={self.rating_id} score={self.score}>"


class Review(db.Model):

    __tablename__ = "reviews"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    comment = db.Column(db.String(255))
    
    user = db.relationship("User", backref="reviews")
    product = db.relationship("Product", backref="reviews")

    def __init__(self, product_id, user_id, comment):
        self.product_id = product_id
        self.user_id =user_id
        self.comment = comment
        
    def __repr__(self):
        return f"<Review review_id ={self.review_id } comment={self.comment}>"
    

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