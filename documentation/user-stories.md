# User Stories

## Epic 1: 🔐 User Account & Authentication - Allows users to create and manage their personal accounts

### 1.1 - As a shopper, I want to register an account using my email address so that I can access personalized features/ save my details for future purchases.

<strong>AC1:</strong> The application should provide a registration option visible from main navigation and also the login page.

<strong>AC2:</strong> The registration form should include fields for email, name and password.

<strong>AC3:</strong> The application should indicate mandatory fields and validate input (e.g., valid email format, password strength) and provide an error message when invalid data is submitted.

<strong>AC4:</strong> The application should prevent duplicate registrations using the same email address.

<strong>AC5:</strong> Upon successful registration, the user should be redirected to the homepage and a success message should be displayed.

### 1.2 - As a shopper, I want to be able to register an account using my social media accounts so that I can quickly create an account without filling out lengthy forms.

<strong>AC1:</strong> The application should provide social media registration options (e.g., Google, Facebook) on the registration page.

<strong>AC2:</strong> Clicking on a social media registration option should redirect the user to the respective social media authentication page. Upon successful authentication, the user should be redirected back to the application and their account should be created using the information retrieved from the social media platform.

<strong>AC3:</strong> Upon successful registration via social media, the user should be redirected to the homepage and a success message should be displayed.

### 1.3 - As a returning shopper I want to securely log in and log out of my account so that I can view my order history and manage my personal details.

<strong>AC1:</strong> The application should provide a login/logout option visible from main navigation.

<strong>AC2:</strong> The login form should include fields for email/username and password.

<strong>AC3:</strong> The application should validate required fields and reject invalid formats or empty inputs.

<strong>AC4:</strong> The application should provide an error message when invalid credentials are submitted.

<strong>AC5:</strong> The user should be redirected to the homepage and a success message should be displayed upon successful login/logout.


### 1.4 - As a returning shopper, I want to reset my password in case I forget it so that I can regain access to my account.

<strong>AC1:</strong> The application should provide a "Forgot Password" option on the login page.

<strong>AC2:</strong> The password reset form should include a field for the registered email address.

<strong>AC3:</strong> The application should validate the email input (e.g., check for correct email format).

<strong>AC4:</strong> Upon submission, the application should send a password reset link to the provided email address if it is registered.

<strong>AC5:</strong> The password reset link should direct the user to a secure page to enter a new password.

<strong>AC6:</strong> The new password form should include fields for the new password and confirmation.

<strong>AC7:</strong> The application should validate the new password input (e.g., password strength, matching confirmation).

<strong>AC8:</strong> Upon successful password reset, the user should receive a confirmation email.

<strong>AC9:</strong> Upon successful password reset, the user should be redirected to the login page with a success message.

### 1.5 - As a shopper, I want to receive confirmation emails for account registration, password resets, and order confirmations so that I have a record of my transactions and account activities.

<strong>AC1:</strong> The application should send a confirmation email upon successful account registration.

<strong>AC2:</strong> The application should send a password reset email when a user requests to reset their password.

<strong>AC3:</strong> The application should send an order confirmation email upon successful purchase with a summary of the order.


### 1.6 - As a returning shopper, I want to access account-based features such as viewing order history and saving personal info for speedy checkout so that I can have a more convenient shopping experience.

<strong>AC1:</strong> The application should provide an "Order History" section accessible from the user's account dashboard.

<strong>AC2:</strong> The "Order History" section should display a list of past orders with details such as order date, items purchased, total amount, and order status.

<strong>AC3:</strong> The application should provide an option to save personal information (e.g., shipping address, payment details) in the user's account settings.

<strong>AC4:</strong> Saved personal information should be automatically populated during the checkout process for a faster experience.

<strong>AC5:</strong> Only authenticated users should have access to account-based features.


## Epic 2: 🛍️ Product Discovery - Enables users to browse and learn about the range of products available

### 2.1 - As a shopper, I want to browse products by categories so that I can easily find items of interest.

