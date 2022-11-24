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
    flash(f"Herb added to cart!")

    return redirect("/products")


@app.route("/empty-cart")
def empty_cart():
    
    session["cart"] = {}
    flash("Your Cart is empty, please choose a product...")

    return redirect("/products")



@app.route("/")
def homepage():
    
    products = crud.get_products()
    
    return render_template("homepage.html", products=products)


@app.route("/products/<product_id>")
def show_product(product_id):

    product = crud.get_product_by_id(product_id)
    
    ratings = crud.get_rating_by_product(product_id)
    total = 0
    for rating in ratings:
        total = total + rating.score
    if len(ratings) != 0:
        avg = total/len(ratings)
    else:
        avg = -1
        
    reviews = crud.get_review_by_product(product_id)

    return render_template("individual_product.html", product=product, avg=avg, reviews=reviews)


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
        flash(f"Welcome {user.first_name}!")
        
        return redirect("/products")


@app.route("/signout")
def signout():
    
    del session["user_email"]
    flash("You have Signed Out")
    return redirect("/")


if __name__ == "__main__":
    connect_to_db(app, echo=False)
    app.run(host="0.0.0.0", debug=True)