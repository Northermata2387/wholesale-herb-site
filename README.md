<h2>Sun Rise Herbs</h2>
 
Sun Rise Herbs is an eCommerce website made for the prupose of selling bulk herbs for direct to customer (DTC) or wholesale (B2B). Python files were created to seed data from JSON and CSV files into a PostgreSQL database. Flask, SQL-alchemy, and Jinja were used to bring this data to the front end for user interaction and sale.

![Sun Rise Herbs Home image](/static/images/readme-images/01-homepage.JPG "Sun Rise Herbs Home image")

<h2>Technologies:</h2>
Flask | Jinja | Python | SQL-alchemy | PostgreSQL
 
<h2>How to locally run Sun Rise Herbs:</h2>
 
Sun Rise Herbs is not deployed at this time. Please see the instructions below to run the application locally on your machine.
 
<ul>
  <li>Clone project to desired folder</li>
  <li>Setup
    <ul>
      <li>Open project folder</li>
      <li>In terminal RUN...</li>
      <li>python -m venv venv</li>
      <li>source venv/Scripts/activate</li>
      <li>pip install -r requirements.txt</li>
      <li></li>
      <li>Create a config.sh file at root</li>
      <li>Add the code below to the config.sh file with your username and password for PostgeSQL</li>
      <li>Note: setup requires PostgeSQL to be installed</li>
      <li>export POSTGRES_URI="postgresql://username:password@localhost:5432/rising-sun-herbs"</li>
      <li>In terminal RUN...</li>
      <li>source config.sh</li>
      <li></li>
      <li>python seed_database.py</li>
    </ul>
</li>
<li>Run Server
    <ul>
      <li>In terminal RUN..</li>
      <li>python server.py</li>
    </ul>
</li>
</ul>
 
<h2>How to use Sun Rise Herbs:</h2>

Use the Home navagation bar to view alternate pages and enjoy the options on the home page.

![Sun Rise Herbs Home image](/static/images/readme-images/01-homepage.JPG "Sun Rise Herbs Home image")

Go to the register page and create your own account.

![Sun Rise Herbs register page](/static/images/readme-images/02-register.JPG "Sun Rise Herbs register page")

After your registered, sign in.

![Sun Rise Herbs sign in page](/static/images/readme-images/03-signin.JPG "Sun Rise Herbs sign in page")

Click on Bulk Herbs page to view and add to your cart

![Sun Rise Herbs all-products page](/static/images/readme-images/04-all-products.JPG "Sun Rise Herbs all-products page")

Go to an individual product page to see additional details, average rating and possibly reviews.

![Sun Rise Herbs individual product page](/static/images/readme-images/05-indv-product.JPG "Sun Rise Herbs individual product page")

Head to the Cart link and see the chosen product and break down of cost.

![Sun Rise Herbs cart page](/static/images/readme-images/06-cart.JPG "Sun Rise Herbs cart page")

Learn more about the developer:<br/>
Mark Nakayama is a software engineer in Denver, CO<br/>
https://www.linkedin.com/in/mark-nakayama-16b004116/
