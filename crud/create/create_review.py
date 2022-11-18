from model import Review


def create_review(product_id, user_id, comment):

    return Review(
        product_id=product_id, 
        user_id=user_id, 
        comment=comment
    )