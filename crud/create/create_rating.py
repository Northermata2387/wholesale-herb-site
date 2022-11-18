from model import Rating, connect_to_db


def create_rating(user_id, product_id, score):

    return Rating(
        user_id=user_id, 
        product_id=product_id, 
        score=score
    )


if __name__ == '__main__':
    from server import app
    connect_to_db(app)