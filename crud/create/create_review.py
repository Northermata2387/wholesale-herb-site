from model import Review, connect_to_db


def create_review(product_id, user_id, comment):

    return Review(
        product_id=product_id, 
        user_id=user_id, 
        comment=comment
    )


if __name__ == '__main__':
    from server import app
    connect_to_db(app)