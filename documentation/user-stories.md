# User Stories and Acceptance Criteria

## Epic 1: User Accounts & Authentication

### **1.1 Email Registration** (Issue #1)
**User Story:**  
As a shopper, I want to register an account using my email address so that I can access personalised features and save my details for future purchases.

**Acceptance Criteria:**
- AC1: Registration option visible from main navigation and login page  
- AC2: Registration form includes email, name, and password fields  
- AC3: Mandatory fields validated (email format, password strength)  
- AC4: Duplicate registrations using the same email are prevented  
- AC5: Success message displayed upon successful registration  

---

### **1.2 Social Media Registration** (Issue #9)
**User Story:**  
As a shopper, I want to register using my social media accounts so that I can quickly create an account without filling out lengthy forms.

**Acceptance Criteria:**
- AC1: Social registration options (Google, Facebook) available  
- AC2: Users redirected to provider authentication and back to the site  
- AC3: Successful registration redirects user to homepage with confirmation  

---

### **1.3 Login / Logout** (Issue #21)
**User Story:**  
As a returning shopper, I want to securely log in and log out so that I can manage my personal details and view my order history.

**Acceptance Criteria:**
- AC1: Login/logout option visible in main navigation  
- AC2: Login form includes email/username and password  
- AC3: Required fields validated  
- AC4: Error message shown for invalid credentials  
- AC5: Success message displayed on login/logout  

---

### **1.4 Password Reset** (Issue #18)
**User Story:**  
As a returning shopper, I want to reset my password if I forget it so that I can regain access to my account.

**Acceptance Criteria:**
- AC1: “Forgot Password” option available  
- AC2: Email field included in reset form  
- AC3: Email format validated  
- AC4: Password reset email sent  
- AC5: Secure password reset page provided  
- AC6: Password confirmation required  

---

### **1.5 Confirmation Emails** (Issue #20)
**User Story:**  
As a shopper, I want to receive confirmation emails for password resets and orders so that I have a record of my account activity.

**Acceptance Criteria:**
- AC1: Password reset email sent on request  
- AC2: Order confirmation email sent after successful purchase  

---

### **1.6 User Profile Management** (Issue #19)
**User Story:**  
As a returning shopper, I want to view my order history and save personal details so that checkout is faster and more convenient.

**Acceptance Criteria:**
- AC1: Order history accessible from account dashboard  
- AC2: Past orders displayed with details  
- AC3: Personal details can be saved  
- AC4: Saved details auto-populate checkout  
- AC5: Only authenticated users can access profile features  

---

## Epic 2: Product Discovery & Shopping Experience

### **2.1 Browse Categories** (Issue #17)
**User Story:**  
As a shopper, I want to browse products by category so that I can easily find items of interest.

**Acceptance Criteria:**
- AC1: Categories visible in navigation  
- AC2: Category selection displays relevant products  

---

### **2.2 Product Detail Page** (Issue #16)
**User Story:**  
As a shopper, I want to view detailed product information so that I can make informed purchasing decisions.

**Acceptance Criteria:**
- AC1: Dedicated product page with full details  
- AC2: “Add to Cart” button available  
- AC3: Out-of-stock message displayed when applicable  

---

### **2.3 Reviews** (Issue #15)
**User Story:**  
As a shopper, I want to read reviews from other customers so that I can decide whether a product is right for me.

**Acceptance Criteria:**
- AC1: Reviews and ratings displayed on product pages  
- AC2: Only authenticated purchasers can submit reviews  

---

### **2.4 Admin Approves Reviews** (Issue #14)
**User Story:**  
As an admin, I want to approve or delete reviews so that inappropriate content does not appear on the site.

**Acceptance Criteria:**
- AC1: Admin can view all reviews  
- AC2: Admin can approve or delete reviews  
- AC3: Feature restricted to admin users  

---

### **2.5 Discounts & Promotions** (Issue #10)
**User Story:**  
As a shopper, I want to see offers and promotions so that I can save money.

**Acceptance Criteria:**
- AC1: Promotions visible on homepage and product pages  
- AC2: Discounted prices clearly displayed  

---

### **2.6 Search Functionality** (Issue #13)
**User Story:**  
As a shopper, I want to search using keywords so that I can quickly find products.

