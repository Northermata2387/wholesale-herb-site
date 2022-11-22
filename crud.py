from model import User, Address, Product, Rating, Review, connect_to_db



def create_user(email, password, first_name, last_name, image):

    return User(
        email=email, 
        password=password,
        first_name=first_name,
        last_name=last_name,
        image=image
    )
    
def get_user_by_email(email):

    return User.query.filter(User.email == email).first()

def create_user_form(email, password):

    return User(
        email=email, 
        password=password
    )

def get_user_by_id(user_id):

    return User.query.get(user_id)


def create_address(user_id, street, city, state, postal_code, country, telephone):

    return Address(
        user_id=user_id,
        street=street, 
        city=city, 
        state=state,
        postal_code=postal_code,
        country=country,
        telephone=telephone
    )

# def get_address():

#     return Address.query.all()

# def get_address_by_id(address_id):

#     return User.query.get(address_id)



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




def create_rating(user_id, product_id, score):

    return Rating(
        user_id=user_id, 
        product_id=product_id, 
        score=score
    )

def update_rating(rating_id, new_score):
    rating = Rating.query.get(rating_id)
    rating.score = new_score
    
    
    
def create_review(product_id, user_id, comment):

    return Review(
        product_id=product_id, 
        user_id=user_id, 
        comment=comment
    )

def update_review(review_id, new_comment):
    review = Review.query.get(review_id)
    review.comment = new_comment



if __name__ == '__main__':
    from server import app
    connect_to_db(app)