<strong>AC1:</strong> The application should provide a visible and accessible product categories menu on the main navigation or homepage.

<strong>AC2:</strong> Clicking on a category should display a list of products belonging to that category.

### 2.2 - As a shopper, I want to view detailed information about the products - description, ingredients, images, prices, size - so that I can make informed purchasing decisions.

<strong>AC1:</strong> Each product should have a dedicated product page accessible by clicking on the product from the product listing. The product page should display the product name, images, detailed description, ingredients, price, size, and any other relevant information.

<strong>AC2:</strong> The product page should include an "Add to Cart" button for easy purchasing.

<strong>AC3:</strong> The product page should display an 'out of stock' message if the stock level is 0.

### 2.3 - As a shopper, I want to view reviews and ratings of products by other shoppers so that I can make an informed purchasing decision.

<strong>AC1:</strong> Each product page should display customer reviews and ratings submitted by other shoppers. Reviews should include the reviewer's name, rating (e.g., star rating), and written feedback.

<strong>AC2:</strong> The application should provide an option for shoppers to sort reviews by date, rating, or helpfulness.

<strong>AC3:</strong> Only authenticated users should be able to submit reviews for products they have purchased.

### 2.4 - As admin, I want to approve or delete customer reviews so that I can monitor the content of feedback on the site.

<strong>AC1:</strong> The admin dashboard should include a "Manage Reviews" section where admins can view all submitted customer reviews.

<strong>AC2:</strong> Admins should have the ability to approve or delete reviews. Approved reviews should be visible on the respective product pages, while deleted reviews should be removed from public view.

<strong>AC3:</strong> Only admin users should be able to access this feature.

### 2.5 - As a shopper, I want to see offers and promotions on products so that I can take advantage of discounts and save money.

<strong>AC1:</strong> The application should display current offers and promotions on the homepage and relevant product pages.

<strong>AC2:</strong> Promotional prices should be clearly indicated alongside the original price on product listings and product pages.

### 2.6 - As a shopper, I want to search for specific items using keywords so that I can quickly find products I am interested in.

<strong>AC1:</strong> The application should provide a visible and accessible search bar on the main navigation or homepage.

<strong>AC2:</strong> The search functionality should return relevant product results based on the entered keywords, displaying product name, image, price, and a brief description.

<strong>AC3:</strong> If no products match the search criteria, the application should display a clear and informative message indicating that no results were found.

### 2.7 - As a shopper, I want to filter products based on preferences such as category, price range, and popularity so that I can find products that meet my needs.

<strong>AC1:</strong> The application should provide filtering options on the product listing pages, allowing users to filter by category, price range, popularity, and other relevant criteria.

<strong>AC2:</strong> Applying filters should dynamically update the product listing to show only products that meet the selected criteria.

### 2.8 - As admin, I want to add, edit, and delete products so that I can manage the product catalog effectively.

<strong>AC1:</strong> The admin dashboard should include a "Product Management" section where admins can view a list of all products.

<strong>AC2:</strong> Admins should have the ability to add new products , edit existing products and delete existing products. 

<strong>AC3:</strong> Only admin users should be able to access this feature.


### 2.9 - As admin, I want to manage product images, descriptions, stock levels and pricing so that I can ensure accurate and up-to-date product information is available to shoppers.

<strong>AC1:</strong> The "Product Management" section should provide options for admins to upload and manage product images, edit product descriptions, update stock levels, and adjust pricing.

<strong>AC2:</strong> Changes made by admins should be reflected on the public-facing product pages immediately upon saving.

<strong>AC3:</strong> Only admin users should be able to access this feature.


## Epic 3: 🛒 Shopping Bag & Checkout - Facilitates the shopping and payment process for users

### 3.1 - As a shopper, I want to view the status of my shopping bag to keep track of my spending so that I can manage my budget effectively.

<strong>AC1:</strong> The application should display a shopping bag icon in the main navigation that shows the number of items and total cost in the bag.

