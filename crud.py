from model import db, User, Product, Rating, Review, connect_to_db



def create_user(email, password, first_name, last_name, image):

    return User(
        email=email, 
        password=password,
        first_name=first_name,
        last_name=last_name,
        image=image
    )
def create_user_form(email, password):

    return User(
        email=email, 
        password=password
    )
    
def get_user_by_email(email):

    return User.query.filter(User.email == email).first()



def create_product(name, part, grade, size, unit, price, botanical_name, origin, desc, sku, image):

    return Product(
        name=name,
        part=part,
        grade=grade,
        size=size,
        unit=unit,
        price=price,
        botanical_name=botanical_name,
        origin=origin,
        desc=desc,
        sku=sku,
        image=image
    )

def get_products():

    return Product.query.all()

def get_product_by_id(product_id):

    return Product.query.get(product_id)

def get_product_by_name(product_name):

    return Product.query.get(product_name)


def create_rating(user_id, product_id, score):

    return Rating(
        user_id=user_id, 
        product_id=product_id, 
        score=score
    )
    
def get_rating_by_product(product_id):
    return Rating.query.filter_by(product_id=product_id).all()



def create_review(product_id, user_id, date, title, comment):

    return Review(
        product_id=product_id, 
        user_id=user_id,
        date=date,
        title=title,
        comment=comment
    )

def get_review_by_product(product_id):

    return Review.query.filter_by(product_id=product_id).all()


if __name__ == '__main__':
    from server import app
    connect_to_db(app)