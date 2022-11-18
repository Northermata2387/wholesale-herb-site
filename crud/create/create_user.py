from model import User, connect_to_db


def create_user(email, password, first_name, last_name, image):

    return User(
        email=email, 
        password=password,
        first_name=first_name,
        last_name=last_name,
        image=image
    )


if __name__ == '__main__':
    from server import app
    connect_to_db(app)