<strong>AC2:</strong> Clicking on the shopping bag icon should display a dropdown or sidebar with a summary of the items in the bag, including product names, quantities, individual prices, and total cost.

<strong>AC3:</strong> The shopping bag summary should include a "View Bag" button that directs users to the full shopping bag page for detailed review and checkout options.

<strong>AC4:</strong> Users should be able to increase the quantity or remove items directly from the shopping bag summary.

<strong>AC5:</strong> The shopping bag should persist through the browsing session until items are removed or purchased.

### 3.2 - As a shopper, I want to increase quantity or remove items in the shopping bag so that I can adjust my order before checkout.

<strong>AC1:</strong> The shopping bag page should display a list of items in the bag with options to increase or decrease the quantity of each item.

<strong>AC2:</strong> The shopping bag page should provide a "Remove" button for each item to allow users to delete items from the bag.

<strong>AC3:</strong> The total cost should update dynamically as quantities are adjusted or items are removed.

### 3.3 - As a shopper, I want to securely enter my payment details during checkout so that I can complete my purchase with confidence.

<strong>AC1:</strong> The checkout page should provide a secure payment form that includes fields for entering payment details (e.g., credit card number, expiration date, CVV).

<strong>AC2:</strong> The application should integrate with a secure payment gateway (Stripe) to process payments.

<strong>AC3:</strong> Errors from the payment gateway (e.g., invalid card details, insufficient funds) should be handled gracefully, providing clear error messages to the user.

### 3.4 - As a shopper, I want to receive a confirmation email containing an order summary on successful purchase so that I have a record of my transaction.

<strong>AC1:</strong> Upon successful purchase, the application should send a confirmation email to the shopper's registered email address.

<strong>AC2:</strong> The confirmation email should include an order summary with details such as order number, items purchased, total amount, and shipping information.

## Epic 4: 🎓 Brand Experience & Engagement - Enhances user experience by providing educational content about the brand and products

### 4.1 - As a shopper, I want to access additional content about the brand, their ethos and products so that I can learn more about their features and benefits and see if it aligns with my values.

<strong>AC1:</strong> The application should provide a dedicated or "About Us" section accessible from the main navigation. The "About Us" section should include educational content about the brand's ethos, product features, sourcing practices, and benefits.

<strong>AC2:</strong> The educational content should clearly communicate the brand's values, sourcing practices, and the health benefits of the products offered.

### 4.2 - As a shopper, I want to see eco-friendly and fair-trade certifications on product pages so that I can align my purchases with my values.

<strong>AC1:</strong> Each product page should display relevant eco-friendly and fair-trade certifications prominently alongside product information.

### 4.3 - As admin, I want to add and update educational content on the website so that I can keep shoppers informed about the brand and products.

<strong>AC1:</strong> The admin dashboard should include a "Content Management" section where admins can add, edit, and update educational content on the website.

<strong>AC2:</strong> Changes made by admins should be reflected on the public-facing website immediately upon saving.

<strong>AC3:</strong> Only admin users should be able to access this feature.

### 4.4 - As a shopper, I want to sign up to receive a newsletter so that I can stay updated on new products, promotions, and educational content.

<strong>AC1:</strong> The application should provide a visible and accessible newsletter signup form on the homepage and footer of the website.

<strong>AC2:</strong> The newsletter signup form should include a field for entering an email address and a "Subscribe" button. Error messages should be displayed for invalid email or empty submissions.

### 4.5 - As a shopper, I want to be able to contact customer support through the website so that I can get assistance with any issues or questions I may have.

<strong>AC1:</strong> The application should provide a "Contact Us" page accessible from the main navigation or footer of the website.

<strong>AC2:</strong> The "Contact Us" page should include a contact form with fields for name, email address, subject, and message.

<strong>AC3:</strong> Upon submission of the contact form, the user should receive a confirmation message indicating that their inquiry has been received.

<strong>AC4:</strong> Only admin users should be able to access this feature.