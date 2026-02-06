# Family Favourites – Testing Details

[View README.md file.](/README.md)

[View (website name) deployed site here.](add link)

## Testing Performed

## Table of Contents

- [Browser Compatibility](#browser-compatibility)
- [Responsiveness](#responsiveness)
- [Validators](#validators)
- [Lighthouse Performance](#lighthouse-performance)
- [Testing User Stories](#testing-user-defined-stories-from-the-ux-section-of-readmemd)
- [Manual Testing and Functionality](#manual-testing-and-functionality-on-each-page)
- [Known Bugs](#known-bugs-discovered)

****

## Browser Compatibility

****

## Responsiveness

****

## Validators

- [W3C Markup validator](https://validator.w3.org/)

As the project uses Django templates the html has been validated by manually clicking through the restaurants pages, copying the source code and validating this rendered version of the html page using [W3C Markup validator](https://validator.w3.org/). There were some errors when first put through the validator but once the errors were corrected the following results of no errors or warnings of the checker are as follows:

- Results of index.html
  - <details>
    <summary>Index Page</summary>

    ![Index Page](readme_documents/testing/html_validation/home-source-rendered-html-validation.png)
  </details>

- Results of menu.html
  - <details>
    <summary>Menu Page</summary>

    ![Menu Page](readme_documents/testing/html_validation/menus-source-rendered-html-validation.png)
  </details>

- Results of contact.html
  - <details>
    <summary>Contact Page</summary>

    ![Contact Page](readme_documents/testing/html_validation/contact-source-rendered-html-validation.png)
  </details>

- Results of Regiser signup.html
  - <details>
    <summary>Sign Up Page</summary>

    ![Sign Up Page](readme_documents/testing/html_validation/register-signup-source-rendered-html-validation.png)
  </details>

- Results of Sign In login.html
  - <details>
    <summary>Login Page</summary>

    ![Login Page](readme_documents/testing/html_validation/login-signin-source-rendered-html-validation.png)
  </details>

- Results of Sign Out logout.html
  - <details>
    <summary>Log Out Page</summary>

    ![Log Out Page](readme_documents/testing/html_validation/logout-source-rendered-html-validation.png)
  </details>

- Results of book_a_table.html
  - <details>
    <summary>Book a Table Page</summary>

    ![Book a Table Page](readme_documents/testing/html_validation/book-a-table-source-rendered-html-validation.png)
  </details>

- Results of bookings.html
  - <details>
    <summary>Bookings Page</summary>

    ![Bookings Page](readme_documents/testing/html_validation/bookings-source-rendered-html-validation.png)
  </details>

- Results of Change edit_bookings.html
  - <details>
    <summary>Edit Bookings Page</summary>

    ![Edit Bookings Page](readme_documents/testing/html_validation/change-booking-source-rendered-html-validation.png)
  </details>

- Results of Cancel delete_bookings.html
  - <details>
    <summary>Delete Bookings Page</summary>

    ![Delete Bookings Page](readme_documents/testing/html_validation/cancel-booking-source-rendered-html-validation.png)
  </details>

- Results of contacts.html
  - <details>
    <summary>Contacts Page</summary>

    ![Contacts Page](readme_documents/testing/html_validation/contacts-source-rendered-html-validation.png)
  </details>

- [W3C CSS validator](https://jigsaw.w3.org/css-validator/)

There was an error in the stylesheet that was corrected, but nothing was done about the warning as it was an imported stylesheet that couldn't be confirmed by this checker. Results are as follows using the [W3C CSS validator](https://jigsaw.w3.org/css-validator/).

- Error results of style.css
  - <details>
    <summary>Errors of style.css</summary>

    ![Error results](readme_documents/testing/css_validation/stylesheet-css-validation-error-results.png)
  </details>

- Results of style.css
  - <details>
    <summary>Results of style.css</summary>

    ![Results style.css](readme_documents/testing/css_validation/stylesheet-css-validation-pass-results.png)
  </details>

- [Code Institute's Python Linter](https://pep8ci.herokuapp.com/)

****

## Lighthouse Performance

When looking at the performance, accessibility, best practices and the SEO of the website, I used Lighthouse in Chrome's development tools. The only one performing below the green was the home page in mobile format, which got a result of 89.

There was an issue that popped up saying that Chrome extensions were affecting the page's performance but apart from the one mentioned above the other pages were all in the green as you can see in the following results:

- Home
  - <details>
    <summary>Desktop Results</summary>

    ![Home Desktop Results](readme_documents/testing/lighthouse_reports/home-desktop.png)
  </details>

  - <details>
    <summary>Mobile Results</summary>

    ![Home Mobile Results](readme_documents/testing/lighthouse_reports/home-mobile.png)
  </details>

- Menu
  - <details>
    <summary>Desktop Results</summary>

    ![Menu Desktop Results](readme_documents/testing/lighthouse_reports/menu-desktop.png)
  </details>

  - <details>
    <summary>Mobile Results</summary>

    ![Menu Mobile Results](readme_documents/testing/lighthouse_reports/menu-mobile.png)
  </details>

- Contact
  - <details>
    <summary>Desktop Results</summary>

    ![Contact Desktop Results](readme_documents/testing/lighthouse_reports/contact-desktop.png)
  </details>

  - <details>
    <summary>Mobile Results</summary>

    ![Contact Mobile Results](readme_documents/testing/lighthouse_reports/contact-mobile.png)
  </details>

- Register/Signup
  - <details>
    <summary>Desktop Results</summary>

    ![Register Desktop Results](readme_documents/testing/lighthouse_reports/register-signup-desktop.png)
  </details>

  - <details>
    <summary>Mobile Results</summary>

    ![Register Mobile Results](readme_documents/testing/lighthouse_reports/register-signup-mobile.png)
  </details>

- Login/Signin
  - <details>
    <summary>Desktop Results</summary>

    ![Login Desktop Results](readme_documents/testing/lighthouse_reports/login-desktop.png)
  </details>

  - <details>
    <summary>Mobile Results</summary>

    ![Login Mobile Results](readme_documents/testing/lighthouse_reports/login-mobile.png)
  </details>

- Logout/Signout
  - <details>
    <summary>Desktop Results</summary>

    ![Logout Desktop Results](readme_documents/testing/lighthouse_reports/logout-desktop.png)
  </details>

  - <details>
    <summary>Mobile Results</summary>

    ![Logout Mobile Results](readme_documents/testing/lighthouse_reports/logout-mobile.png)
  </details>

- Book a Table
  - <details>
    <summary>Desktop Results</summary>

    ![Book a Table Desktop Results](readme_documents/testing/lighthouse_reports/book-a-table-desktop.png)
  </details>

  - <details>
    <summary>Mobile Results</summary>

    ![Book a Table Mobile Results](readme_documents/testing/lighthouse_reports/book-a-table-mobile.png)
  </details>

- Bookings
  - <details>
    <summary>Desktop Results</summary>

    ![Bookings Desktop Results](readme_documents/testing/lighthouse_reports/bookings-desktop.png)
  </details>

  - <details>
    <summary>Mobile Results</summary>

    ![Bookings Mobile Results](readme_documents/testing/lighthouse_reports/bookings-mobile.png)
  </details>

- Change/Edit Bookings
  - <details>
    <summary>Desktop Results</summary>

    ![Change Bookings Desktop Results](readme_documents/testing/lighthouse_reports/change-booking-desktop.png)
  </details>

  - <details>
    <summary>Mobile Results</summary>

    ![Change Bookings Mobile Results](readme_documents/testing/lighthouse_reports/change-booking-mobile.png)
  </details>

- Cancel/Delete Bookings
  - <details>
    <summary>Desktop Results</summary>

    ![Canel Bookings Desktop Results](readme_documents/testing/lighthouse_reports/cancel-booking-desktop.png)
  </details>

  - <details>
    <summary>Mobile Results</summary>

    ![Cancel Bookings Mobile Results](readme_documents/testing/lighthouse_reports/cancel-booking-mobile.png)
  </details>

- Contacts
  - <details>
    <summary>Desktop Results</summary>

    ![Contacts Desktop Results](readme_documents/testing/lighthouse_reports/contacts-desktop.png)
  </details>

  - <details>
    <summary>Mobile Results</summary>

    ![Contacts Mobile Results](readme_documents/testing/lighthouse_reports/contacts-mobile.png)
  </details>

****

## Testing user defined stories from the UX section of READMe.md

### Epic A: Website Content

#### User Story A1: What kind of site

- As a first time user to the site I want to be able to see what kind of site it is and to navigate the site easily.

#### User Story A2: Location of the restaurant

- As a potential customer I want to be able to go to the restaurant and book a table at the restaurant.

#### User Story A3: Call the restaurant

- As a potential customer I want to be able to book, change and cancel a booking on the phone before visiting the restaurant.

#### User Story A4: Menu

- As a potential customer I want to browse the menu to see what is available before visiting the restaurant.

#### User Story A5: Reviews

- As a potential customer I want to read what people thought of the restaurant before I visit.

### Epic B: User Profile

#### User Story B1: Contact the Restaurant

- As a site user I want to be able to contact the restaurant via email.

#### User Story B2: Book a Table

- As a site user I want to be able to book a table at the restaurant online before going.

#### User Story B3: View my Booking

- As a site user I want to be able to view my bookings to show the booking has been made.

#### User Story B4: Change my Booking

- As a site user I want to be able to make changes to my booking in my account if necessary.

#### User Story B5: Cancel my Booking

- As a site user I want to be able to cancel my booking in my account if necessary.

#### User Story B6: Reviews

- As a customer I want to be able to write a review of how my meal and the service I received were.

#### User Story B7: Order a Meal

- As a site user I want to be able to order a meal online and either be able to pick it up or have it delivered to my door.

### Epic C: Admin Profile

#### User Story C1: Manage the Menus

- As a site admin I want to be able to create, read, update and delete the menus to make sure that the menus are current on the site.

#### User Story C2: Manage User Bookings

- As a site admin I want to be able to create, read, update and delete user bookings when required.

#### User Story C3: Approve Reviews

- As a site admin I want to be able to approve potential reviews from customers before they are displayed on the site.

****

## Manual Testing and Functionality on each page

Manual testing of the features was carried out with the tests and results below:

- [Navbar Links, Dropdown Menu and Buttons](readme_documents/testing/manual_testing/navbar-dropdown-buttons-manual-testing.pdf)

- [Contact Us Form](readme_documents/testing/manual_testing/contact-us-form-manual-testing.pdf)

- [Register Form](readme_documents/testing/manual_testing/register-signup-form-manual-testing.pdf)

- [Login Form](readme_documents/testing/manual_testing/login-signin-form-manual-testing.pdf)

- [Book A Table Form](readme_documents/testing/manual_testing/book-a-table-form-manual-testing.pdf)

## Further Testing

****

## Known bugs discovered
