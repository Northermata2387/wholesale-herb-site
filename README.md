<h2>Sun Rise Herbs</h2>
 
Sun Rise Herbs is an eCommerce website made for the prupose of selling bulk herbs for direct to customer (DTC) or wholesale (B2B). Python files were created to seed data from JSON and CSV files into a PostgreSQL database. Flask, SQL-alchemy, and Jinja were used to bring this data to the front end for user interaction and sale.

![Sun Rise Herbs Home image](/static/images/readme-images/01-home-page.JPG "Sun Rise Herbs Home image")

<h2>Technologies:</h2>
Flask | Jinja | Python | SQL-alchemy | PostgreSQL
 
<h2>How to locally run Sun Rise Herbs:</h2>
 
Sun Rise Herbs is not deployed at this time. Please see the instructions below to run the application locally on your machine.
 
<ul>
  <li>Clone project to desired folder</li>
  <li>Setup
    <ul>
      <li>Open project folder</li>
      <li>Virtual Enviroment 
        <ul>- In terminal RUN...</ul>
        <ul>- python -m venv venv</ul>
        <ul>- source venv/Scripts/activate</ul>
        <ul>- pip install -r requirements.txt</ul>
      </li>
      <li>PostgreSQL_URI
        <ul>- Note: setup requires PostgeSQL to be installed on localhost</ul>
        <ul>- Create a config.sh file at root</ul>
        <ul>- Add the code below to the config.sh</ul>
        <ul>- export POSTGRES_URI="postgresql://username:password@localhost:5432/rising-sun-herbs"</ul>
        <ul>- Add your username and password for PostgeSQL</ul>
        <ul>- In terminal RUN... </ul>
        <ul>- source config.sh</ul>
      </li>
      <li>In terminal RUN...
        <ul>- python seed_database.py</ul></li>
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

Use the navagation bar at the top to view alternate pages and enjoy the options on the home page.

![Sun Rise Herbs Home image](/static/images/readme-images/01-home-page.JPG "Sun Rise Herbs Home image")

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
