# Manual testing of the Acceptance Criteria of User Stories

### User Story 1.1 — Register with Email

| US ID | AC ID | Description | Test Steps | Expected Result | Pass/Fail |
|-------|-------|-------------|------------|-----------------|-----------|
| 1.1 | AC1 | Registration option visible | 1. Open homepage<br>2. Check main navigation<br>3. Open login page | "Sign up" visible on main navigation and login page | |
| 1.1 | AC2 | Registration form fields present | 1. Click "Sign up"<br>2. View registration form | Email + password fields visible (social login if enabled) | |
| 1.1 | AC3 | Input validation + error messages | 1. Submit invalid/empty form<br>2. Try invalid email<br>3. Try weak password | Errors displayed for invalid or missing input | |
| 1.1 | AC4 | Prevent duplicate registrations | 1. Register with Email A<br>2. Try registering again with Email A | Error: “Email already registered” | |
| 1.1 | AC5 | Successful registration | 1. Register with valid data<br>2. Submit |  success message shown | |
| 1.1 | AC6 | Social login option visible | 1. View registration page | Social login buttons (Google/Facebook/etc.) visible | |

### User Story 1.2 — Register Using Social Media

| US ID | AC ID | Description | Test Steps | Expected Result | Pass/Fail |
|-------|-------|-------------|------------|-----------------|-----------|
| 1.2 | AC1 | Social login options visible | 1. Open registration page | Social login buttons visible | |
| 1.2 | AC2 | Social login flow | 1. Click provider<br>2. Authenticate externally | User returned to site and account created | |
| 1.2 | AC3 | Successful social registration redirect | 1. Complete social registration | Success message | |

### User Story 1.3 — Login & Logout

| US ID | AC ID | Description | Test Steps | Expected Result | Pass/Fail |
|-------|-------|-------------|------------|-----------------|-----------|
| 1.3 | AC1 | Login/Logout visibility | 1. Open homepage logged out<br>2. Log in<br>3. Check nav | Logged out: Login visible<br>Logged in: Logout visible | |
| 1.3 | AC2 | Login form fields present | 1. Click "Login" | Email/username + password fields visible | |
| 1.3 | AC3 | Input validation | 1. Submit invalid/empty form | Correct validation errors shown | |
| 1.3 | AC4 | Incorrect credentials error | 1. Enter wrong details<br>2. Submit | Error shown; login not allowed | |
| 1.3 | AC5 | Successful login & logout | 1. Log in<br>2. Log out | Redirect to homepage with success messages | |

### User Story 1.4 — Reset Password

| US ID | AC ID | Description | Test Steps | Expected Result | Pass/Fail |
|-------|-------|-------------|------------|-----------------|-----------|
| 1.4 | AC1 | Forgot password link visible | 1. Open login page | “Forgot Password?” link visible | |
| 1.4 | AC2 | Reset form email field present | 1. Click link | Email input visible | |
| 1.4 | AC3 | Email validation | 1. Enter invalid email<br>2. Submit | Error displayed; reset not sent | |
| 1.4 | AC4 | Reset email sent | 1. Enter registered email<br>2. Submit | Password reset email received | |
| 1.4 | AC5 | Reset link opens secure page | 1. Open link from email | Secure “Set New Password” page visible | |
| 1.4 | AC6 | New password fields visible | 1. View reset form | New password + confirmation fields visible | |
| 1.4 | AC7 | Password validation | 1. Enter weak/mismatched passwords | Validation errors displayed | |
| 1.4 | AC8 | Confirmation email sent | 1. Successfully reset password | Confirmation email received | |
| 1.4 | AC9 | Redirect after reset | 1. Submit new password | Redirect to login page + success message | |

### User Story 1.5 — Confirmation Emails

| US ID | AC ID | Description | Test Steps | Expected Result | Pass/Fail |
|-------|-------|-------------|------------|-----------------|-----------|
| 1.5 | AC1 | Registration email sent | 1. Register new user | Confirmation email received | |
| 1.5 | AC2 | Password reset email sent | 1. Request reset | Reset email received | |
| 1.5 | AC3 | Order confirmation email sent | 1. Place an order | Email includes order summary | |

### User Story 1.6 — Account-Based Features

| US ID | AC ID | Description | Test Steps | Expected Result | Pass/Fail |
|-------|-------|-------------|------------|-----------------|-----------|
| 1.6 | AC1 | Order History visible | 1. Log in<br>2. Open account dashboard | “Order History” visible | |
| 1.6 | AC2 | Order History displays details | 1. Ensure user has orders<br>2. View Order History | Shows dates, totals, status, items | |
| 1.6 | AC3 | Save personal info | 1. Enter address/payment info<br>2. Save | Details stored | |
| 1.6 | AC4 | Checkout autofills saved info | 1. Save info<br>2. Go to checkout | Checkout fields pre-populated | |
| 1.6 | AC5 | Auth-only protection | 1. Log out<br>2. Try to access account URL directly | Redirect to login or permission denied | |

