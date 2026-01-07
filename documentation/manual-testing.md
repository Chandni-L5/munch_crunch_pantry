# Full Manual Testing Documentation

<details>
<Summary><strong>Base - Nav, Footer</strong></Summary>

| Area | User Role | Test Scenario | Steps | Expected Result |
|------|-----------|---------------|-------|-----------------|
| Navigation 🧭 | All users | Navbar links work and indicate current page | 1. Open site 2. Click Home icon, Menu - About us/ Product origins/Contact us, FAQs, My Account, Basket| Correct pages load, hover effects over selections, no console errors |
| New user | Guest | My account displays 'Log in' and 'Register' | 1. click on My account menu, 2. dropdown displays, click on options | 'Log in' and 'Register' options visible, correct pages load, hover effect over selections | 
| Existing user | User | My account displays 'My Profile' and 'Logout'| 1. click on My account menu, 2. dropdown displays, click on options | 'My Profile' and 'Logout' options visible, correct pages load, hover effect over selections |
| Basket | All users | Basket value updates correctly when items are added/removed | 1. Add item to basket from product detail page, 2. Remove item from basket page, 3. Add a different item to the basket | Basket icon updates with correct item total value after addition/removal |
| Search Bar 🔍 | All users | Search bar functions correctly | 1. Enter search term (e.g., 'hazelnut'), 2. Click search icon or press enter | Relevant products displayed, search term shown in results page |
| Empty input | All users | Search bar handles empty input | 1. Leave search bar empty, 2. Click search icon or press enter | returns all products |
| No results | All users | Search bar handles no results | 1. Enter gibberish term (e.g., 'xyzabc'), 2. Click search icon or press enter | User feedback shown (e.g., 'No products found') |
| Full screen modal | All users | Search bar displays full-screen modal on smaller screens | 1. Reduce viewport size, 2. Click search icon | Full screen search modal appears, input field focused |
| Smaller screens navigation 📱 | All users | Navbar collapses correctly on mobile | 1. Reduce viewport size, 2. Click menu toggler, 3. Click each link | Menu opens/closes cleanly, no overlap, links usable |
| | | | |
| Category banner | All users | Category banner displayed on desktop and collapses into burger menu on mobile | 1. Open site on any page, 2. Observe category banner on desktop, 3. Reduce viewport size to mobile and observe burger menu | Category banner visible on desktop, burger menu appears on mobile, functions correctly |
| Category filtering/links | All users | Category links filter products correctly, links open correctly | 1. Click category from banner | Only category products display; heading matches category\ All displays all products |
| |
| Info banner | All users | Info banner displays correctly on all pages | 1. Open site on any page, 2. Observe info banner, 3. click on banner | Info banner visible with correct text and styling, scroll stops when hovered/clicked on |
| |
| Newsletter signup banner | All users | Newsletter signup banner displays correctly on all pages | 1. Open site on any page, 2. Observe newsletter signup banner, 3. Enter email and submit | Newsletter signup banner visible with correct text and styling, submission works correctly, validation message displayed |
| Duplicate email | All users | Duplicate email submission | 1. Enter already registered email and submit | Validation message displayed indicating email already registered |
| Invalid email | All users | Invalid email format submission | 1. Enter invalid email format and submit | Validation message displayed indicating invalid email format |
| Blank email | All users | blank email submission | 1. Leave email field blank and submit | Validation message displayed indicating email is required |
| Newsletter toggle | All users | Toggle newsletter banner visibility | 1. Click close chevron icon on newsletter banner | Banner collapses and chevron flips 180 degrees, when clicked again it displays the banner again |
| |
| Footer | All users | Footer Displays correctly on all pages, responsive | 1. Open site on any page, 2. Observe footer, 3. Reduce viewport size to mobile and observe footer | Footer visible with correct text and styling on all pages, responsive on mobile |
| Footer links | All users | Footer links work correctly | 1. Click each footer link | Correct pages load without errors, external links open in a new tab, pointer cursor shown |
| |
| Back to top button ⬆️ | All users | Back to top button appears after scrolling and works correctly | 1. Scroll down any page, 2. Click back to top button | Button appears after scrolling down, clicking button scrolls page back to top smoothly |
</details>

