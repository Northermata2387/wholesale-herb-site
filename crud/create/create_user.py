from model import User


def create_user(email, password, first_name, last_name, image):

    return User(
        email=email, 
        password=password,
        first_name=first_name,
        last_name=last_name,
        image=image
    )