### User Story 2.1 — Browse Products by Categories

| US ID | AC ID | Description | Test Steps | Expected Result | Pass/Fail |
|-------|-------|-------------|------------|-----------------|-----------|
| 2.1 | AC1 | Category menu visible | 1. Open homepage<br>2. Locate category menu | Category menu is visible on homepage or main navigation | |
| 2.1 | AC2 | Category listing displays correct products | 1. Click a product category | Listing page shows only products within that category | |

### User Story 2.2 — View Product Details

| US ID | AC ID | Description | Test Steps | Expected Result | Pass/Fail |
|-------|-------|-------------|------------|-----------------|-----------|
| 2.2 | AC1 | Product detail page displays full info | 1. Open product listing<br>2. Click a product | Product page shows name, description, images, price, size, ingredients | |
| 2.2 | AC2 | Add to Cart button visible | 1. Open product detail page | “Add to Cart” button is displayed | |
| 2.2 | AC3 | Out-of-stock message displays correctly | 1. Set stock to 0 in admin<br>2. Open product page | “Out of Stock” displayed; cannot add to cart | |

### User Story 2.3 — View Product Reviews & Ratings

| US ID | AC ID | Description | Test Steps | Expected Result | Pass/Fail |
|-------|-------|-------------|------------|-----------------|-----------|
| 2.3 | AC1 | Reviews and ratings are visible | 1. Open product page with approved reviews | Reviews show reviewer name, rating, and written feedback | |
| 2.3 | AC2 | Review sorting options function | 1. Change sort filters (date, rating, helpfulness) | Reviews reorder correctly according to selected option | |
| 2.3 | AC3 | Only authenticated purchasers may review | 1. Try leaving review logged out<br>2. Try logged in without purchase<br>3. Try after purchasing | Only users who bought the product can leave a review | |

### User Story 2.4 — Admin Review Moderation

| US ID | AC ID | Description | Test Steps | Expected Result | Pass/Fail |
|-------|-------|-------------|------------|-----------------|-----------|
| 2.4 | AC1 | Admin can view all reviews | 1. Log in as admin<br>2. Navigate to Manage Reviews | All submitted reviews are visible | |
| 2.4 | AC2 | Admin can approve or delete reviews | 1. Approve one review<br>2. Delete another<br>3. Refresh product page | Approved review shows publicly; deleted review is removed | |

### User Story 2.6 — View Offers & Promotions

| US ID | AC ID | Description | Test Steps | Expected Result | Pass/Fail |
|-------|-------|-------------|------------|-----------------|-----------|
| 2.6 | AC1 | Promotions display correctly | 1. Apply promotion in admin<br>2. View homepage/product pages | Promotional badges or pricing appear correctly | |
| 2.6 | AC2 | Promotional pricing correctly displayed | 1. View discounted product | Original price + discounted price shown clearly (e.g., strikethrough) | |

### User Story 2.7 — Search for Products

| US ID | AC ID | Description | Test Steps | Expected Result | Pass/Fail |
|-------|-------|-------------|------------|-----------------|-----------|
| 2.7 | AC1 | Search bar visible | 1. Open homepage | Search bar is visible on navigation or homepage | |
| 2.7 | AC2 | Search returns matching results | 1. Search for keyword matching a product | Correct products appear with image, price, brief info | |

### User Story 2.8 — Filter Products

| US ID | AC ID | Description | Test Steps | Expected Result | Pass/Fail |
|-------|-------|-------------|------------|-----------------|-----------|
| 2.8 | AC1 | Filters are visible | 1. Open product listing page | Filters for price range, category, popularity, etc. are present | |
| 2.8 | AC2 | Filtering updates the product list | 1. Apply filter (e.g., price range) | Only products that match the filter are displayed | |
| 2.8 | AC3 | Filters can be cleared | 1. Apply filters<br>2. Click “Clear filters” | All filters reset and full product listing reappears | |

### User Story 2.9 — Admin Product Management

| US ID | AC ID | Description | Test Steps | Expected Result | Pass/Fail |
|-------|-------|-------------|------------|-----------------|-----------|
| 2.9 | AC1 | Product management page accessible | 1. Log in as admin<br>2. Open Product Management | All products are visible in admin listing | |
| 2.9 | AC2 | Admin can add, edit, delete products | 1. Add product<br>2. Edit product<br>3. Delete product | Add = product appears on site<br>Edit = updates show<br>Delete = product removed | |

### User Story 2.10 — Manage Product Images, Stock, Pricing

| US ID | AC ID | Description | Test Steps | Expected Result | Pass/Fail |
|-------|-------|-------------|------------|-----------------|-----------|
| 2.10 | AC1 | Admin can update product metadata | 1. Log in as admin<br>2. Edit product image, description, stock, price<br>3. Save | Updates successfully saved in admin | |
| 2.10 | AC2 | Public site reflects admin updates | 1. View updated product page | Page shows latest image, stock level, price, description | |

### User Story 3.1 — View Shopping Bag Summary

