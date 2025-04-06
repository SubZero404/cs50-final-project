# CS50 Final Project: E-Commerce Website

#### Video Demo:  https://youtu.be/cELsCu7AL7Q

## Description
This is my final project for Harvard's CS50x course. The project is an **e-commerce website** where users can browse products, add them to a shopping cart, and place orders. The website is built using **Flask** (Python web framework) and **SQLite** (database), with **HTML**, **CSS**, **JavaScript**, and **Node.js** for the front-end. The project demonstrates key concepts learned throughout the course, including web development, user authentication, and working with databases.

The primary goal of this project was to create a simple, functional online store where users can interact with a variety of products, make selections, and process orders. This project provided me with an opportunity to work with Flask to build a full-stack application, focusing on both the front-end and back-end aspects of web development.

## Technologies Used
- **Flask**: A Python web framework for building web applications.
- **SQLite**: A lightweight database used to store product information, user details, and order history.
- **HTML, CSS, JavaScript**: Used for creating the structure, style, and interactivity of the website.
- **Node.js & npm**: Used for managing front-end libraries.
- **Jinja2**: A templating engine for dynamically generating HTML from Python variables.

## Acknowledgements

This project was developed with the assistance of the following tools:

- **ChatGPT** by OpenAI — Used for guidance, explanations, and code suggestions during development and debugging.
- **GitHub Copilot** — Used for code autocompletion and generating boilerplate code efficiently.

These tools supported the learning process and helped streamline development.


### Front-End Libraries Installed via npm
- **Bootstrap**: A popular CSS framework for building responsive and mobile-first websites.
- **Bootstrap-icons**: Provides a set of customizable icons to use in the project.
- **SweetAlert2**: A library for creating beautiful and customizable alert pop-ups.
- **Glide.js**: A lightweight, responsive, and flexible slider library for displaying images or content in a carousel.
- **Summernote**: A WYSIWYG (What You See Is What You Get) editor that allows users to format text and add media content.
- **jQuery**: A fast, small, and feature-rich JavaScript library used for DOM manipulation, event handling, and AJAX requests.

## Features
The website has several key features:
1. **User Registration and Login**:
   - Users can create an account by providing a username, email, and password.
   - The system ensures that usernames and emails are unique and that passwords are securely hashed.
   - Registered users can log in to access their cart and previous orders.
   
2. **Product Listing**:
   - The website displays a list of available products, including product names, images, and prices.
   - Users can view detailed information about each product by clicking on individual items.

3. **Shopping Cart**:
   - Users can add products to their cart, increase or decrease the quantity of items, and remove items.
   - The cart is stored in the user's session, so it persists across pages.

4. **Checkout and Order History**:
   - Users can proceed to checkout, where they review their cart, enter shipping details, and complete the order.
   - After a successful purchase, users can view their order history.

5. **Change Password**:
   - Registered users can change their account password by entering their old password, followed by the new password.
   - Passwords are securely hashed before being stored in the database.

6. **Contact Us**:
   - The website features a "Contact Us" page where users can reach out for support or inquiries. It includes a simple contact form for sending messages.

7. **About Us**:
   - The "About Us" page provides information about the website, including its mission, goals, and background.

8. **Admin Dashboard**:
   - **Product Management**: Admins can add new products, update existing products, or delete products from the website.
   - **Brand Management**: Admins can add, update, or delete brands associated with products.
   - **Category Management**: Admins can create, update, or remove product categories for better organization.
   - The admin dashboard is protected by authentication and only accessible by users with admin privileges.

9. **Responsive Design**:
   - The website is designed to be mobile-friendly, ensuring a seamless shopping experience across various devices.

## File Structure and Explanation

The project consists of the following key files and directories:

### `app.py`
- The main Flask application file. It defines the routes, views, and database interaction logic. It contains the core functionality for user registration, login, viewing products, managing the shopping cart, processing orders, and handling the admin dashboard.

### `templates/`
- This directory contains the HTML files used by the Flask application, rendered using Jinja2 templates.
  - `layout.html`: The base template that includes the header, footer, and common layout elements.
  - `index.html`: The homepage displaying product listings.
  - `login.html`, `register.html`: Templates for user login and registration forms.
  - `cart.html`: The shopping cart page where users can review and modify their cart.
  - `checkout.html`: The checkout page where users can confirm their orders.
  - `change_password.html`: The page for changing a user's password.
  - `contact_us.html`: The page containing the contact form.
  - `about_us.html`: The page providing information about the website.

### `static/`
- This directory contains the static files such as CSS, JavaScript, and images.
  - `style.css`: The main stylesheet for the project.
  - `script.js`: JavaScript for dynamic interactions, like updating the cart quantity.
  - `images/`: Product images and logo files.

