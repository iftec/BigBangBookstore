
# The Big Bang Bookstore

## Site Overview
An online bookstore specialising in books that deal with space, quantum physics, time, reality, and other mysteries of the universe.

**Live Site:** [View the live site here](#)

## Table of Contents
- [Site Overview](#site-overview)
- [User Experience (UX)](#user-experience-ux)
  - [Target Audiences](#target-audiences)
  - [User Stories](#user-stories)
  - [Site Aims](#site-aims)
- [How This Will Be Achieved](#how-this-will-be-achieved)
- [Wireframes](#wireframes)
- [Colour Scheme](#colour-scheme)
- [Typography](#typography)
- [Technologies Used](#technologies-used)
- [Current Features Common to All Pages](#current-features-common-to-all-pages)
- [Individual Page Features](#individual-page-features)
- [Models & Schema](#models--schema)
- [Database](#database)
- [Process](#process)
- [Testing Phase](#testing-phase)
  - [During Development Testing](#during-development-testing)
  - [Manual Testing](#manual-testing)
  - [Bugs & Fixes](#bugs--fixes)
- [Deployment](#deployment)
  - [Setting Up Your Local Development Environment](#setting-up-your-local-development-environment)
  - [Set Up a Virtual Environment](#set-up-a-virtual-environment)
  - [Install Dependencies](#install-dependencies)
  - [Set Up the Database](#set-up-the-database)
  - [Run Database Migrations](#run-database-migrations)
  - [Create a Superuser (Optional)](#create-a-superuser-optional)
  - [Run the Development Server](#run-the-development-server)
  - [Deploying Changes to GitHub](#deploying-changes-to-github)
- [Future Enhancements](#future-enhancements)
- [Credits](#credits)

## User Experience (UX)

### Target Audiences
The target audience is for people with interests in the sciences, particularly in the universe, quantum mechanics, and the nature of reality.

### User Stories
As a user, I want to:
- Search for and find books of interest.
- Easily navigate the site without feeling lost.
- Purchase books online.
- Read detailed descriptions of the books.
- Keep track of my orders and manage my account.

### Site Aims
- Provide a quick and simple way for users to search for books.
- Ensure easy navigation throughout the site.
- Encourage users to sign up and create an account.
- Create a mobile-friendly site.
- Provide a visually appealing layout to recognize book covers and authors.

## How This Will Be Achieved
The site will feature:
- A landing page with prominent search and filter functions.
- Login/Signup options.
- Relevant images and text that connect to the theme.
- A clear layout displaying book images with brief descriptions, alongside options for more details or purchase.

## Wireframes
<p dir="auto"><a target="_blank" rel="noopener noreferrer" href="https://github.com/iftec/bigbangbookstore/blob/main/documentation/wireframes4.png?raw=true"><img src="https://github.com/iftec/bigbangbookstore/blob/main/documentation//wireframes4.png?raw=true" alt="layouts" style="max-width: 100%;"></a></p>

### **Colour Scheme**
an off-white background, which is clean and neutral, creating a modern and inviting atmosphere for the bookstore website using the following colour scheme inspired by the cosmic image:

1. Background:
Off-White (Background): #F8F8F8
A soft, warm off-white that provides a clean canvas without being stark, ideal for a bookstore environment.
2. Primary Colors (Buttons and Key Elements):
Deep Purple (Primary Buttons): #5A3E85
A rich, deep purple for primary buttons adds a touch of elegance and sophistication, inspired by the cosmic theme.
Vibrant Blue (Secondary Buttons/Links): #3B5998 This vibrant blue provides contrast while maintaining a calm, trustworthy vibe.
3. Font Colors:
Charcoal Gray (Main Text): #333333
A dark, charcoal gray for the main body text ensures readability against the off-white background without being as harsh as pure black.
Midnight Blue (Headings): #2C3E50
A deep, almost-black blue for headings and subheadings adds a touch of depth and professionalism, tying into the space theme subtly.
A light, pastel purple can be used for section backgrounds, like cards or banners, to differentiate them from the main off-white background while maintaining a cohesive look.
4. Button and Link Text:
Pure White (Text on Buttons): #FFFFFF
For text on buttons, white will ensure the highest contrast and readability, especially against the deeper purple and blue backgrounds.
Color Usage :
Buttons: Use Deep Purple and Vibrant Blue.
Fonts: Charcoal Gray for body text and Midnight Blue for headings will create a clear, structured layout that's easy on the eyes.
<p dir="auto"><a target="_blank" rel="noopener noreferrer" href="https://github.com/iftec/bigbangbookstore/blob/main/documentation/landing_page.webp?raw=true"><img src="https://github.com/iftec/bigbangbookstore/blob/main/documentation//landing_page.webp?raw=true" alt="layouts" style="max-width: 100%;"></a></p>
### **Typography**

* 1. Header Fonts (for Titles and Headings):
Montserrat: A modern, geometric sans-serif font that is clean and versatile. It’s excellent for creating a strong, impactful header.

Backup: Arial, sans-serif
Oswald: A condensed sans-serif font that adds a bold and striking touch to headers. It has a slightly more editorial feel, which can give your site a unique and stylish appearance.

Backup: Helvetica, sans-serif
2. Body Text Fonts (for Paragraphs and Descriptions):
Lora: A serif font that combines readability with a touch of elegance. It pairs well with more modern, sans-serif headers to create a balanced look.

Backup: Georgia, serif
Roboto: A highly readable sans-serif font that is versatile and clean, perfect for longer blocks of text. It complements almost any header font.

Backup: Verdana, sans-serif
3. Accent Fonts (for Buttons, Banners, and Special Text):
Poppins: A rounded, geometric sans-serif font that works beautifully for buttons and small pieces of text. It’s friendly and approachable, ideal for drawing attention.

Backup: Tahoma, sans-serif
Raleway: A clean, elegant sans-serif font that is slightly more refined, making it great for buttons or smaller text accents where you want to maintain readability with a touch of sophistication.

Backup: Arial, sans-serif
* Responsive across all devices, to make images scale properly and not end up pixelated, text is readable on all devices.
<p dir="auto"><a target="_blank" rel="noopener noreferrer" href="https://github.com/iftec/bigbangbookstore/blob/main/documentation/responsive_layout.webp?raw=true"><img src="https://github.com/iftec/bigbangbookstore/blob/main/documentation//responsive_layout.webp?raw=true" alt="layouts" style="max-width: 100%;"></a></p>

### **Technologies Used**

Used for Some function creation.
- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)

Used as the basic building block for the project and to structure the content.
- [CSS](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics)


Used to style web content across the website.
Bootstrap, CSS, grid, flexbox, and media queries were used to create the layout of the site.


Used for site functionality.
- [JavaScript](https://www.javascript.com/)
- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Stripe] (https://stripe.com/)
- HTML


- [Google Developer Tools](https://developer.chrome.com/docs/devtools/)

Used as a primary method of fixing issues, finding bugs, and testing responsiveness across the project.

- [Github](https://github.com/)
Used to store code for the project after being pushed.

- [Github Desktop](https://desktop.github.com/)

Used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.


- [Chat GPT](https://chat.openai.com/)

Used for Some function creation, some styling and code checking.

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)

Used as the basic building block for the project and to structure the content.

- [CSS](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics)

Used to style web content across the website.
CSS grid, Bootstrap, flexbox, and media queries were used to create the layout of the site.
- [Bootstrap] (https://getbootstrap.com/)


- [Balsamiq](https://balsamiq.com/)

Used to create the wireframes for the project.

- [Grammarly](https://app.grammarly.com/)

Used to fix grammar errors across the project.

## **Current Features Common to all pages**
* Store name
* Basket
* Login/Account
* Colours 
## **Individual Page Content features**

# **Base HTML**
* Login/Logout
* Signup
* Account Details
* Footer
<p dir="auto"><a target="_blank" rel="noopener noreferrer" href="https://github.com/iftec/bigbangbookstore/blob/main/documentation/base_html.webp?raw=true"><img src="https://github.com/iftec/bigbangbookstore/blob/main/documentation//base_html.webp?raw=true" alt="layouts" style="max-width: 100%;"></a></p>

## **Landing Page**
* Base HTML
* Splash image of the Big Bang
* Filter book options
* Search box
* Images showing list of available books
* More info and add to basket links
* Quantity option
* Sign up or Login links and basket(from base html)
<p dir="auto"><a target="_blank" rel="noopener noreferrer" href="https://github.com/iftec/bigbangbookstore/blob/main/documentation/landing_page.webp?raw=true"><img src="https://github.com/iftec/bigbangbookstore/blob/main/documentation//landing_page.webp?raw=true" alt="layouts" style="max-width: 100%;"></a></p>


# **Accounts page**
* Base HTML
* User account details
* Past orders
* Change password option
* Delete account option
<p dir="auto"><a target="_blank" rel="noopener noreferrer" href="https://github.com/iftec/bigbangbookstore/blob/main/documentation/account_page.webp?raw=true"><img src="https://github.com/iftec/bigbangbookstore/blob/main/documentation//account_page?raw=true" alt="layouts" style="max-width: 100%;"></a></p>

# **Register page**
* Base HTML
* User registration form
* Famous quote
<p dir="auto"><a target="_blank" rel="noopener noreferrer" href="https://github.com/iftec/bigbangbookstore/blob/main/documentation/register.webp?raw=true"><img src="https://github.com/iftec/bigbangbookstore/blob/main/documentation//register.webp?raw=true" alt="layouts" style="max-width: 100%;"></a></p>

# **Search results page**
* Base HTML
* Search box
* List of results with image and small description
<p dir="auto"><a target="_blank" rel="noopener noreferrer" href="https://github.com/iftec/bigbangbookstore/blob/main/documentation/search.webp?raw=true"><img src="https://github.com/iftec/bigbangbookstore/blob/main/documentation//search.webp?raw=true" alt="layouts" style="max-width: 100%;"></a></p>

# **Details page**
* Base HTML
* Book image
* Book detail
* Price
* Add to basket
* Quantity option
* Continue shopping
<p dir="auto"><a target="_blank" rel="noopener noreferrer" href="https://github.com/iftec/bigbangbookstore/blob/main/documentation/details.webp?raw=true"><img src="https://github.com/iftec/bigbangbookstore/blob/main/documentation//details.webp?raw=true" alt="layouts" style="max-width: 100%;"></a></p>

# **Models & Schema**
### **Database**
* For the implementation of the Bookstore Application, I required the use of a database to store both the user information, orders and books
* For the database I have opted to use Postgres
* Below is a view of the entity relationships for this database.
<p dir="auto"><a target="_blank" rel="noopener noreferrer" href="https://github.com/iftec/bigbangbookstore/blob/main/documentation/entity_relationships.webp?raw=true"><img src="https://github.com/iftec/bigbangbookstore/blob/main/documentation//entity_relationships.webp?raw=true" alt="layouts" style="max-width: 100%;"></a></p>

* Once the user has registered on the site, their sign-up information is stored along with a unique ID in the database.
* Everytime the user creates an order, this unique ID is stored with that order in a separate 'orders' table.

### Process

#### Creating an Account

**Navigate to the Registration Page:**
- Users can find the registration link on the landing page or the login page.

**Fill Out the Registration Form:**
- The form requires:
  - **Email Address**: A valid email address, used for username.
  - **Password**: A secure password (minimum length, special characters, etc.).
  - **Confirm Password**: Re-enter the password to ensure it matches.

**Submit the Registration Form:**
- After filling out the form, the user clicks the "Register" button.
- The system checks for existing users with the same username or email.
- If successful, the user is redirected to the login page.


#### Logging In

**Navigate to the Login Link:**
- Users can find the login link on the landing page shown by the icon on the top right of the screen

**Enter Login Credentials:**
- Users input their:
  - **Email**: The email used during registration.
  - **Password**: The password set during registration.

**Submit Login Form:**
- Upon clicking the "Login" button, the system checks the credentials.
- If valid, the user is redirected to their account page.

**Accessing Account Features:**
- Users can view their account details, past orders, and make any changes.

#### Adding Items to the Basket

**Navigate to Book Listings:**
- Users can browse books on the landing page or search results page.

**Select a Book:**
- Clicking on a book image or title will take users to the details page.

**Add to Basket:**
- On the book details page, users can select the desired quantity and click the "Add to Basket" button.
- A confirmation message will appear, indicating the item has been added.

#### Updating the Basket

**Navigate to the Basket:**
- Users can access their basket by clicking on the shopping cart icon in the header.

**Update Item Quantity:**
- In the basket view, users can adjust the quantity of each item using "+" and "-" buttons.
- The total price will update accordingly.

**Remove Items:**
- Users can remove items by clicking the "Remove" button next to each item.

**Proceed to Checkout:**
- Once satisfied with the basket contents, users can click the "Checkout" button to proceed with the purchase.

#### Searching for Books

**Navigate to the Search Bar:**
- Users can find the search bar prominently displayed on the landing page.

**Enter Search Query:**
- Users can type keywords related to the book title, author, or genre.

**Submit Search:**
- After entering the query, users can hit "Enter" or click the search icon to view results.

**View Search Results:**
- Users will be directed to a page displaying relevant book listings based on the search criteria.

#### Filtering Books

**Access Filtering Options:**
- Users can find filtering options on the search results page, typically on the left sidebar.

**Select Filters:**
- Users can filter books by:
  - **Genre**: Choose from a list of genres.
  - **Price Range**: Set a minimum and maximum price.
  - **Rating**: Filter by user ratings.


#### Logging Out

**Access the Logout Option:**
- Users can find the logout link in the top icon dropdown.

**Confirm Logout:**
- Clicking the logout link will log the user out and redirect them to the homepage.
- Users will need to log in again to access their account.

#### Resetting Password

**Navigate Accounts Page:**
- Scroll to change password section
- Enter old password 
- Enter a new password.
- Confirm the new password by entering it a second time.

**Submit New Password:**
- After submitting, the new password will be set, and the user can log in with the new credentials.

#### Deleting Account

**Navigate to Accounts Page:**
 - Scroll to the bottom of the page
 - Choose Delete Account Option
 - Please Note: The Delete option is not shown for Admin users 


**Navigate to Checkout:**
- Once users have added items to their basket, they click the "Checkout" button.

**Enter Shipping Information**
- Users must provide shipping details, including:
  - **Name**
  - **Address**
  - **City**
  - **Postal Code**
  - **Country**


**Enter Payment Information:**
- Users input their credit/debit card details, including:
  - **Card Number**
  - **Expiration Date**
  - **CVV**
  - The system processes the payment through Stripe.


**Submit Payment:**
- After confirming the order, users click the "Pay Now" button.


**Confirmation:**
- Upon successful payment, users will receive an order confirmation page.



## **Testing Phase**
### **During Development Testing**
* Google Chrome Developers Tools
* Lighthouse
* W3C Markup Validation Service
* W3C CSS Validation Service
* Jest 
* pytest


### **Manual Testing:**
* Google Chrome
* Microsoft Edge
* Mozilla Firefox
* Opera
* Windows Laptop
* Windows Desktop
* iPhone 11 pro
* Galaxy S20 FE
* Galaxy Flip 3
* Galaxy S21 Ultra

### **Testing User Stories**
As a user, I want to...
* Have somewhere to easily find books about the universe and reality.
    * The user can easily find books relating to those specific subjects.
* Easily understand how to use the website
    * The website has a simple layout with intuitive icons and labels.
* Register with the site.
    * The user can register their details with the site, or log in if they already have an account.
* Log in to the site.
    * The user can log in to the site using their username or email and password.
* Log out of the site.
    * The user can log out of the site at any time.
* View my account and change details.
    * The user can view  and change their account details, and password.
* Purchase book as a guest.
    *The user can purchase book as a guest without the need to register or log in.
*  View all books in the database.
    * The user can view all books in the database, and can filter by genre, price, and rating.
* Search for books.
    The user can search by name or title for books in the database.
* Delete my account
    * The user can delete their account from the accounts page.
### ***Bugs and Fixes:***
* Still needs loads more styling.
    Chat GTP was correct and helped about 50% of the time, the other 50% it would make things worse


#### **Validators**

#### ***HTML*** - https://validator.w3.org/nu/

<p dir="auto"><a target="_blank" rel="noopener noreferrer" href="https://github.com/iftec/bigbangbookstore/blob/main/documentation/responsive_layout.webp?raw=true"><img src="https://github.com/iftec/bigbangbookstore/blob/main/documentation//responsive_layout.webp?raw=true" alt="layouts" style="max-width: 100%;"></a></p>



#### ***CSS*** - https://jigsaw.w3.org/css-validator/
<p dir="auto"><a target="_blank" rel="noopener noreferrer" href="https://github.com/iftec/bigbangbookstore/blob/main/documentation/responsive_layout.webp?raw=true"><img src="https://github.com/iftec/bigbangbookstore/blob/main/documentation//responsive_layout.webp?raw=true" alt="layouts" style="max-width: 100%;"></a></p>

### **Lighthouse Scores**
<p dir="auto"><a target="_blank" rel="noopener noreferrer" href="https://github.com/iftec/bigbangbookstore/blob/main/documentation/responsive_layout.webp?raw=true"><img src="https://github.com/iftec/bigbangbookstore/blob/main/documentation//responsive_layout.webp?raw=true" alt="layouts" style="max-width: 100%;"></a></p>


## **Testing Phase**
* Several tests were built in order to test the full functionality of the web application. And can be ran using the 'pytest' command.
* These tests include emulations of:
    1. Signing up as a new user.
    2. Logging in.
    3. Adding a book to the basket.
    4. Updating the basket .
    5. removing a book from the basket .
    6. Searching for a book.
    7. Add to favorites.
    8. Updating user details
* Full tests shown below:
<p dir="auto"><a target="_blank" rel="noopener noreferrer" href="https://github.com/iftec/bigbangbookstore/blob/main/documentation/responsive_layout.webp?raw=true"><img src="https://github.com/iftec/bigbangbookstore/blob/main/documentation//responsive_layout.webp?raw=true" alt="layouts" style="max-width: 100%;"></a></p>


## **Deployment**
### Prerequisites

Before you begin, ensure you have the following installed on your local machine:

- [Python](https://www.python.org/downloads/) (version 3.6 or higher)
- [Git](https://git-scm.com/downloads)
- [pip](https://pip.pypa.io/en/stable/installation/) (Python package installer)
- [Virtualenv](https://virtualenv.pypa.io/en/latest/installation.html) (optional but recommended)

### Steps to Download and Set Up the Project

1. Clone the Repository

   Open your terminal or command prompt and run the following command to clone the repository:

   git clone https://github.com/iftec/bigbangbookstore.git

2. Navigate to the Project Directory

   Change your directory to the project folder:

   cd bigbangbookstore

3. Create a Virtual Environment

   It is recommended to create a virtual environment to manage dependencies. Run the following command to create a virtual environment:

   python -m venv venv

4. Activate the Virtual Environment

   - On Windows:

     venv\Scripts\activate

   - On macOS/Linux:

     source venv/bin/activate

5. Install Dependencies

   Install the required dependencies using pip:

   pip install -r requirements.txt

6. Apply Migrations

   Apply the database migrations to set up the database schema:

   python manage.py migrate

7. Create a Superuser

   Create a superuser to access the Django admin interface:

   python manage.py createsuperuser

   Follow the prompts to set up the superuser account.

8. Run the Development Server

   Start the Django development server:

   python manage.py runserver

9. Access the Application

   Open your web browser and navigate to http://127.0.0.1:8000 to access the application.

10. Access the Admin Interface

    Navigate to http://127.0.0.1:8000/admin and log in with the superuser credentials you created earlier to access the Django admin interface.

Additional Notes

- Static Files: If you have static files, you may need to collect them using the following command:

  python manage.py collectstatic

- Environment Variables: Ensure you set up any required environment variables, such as database credentials, secret keys, etc. You can use a .env file and the python-decouple package to manage these variables.

Deployment

Deployment

This project is deployed using GitHub Pages using the following process:

Deploying a GitHub Repository via GitHub Pages

1. In your Repository section, select the Repository you wish to deploy.
2. In the top horizontal Menu, locate and click the Settings link.
3. Inside the Setting page, around halfway down locate the GitHub Pages Section.
4. Under Source, select the None tab and change it to Master, and click Save.
5. Finally, once the page resets, scroll back down to the GitHub Pages Section to see the following message: "Your site is ready to be published at (Link to the GitHub Page Web Address)". It can take time for the link to open your project initially, so please don't be worried if it does not load immediately.

Forking the GitHub Repository

You can fork a GitHub Repository to make a copy of the original repository to view or make changes without affecting the original repository.

1. Find the GitHub repository.
2. At the top of the page to the right, under your account, click the Fork button.
3. You will now have a copy of the repository in your GitHub account.

Making a Local Clone

1. Find the GitHub Repository.
2. Click the Code button.
3. Copy the link shown.
4. In Gitpod, change the directory to the location you would like the cloned directory to be located.
5. Type git clone, and paste the link you copied in step 3.
6. Press Enter to have the local clone created.
## **Credits**
* https://www.bootstrap.com
    * Used for the bootstrap template.
* https://www.w3schools.com/
    * Used for HTML and CSS documentation reference and examples.
* https://learn.codeinstitute.net/
    * Used for reference from the many examples shown on the course.
* https://chat.openai.com/
    * Used for creating search section of the site.
    * Used to check the format of the code for the site.
    * Used to analyse the some of code issues for the site.
    * Used to create some of the python functions.
* https://www.amazon.co.uk/
    * Images and descriptions for the books.
* https://www.grammarly.com/
    * Used to check the grammar of the text.
* https://github.com/isdanryan
    * For help solving the merge conflicts and the late night calls.

Many thanks to the teachers at the City of Bristol College for their help and support.
# The Big Bang Bookstore

