from model import Address


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