**Acceptance Criteria:**
- AC1: Search bar visible and accessible  
- AC2: Relevant results returned  
- AC3: Clear “no results” message displayed  

---

### **2.7 Filters** (Issue #12)
**User Story:**  
As a shopper, I want to filter products so that I can narrow results to my preferences.

**Acceptance Criteria:**
- AC1: Filtering by category, price, popularity available  
- AC2: Product listings update dynamically  

---

### **2.8 Admin CRUD** (Issue #11)
**User Story:**  
As an admin, I want to add, edit, and delete products so that I can manage the product catalogue.

**Acceptance Criteria:**
- AC1: Admin can view all products  
- AC2: Admin can add, edit, and delete products  
- AC3: Restricted to admin users  

---

### **2.9 Admin Product Management** (Issue #8)
**User Story:**  
As an admin, I want to manage product data so that information remains accurate.

**Acceptance Criteria:**
- AC1: Admin can manage images, descriptions, stock, and pricing  
- AC2: Changes reflected immediately on frontend  
- AC3: Restricted to admin users  

---

## Epic 3: Basket & Checkout

### **3.1 Shopping Bag Summary** (Issue #22)
**User Story:**  
As a shopper, I want to view my bag summary so that I can manage my spending.

**Acceptance Criteria:**
- AC1: Bag icon shows item count and total  
- AC2: Summary dropdown displays bag contents  
- AC3: “View Bag” button available  
- AC4: Quantity adjustment and removal supported  
- AC5: Bag persists during session  

---

### **3.2 Adjust Bag Items** (Issue #23)
**User Story:**  
As a shopper, I want to adjust or remove items before checkout.

**Acceptance Criteria:**
- AC1: Quantity adjustment available  
- AC2: Remove button for each item  
- AC3: Totals update dynamically  

---

### **3.3 Secure Checkout** (Issue #24)
**User Story:**  
As a shopper, I want to securely enter payment details so that I can checkout with confidence.

**Acceptance Criteria:**
- AC1: Secure payment form provided  
- AC2: Stripe used for payment processing  
- AC3: Payment errors handled clearly  

---

### **3.4 Order Confirmation** (Issue #25)
**User Story:**  
As a shopper, I want to receive an order confirmation email so that I have a record of my purchase.

**Acceptance Criteria:**
- AC1: Confirmation email sent after purchase  
- AC2: Email includes full order summary  

---

## Epic 4: Content, Marketing & Engagement

### **4.1 About & Educational Content** (Issue #7)
**User Story:**  
As a shopper, I want to learn about the brand so that I can decide if it aligns with my values.

**Acceptance Criteria:**
- AC1: About section accessible from navigation  
- AC2: Values, sourcing, and benefits clearly communicated  

---

### **4.2 Certifications** (Issue #6)
**User Story:**  
As a shopper, I want to see certifications so that I can shop ethically.

**Acceptance Criteria:**
- AC1: Certifications displayed on product pages  

---

### **4.3 Admin Content Management** (Issue #5)
**User Story:**  
As an admin, I want to manage educational content so that information stays up to date.

**Acceptance Criteria:**
- AC1: Admin can add/edit content  
- AC2: Changes reflected immediately  
- AC3: Restricted to admin users  

---

### **4.4 Newsletter Signup** (Issue #4)
**User Story:**  
As a shopper, I want to sign up for newsletters so that I stay informed.

**Acceptance Criteria:**
- AC1: Signup form visible on homepage and footer  
- AC2: Email validation and error handling  

---

### **4.5 Newsletter Admin** (Issue #3)
**User Story:**  
As an admin, I want to manage newsletter subscribers.

**Acceptance Criteria:**
- AC1: Admin can view/add/remove subscribers  
- AC2: Restricted to admin users  

---

### **4.6 Contact Form** (Issue #2)
**User Story:**  
As a shopper, I want to contact support so that I can get help when needed.

**Acceptance Criteria:**
- AC1: Contact page accessible  
- AC2: Contact form with required fields  
- AC3: Confirmation shown on submission  
- AC4: Restricted to admin users  

---

## Agile Workflow Summary
- **Tooling:** GitHub Issues & Projects  
- **Methodology:** Agile / User-Story driven  
- **Validation:** Acceptance Criteria used to confirm completion  
- **Development:** Iterative, incremental delivery