<details>
<Summary><strong>Homepage</strong></Summary>

| Area | User Role | Test Scenario | Steps | Expected Result |
|------|-----------|---------------|-------|-----------------|
| Homepage 🏡 | All users | Homepage loads correctly with all sections visible | 1. Open homepage | All sections visible (hero, unique selling points, featured products (best sellers, new arrivals) | 
| Product link | All users | clicking on any product image/name navigates to product detail page | 1. Click on any product image in featured products section | Correct product detail page loads without errors | 
| View all button | All users | View all products button works, hover effects | 1. Click View all products button | Button hover effect works, clicking button navigates to products page |
| Explore/Browse button | All users | Explore/Browse products button works, hover effects | 1. Click Explore/Browse products button | Button hover effect works, clicking button navigates to products page |
| Find out more button | All users | Find out more buttons work, hover effects | 1. Click Find out more button... | Button hover effect works, clicking button navigates to about us page |
| Learn more button | All users | Learn more button works, hover effects | 1. Click Learn button | Button hover effect works, clicking button navigates to product origins intro page |
</details>

<details>
<Summary><strong>Allauth/Authentication Tests</strong></Summary>

<strong> Login/Registration/Logout Tests 🔐 </strong>

| Area | User Role | Test Scenario | Steps | Expected Result |
|------|-----------|---------------|-------|-----------------|
| Registration with email📝 | Guest | Registration works with valid input | 1. Complete registration form, 2. Select sign up button  | User created; redirected to confirm email page, display alert message|
| Duplicate | Guest | Registration with existing email/existing username | 1. Complete registration form with existing email, 2. Select sign up button | Validation message displayed indicating email already registered |
| Facebook OAuth | Guest | Registration/Login via Facebook OAuth works | 1. Click 'Sign up with Facebook' button, 2. Complete Facebook OAuth flow | User created/logged in; redirected appropriately; no errors |
| Google OAuth | Guest | Registration/Login via Google OAuth works | 1. Click 'Sign up with Google' button, 2. Complete Google OAuth flow | User created/logged in; redirected appropriately; no errors |
| Successful sign up/login 🔓 | Guest | User can log in with valid credentials | 1. Enter valid username/email and password, 2. Click login/sign up | User logged in; redirected to homepage; success message displayed |
| Unsuccessful login ⛔️ | Guest | User cannot log in with invalid credentials | 1. Enter invalid username/email or password, 2. Click login/sign up | Validation message displayed indicating invalid credentials |
| Logout 🔒 | User | Logout works correctly | 1. Click logout button, 2. Redirected to confirmation, 3. Sign out/cancel button selected | Redirected to homepage with success message/no message if cancel selected |

OAuth authentication was tested using live Google and Facebook developer credentials to ensure real-world login flows function correctly.

<strong> Manage email / Change password Tests 🔐 </strong>

[/accounts/email/](https://munch-crunch-pantry-c0989406ec70.herokuapp.com/accounts/email/) - (You must be logged in to access this page)

| Area | User Role | Test Scenario | Steps | Expected Result |
|------|-----------|---------------|-------|-----------------|
| Change email address | User | Change email address with valid input | 1. Open profile page, 2. Click on manage email button, 3. enter a new email and click add email | Email updated, alert message displayed (confirmation sent), new email added to list |
| Remove/make primary email | User | Remove/make primary email address | 1.Click on remove/make primary email button next to email address | Email removed/made primary, alert message displayed |
| Removal/change of primary email | User - email unverified | Attempt to remove un-verified email address | 1. Click on radio button for the un-verified email, 2. Click make primary/remove button | Validation message displayed indicating email must be verified before change/removal |
| Only one email present | User | Attempt to remove only email address | No action required | Button is disabled, hover message displayed indicating at least one email required |
| Resend verification email | User | Re-send verification email works correctly | 1. Click on re-send verification email button | Email re-sent, alert message displayed, email received |
| Make primary | User | Make different verified email primary | 1. Click on radio button for different email, 2. Click make primary button | Primary email changed, alert message displayed |

[/accounts/password/change/](https://munch-crunch-pantry-c0989406ec70.herokuapp.com/accounts/password/change/) - (You must be logged in to access this page)

| Area | User Role | Test Scenario | Steps | Expected Result |
|------|-----------|---------------|-------|-----------------|
| Change password | User | Change password with valid input | 1. Open profile page, 2. Click on change password button, 3. enter current password, new password and confirm new password, 4. click change password button | Password changed, alert message displayed, user remains logged in, redirected to confirmation page |
| Incorrect current password | User | Attempt to change password with incorrect current password | 1. Enter incorrect current password, new password and confirm new password, 4. click change password button | Validation message displayed indicating incorrect current password |
| Mismatched new passwords | User | Attempt to change password with mismatched new passwords | 1. Enter correct current password, new password and different confirm new password, 4. click change password button | Validation message displayed indicating new passwords do not match |
| Weak new password | User | Attempt to change password with weak new password | 1. Enter correct current password, weak new password and confirm new password, 4. click change password button | Validation message displayed indicating new password is too weak |
| Blank fields | User | Attempt to change password with blank fields | 1. Leave one or more fields blank, 4. click change password button | Validation message displayed indicating required fields |

</details>

<details>
<Summary><strong>Profile Tests</strong></Summary>

| Area | User Role | Test Scenario | Steps | Expected Result |
|------|-----------|---------------|-------|-----------------|
| Profile page 🧑‍💼 | User | Profile page loads correctly with all sections | 1. Click on my account in navbar, 2. click on My Profile | Your account page loads successfully, displays Your details/ Order History/ Your Queries. |
| Your details | User - registered but no orders placed | Your details section displays correctly without prepopulated data | 1. Open profile page as newly registered user - dependant on if the radio button on checkout page was selected to remember details | Your details section displays correctly with empty fields for first name, last name, email, phone number, address, postcode, town/city, country |
| Your details | User - with orders placed | Your details section displays correctly with prepopulated data | 1. Open profile page as user with orders placed | Your details section displays correctly with fields prepopulated with user's info |
| Details - validation | User | Your details section validates input correctly | 1. Enter invalid data in fields (e.g., invalid email format, non-numeric phone number), 2. Click save changes button | Validation messages displayed for invalid inputs |
| Details - successful update | User | Your details section updates successfully with valid input | 1. Enter valid data in fields, 2. Click save changes button | Details updated successfully, success message displayed |
| Order history | User - no orders placed | Order history section displays appropriate message when no orders placed | 1. Open profile page as user with no orders placed | Message displayed indicating no orders have been placed yet |
| Order history | User - with orders placed | Order history section displays list of orders correctly | 1. Open profile page as user with orders placed | List of orders displayed with correct details (order number, date, total) |
| Order details | User | Order details link works correctly | 1. Click on order number link in order history section | Correct order details page loads without errors, alert message displayed confirming this is a previous order |
| Your queries | User - no queries submitted | Your queries section displays appropriate message when no queries submitted | 1. Open profile page as user with no queries submitted | Message displayed indicating no queries have been submitted yet |
| Your queries | User - with queries submitted | Your queries section displays list of queries correctly | | 1. Open profile page as user with queries submitted | List of queries displayed with correct details - date, subject, message dropdown - message displayed and response status |


</details>

<details>
<Summary><strong>All Products/Category Pages</strong></Summary>

| Area | User Role | Test Scenario | Steps | Expected Result |
|------|-----------|---------------|-------|-----------------|
| Products index | All users | Products page loads correctly with all sections visible | 1. Open products page | All sections visible (category filter, product grid, sorting options) |
| Page links | All users | Product card links work correctly | 1. Click on any product image in product grid, 2. Click on category tag, 3. Click on 'Products Home' | Correct product detail page loads without errors, 2. Directed to 'All products' page, 3. Directed to the relevant category page |
| Sort by | All users | Sorting options work correctly | 1. Select different sorting options from dropdown | Products sorted correctly based on selected option |
| No products in category | All users | If no products in category, appropriate message displayed | 1. Navigate to empty category page | Message displayed indicating no products available in this category |

</details>

<details>
<Summary><strong>Product Detail Page</strong></Summary>

| Area | User Role | Test Scenario | Steps | Expected Result |
|------|-----------|---------------|-------|-----------------|
| Product detail page | All users | Product detail page loads correctly with all sections visible | 1. Open any product detail page from products page | All sections visible (product images, name, price, description, add to basket button, reviews) |
| Navigation | All users | Keep shopping link works | 1. Click 'Keep shopping' link | Redirected to products page without errors |
| Category link | All users | Category tag link works | 1. Click on category tag | Redirected to relevant category page without errors |
| Rating link | All users | displays star rating, rating link works | 1. Click on rating link | Page scrolls down to reviews section |
| Product options | All users | Product options (size, quantity) work correctly | 1. Select different size/quantity options, hover effect when passing over and selection effect when once is selected | Selected options changes colour, and becomes obvious its selected  |
| Out of stock | All users | Out of stock products display appropriate message and selection disabled | 1. Open out of stock product detail page | Message displayed indicating product is out of stock, user unable to select |
| Quantity selector | All users | Quantity selector works correctly | 1. Increase/decrease quantity using buttons/input field | Quantity updates correctly based on user input, doesn't go below 1 |
| Add to basket - no selection | All users | Add to basket without selecting required options | 1. Try to click add to basket button without selecting required options | Validation message displayed indicating required options must be selected and button disabled |
| Add to basket - successful | All users | Add to basket with valid selections | 1. Select required options, 2. Click add to basket button | Product added to basket, success message displayed, basket preview displayed |
| Toast functionality |
| Success Toast | All users | Success toast displays correctly after adding to basket | 1. Add product to basket, 2. Success toast displayed showing the product, size, wty and total of basket | Toast appears with correct message |
| Go to basket button | All users | Go to basket button in toast works correctly | 1. Click go to basket button in success toast | Redirected to basket page without errors |
| Close toast button | All users | Close button in toast works correctly | 1. Click close button in success toast | Toast disappears smoothly |
| Product info accordion | All users | Product info accordion works correctly | 1. Click on each accordion header | Accordion expands/collapses correctly, content visible when expanded |
| Reviews |
| Review count | All users | Review count displays correctly | 1. Open product detail page with reviews | Review count displayed correctly based on number of reviews, matches number displayed at top of the page in brackets |
| Approved reviews | All users | Only approved reviews displayed | 1. Open product detail page with reviews | Only reviews that have been approved by admin are visible |
| No reviews | All users | Appropriate message displayed when no reviews | 1. Open product detail page with no reviews | Message displayed indicating no reviews yet |
| Your review | Guest | Log in link displayed for guest users | 1. Open product detail page as guest user | Log in link displayed in 'Your review' section, clicking link redirects to login page |
| Your review | User | Review form displayed for logged in users if they have purchased the item previously | 1. Open product detail page as logged in user who has purchased the item | Review form displayed correctly |
| Your review | User | Review form displayed for logged in users who have not purchased the product previously | 1. Open product detail page as logged in user who has not purchased the item | Message displayed indicating only users who have purchased the product can leave a review |
| Submit review | User | Submit review and rating with valid input | 1. Complete review form with valid input and select a rating, 2. Click submit review button | Review submitted successfully, success message displayed indicating review is pending approval |
| Review pending approval | User | Submitted review displayed as pending approval, edit and delete options available | 1. Submit review as logged in user, 2. Open product detail page again | Submitted review displayed with 'Pending approval' message,  |
| Edit review | User | Edit submitted review | 1. Submit review as logged in user, 2. Click edit button on pending review, 3. Update review content and rating, 4. Click save button | Page reloads and scrolls to review section, displays editable text in your reviews field, enter amendment, Review updated successfully, save changes button - success message displayed indicating review is pending approval, cancel button back to previous screen |
| Delete review | User | Delete submitted review | 1. Submit review as logged in user, 2. Click delete button in your reviews section, 3. Confirm modal displaying the review/rating being deleted | Review deleted successfully, success message displayed indicating review has been deleted |

</details>

<details>
<Summary><strong>Basket Tests</strong></Summary>

| Area | User Role | Test Scenario | Steps | Expected Result |
|------|-----------|---------------|-------|-----------------|
| Basket page 🛒 | All users | Basket page loads correctly with all sections visible | 1. Click on the basket icon in navbar/ 1. Add a product to basket, 2. Click on Go to your basket button | 
| Empty basket | All users | Appropriate message displayed when basket is empty | 1. Open basket page with no items in basket | Message displayed indicating basket is empty, link to continue shopping works correctly |
| Basket items | All users | Basket items display correctly with all details | 1. Open basket page with items in basket | Each basket item displays correct image, name, size, quantity, price, subtotal |
| Update quantity | All users | Update item quantity in basket works correctly | | 1. Change quantity of an item using input field/buttons, 2. Click update basket button | Item quantity updates correctly, subtotal and total update accordingly, success message displayed |
| Remove item | All users | Remove item from basket works correctly | 1. Click remove item button for an item, 2. Confirm remove item in confirmation modal/cancel modal | Item removed from basket, subtotal and total update accordingly, success message displayed \ no change made |
| Discount code | All users | Apply valid discount code works correctly | 1. Enter valid discount code in discount code field, 2. Click apply button | Discount applied successfully, total updates accordingly, success message displayed |
| Invalid discount code | All users | Apply invalid discount code | 1. Enter invalid discount code in discount code field, 2. Click apply button | Validation message displayed indicating invalid discount code |
| Blank discount code | All users | Apply blank discount code | 1. Leave discount code field blank, 2. Click apply button | Validation message displayed indicating discount code is required |
| Totals display | All users | Basket totals display correctly | 1. Open basket page with items in basket | Subtotal, discount (if applicable), and total display correctly based on basket contents |
| Delivery info | All users | Delivery info displays correctly based on basket total | 1. Open basket page with items in basket below/above free delivery threshold | Delivery info displays correct message based on basket total (e.g., amount needed for free delivery or confirmation of free delivery) |
| Continue shopping button | All users | Continue shopping button works correctly | 1. Click continue shopping button | Redirected to products page without errors |
| Proceed to checkout button | All users | Proceed to checkout button works correctly | 1. Click proceed to checkout button | Redirected to checkout page without errors |

</details>

<details>
<Summary><strong>Checkout/ Stripe </strong></Summary>

<strong> Order Summary, Details and Delivery Form 🛍️ </strong>

| Area | User Role | Test Scenario | Steps | Expected Result |
|------|-----------|---------------|-------|-----------------|
| Order summary panel | All users | Order summary panel displays correctly with all details | 1. Open checkout page with items in basket | Order summary panel displays correct product details (name, size, quantity, subtotal), order total, discount (if applicable) delivery cost, grand total |
| Checkout page | All users | Checkout page loads correctly with all sections visible | 1. Open checkout page with items in basket | All sections visible (details form, delivery options, order summary, payment section) |
| Complete payment button disabled | All users | Complete payment button disabled until all required fields completed | 1. Open checkout page, 2. Observe complete payment button state | Complete payment button is disabled initially, remains disabled until all required fields are completed |
| Details form | Guest | Details form validates input correctly | 1. Enter invalid data in fields (e.g., invalid email format, non-numeric phone number), 2. Click continue to payment button | Validation messages displayed for invalid inputs |
| Details form | User | Details form prepopulated with user's info | 1. Open checkout page as logged in user | Details form fields prepopulated with user's info |
| Email field | All users | Immediate validation if invalid email entered | 1. Enter invalid email format in email field, 2. Move focus away from email field | Validation message displayed indicating invalid email format |
| Phone number field | All users | Immediate validation if non-numeric phone number/insufficient numbers entered | 1. Enter non-numeric characters in phone number field, 2. Enter insufficient numbers, 3. Move focus away from phone number field | Validation message displayed indicating phone number must be numeric |
| Leaflet Address predictive search | All users | Leaflet Address predictive search works correctly | 1. Start typing address in address field, 2. Select address from dropdown | Address field populated with selected address, no errors |
| Type address manually | All users | Manually entering address works correctly | 1. Type full address manually in address field | Address field populated with manually entered address, no errors |
| Save details checkbox | User | Save details checkbox works correctly | 1. Check save details checkbox, 2. Complete order, 3. Open profile page | User's details saved and prepopulated in profile page |
| Prompt to sign up/login | Guest | Prompt to sign up/login displayed for guest users | 1. Open checkout page as guest user, 2. click on prompt links | Prompt displayed with links to login/register pages, redirects to correct page |
| Order confirmation email | All users | Order confirmation email sent after successful order | 1. Complete order successfully, 2. Check email inbox | Order confirmation email received with correct order details |


<strong> Stripe Payment Integration 💳 </strong>

| Area | User Role | Test Scenario | Steps | Expected Result |
|------|-----------|---------------|-------|-----------------|
| Stripe payment section | All users | Stripe payment section loads correctly with all elements visible | | 1. Open checkout page | Stripe payment section visible with card input fields, complete payment button |
| Validation short card details | All users | Validation message displays if the number is invalid/incomplete | 1. Enter short/invalid card number in card number field, 2. Move focus away from field | Validation message displayed indicating invalid/incomplete card number |
| Validation expired card | All users | Validation message displays if the card is expired | 1. Enter expired date in expiry field, 2. Move focus away from field | Validation message displayed indicating expired card |
| Payment with valid card details | All users | Payment processes successfully with valid card details | 1. Enter valid card details in Stripe payment section, 2. Click complete payment button | Payment processed successfully, redirected to order confirmation page, success message displayed |
| Payment with invalid card details | All users | Payment fails with invalid card details | 1. Enter invalid card details in Stripe payment section, 2. Click complete payment button | Payment fails, validation message displayed indicating payment error |
| Stripe webhooks | All users | Stripe webhooks process order correctly and finalize order after payment | 1. Run CLI listener locally, 2. Complete a payment, 3. Check webhook events fired | Relevant events received, order marked completed, confirmation email triggered |
| Duplicate prevention | All users | Refreshing success page does not duplicate order | 1. Complete payment, 2. Refresh order confirmation page/move back to checkout and resubmit | No duplicate orders created, user redirected to order confirmation page of original order |
| Failed payment redirection | All users | User redirected back to checkout page after failed payment | 1. Enter invalid card details in Stripe payment section, 2. Click complete payment button | User remains on checkout page, validation message displayed indicating payment error |
| Order success page | All users | Order confirmation page loads correctly with all sections visible | 1. Complete payment successfully | All sections visible (order summary, delivery info, thank you message) |
| Back button | All users | Basket emptied after successful order and back button redirects to products page | 1. Complete payment successfully, 2. Redirected to success page, 3. Click back button, 4. Redirected to products page | Basket emptied, redirected to products page without errors |

![Checkout Stripe Testing](/documentation/images/stripe-dashboard.png)

![Checkout Webhook Testing](/documentation/images/stripe-webhook-output.png)

![Checkout Webhook Events](/documentation/images/stripe-events-output.png)
</details>

<details>
<Summary><strong> Misc Pages - Pass ✅</strong></Summary>

| Area | User Role | Test Scenario | Steps | Expected Result |
|------|-----------|---------------|-------|-----------------|
| About us page | All users | About us page loads correctly with all sections visible | 1. Open about us page | All sections visible, 2. Test external links open in a new tab by clicking on the link, 3. Test buttons, hover effect and link to the appropriate page, 4. test origin story cards, links to relevant story page |
|Product origins intro page | All users | Product origins intro page loads correctly with all sections visible | 1. Open product origins intro page | All sections visible, 2. Test buttons, hover effect and link to the appropriate page, 3. test origin story cards, links to relevant story page |
| Story detail pages | All users | Story detail pages load correctly with all sections visible | 1. Open each story detail page from product origins intro page, 2. check Geoapify displays the correct country, 3. Ensure view button links to search view of products containing ' ' | All sections visible, custom content displayed as expected and button links to search result page with the product title populated |
| FAQs page | All users | FAQs page loads correctly with all sections visible | 1. Open FAQs page, 2. test accordion dropdowns, 3. test links and buttons | All sections visible, accordion functions correctly, links and buttons link to the correct pages |
| Privacy/TOS/Shipping/R&R pages | All users | Privacy/TOS/Shipping/R&R pages loads correctly with all sections visible | 1. Open Privacy/TOS page | All sections visible, no console errors, internal links to correct pages |
| Contact us page | All users | Contact us page loads correctly with all sections visible | 1. Open contact us page, 2. test form validation (empty fields, invalid email), 3. test successful submission | All sections visible, form validation works correctly, success message displayed on submission |
| Contact us - reply - email | All users | Contact us form sends email reply correctly | 1. Submit contact us form as user, 2. Admin - responds to query in the admin dashboard, 3. Check email inbox for reply | Email received with correct subject and message content |
| | User | Name and email panel prepopulated for logged in users | 1. Open contact us page as logged in user | Name and email fields prepopulated with user's info |
| | Admin | Contact us form submission records message in admin panel | 1. Submit contact us form as user, 2. Check admin panel for new message | Message recorded in admin panel with correct details |
| | All users | Contact success message displayed after submission | 1. Submit contact us form | Success message displayed confirming receipt of message |
</details>

<details>
<Summary><strong>Error pages</strong></Summary>

| Area | User Role | Test Scenario | Steps | Expected Result |
|------|-----------|---------------|-------|-----------------|
| 404 | All users | 404 error page loads correctly with all sections visible | | 1. Navigate to non-existent URL on site | 404 error page loads with correct styling and message, link to products works correctly |
| 500 | All users | 500 error page loads correctly with all sections visible | | 1. Simulate server error (e.g., raise exception in view) | 500 error page loads with correct styling and message, link to products works correctly |
| 400 | All users | 400 error page loads correctly with all sections visible | | 1. Simulate bad request (e.g., invalid form submission) | 400 error page loads with correct styling and message, link to products works correctly |

403 - As there are no Admin specific pages within the application on the front-end, a 403 error page test is not applicable. A page has been created for completeness, but no specific test scenarios have been defined.

</details>

<details>
<Summary><strong>S3 Media and Static Storage</strong></Summary>

| Area | User Role | Test Scenario | Steps | Expected Result |
|------|-----------|---------------|-------|-----------------|
| File served by AWS S3 | Admin | Static files served correctly from AWS S3 | 1. Open site, 2. Inspect network requests for static files | Static files (CSS, JS, images) served from AWS S3 without errors |
| ManifestFilesMixin | Admin | Confirm hashed filenames are used for static files | 1. Inspect static file URLs in network requests | Static file URLs include hash values for cache busting |
| S3 bucket dashboard | Admin | Confirm files are uploaded to S3 bucket correctly | 1. Access AWS S3 bucket dashboard, 2. Check for presence of static and media files | Static and media files present in S3 bucket with correct structure |
| Media storage public | - | Media files are publicly accessible | 1. Access the file via its URL in incognito mode | Media file is accessible publicly (200) |

</details>

<details>
<Summary><strong>Admin</strong></Summary>

| Area | User Role | Test Scenario | Steps | Expected Result |
|------|-----------|---------------|-------|-----------------|
| Admin login 🔐 | Admin | Admin can log in with valid credentials | 1. Navigate to admin login page, 2. Enter valid credentials | Admin user is logged in and redirected to admin dashboard |
| Admin logout 🔒 | Admin | Admin can log out successfully | 1. Click logout button in admin dashboard | Admin user is logged out and redirected to admin login page |
| Accounts app - Email addresses | Admin | Admin can view and manage user email addresses | 1. Navigate to Accounts app in admin dashboard, 2. View and edit user email addresses | Admin can view, add, edit, and delete user email addresses without errors |
| Authentication app - Users | Admin | Admin can view and manage users | 1. Navigate to Authentication app in admin dashboard, 2. View and edit user details | Admin can view, add, edit, and delete users without errors |
| Checkout app - Orders | Admin | Admin can view and manage orders | 1. Navigate to Checkout app in admin dashboard, 2. View and edit order details | Admin can view, add, edit, and delete orders without errors |
| Newsletter app - Subscribers | Admin | Admin can view and manage newsletter subscribers | 1. Navigate to Newsletter app in admin dashboard, 2. View and edit subscriber details | Admin can view, add, edit, and delete subscribers without errors |
| Products app - Categories | Admin | Admin can view and manage product categories | 1. Navigate to Products app in admin dashboard, 2. View and edit product categories | Admin can view, add, edit, and delete product categories without errors |
| Products app - Nutrition metrics | Admin | Admin can view and manage Nutrition metrics| 1. Navigate to Products app in admin dashboard, 2. View and edit nutrition metrics | Admin can view, add, edit, and delete nutrition metrics without errors |
| Products app - Products | Admin | Admin can view and manage products | 1. Navigate to Products app in admin dashboard, 2. View and edit product details | Admin can view, add, edit, and delete products without errors |
| Products app - Quantities | Admin | Admin can view and manage product quantities | 1. Navigate to Products app in admin dashboard, 2. View and edit product quantities | Admin can view, add, edit, and delete product quantities without errors |
| Customer Support - Customer Queries | Admin | Admin can view and respond to customer queries | 1. Navigate to Customer Support app in admin dashboard, 2. View and respond to customer queries | Admin can view, respond to, and manage customer queries without errors |
| Reviews and Ratings - Reviews and Ratings | Admin | Admin can view and manage product reviews | 1. Navigate to Reviews and Ratings app in admin dashboard, 2. View and approve/reject reviews | Admin can view, approve, reject, and delete reviews without errors |
| Social accounts - Social Accounts | Admin | Admin can view and manage social accounts | 1. Navigate to Social accounts app in admin dashboard, 2. View and edit social account details | Admin can view, add, edit, and delete social accounts without errors |
| Social accounts - social application | Admin | Admin can view and manage social applications | 1. Navigate to Social accounts app in admin dashboard, 2. View and edit social application details | Admin can view, add, edit, and delete social applications without errors |
| Stories - Stories | Admin | Admin can view and manage product origin stories | 1. Navigate to Stories app in admin dashboard, 2. View and edit story details | Admin can view, add, edit, and delete stories without errors | 

</details>