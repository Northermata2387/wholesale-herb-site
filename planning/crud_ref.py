from model import User, Address, Product, Option, Rating, Review, connect_to_db


def get_users():

    return User.query.all()

def get_user_by_id(user_id):

    return User.query.get(user_id)

def get_user_by_email(email):

    return User.query.filter(User.email == email).first()


def get_address():

    return Address.query.all()

def get_address_by_id(address_id):

    return User.query.get(address_id)


def get_products():

    return Product.query.all()

def get_product_by_id(product_id):

    return Product.query.get(product_id)


def get_product_option():

    return Option.query.all()

def get_product_option_by_id(option_id):

    return Option.query.get(option_id)



def update_rating(rating_id, new_score):
    rating = Rating.query.get(rating_id)
    rating.score = new_score
    
def update_review(review_id, new_comment):
    review = Review.query.get(review_id)
    review.comment = new_comment


if __name__ == '__main__':
    from server import app
    connect_to_db(app)