| US ID | AC ID | Description | Test Steps | Expected Result | Pass/Fail |
|-------|-------|-------------|------------|-----------------|-----------|
| 3.1 | AC1 | Bag icon shows item count + total | 1. Add items to bag<br>2. View main navigation | Bag icon displays correct item count and total cost | |
| 3.1 | AC2 | Bag summary dropdown/sidebar visible | 1. Click bag icon | Summary shows items, quantity, price, total | |
| 3.1 | AC3 | "View Bag" button works | 1. Open bag summary<br>2. Click "View Bag" | Redirects to full shopping bag page | |
| 3.1 | AC4 | Update/remove items directly from summary | 1. Increase quantity<br>2. Remove item from summary | Quantity updates and items removed correctly; totals recalculate | |

### User Story 3.2 — Adjust Items in Shopping Bag

| US ID | AC ID | Description | Test Steps | Expected Result | Pass/Fail |
|-------|-------|-------------|------------|-----------------|-----------|
| 3.2 | AC1 | Adjust item quantity on bag page | 1. Open shopping bag page<br>2. Increase/decrease quantity | Quantity updates and reflects in totals | |
| 3.2 | AC2 | Remove item from bag | 1. Click "Remove" on an item | Item is removed from bag list | |
| 3.2 | AC3 | Total updates dynamically | 1. Adjust quantities<br>2. Remove items | Total recalculates correctly after changes | |

### User Story 3.3 — Secure Payment & Checkout

| US ID | AC ID | Description | Test Steps | Expected Result | Pass/Fail |
|-------|-------|-------------|------------|-----------------|-----------|
| 3.3 | AC1 | Secure payment form visible | 1. Proceed to checkout page<br>2. View payment section | Card number, expiry date, CVV fields visible | |
| 3.3 | AC2 | Stripe processes valid payments | 1. Enter valid test card<br>2. Submit | Payment succeeds; order created | |
| 3.3 | AC3 | Stripe errors handled gracefully | 1. Use invalid test card<br>2. Submit | User receives clear error message; no order is created | |

### User Story 3.4 — Order Confirmation Email

| US ID | AC ID | Description | Test Steps | Expected Result | Pass/Fail |
|-------|-------|-------------|------------|-----------------|-----------|
| 3.4 | AC1 | Confirmation email is sent | 1. Complete a successful checkout | Order confirmation email received | |
| 3.4 | AC2 | Email contains order summary | 1. Open the confirmation email | Order number, items, totals, shipping info displayed | |

### User Story 4.1 — Access Brand Information & Educational Content

| US ID | AC ID | Description | Test Steps | Expected Result | Pass/Fail |
|-------|-------|-------------|------------|-----------------|-----------|
| 4.1 | AC1 | "About Us" section is visible and accessible | 1. Open navigation<br>2. Click "About Us" | About page loads successfully | |
| 4.1 | AC2 | Brand values, sourcing and benefits clearly displayed | 1. Open About page<br>2. Read conte

### User Story 4.2 — View Certifications on Product Pages

| US ID | AC ID | Description | Test Steps | Expected Result | Pass/Fail |
|-------|-------|-------------|------------|-----------------|-----------|
| 4.2 | AC1 | Certifications are displayed on product pages | 1. Assign certifications to a product in admin<br>2. Open product page | Eco-friendly / fair-trade badges appear alongside product info | |

### User Story 4.3 — Admin Content Management

| US ID | AC ID | Description | Test Steps | Expected Result | Pass/Fail |
|-------|-------|-------------|------------|-----------------|-----------|
| 4.3 | AC1 | Admin can access Content Management section | 1. Log in as admin<br>2. Open admin dashboard | Content Management section visible | |
| 4.3 | AC2 | Updates reflect instantly on the live site | 1. Edit content in admin<br>2. Save<br>3. View About/Info page | Changes visible immediately to users | |

### User Story 4.4 — Newsletter Signup

| US ID | AC ID | Description | Test Steps | Expected Result | Pass/Fail |
|-------|-------|-------------|------------|-----------------|-----------|
| 4.4 | AC1 | Newsletter form visible | 1. Open homepage<br>2. Scroll to footer | Newsletter signup form is displayed | |
| 4.4 | AC2 | Validation for email input works | 1. Submit empty form<br>2. Submit invalid email<br>3. Submit duplicate email | Appropriate error messages shown | |

### User Story 4.5 — Contact Customer Support

| US ID | AC ID | Description | Test Steps | Expected Result | Pass/Fail |
|-------|-------|-------------|------------|-----------------|-----------|
| 4.5 | AC1 | Contact page accessible from navigation/footer | 1. Open site navigation or footer<br>2. Click “Contact Us” | Contact page loads successfully | |
| 4.5 | AC2 | Contact form fields visible | 1. View contact form | Name, email, subject, and message fields are visible | |
| 4.5 | AC3 | Confirmation message displays after submission | 1. Fill in form with valid data<br>2. Submit | Confirmation message displayed (“Your message has been received”) | |