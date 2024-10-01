
# The Big Bang Bookstore
<p dir="auto"><a target="_blank" rel="noopener noreferrer" href="https://github.com/iftec/bigbangbookstore/blob/main/documentation/responsive_layout.webp?raw=true"><img src="https://github.com/iftec/bigbangbookstore/blob/main/documentation//responsive_layout.webp?raw=true" alt="layouts" style="max-width: 100%;"></a></p>

## Site Overview
- An online bookstore specialising in books that deal with space, quantum physics, time, reality, and other mysteries of the universe.
- The site is designed to be easy to navigate and use, with a focus on providing a seamless shopping experience for customers.
- The project can be broken down into several applications, each with its own purpose and functionality.
 - The main application is the 'bigbangbookstore' application, which contains the core functionality of the site.
 - The 'stores' application is used to manage user profiles, authentication and orders.
 - The 'checkout' application is used to handle the checkout process and payment processing.
 - The 'basket' application is used to manage the user's shopping basket.


**Live Site:** [View live site here](https://www.bigbangbookstore.uk/) 

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
  - [Testing User Stories](#testing-user-stories)
  - [Automated Testing](#automated-testing)
  - [Bugs & Fixes](#bugs--fixes)
- [Deployment](#deployment)
- [Future Features](#future-features)
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

- [GitHub Desktop](https://desktop.github.com/)

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
<p dir="auto"><a target="_blank" rel="noopener noreferrer" href="https://github.com/iftec/bigbangbookstore/blob/main/documentation/account_page.webp?raw=true"><img src="https://github.com/iftec/bigbangbookstore/blob/main/documentation//account_page.webp?raw=true" alt="layouts" style="max-width: 100%;"></a></p>

# **Register page**
* Base HTML
* User registration form
* Famous quote
<p dir="auto"><a target="_blank" rel="noopener noreferrer" href="https://github.com/iftec/bigbangbookstore/blob/main/documentation/register1.webp?raw=true"><img src="https://github.com/iftec/bigbangbookstore/blob/main/documentation//register1.webp?raw=true" alt="layouts" style="max-width: 100%;"></a></p>

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
* Every time the user creates an order, this unique ID is stored with that order in a separate 'orders' table.

### Process

#### Creating an Account

**Navigate to the Registration Page:**
- Users can find the registration link on the landing page or the login page.

**Fill Out the Registration Form:**
- The form requires:
  - **Name**: The clients name.
  - **Email Address**: A valid email address (this is used for their username).
  - **Password**: A secure password (minimum length, special characters, etc.).
  - **Confirm Password**: Re-enter the password to ensure it matches.

**Submit the Registration Form:**
- After filling out the form, the user clicks the "Register" button.
- The system checks for existing users with the same username or email.
- If successful, the user is redirected to the landing page.


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
* Have somewhere to find books about the universe and reality easily.
    * The user can easily find books relating to those specific subjects.
* Easily understand how to use the website
    * The website has a simple layout with intuitive icons and labels.
* Register with the site.
    * The user can register their details with the site, or log in if they already have an account.
* Login to the site.
    * The user can log in to the site using their email and password.
* Log out of the site.
    * The user can log out of the site at any time.
* View my account and change details.
    * The user can view and change their account details, and password.
* Purchase book as a guest.
    *The user can purchase a book as a guest without the need to register or log in.
*  View all books in the database.
    * The user can view all books in the database and can filter by genre, price, and rating.
* Search for books.
    The user can search the database by name or title for books.
* Delete my account
    * The user can delete their account from the accounts page.
* Ensure my payment details are secure.
    * The Payment system uses Stripe to ensure the payment details are secure.

### Automated Testing 
Automated Testing 
Using Django's testing framework I carried out several unit tests on the key operations of the site, such as Authentication and CRUD functions for each module. These tests can be ran under local deployment using the relevant python command for your cli followed by manage.py tests. Each modules tests are located in their respective tests.py file.
<p dir="auto"><a target="_blank" rel="noopener noreferrer" href="https://github.com/iftec/bigbangbookstore/blob/main/documentation/testing_py.webp?raw=true"><img src="https://github.com/iftec/bigbangbookstore/blob/main/documentation//testing_py.webp?raw=true" alt="layouts" style="max-width: 100%;"></a></p>

### ***Bugs and Known Issues:***
* Problems caused by an accidental branch and following merges.
    The merges of the branches kept causing me errors, not wanting to do a force merge and lose my history in GitHub, I had someone else try a couple of uploads to see if the issue was my end.
    As such, two uploads in my GitHub repo show being uploaded by isdanryan.
    I have spoken to my course tutor Manuel and he has confirmed that this will be ok.
    - As it was, I had fixed all the issues on my last merge, but at that point, I was unaware of this and wanted to confirm the issue was not on my machine.

* Some issues with Bootstrap overriding my CSS.
    In some cases, using !important to override the Bootstrap styling worked, but in others, it did not, so Bootstrap was removed for those elements and custom CSS was used instead.

* Chat GTP was correct and helped about 50% of the time, the other 50% it would lose the plot and make things worse. However it did help when explaining code and as such made it easier to fix some of the silly  mistakes, it also helped with quickly re styling some elements.

* I had to restyle and change the spacing of some of my Icons to conform to accesabilty standards.

* As far as I'm aware there are now no bugs left in the code, had plenty of typo's and small errors that I had to go back and fix, but nothing major.


#### **Validators**
The following validators were used during final testing to ensure all code was up to standards;

* Javascript - JSHint
* Python - Flake8 VS Code Extension
* CSS - W3C CSS Validator
* HTML - W3C HTML Validator
- Note: W3C's HTML Validator doesn't work well with Django's HTML template language, so after pasting in the code, I ignored some of the errors and only paid attention to the ones directly relating to the HTML language and formatting.

#### ***CSS*** - https://jigsaw.w3.org/css-validator/
<p dir="auto"><a target="_blank" rel="noopener noreferrer" href="https://github.com/iftec/bigbangbookstore/blob/main/documentation/css_validation.webp?raw=true"><img src="https://github.com/iftec/bigbangbookstore/blob/main/documentation//css_validation.webp?raw=true" alt="validation" style="max-width: 100%;"></a></p>

### **Lighthouse Scores**
<p dir="auto"><a target="_blank" rel="noopener noreferrer" href="https://github.com/iftec/bigbangbookstore/blob/main/documentation/lighthouse1.webp?raw=true"><img src="https://github.com/iftec/bigbangbookstore/blob/main/documentation//lighthouse1.webp?raw=true" alt="scores" style="max-width: 100%;"></a></p>
<p dir="auto"><a target="_blank" rel="noopener noreferrer" href="https://github.com/iftec/bigbangbookstore/blob/main/documentation/lighthouse2.webp?raw=true"><img src="https://github.com/iftec/bigbangbookstore/blob/main/documentation//lighthouse2.webp?raw=true" alt="scores" style="max-width: 100%;"></a></p>


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

- Environment Variables: Ensure you set up any required environment variables, such as database credentials, secret keys, etc. 
- You can use a .env file and the python-decouple package to manage these variables.
- You may also need to change debug settings to True in settings.py to enable debugging.
- You may also need to change allowed hosts in settings.py to allow access from your domain name.

## **Future Features**
* Still needs loads more styling.
* Setup mailserver for sending conformation emails.

## **Credits**
* https://www.bootstrap.com
    * Used for the bootstrap template.
* https://www.w3schools.com/
    * Used for HTML and CSS documentation reference and examples.
* https://learn.codeinstitute.net/
    * Used for reference from the many examples shown on the course.
* https://chat.openai.com/
    * Used to help in the creation of search section of the site.
    * Used to check the format of the code for the site.
    * Used to analyse the some of code issues for the site.
    * Used to create some of the Python functions.
* https://www.amazon.co.uk/
    * Images and descriptions for the books.
* https://plus.nasa.gov/
    * Used for BigBang image
* https://www.grammarly.com/
    * Used to check the grammar of the text.
* https://github.com/isdanryan
    * For help solving the merge conflicts, suggestions, and the late-night calls.

Many, many thanks to: 	
- Pasquale Fasulo, Manuel Perez Romero, and all those at The City of Bristol College for their help and support throught this course, at times it's been tough going, but you've all been great and very approachable.
# The Big Bang Bookstore

