from model import Rating


def create_rating(user_id, product_id, score):

    return Rating(
        user_id=user_id, 
        product_id=product_id, 
        score=score
    )