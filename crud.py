from model import User, Address, Product, Option, Rating, Review, connect_to_db



def create_user(email, password):

    user = User(email=email, password=password)

    return user

def get_users():

    return User.query.all()

def get_user_by_id(user_id):

    return User.query.get(user_id)

def get_user_by_email(email):

    return User.query.filter(User.email == email).first()



def create_address(street, city, zip_code, state):

    address = Address(street=street, city=city, zip_code=zip_code, state=state)

    return address

def get_address():

    return Address.query.all()

def get_address_by_id(address_id):

    return User.query.get(address_id)



def get_users():

    return User.query.all()

def get_user_by_id(user_id):

    return User.query.get(user_id)

def get_user_by_email(email):

    return User.query.filter(User.email == email).first()



def create_product(title, botanical_name, origin, description, image):

    product = Product(
        title=title,
        botanical_name=botanical_name,
        origin=origin,
        description=description,
        image=image,
    )

    return product

def get_products():

    return Product.query.all()

def get_product_by_id(product_id):

    return Product.query.get(product_id)



def create_option(size, price):

    option = Option(size=size, price=price)

    return option

def get_option():

    return Option.query.all()

def get_option_by_id(option_id):

    return Option.query.get(option_id)



def create_rating(user, product, score):

    rating = Rating(user=user, product=product, score=score)

    return rating

def update_rating(rating_id, new_score):
    rating = Rating.query.get(rating_id)
    rating.score = new_score


if __name__ == '__main__':
    from server import app
    connect_to_db(app)