### `requirements.txt`
- A list of Python dependencies required to run the project, such as Flask and SQLAlchemy. This file ensures that anyone who wants to run the project can install the necessary libraries using `pip`.

### `database.db`
- The SQLite database used to store user data, product details, and order history. It is a local file and should be kept in the project directory.

### `README.md`
- This file, which documents the project, including the setup instructions, features, and functionality.

### `package.json`
- The Node.js package file that lists all front-end dependencies managed with npm, such as Bootstrap, SweetAlert2, and others.

## Database Seeding
This project uses **Flask-Seeds** to automatically populate the database with initial data for categories, brands, and products. This allows for a quick setup and provides a sample set of data for testing and development.

## Design Decisions
### 1. **Flask Framework**
   - Flask was chosen because of its simplicity and flexibility. It allowed me to build the project without unnecessary complexity, while still providing the tools needed to create a fully functional web application. Flask also made it easy to integrate with SQLite and use Jinja2 for templating.

### 2. **Session-based Cart**
   - I decided to use Flask's session mechanism to store the shopping cart. This allows the cart data to persist across different pages without requiring a login. While the cart is stored in the user session, a logged-in user’s cart will persist even after they log out.

### 3. **SQLite Database**
   - SQLite was chosen for its simplicity and ease of setup. Since this project is small and doesn’t require a heavy-duty database system, SQLite is sufficient for storing user and order information. For larger-scale projects, a more robust database like PostgreSQL or MySQL would be more appropriate.

### 4. **Node.js for Front-End Libraries**
   - Using **npm** to manage front-end libraries was a key decision to ensure scalability and keep the dependencies up-to-date. This approach allows for easy installation and management of popular libraries like Bootstrap, SweetAlert2, Glide.js, Summernote, and jQuery.

### 5. **Mobile-First Design**
   - I opted for a responsive, mobile-first design to ensure that the website looks great on all devices. This is crucial for e-commerce websites, as many users browse and shop from their smartphones.

## Future Improvements
- **Payment Integration**: Add support for integrating a payment gateway like Stripe or PayPal to process real transactions.
- **User Reviews and Ratings**: Implement a system for users to review and rate products.
- **Admin Dashboard Enhancements**: Improve the admin dashboard with features like product search and bulk actions (delete multiple products).

## How to Run the Project Locally

To run this project on your local machine, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/SubZero404/cs50-final-project.git
   cd cs50-final-project

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt

3. Install front-end dependencies with npm:
    ```bash
    npm install

4. create database or migration 
    ```bash
    flask db init
    flask db migrate -m "Initial migration"
    flask db upgrade

5. seed the database with initial data
    ```bash
    python -m website.seed

6. Run the Flask application:
    ```bash
    flask run

7. Open a web browser and go to http://127.0.0.1:5000/ to view the project.


# Project Structure
```
project-root/
│
├── instance/                   # Instance-specific configuration files
├── migrations/                 # Database migration files
├── node_modules/               # Node.js dependencies (if any)
├── venv/                       # Python virtual environment (excluded in .gitignore)
│
├── website/                    # Main application package
│   ├── __pycache__/            # Python bytecode cache
│   ├── static/                 # Static assets
│   │   ├── css/                # CSS stylesheets
│   │   ├── img/                # Image assets
│   │   └── js/                 # JavaScript files
│   │
│   ├── templates/              # HTML templates
│   │   ├── admin/              # Admin-specific templates
│   │   ├── views/              # View-specific templates
│   │   ├── 404.html            # 404 error page
│   │   ├── index.html          # Home page
│   │   ├── login.html          # Login page
│   │   └── register.html       # Registration page
│   │
│   ├── __init__.py             # Package initialization
│   ├── admin.py                # Admin configuration
│   ├── auth.py                 # Authentication logic
│   ├── forms.py                # Form definitions
│   ├── models.py               # Database models
│   ├── seed.py                 # Database seeding
│   └── views.py                # Application views/routes
│
├── .gitignore                  # Specifies untracked files
└── app.py                      # Main application entry point
```


### Key Files Explanation:
- **Configuration**:
  - `.gitignore` - Lists files/folders to exclude from version control
  - `app.py` - Flask application entry point

- **Core Application**:
  - `website/` - Main package containing all application logic
  - `models.py` - Database models and schema
  - `views.py` - Route handlers and business logic

- **Templates/Static**:
  - `templates/` - All HTML templates (Jinja2)
  - `static/` - Frontend assets (CSS/JS/images)

- **Environment**:
  - `venv/` - Python virtual environment (excluded from Git)
  - `migrations/` - Database migration scripts (if using Flask-Migrate)