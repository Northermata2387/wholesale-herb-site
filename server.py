from flask import Flask, render_template, request, flash, session, redirect

from model import connect_to_db, db
import crud



app = Flask(__name__)
app.secret_key = "secret_key"


@app.errorhandler(404)
def error_404(e):
    return render_template("404.html")


@app.route("/products")
def all_products():

    products = crud.get_products()

    return render_template("all_products.html", products=products)


@app.route("/cart")
def cart():
    
    order_total = 0
    cart_products = []
    
    cart = session.get("cart", {})
    
    for product_id, quantity in cart.items():
        product = crud.get_product_by_id(product_id)

        total_cost = quantity * product.price
        order_total += total_cost

        product.quantity = quantity
        product.total_cost = total_cost

        cart_products.append(product)
    
    return render_template("cart.html", cart_products=cart_products, order_total=order_total)


@app.route("/add_to_cart/<product_id>")
def add_to_cart(product_id):
    
    if 'cart' not in session:
        session['cart'] = {}
    cart = session['cart']
    
    cart[product_id] = cart.get(product_id, 0) + 1
    session.modified = True
    flash(f"product {product_id} successfully added to cart.")
    print(cart)

    return redirect("/cart")


@app.route("/empty-cart-item")
def remove_cart_product(product_id):
    
    # crud.delete_cart_item(product_id)
    # flash(f"Item has been removed.")
    
    session["cart"].pop(product_id)

    return redirect("/cart")


@app.route("/")
def homepage():
    
    return render_template("homepage.html")


@app.route("/products/<product_id>")
def show_product(product_id):

    product = crud.get_product_by_id(product_id)

    return render_template("individual_product.html", product=product)


@app.route("/register")
def register():
    
    return render_template("register.html")


@app.route("/register", methods=["POST"])
def register_user():

    email = request.form.get("email")
    password = request.form.get("password")
    
    user = crud.get_user_by_email(email)
    if user:
        flash("Your account already exists. Please Sing In")
    else:
        user = crud.create_user_form(email, password)
        db.session.add(user)
        db.session.commit()
        flash("Account created! Please Sign In")

    return redirect("/signin")


@app.route("/signin")
def signin():
    
    return render_template("signin.html")


@app.route("/signin", methods=["POST"])
def process_signin():

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    
    if not user or user.password != password:
        flash("Email or password was slightly off, please try again")
        
        return redirect("/signin")
    else:
        session["user_email"] = user.email
        flash(f"Welcome {user.email}!")
        
        return redirect("/products")


@app.route("/signout")
def signout():
    
    del session["user_email"]
    flash("You have Signed Out")
    return redirect("/")


@app.route("/profile")
def show_profile():
    
    
    return render_template("user_profile.html")


# @app.route("/profile", methods=["POST"])
# def show_profile():
    
    
#     return render_template("user_profile.html")


@app.route("/update_rating", methods=["POST"])
def update_rating():
    rating_id = request.json["rating_id"]
    updated_score = request.json["updated_score"]
    crud.update_rating(rating_id, updated_score)
    db.session.commit()

    return "Updated Rating"


@app.route("/products/<product_id>/ratings", methods=["POST"])
def create_rating(product_id):

    logged_in_email = session.get("user_email")
    rating_score = request.form.get("rating")

    if logged_in_email is None:
        flash("You must log in to rate a product.")
    elif not rating_score:
        flash("Oops! You didn't select a score for your rating.")
    else:
        user = crud.get_user_by_email(logged_in_email)
        product = crud.get_product_by_id(product_id)

        rating = crud.create_rating(user, product, int(rating_score))
        db.session.add(rating)
        db.session.commit()

        flash(f"You rated this product {rating_score} out of 5")

    return redirect(f"/products/{product_id}")


@app.route("/update_review", methods=["POST"])
def update_review():
    review_id = request.json["review_id"]
    updated_comment = request.json["updated_comment"]
    crud.update_review(review_id, updated_comment)
    db.session.commit()

    return "Updated Review"


@app.route("/products/<product_id>/reviews", methods=["POST"])
def create_review(product_id):

    logged_in_email = session.get("user_email")
    review_comment = request.form.get("review")

    if logged_in_email is None:
        flash("You must log in to review a product.")
    elif not review_comment:
        flash("Oops! You didn't enter a comment for your review.")
    else:
        user = crud.get_user_by_email(logged_in_email)
        product = crud.get_product_by_id(product_id)

        review = crud.create_review(user, product, int(review_comment))
        db.session.add(review)
        db.session.commit()

        flash(f"Thank you for your review!")

    return redirect(f"/products/{product_id}")


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)