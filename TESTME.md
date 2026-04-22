# Family Favourites – Testing Details

[View README.md file.](/README.md)

[View Family Favourites deployed site here.](https://family-favourites-b117b469baf2.herokuapp.com/)

![Mochups of Family Favourites](readme_documents/responsiveness/am-i-responsive-mochups.png)

## Testing Performed

## Table of Contents

- [Browser Compatibility and Responsiveness](#browser-compatibility-and-responsiveness)
- [Validators](#validators)
- [Lighthouse Performance](#lighthouse-performance)
- [WAVE Web Accessibility Evaluation Tool](#wave-web-accessibility-evaluation-tool)
- [Testing User Stories](#testing-user-defined-stories-from-the-ux-section-of-readmemd)
- [Manual Testing and Functionality](#manual-testing-and-functionality-on-each-page)
- [Known Bugs](#known-bugs-discovered)

****

## Browser Compatibility and Responsiveness

The Family Favourites site compatability was tested on the following browsers with each showing the website as intended:

- Google Chrome
- Firefox
- Microsoft Edge
- Opera 
- DuckDuckGo

The development tools on Chrome, Edge and Opera was used to test the responsiveness of the site on different size screens, from mobile, tablet, laptop and desktop pc's. When on mobile devices everything is reduced to a single column. The navigation links being reduced to a burger bar with the logo and dropdown menu positioned above. When on tablet the header is in a line with the navigation links still showing as a burger bar and the footer in two colums. Then on laptop or desktop the navigation bar is showing all the items separately within the header.

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

While using [Code Institute's Python Linter](https://pep8ci.herokuapp.com/) I changed the errors which had white space on blank lines, needing white space, or needing extra blank lines, and some of the ones that stated that the lines were too long. Other lines that were too long that couldn't be changed due to causing other errors were left as they were.

- Family Favourites Project
  - <details>
    <summary>project settings.py validation</summary>

    ![Family Favourites settings](readme_documents/testing/python_linter_validation/family_favourites/family-favourites-settings-python-linter.png)
  </details>

  - <details>
    <summary>project urls.py validation</summary>

    ![Family Favourites urls](readme_documents/testing/python_linter_validation/family_favourites/family-favourites-urls-python-linter.png)
  </details>

  - <details>
    <summary>project asgi.py validation</summary>

    ![Family Favourites asgi](readme_documents/testing/python_linter_validation/family_favourites/family-favourites-asgi-python-linter.png)
  </details>

  - <details>
    <summary>project wsgi.py validation</summary>

    ![Family Favourites wsgi](readme_documents/testing/python_linter_validation/family_favourites/family-favourites-wsgi-python-linter.png)
  </details>

- Home App
  - <details>
    <summary>home apps.py validation</summary>

    ![Home apps](readme_documents/testing/python_linter_validation/home/home-apps-python-linter.png)
  </details>

  - <details>
    <summary>home urls.py validation</summary>

    ![Home urls](readme_documents/testing/python_linter_validation/home/home-urls-python-linter.png)
  </details>

  - <details>
    <summary>home views.py validation</summary>

    ![Home views](readme_documents/testing/python_linter_validation/home/home-views-python-linter.png)
  </details>

- Menu App
  - <details>
    <summary>menu apps.py validation</summary>

    ![Menu apps](readme_documents/testing/python_linter_validation/menu/menu-apps-python-linter.png)
  </details>

  - <details>
    <summary>menu urls.py validation</summary>

    ![Menu urls](readme_documents/testing/python_linter_validation/menu/menu-urls-python-linter.png)
  </details>

  - <details>
    <summary>menu views.py validation</summary>

    ![Menu views](readme_documents/testing/python_linter_validation/menu/menu-views-python-linter.png)
  </details>

- Contact App
  - <details>
    <summary>contact admin.py validation</summary>

    ![Contact admin](readme_documents/testing/python_linter_validation/contact/contact-admin-python-linter.png)
  </details>

  - <details>
    <summary>contact apps.py validation</summary>

    ![Contact apps](readme_documents/testing/python_linter_validation/contact/contact-apps-python-linter.png)
  </details>

  - <details>
    <summary>contact forms.py validation</summary>

    ![Contact forms](readme_documents/testing/python_linter_validation/contact/contact-forms-python-linter.png)
  </details>

  - <details>
    <summary>contact models.py validation</summary>

    ![Contact models](readme_documents/testing/python_linter_validation/contact/contact-models-python-linter.png)
  </details>
  
  - <details>
    <summary>contact urls.py validation</summary>

    ![Contact urls](readme_documents/testing/python_linter_validation/contact/contact-urls-python-linter.png)
  </details>

  - <details>
    <summary>contact views.py validation</summary>

    ![Contact views](readme_documents/testing/python_linter_validation/contact/contact-views-python-linter.png)
  </details>

- Book a Table App
  - <details>
    <summary>book a table admin.py validation</summary>

    ![Book a Table admin](readme_documents/testing/python_linter_validation/book_a_table/book-a-table-admin-python-linter.png)
  </details>

  - <details>
    <summary>book a table apps.py validation</summary>

    ![Book a Table apps](readme_documents/testing/python_linter_validation/book_a_table/book-a-table-apps-python-linter.png)
  </details>

  - <details>
    <summary>book a table forms.py validation</summary>

    ![Book a Table forms](readme_documents/testing/python_linter_validation/book_a_table/book-a-table-forms-python-linter.png)
  </details>

  - <details>
    <summary>book a table models.py validation</summary>

    ![Book a Table models](readme_documents/testing/python_linter_validation/book_a_table/book-a-table-models-python-linter.png)
  </details>
  
  - <details>
    <summary>book a table urls.py validation</summary>

    ![Book a Table urls](readme_documents/testing/python_linter_validation/book_a_table/book-a-table-urls-python-linter.png)
  </details>

  - <details>
    <summary>book a table views.py validation</summary>

    ![Book a Table views](readme_documents/testing/python_linter_validation/book_a_table/book-a-table-views-python-linter.png)
  </details>

****

## Lighthouse Performance

When looking at the performance, accessibility, best practices and the SEO of the website, I used Lighthouse in Chrome's development tools. The only one performing below the green was the menu page in mobile format, which got a result of 89.

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

## WAVE Web Accessibility Evaluation Tool

[WAVE](https://wave.webaim.org/) was used to check that the Family Favourites site is also accessible to people with disabilities. Any errors were dealt with, but I did leave the contrast errors of the page links for each page, as the page that was visibly accessible and the two other page links were greyer rather than black so the person could see which page they were currently on.

- [WAVE Results](readme_documents/testing/wave_accessibility/wave-web-accessibility-evaluation.pdf)

****

## Testing user defined stories from the UX section of READMe.md

The link below details the user defined story testing with reference to the features.

[User Defined Story Testing](readme_documents/features/user-defined-story-testing.pdf)

****

## Manual Testing and Functionality on each page

Manual testing of the features was carried out with the tests and results below:

- [Navbar Links, Dropdown Menu and Buttons](readme_documents/testing/manual_testing/navbar-dropdown-buttons-manual-testing.pdf)

- [Contact Us Form](readme_documents/testing/manual_testing/contact-us-form-manual-testing.pdf)

- [Register Form](readme_documents/testing/manual_testing/register-signup-form-manual-testing.pdf)

- [Login Form](readme_documents/testing/manual_testing/login-signin-form-manual-testing.pdf)

- [Book A Table Form](readme_documents/testing/manual_testing/book-a-table-form-manual-testing.pdf)

****

## Known bugs discovered

- When you tab between the different menus on the menu page the page showed a lot of white space between the first and second tab, and between the second and third tabs. When I searched Google the AI showed that the Bootstrap's display needed to implement none. So when the following CSS was included there was no further white space showing on the menus.

![CSS pane display](readme_documents/testing/bugs_images/pane-display-css.png)

- The Home page didn’t have the underline to show that it was active and that, that was the page that you were currently on. This was due to the request path being home_url and not index_url. 

![Request path equals home_url](readme_documents/testing/bugs_images/request-path-home-url.png)
![Request path equals index_url](readme_documents/testing/bugs_images/request-path-index-url.png)

- When the book a table form was filled in incorrectly the errors were not showing and the form wasn't repopulated with the information. This was due to the retun render request by rendering the template without passing the form back with its context.

![Return request without passing form](readme_documents/testing/bugs_images/return-request-no-form.png)
![Return request with passing form](readme_documents/testing/bugs_images/return-request-with-form.png)

- When clicking on the button to update or delete a booking the user couldn't go to the template for the booking requested. The reason being that the id number was not being picked up giving the error below.

![Edit booking template error](readme_documents/testing/bugs_images/edit-booking-template-error.png)

To rectify this the booking.id was changed to booking.pk for both the edit and delete bookings template.

![Edit booking primary key](readme_documents/testing/bugs_images/edit-booking-template-pk.png)
