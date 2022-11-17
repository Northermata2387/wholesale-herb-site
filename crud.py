from model import User, Address, Product, Option, Rating, Review, connect_to_db



def create_user(email, password, first_name, last_name):

    return User(
        email=email, 
        password=password,
        first_name=first_name,
        last_name=last_name
    )

def get_users():

    return User.query.all()

def get_user_by_id(user_id):

    return User.query.get(user_id)

def get_user_by_email(email):

    return User.query.filter(User.email == email).first()



def create_address(street, city, state, postal_code, country, telephone):

    return Address(
        street=street, 
        city=city, 
        state=state,
        postal_code=postal_code,
        country=country,
        telephone=telephone
    )

def get_address():

    return Address.query.all()

def get_address_by_id(address_id):

    return User.query.get(address_id)



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

def get_products():

    return Product.query.all()

def get_product_by_id(product_id):

    return Product.query.get(product_id)



def create_option(size, price):

    return Option(
        size=size, 
        price=price
    )

def get_option():

    return Option.query.all()

def get_option_by_id(option_id):

    return Option.query.get(option_id)



def create_rating(user, product, score):

    return Rating(
        user=user, 
        product=product, 
        score=score
    )

def update_rating(rating_id, new_score):
    rating = Rating.query.get(rating_id)
    rating.score = new_score
    
    
    
def create_review(user, product, comment):

    return Review(
        user=user, 
        product=product, 
        comment=comment
    )

def update_review(review_id, new_comment):
    review = Review.query.get(review_id)
    review.comment = new_comment



if __name__ == '__main__':
    from server import app
    connect_to_db(app)