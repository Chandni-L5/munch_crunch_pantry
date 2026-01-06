# Munch Crunch Pantry 

Munch Crunch pantry is an online ecommerce store dedicated to providing a wide variety of healthy wholefood snacks. Our mission is to promote wellness and healthy living by offering nutritious, delicious, and convenient snack options for people on the go.

Munch Crunch Pantry operates on a B2C (Business-to-Consumer) e-commerce model. The platform allows direct online sales of products sold by the business to individual consumers.

It features a user-friendly interface, secure payment processing, and a seamless shopping experience. Customers can browse through our catalog of snacks, read detailed product descriptions, and make secure purchases with ease.

Revenue is generated through direct online sales of the wholefoods products, particularly one-off consumer purchases.

## User Experience (UX) & Agile Planning and Development
### Goals & Objectives 
The aim of the Munch Crunch Pantry project is to develop a comprehensive e-commerce platform that caters to health-conscious consumers looking for convenient snack options. The primary goals and objectives include:
- A user-friendly online shopping experience for customers seeking healthy snacks.
- To provide detailed product information, including nutritional facts and ingredients, to help customers make informed choices
-  Providing the background story of the products and their journeys from across the world to their own pantry.
- To implement a secure and efficient checkout process that ensures customer data privacy and payment security.
- To create an admin interface that allows for easy management of products, orders, and customer information.
- To optimize the website for search engines to increase visibility and attract a broader audience.

### Target Audience & Brand Philosophy
The target audience for Munch Crunch Pantry includes health-conscious individuals, busy professionals, fitness enthusiasts, and anyone looking for convenient and nutritious snack options. The website aims to cater to a diverse demographic, including different age groups and dietary preferences.

The philosophy behind Munch Crunch Pantry is to promote healthy living by making nutritious snacks easily accessible to everyone. The website emphasizes the importance of whole foods and natural, sustainable, high quality and ethically sourced ingredients. In addition this philosophy strengthens customer trust and align to the platform with conscious consumer values.

### Scope
The B2C model is implemented through a number of core features that enhance the user experience and streamline the shopping process.

#### User/Customer Features:
- Responsive design for optimal viewing on various devices (desktops, tablets, smartphones).
- CRUD Functionality - Customers are able to log in, create accounts, view their past orders and leave reviews on products. 
- Authentication and account management - Users can register, log in, reset passwords, and manage their account details.
- Product browsing and search functionality - Users can browse products by categories and search for specific items.
- Detailed product pages - Each product has a dedicated page with images, descriptions, nutritional information and customer reviews.
- Shopping cart - Users can add products to their cart, view cart contents, update quantities, and remove items.
- Secure checkout process - Integration with Stripe for secure payment processing, order summary, and confirmation.
- Order history - Customers can view their past orders and order details.
- Customer reviews and ratings - Users can leave reviews and ratings for products they have purchased.

These features encourage repeat business and long-term customer retention, which are key objectives of the B2C e-commerce model.

#### Admin Features
- Admin dashboard - A dedicated interface for administrators to manage products, orders, and customer information, Admins can add, edit, and delete products, including images, descriptions, and pricing.

### Agile Development & Planning 
#### User Stories
The development and the planning of this project has been created with the Agile methodologies in mind throughout.

Epics have been condensed to bitesize user stories.

[📚 The epics can be viewed here](/documentation/epics.md)

[📓 The user stories can be viewed here](/documentation/user-stories.md)

#### Estimation
I have used the MoSCoW method to prioritize the user stories into Must have, Should have, Could have and Won't have for this project. These categories are also represented on the KanBan board, with coloured labels for easy reference by the development team. At the start of the project, 'Won't have' items will not be applied, but this will be reviewed at the end of the project for potential future implementations depending on the progress made. 

To support the estimation, I have also used story points based on a Fibonacci methodology to estimate the effort required for each user story. This allows for a more accurate assessment of the complexity and time needed for implementation and helps to guide prioritization and ordering of tasks during the development process.

#### Epic 1: User Account & Authentication

| Requirement | User Story | AC Numbers | Story Points | Complexity |
|------------|------------|------------|--------------|------------|
| 🟥 Must have | **1.1** Email Registration | AC1–AC5 | 5 | 🟡 Medium |
| 🟩 Could have | **1.2** Social Media Registration | AC1–AC3 | 5 | 🟡 Medium |
| 🟥 Must have | **1.3** Login / Logout | AC1–AC5 | 3 | 🟢 Low |
| 🟥 Must have | **1.4** Password Reset | AC1–AC6 | 5 | 🟡 Medium |
| 🟥 Must have | **1.5** Confirmation Emails | AC1–AC2 | 3 | 🟢 Low |
| 🟥 Must have | **1.6** User Profile Management | AC1–AC5 | 8 | 🔴 High |

---

#### Epic 2: Product Discovery & Shopping Experience

| Requirement | User Story | AC Numbers | Story Points | Complexity |
|------------|------------|------------|--------------|------------|
| 🟥 Must have | **2.1** Browse Categories | AC1–AC2 | 2 | 🟢 Low |
| 🟥 Must have | **2.2** Product Detail Page | AC1–AC3 | 5 | 🟡 Medium |
| 🟧 Should have | **2.3** Reviews | AC1–AC2 | 5 | 🟡 Medium |
| 🟧 Should have | **2.4** Admin Approves Reviews | AC1–AC3 | 3 | 🟢 Low |
| 🟩 Could have | **2.5** Discounts & Promotions | AC1–AC2 | 3 | 🟢 Low |
| 🟥 Must have | **2.6** Search Functionality | AC1–AC3 | 5 | 🟡 Medium |
| 🟧 Should have | **2.7** Filters | AC1–AC2 | 5 | 🟡 Medium |
| 🟥 Must have | **2.8** Admin CRUD | AC1–AC3 | 5 | 🟡 Medium |
| 🟥 Must have | **2.9** Admin Product Management | AC1–AC3 | 8 | 🔴 High |

---

#### Epic 3: Basket & Checkout

| Requirement | User Story | AC Numbers | Story Points | Complexity |
|------------|------------|------------|--------------|------------|
| 🟥 Must have | **3.1** Shopping Bag Summary | AC1–AC5 | 5 | 🟡 Medium |
| 🟥 Must have | **3.2** Adjust Bag Items | AC1–AC3 | 3 | 🟢 Low |
| 🟥 Must have | **3.3** Secure Checkout | AC1–AC3 | 8 | 🔴 High |
| 🟥 Must have | **3.4** Order Confirmation | AC1–AC2 | 3 | 🟢 Low |

---

#### Epic 4: Content, Marketing & Engagement

| Requirement | User Story | AC Numbers | Story Points | Complexity |
|------------|------------|------------|--------------|------------|
| 🟧 Should have | **4.1** About & Educational Content | AC1–AC2 | 3 | 🟢 Low |
| 🟩 Could have | **4.2** Certifications | AC1 | 2 | 🟢 Low |
| 🟩 Could have | **4.3** Admin Content Management | AC1–AC3 | 5 | 🟡 Medium |
| 🟩 Could have | **4.4** Newsletter Signup | AC1–AC2 | 2 | 🟢 Low |
| 🟩 Could have | **4.5** Newsletter Admin | AC1–AC2 | 3 | 🟢 Low |
| 🟧 Should have | **4.6** Contact Form | AC1–AC4 | 3 | 🟢 Low |

---

#### MoSCoW Summary

| Priority | Count | Percentage |
|--------|------|------------|
| 🟥 Must Have | 14 | **56%** |
| 🟧 Should Have | 5 | **20%** |
| 🟩 Could Have | 6 | **24%** |
| **Total** | 25 | 100% |

---

#### Story Point Summary

- **Must Have:** 68 story points  
- **Should Have:** 19 story points  
- **Could Have:** 20 story points  

**Total:** **107 story points** (including Could Have features)

---

#### Planning Rationale

During the planning stages, the MoSCoW priorities were distributed as **56% Must have**, **20% Should have**, and **24% Could have**.  
The total number of story points estimated for the project was **107**, including the Could have features.

This distribution aligns with Agile best practice and reflects the requirements of an e-commerce MVP, where authentication, product management, basket functionality, and secure checkout are essential for a viable product.

The implementation and prioritization of user stories as well as the acceptance criteria is recorded and tracked dynamically through the use of GitHub Projects Kanban board. The Kanban board records the user story, acceptance criteria and tasks. These are checked off as we progress through the project. 

Each issue recorded on the Kanban board has been assigned multiple labels depending on the MoSCoW priority and the epic it belongs to. This allows for easy tracking and filtering of tasks for the development team.

[📊 The board can be viewed here](https://github.com/users/Chandni-L5/projects/14)

### Database Design

The database for Munch Crunch Pantry has been designed to efficiently store and manage data related to products, users, orders, and other relevant information. The design follows a relational database model, ensuring data integrity and consistency. The main entities in the database include:
- Users & Profile
- Catalogue Products
- Content/ Brand
- Orders & Checkout
- Engagement 

#### ERD
The Entity-Relationship Diagram (ERD) below illustrates the relationships between the main entities in the Munch Crunch Pantry database. It shows how users, products, orders, and other related data are interconnected.

![ERD Diagram](/documentation/images/erd.png)

#### Relational Data Model
The relational data model for Munch Crunch Pantry is structured to support the e-commerce functionality of the website. PostgreSQL has been used as the database management system to implement the relational model in production.

The model is designed to handle various standard aspects of an e-commerce platform, such as user accounts, products catalog, reviews, shopping cart, orders, and payment processing. The relationships between tables are established using foreign keys to ensure data integrity and consistency whilst also reducing duplication of data

Some additional features that have been incorporated into the relational data model include:
- Nutritional information for products
- Product origin stories
- Customer reviews and ratings
- Newsletter subscriptions
- Discount codes and promotions
- Detailed order history
- Customer support history

#### Database Schema
The database schema for Munch Crunch Pantry is designed to efficiently store and manage data related to products, users, orders, and other relevant information. The schema follows a relational database model, ensuring data integrity and consistency. 

The schema includes primary keys for each table to uniquely identify records, as well as foreign keys to establish relationships between tables. This design allows for efficient querying and data retrieval, supporting the e-commerce functionality of the website.

##### Category → Product (1-to-many)
- A category can have multiple products, but each product belongs to only one category.
- Category uses a unique slug for clean, SEO friendly URLS
- Product has foreign key reference to Category

##### Product sizes and pricing (many-to-many)
- A product can have multiple sizes, and each size can be associated with multiple products.
- Each individual product size has its own price - Implemented through an intermediary table ProductQuantity that links products to their available sizes and prices.
- ProductQuantity has foreign key references to both Product and Quantity tables.

##### Product → NutritionLabel (1-to-1)
- Each product has one associated nutrition label, and each nutrition label corresponds to one product.
- Product has a foreign key reference to NutritionLabel.
- NutritionLabel contains multiple nutrition metrics (e.g., calories, fat, protein) stored in a separate NutritionMetric table.
- The separation between NutritionLabel and NutritionMetric allows for flexibility in adding or modifying nutrition metrics without altering the product table structure.

##### Review → Product/User (many-to-1)
- A product can have multiple reviews, and a user can write multiple reviews, but each review is associated with only one product and one user.
- Review has foreign key references to both Product and User tables.
- `rating_avg` and `rating_count` fields in Product table to store average rating and total number of reviews for quick access - particularly useful for displaying ratings on product listing pages.

##### User profile and customer contact messages
- Each user has one associated profile, and each profile corresponds to one user.
- User has a foreign key reference to Profile.
- Profile contains additional user information such as phone number and address.
- Contact messages are linked to users through a foreign key reference in the ContactMessage table.

##### OrderLineItem and Orders (checkout)
- An order line item represents a specific product and quantity within an order - Links to foreign keys for both Order and ProductQuantity.
- An order can have multiple line items, but each line item belongs to only one order.
- Order has foreign key reference to User.
- various details related to payment and shipping are stored in the Order table - linked to a single user as well as costing details, Stripe reference and basket snapshot.
- An order can have multiple line items, but each line item belongs to only one order.

##### Discounts
- Discount codes are stored in a separate Discount table, which includes fields for code, email of the user it is assigned to/email and order minimums.
- Discounts can be applied to orders during checkout, with the discount code linked to the Order table through a foreign key reference.

##### Newsletter Subscriptions
- Newsletter subscriptions are managed through a separate NewsletterSubscription table, which includes fields for email and subscription status.
- This is designed independently from the User table to allow for non-registered users to subscribe to the newsletter.


##### Origin Stories - Content Marketing 
- Origin stories are stored in a separate OriginStory table, which includes fields for title, content and origin country.
- Each origin story can be linked to multiple products, establishing a many-to-many relationship through an intermediary table ProductOriginStory that links products to their associated origin stories.

#### Summary 
- All tables have been designed with appropriate data types and constraints to ensure data integrity and consistency with the use of a numeric Primary Key. 
- Relationships between tables are established using foreign keys to support the e-commerce functionality of the website.
- Unique constraints have been applied where appropriate such as `Category.slug` and `Story.slug` to prevent duplicate entries and support consistent routing.
- The Join tables (ProductQuantity, NutritionLabel) effectively manage many-to-many relationships between products and their sizes/prices as well as allowing additional attributes to be stored in relation to products independently.

##### Benefits of this design: 
- **Normalization**: avoids repetition of product rows for every size or nutrient metric
- **Scalability**: allows for easy addition of new sizes, nutrient metrics, and other attributes without altering the core product table structure
- **Accurate ordering**: ensures that each order line item accurately reflects the selected product size and price at the time of purchase
- **Auditable discounts**: single use discount tracking prevents misuse
- **Flexibility**: allows for easy modification and expansion of the database schema as the e-commerce platform evolves.
- **Marketing-ready**: supports content marketing strategies through origin stories linked to products.

### Web Marketing Strategies

#### Search Engine Optimisation (SEO)
When considering SEO optimisation for the Munch Crunch Pantry website, I have implemented several strategies to improve the site's visibility and ranking on search engines. 

The goals was to identify high-intent keywords relevant to the healthy wholefoods niche, particularly to those looking for natural, global wholefoods that are ethically sourced and of high quality.

The research process involved brainstorming topics, generating keyword ideas from these topics, research search behaviors on Google, creating a list of short and long-tail keywords, and analyzing competitors' keywords. In addition I have looked into keyword volume and competition using tools such as [wordtracker.com](https://www.wordtracker.com/), [Ubersuggest](https://neilpatel.com/ubersuggest/) and [Google Keyword Planner](https://ads.google.com/home/tools/keyword-planner/).

![SEO Keyword Research](/documentation/images/seo-content/SEO-keywords.png)

<details>
<summary> Click to view screenshots of wordtracker.com searches </summary>

![Wordtracker Screenshot 1](/documentation/images/seo-content/wordtracker-screenshot1.png)
![Wordtracker Screenshot 2](/documentation/images/seo-content/wordtracker-screenshot2.png)
![Wordtracker Screenshot 3](/documentation/images/seo-content/wordtracker-screenshot3.png)
![Wordtracker Screenshot 4](/documentation/images/seo-content/wordtracker-screenshot4.png)

</details>
<details>
<summary> Click to view results of Ubersuggest keyword analysis </summary>

| No | Keyword                                   | Search Volume | SEO Difficulty |
|----|--------------------------------------------|----------------|----------------|
| 1  | wholefoods                                 | 12100          | 91             |
| 2  | nuts                                       | 27100          | 63             |
| 3  | nuts and seeds                             | 1300           | 52             |
| 4  | seeds                                      | 33100          | 82             |
| 5  | organic                                    | 12100          | 75             |
| 6  | ethically-sourced                          | 390            | 33             |
| 7  | vegan                                      | 135000         | 92             |
| 8  | healthy snacks                             | 49500          | 74             |
| 9  | superfoods                                 | 14800          | 58             |
| 10 | buy organic nuts and seeds online          | 0              | 4              |
| 11 | raw nuts and seeds uk                      | 10             | 5              |
| 12 | GMO                                        | 4400           | 32             |
| 13 | fried fruits                                | 70             | 47             |
| 14 | globally sourced                           | 1900           | 36             |
| 15 | ethical consumers                          | 2400           | 59             |
| 16 | fairtrade                                  | 18100          | 63             |
| 17 | sustainable                                | 40500          | 91             |
| 18 | vegan pantry staples delivered             | 0              | 4              |
| 19 | buy superfoods online uk                   | 10             | 5              |
| 20 | tropical pantry ingredients uk             | 0              | 4              |
| 21 | organic beans                              | 260            | 28             |
| 22 | lentils and grains uk                      | 0              | 4              |
| 23 | natural wholefoods from around the world   | 0              | 4              |
| 24 | fairtrade products for conscious shoppers  | 0              | 4              |
| 25 | fairtrade cocoa and sugar                  | 0              | 4              |
| 26 | fairtrade farming practices                | 0              | 12             |
| 27 | eco-friendly food products uk              | 0              | 4              |
| 28 | wholefoods online uk                       | 1900           | 65             |
| 29 | buy nuts online uk                         | 30             | 36             |
| 30 | organic nuts and seeds                     | 90             | 19             |
| 31 | dried fruits uk                            | 210            | 25             |
| 32 | superfoods online uk                       | 10             | 13             |
| 33 | organic wholefoods delivery                | 10             | 13             |
| 34 | healthy snacks online                      | 70             | 4              |
| 35 | bulk nuts and seeds uk                     | 10             | 36             |
| 36 | raw nuts uk                                | 20             | 44             |
| 37 | natural pantry ingredients                 | 0              | 12             |
| 38 | organic grains and legumes                 | 0              | 4              |
| 39 | world foods online uk                      | 20             | 36             |
| 40 | global pantry essentials                   | 0              | 12             |
| 41 | tropical dried fruits uk                   | 0              | 4              |
| 42 | organic seeds online                       | 70             | 65             |
| 43 | premium nuts and dried fruit               | 0              | 4              |
| 44 | vegan pantry staples                       | 20             | 43             |
| 45 | ethically sourced wholefoods               | 0              | 12             |
| 46 | buy dried fruits online uk                 | 0              | 4              |
| 47 | bulk wholefoods delivery                   | 0              | 12             |
| 48 | organic beans and lentils uk               | 0              | 4              |
| 49 | natural superfoods powder                  | 0              | 12             |
| 50 | health food store online uk                | 110            | 35             |
</details>

The keywords identified to be used throughout the application are based on the high relevance to the products offered, strong commercial intent, mix of difficulty levels and with a UK market focus. In addition some of the listed keywords link the brand values of ethical sourcing, sustainability and fairtrade practices.

The content on the website has been optimized by incorporating these keywords naturally into product descriptions, blog posts, meta tags, and other relevant areas of the site. This helps improve the site's relevance for search queries related to healthy wholefoods and increases the likelihood of attracting organic traffic from search engines.

##### Sitemap and Robots.txt
A robots.txt file has been used to guide search engine crawlers by restricting access to non-SEO and sensitive areas of the site such as authentication, checkout, basket, and admin pages.

 The public content pages remain crawlable, while static and media assets are explicitly allowed to ensure proper rendering and image indexing. A sitemap reference is included to support search engine discovery and indexing.

#### Content Strategy

User Requirements:
- High quality, accurate product information
- clear pricing and quantity details
- Confidence in the sourcing and ethical practices behind the products
- Easy navigation and search functionality to find specific products
- Secure and straightforward checkout process
- Reassurance that the products align with their dietary preferences and values
- Fast answers to common questions

Content:
- Detailed product descriptions highlighting key features, benefits, and nutritional information through structured product pages.
- Clear product categories and filters to help users easily find products based on their preferences.
- Origin stories linking to the people and communities behind the products.
- Trust signals such as certifications, customer reviews, and testimonials to build credibility.
- Customer support content including FAQs, shipping information, and return policies to address common concerns.

Internal Linking:
- Category pages linking to individual product pages.
- Hyperlinks within product descriptions to 'Origin stories' articles.
- Links from 'Origin stories' to recommended products.
- Navigation links to category pages 
- Footer links to important informational pages like FAQs and contact information.

External Linking:
- Links to certification bodies 
    - [Fairtrade](https://www.fairtrade.net/en.html)
    - [Soil Association](https://www.soilassociation.org/)
    - [Rainforest Alliance](https://www.rainforest-alliance.org/)
    - [Ethical Consumer](https://www.ethicalconsumer.org/)
- References to reputable sources for health benefits of ingredients used in products.
    - [NHS](https://www.nhs.uk/live-well/eat-well/how-to-eat-a-balanced-diet/eating-a-balanced-diet/)
    - [WHO](https://www.who.int/news-room/fact-sheets/detail/healthy-diet)
    - [healthline.com](https://www.healthline.com/nutrition/50-super-healthy-foods)

#### Social Media Strategy
 For this project, I have created a social media business profile on Facebook to promote the Munch Crunch Pantry brand and engage with potential customers. The Facebook page serves as a platform to share updates, product launches, promotions, and educational content related to healthy wholefoods.

 This approach aligns with the needs of the target audience, who are likely to be active on social media and interested in health and wellness topics. By maintaining an active presence on Facebook, Munch Crunch Pantry can build brand awareness, foster a community of health-conscious individuals, and drive traffic to the e-commerce website.

 If the project were to be developed further, I would consider expanding the social media strategy to include other platforms such as Instagram and TikTok, which are also popular among health-conscious consumers. This would allow for a broader reach and more diverse content formats, such as visually appealing images and videos showcasing the products and their benefits.

[Click here to view the Munch Crunch Pantry Facebook Page](https://www.facebook.com/profile.php?id=61583634615736&locale=en_GB)

 ![Munch Crunch Pantry Facebook Page](/documentation/images/facebook.png)

#### Email Marketing Strategy
For this project I plan to implement a simple but effective email marketing strategy using the third-party service, [Mailchimp](https://mailchimp.com/). This will allow me to create and manage a mailing list of customers and potential customers who are interested in receiving updates and promotions from Munch Crunch Pantry.

The project requirements dictate that only an option to sign up to a newsletter is to be implemented at this stage. However, if the project were to be developed further, I would consider expanding the email marketing strategy to include regular newsletters, promotional offers, and personalized recommendations based on customer preferences and purchase history.

## User Interface (UI) Design
### Colour Scheme
I used [color-hex](https://www.color-hex.com/) to compare and create a colour palette to apply to the creation of the logo of the Munch Crunch Pantry brand as well as the website design. The colours were chosen to represent health, vitality, and natural ingredients, aligning with the brand's focus on healthy wholefood snacks.

![Colour Palette](/documentation/images/colour-palette1.png)
![Colour Palette](/documentation/images/colour-palette2.png)

The colours have also been assessed using a contrast checker to ensure they pass all visibility checks and improve user experience. Please see the [Accessibility](#accessibility) section of of this document for results of the contrast checks.

### Typography
[Google Fonts](https://fonts.google.com/) are used to apply Montserrat for page headings and Montserrat Alternates for body text. These fonts were chosen for their modern and clean appearance, which enhances readability and user experience.

After opening up the project for feedback from fellow Code Institute students and alumni it was notes that the secondary font Montserrat Alternates was somewhat difficult to read from a neurodivergent perspective. Therefore I have changed the secondary front to Sansation, which is also a Google Font and has been designed specifically for improved readability.

![Typography Sample](/documentation/images/google-fonts.png)

### Imagery
Some of the images used throughout the site were sourced from [pexels.com](https://www.pexels.com/). Images from this source are licensed for free use. I have also used [Sora](https://sora.chatgpt.com/explore) to create some AI images.

 [befunky.com](https://www.befunky.com/) has been used to resize the images.

### Wireframes
Wireframes have been created with desktop, tablet and mobile viewports in mind. I have used [Canva](https://www.canva.com/) to plan the layout and user flow of the application.

<strong>
<details>
<summary> Homepage 🏡 </summary>

Desktop Viewport

![Homepage Wireframe - Desktop](/documentation/images/wireframes/wireframe-homepage-desktop.png) 

Tablet Viewport
![Homepage Wireframe - Tablet](/documentation/images/wireframes/wireframe-homepage-ipad.png)

Mobile Viewport
![Homepage Wireframe - Mobile](/documentation/images/wireframes/wireframe-homepage-mobile.png)

</details>

<details>
<summary> About us 📖</summary>

![About Us Wireframe - Desktop](/documentation/images/wireframes/wireframe-about.png)
</details>

<details>
<summary> Shop View/ All Products View 🏬 </summary>

![Shop View Wireframe](/documentation/images/wireframes/wireframe-product-view.png)

</details>

<details>
<summary> Product Detail Page 🥜 </summary>

Desktop Viewport

![Product detail page wireframe - desktop](/documentation/images/wireframes/wireframe-productpage-desktop.png)

Tablet Viewport

![Product detail page wireframe - tablet](/documentation/images/wireframes/wireframe-productpage-tablet.png)

Mobile Viewport

![Product detail page wireframe - mobile](/documentation/images/wireframes/wireframe-productpage-mobile.png)

Enlargement of the Product Details Section

![Product detail section enlargement wireframe](/documentation/images/wireframes/wireframe-info-enlargement.png)

</details>

<details>
<summary> Product Origin Page 🌍 </summary>

![Product Origin Wireframe](/documentation/images/wireframes/wireframe-product-origin.png)

</details>

<details>
<summary> Shopping Bag Preview 🛒 </summary>

![Shopping Bag Wireframe](/documentation/images/wireframes/wireframe-bag-preview.png)

</details>

<details>
<summary> Shopping Bag  🛍️ </summary>

![Shopping Bag Wireframe](/documentation/images/wireframes/wireframe-shopping-bag.png)

</details>

<details>
<summary> Checkout Page 🔐 </summary>

![Checkout Page Wireframe](/documentation/images/wireframes/wireframe-checkout.png)
</details>

<details>
<summary> Registration Page 📑 </summary>

![Registration Page Wireframe](/documentation/images/wireframes/wireframe-registration.png)

</details>

</details>

<details>
<summary> Login Page  🧑‍🧒</summary>

![Login Page Wireframe](/documentation/images/wireframes/wireframe-login.png)

</details>

</details>

<details>
<summary> Contact us Page 📧 </summary>

![Contact Us Wireframe](/documentation/images/wireframes/wireframe-contact.png)
</details>

</details>

<details>
<summary> Miscellaneous Pages 📦 </summary>

General planned format for other pages such as FAQ, Shipping Information, Returns & Refunds and error pages etc.

![miscellaneous pages Wireframe](/documentation/images/wireframes/wireframe-misc.png)
</details>
</strong> 

## Features
### Universal Features
### Account Management 
### Page Specific Features
#### Home Page
#### Products Page
#### Product Detail Page
#### Shopping Cart Page
#### Checkout Page

**Geoapify API Integration**

To improve the user experience during checkout, I implemented address autocomplete using the [Geoapify API](https://www.geoapify.com/). This allows the user to start typing their address and receive suggestions to complete it quickly. The form fields are then automatically populated based on the selected suggestion.

**Why?**
- Speeds up checkout process by reducing the time taken to enter address details manually.
- Reduces errors in address entry, leading to more accurate shipping information.
- Enhances user experience by providing a modern and convenient feature.

**API Integration Details**
- I created a free account on [Geoapify](https://www.geoapify.com/) to obtain an API key for address autocomplete functionality.
- The API key is securely stored in environment variables to prevent exposure in the codebase.
- On the frontend the key is exposed as a JS constant making it easy to change between development and production environments.
- The address autocomplete feature is implemented using JavaScript to interact with the Geoapify Places API
- A non-model field called `address_search` is added to the checkout form to capture the input from the user to predict their address.
  - As the user types, requests are sent to the Geoapify API to fetch address suggestions based on the input.
  - When a suggestion is selected, the corresponding address components are automatically populated in the form fields.
  - The Geoapify logic is encapsulated in a separate JavaScript static file and initialized on the checkout page only to avoid unnecessary API calls on other pages.
- This field is not submitted to the backend, only used for frontend address prediction and population of other fields.
- The rest of the address fields are still standard Django crispy form fields that are submitted to the backend for order processing. Each field can still be manually edited if needed.



#### Order Confirmation Page
#### User Profile Page
#### Admin Dashboard
### Features Left to Implement
### Defensive Design & Permissions
### Accessibility

During the designing and styling process of the website, I have kept in mind to aim to make the page as user friendly and accessible as possible. I have achieved this by:

* Semantic HTML -Use of descriptive alt attributes on the images used throughout the site. 
* Use of ARIA labels to improve accessibility for screen readers.
* Use of Bootstrap framework to ensure responsive design across different devices and screen sizes.
* Use of legible fonts and appropriate font sizes to enhance readability.
* Consistent navigation structure across all pages.
* Alt text for all images.
* I have checked the colour scheme used on the application using [colourcontrast.cc](https://colourcontrast.cc/) to assess the contrast of the colours used. 

<details>
<summary> Click to view results of colour contrast comparison</summary>

![Colour Contrast Results 1](/documentation/images/accessibility/color-contrast1.png)
![Colour Contrast Results 2](/documentation/images/accessibility/color-contrast2.png)
![Colour Contrast Results 3](/documentation/images/accessibility/color-contrast3.png)
![Colour Contrast Results 4](/documentation/images/accessibility/color-contrast4.png)
![Colour Contrast Results 5](/documentation/images/accessibility/color-contrast5.png)
![Colour Contrast Results 6](/documentation/images/accessibility/color-contrast6.png)
</details>

## Technologies Used

- **Frontend Languages:** - HTML, CSS, JavaScript, 
- **Backend Technologies:** - Python, Django, PostgreSQL
- **Version Control:** - Git, GitHub
- **Deployment Platform:** - Heroku
- **Payment Processing:** - Stripe
- **Cloud Storage:** - AWS S3 for static and media file storage
- **Administrative Interface:** - Django Admin
- **Additional Libraries & Packages:** - Bootstrap 5, Font Awesome, Geoapify API, Google Fonts, Django Allauth and Socialaccount, Crispy Forms, Pillow, Boto3, Django Storages, Psycopg2, Gunicorn, Django CKEditor, Django Countries, Leaflet JS library

## Deployment

## Testing
### Automated Testing

The Munch Crunch Pantry project includes a comprehensive suite of automated tests to ensure the reliability and correctness of its core functionality. The tests cover various aspects of the application, including utility functions, views, forms, and webhook handling. The tests are implemented using Django's built-in testing framework, which provides a robust and efficient way to validate the application's behaviour.

```markdown
This output confirms that all 36 automated tests pass successfully, including
error-handling scenarios such as simulated email delivery failure.


>bash
python3 manage.py test
Found 36 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
...........Failed to send contact email: boom
.........................
--------------------------------------------------------
Ran 36 tests in 2.171s

OK
Destroying test database for alias 'default'...
```


#### Basket App Tests
Most utility functions were tested indirectly through view, form, and webhook tests where they are used in critical flows such as checkout and order creation.

Utility tests were implemented for discount-handling logic to ensure pricing integrity during checkout.

The get_discount_amount() helper was tested to confirm valid discount codes are correctly applied, invalid or expired codes are safely rejected and removed from session data, and default values are returned when no discount is present.

This ensures discounts cannot be incorrectly applied or persisted, protecting order totals and checkout accuracy.

#### Checkout App Tests

The tests focus on the most critical parts of the purchase flow: creating Stripe PaymentIntents, caching checkout metadata, validating incoming webhooks, and ensuring successful payments reliably create orders and line items.

What was tested:
- Create Payment Intent (View)
  - Verified that if the basket is empty, `create_payment_intent` returns **HTTP 400** and **does not call Stripe** (`stripe.PaymentIntent.create` is mocked).

 This protects the checkout flow from invalid requests and prevents unnecessary Stripe API calls.

- Cache Checkout Data (View)
  - Confirmed `cache_checkout_data` returns **HTTP 200** and calls `stripe.PaymentIntent.modify()` exactly once (mocked), ensuring metadata such as `save_info` is correctly stored against the PaymentIntent before payment confirmation.

- Webhook Endpoint (View)
  - Tested that invalid JSON posted to the webhook returns **HTTP 400**, ensuring the endpoint fails safely.
  - Tested that valid webhook payloads are passed through Stripe’s event validation (`stripe.Webhook.construct_event` mocked), then correctly dispatched to the relevant handler method (e.g., `handle_payment_intent_succeeded`) on `StripeWH_Handler`.

- Webhook Handler (Business Logic)
  - Using a minimal `ProductQuantity` setup (Category → Product → Quantity → ProductQuantity), confirmed a `payment_intent.succeeded` event with basket metadata:
    - returns **HTTP 200**
    - creates exactly **one Order**
    - creates exactly **one OrderLineItem**
    - stores the correct email and line item quantity.
  - Tested resilience logic where the handler retries up to **5 times** to locate an existing order before creating a new one (`time.sleep` mocked and counted). This helps prevent duplicate orders during delayed/async webhook processing.

- OrderForm Validation
  - Confirmed the checkout form enforces required fields by verifying `full_name` is required and returns validation errors when missing.

**Mocking approach**
Stripe calls were mocked throughout the suite (`PaymentIntent.create`, `PaymentIntent.modify`, `Webhook.construct_event`, `Charge.retrieve`) so tests run quickly, deterministically, and without external API dependence, while still verifying that the integration points are called correctly.

#### Home App Tests
Automated tests were implemented to verify correct template rendering and robust error handling within the Home app.

Tests confirm that:

- The newsletter banner is correctly included in the base template and rendered on the home page, including the newsletter form markup and associated JavaScript file
- The contact view gracefully handles email-sending failures by displaying a user-friendly error message instead of crashing
- The contact page is re-rendered with the correct template when an email error occurs
- Email failure handling is tested using mocking to simulate an exception during the email send process, ensuring the application remains stable even when external services fail.

These tests help ensure a reliable user experience and defensive error handling across key user-facing pages.

#### Profiles App Tests
Automated tests were implemented for the UserProfile and ContactMessage models to ensure correct default behaviour, signal handling, and string representations.

Tests confirm that:
- A UserProfile is automatically created whenever a new user account is registered, via a post_save signal
- The UserProfile string representation correctly returns the associated user’s username
- ContactMessage instances default to a status of “new” upon creation
- Optional fields on ContactMessage (including user profile, order number, and email) can be left blank without causing errors
- The ContactMessage string representation outputs a clear, readable summary used in the admin interface

These tests help ensure reliable user profile management and safe handling of customer contact submissions throughout the application.

#### Reviews App Tests
The Review model is covered by automated tests to ensure correct default behaviour, data integrity, and custom query logic.

Tests confirm that:
- Default fields are set correctly on creation, including moderation status and timestamps
- The model’s string representation outputs a clear, user-friendly format used in the frontend
- Each user can submit only one review per product, enforced via a database-level unique constraint
- The approved_for_product() helper method returns only approved reviews for a given product

All tests use a minimal valid Product instance and Django’s built-in user model to reflect real application behaviour while keeping tests lightweight and maintainable.

#### Stories App Tests
Automated unit tests were implemented for the Story model to ensure its core behaviour, field constraints, and metadata function correctly. These tests help maintain data integrity, support predictable application behaviour, and prevent regressions as the project evolves.

- Default Field Values
    - Confirms that newly created stories are unpublished by default (is_published = False).
    - Verifies that the created_at timestamp is automatically populated when a story is created.
- String Representation
    - Ensures the __str__() method returns the story’s title.
    - This provides clear, human-readable object labels within the Django admin interface and during debugging.
- Slug Generation and Persistence
    - Verifies that a URL-friendly slug is automatically generated from the story title when no slug is provided.
    - Confirms that an existing slug is preserved and not overwritten if the title is later changed, ensuring stable URLs.

- Model Ordering
    - Validates that stories are ordered alphabetically by title by default, as defined in the model’s Meta.ordering configuration.
- Required Field Validation
    - Confirms that the origin_country field is mandatory.
    - Verifies that attempting to save a story without an origin country fails validation, enforcing consistent and complete data entry.

#### Products App Tests
I created automated unit tests for the products app (models and constraints) and run them using python3 manage.py test products to ensure data integrity and model behaviour remain correct as the project evolves.

The tests cover:
- Category model string representation
- Product model string representation
- Quantity model string representation
- ProductQuantity model string representation and unique_together constraint
- NutritionMetric model string representation
- NutritionLabel model string representation and unique_together constraint

They ensure that the models behave as expected and that data integrity is maintained through unique constraints. In addition these checks are repeatable as the project develops further. The full directory of products have not been included in the early stages and as more products are added, the integrity of the data entered in relation to products can be verified through the same tests.

### Manual Testing

The following manual tests were carried out to assess **functionality, usability, responsiveness and data management** across the full application.

**Scope**:
The manual testing covers the user journey across the entire e-commerce application, from browsing products to checkout and order confirmation, as well as public pages, authentication, reviews, newsletter and also admin management.

**Test Environments**:
- Local development - Django development server
- Deployed production - Heroku live site
- Browsers: Chrome, Firefox, Edge, Safari
- Device Breakpoints: Desktop (≥1024px), Tablet (768px), Mobile (≤480px)

**Tester Roles**:
- Guest (not logged in)
-  User (registered and logged in)
-  Admin (Django admin user)

| Feature | Guest | User | Admin |
|---------|-------|------|-------|
|Access to profile page|❌|✅|❌|
|Access to admin dashboard|❌|❌|✅|
|Order history view|❌|✅|✅|
|Product review submission|❌|✅|✅|
|Newsletter signup|✅|✅|✅|
|Moderation of reviews|❌|❌|✅|
|Creation or amendments of reviews|❌|✅|✅|
|Product management|❌|❌|✅|
|Order management|❌|❌|✅|
|Contact form submission|✅|✅|✅|
|Contact message management|❌|❌|✅|
|Contact message record|❌|✅|✅|

#### Base Template Tests
| Area | User Role | Test Scenario | Steps | Expected Result | Actual Result |
|------|-----------|---------------|-------|-----------------|--------------|
| Navigation 🧭 | All users | Navbar links work and indicate current page | 1. Open site 2. Click Home icon, Menu - About us/ Product origins/Contact us, FAQs, My Account, Basket| Correct pages load, hover effects over selections, no console errors | Pass ✅ |
| New user | Guest | My account displays 'Log in' and 'Register' | 1. click on My account menu, 2. dropdown displays, click on options | 'Log in' and 'Register' options visible, correct pages load, hover effect over selections | Pass ✅ | 
| Existing user | User | My account displays 'My Profile' and 'Logout'| 1. click on My account menu, 2. dropdown displays, click on options | 'My Profile' and 'Logout' options visible, correct pages load, hover effect over selections | Pass ✅ |
| Search Bar 🔍 | All users | Search bar functions correctly | 1. Enter search term (e.g., 'hazelnut'), 2. Click search icon or press enter | Relevant products displayed, search term shown in results page | Pass ✅ |
| Empty input | All users | Search bar handles empty input | 1. Leave search bar empty, 2. Click search icon or press enter | returns all products | Pass ✅ |
| No results | All users | Search bar handles no results | 1. Enter gibberish term (e.g., 'xyzabc'), 2. Click search icon or press enter | User feedback shown (e.g., 'No products found') | Pass ✅ |
| Full screen modal | All users | Search bar displays full-screen modal on smaller screens | 1. Reduce viewport size, 2. Click search icon | Full screen search modal appears, input field focused | Pass ✅ |
| Smaller screens navigation 📱 | All users | Navbar collapses correctly on mobile | 1. Reduce viewport size, 2. Click menu toggler, 3. Click each link | Menu opens/closes cleanly, no overlap, links usable | Pass ✅ |
| | | | |
| Category banner | All users | Category banner displayed on desktop and collapses into burger menu on mobile | 1. Open site on any page, 2. Observe category banner on desktop, 3. Reduce viewport size to mobile and observe burger menu | Category banner visible on desktop, burger menu appears on mobile, functions correctly | Pass ✅ |
| Category filtering/links | All users | Category links filter products correctly, links open correctly | 1. Click category from banner | Only category products display; heading matches category\ All displays all products | Pass ✅ |
| |
| Info banner | All users | Info banner displays correctly on all pages | 1. Open site on any page, 2. Observe info banner, 3. click on banner | Info banner visible with correct text and styling, scroll stops when hovered/clicked on | Pass ✅ |
| |
| Newsletter signup banner | All users | Newsletter signup banner displays correctly on all pages | 1. Open site on any page, 2. Observe newsletter signup banner, 3. Enter email and submit | Newsletter signup banner visible with correct text and styling, submission works correctly, validation message displayed | Pass ✅ |
| Duplicate email | All users | Duplicate email submission | 1. Enter already registered email and submit | Validation message displayed indicating email already registered | Pass ✅ |
| Invalid email | All users | Invalid email format submission | 1. Enter invalid email format and submit | Validation message displayed indicating invalid email format | Pass ✅ |
| Blank email | All users | blank email submission | 1. Leave email field blank and submit | Validation message displayed indicating email is required | Pass ✅ |
| Newsletter toggle | All users | Toggle newsletter banner visibility | 1. Click close chevron icon on newsletter banner | Banner collapses and chevron flips 180 degrees, when clicked again it displays the banner again | Pass ✅ |
| |
| Footer | All users | Footer Displays correctly on all pages, responsive | 1. Open site on any page, 2. Observe footer, 3. Reduce viewport size to mobile and observe footer | Footer visible with correct text and styling on all pages, responsive on mobile | Pass ✅ |
| Footer links | All users | Footer links work correctly | 1. Click each footer link | Correct pages load without errors, external links open in a new tab, pointer cursor shown | Pass ✅ |
| |
| Back to top button ⬆️ | All users | Back to top button appears after scrolling and works correctly | 1. Scroll down any page, 2. Click back to top button | Button appears after scrolling down, clicking button scrolls page back to top smoothly | Pass ✅ |

#### Homepage Tests 
| Area | User Role | Test Scenario | Steps | Expected Result | Actual Result |
|------|-----------|---------------|-------|-----------------|--------------|
| Homepage 🏡 | All users | Homepage loads correctly with all sections visible | 1. Open homepage | All sections visible (hero, unique selling points, featured products (best sellers, new arrivals) | Pass ✅ | 
| Product link | All users | clicking on any product image/name navigates to product detail page | 1. Click on any product image in featured products section | Correct product detail page loads without errors | Pass ✅ | 
| View all button | All users | View all products button works, hover effects | 1. Click View all products button | Button hover effect works, clicking button navigates to products page | Pass ✅ |
| Explore/Browse button | All users | Explore/Browse products button works, hover effects | 1. Click Explore/Browse products button | Button hover effect works, clicking button navigates to products page | Pass ✅ |
| Find out more button | All users | Find out more buttons work, hover effects | 1. Click Find out more button... | Button hover effect works, clicking button navigates to about us page | Pass ✅ |
| Learn more button | All users | Learn more button works, hover effects | 1. Click Learn button | Button hover effect works, clicking button navigates to product origins intro page | Pass ✅ |

#### Authentication Tests
| Area | User Role | Test Scenario | Steps | Expected Result | Actual Result |
|------|-----------|---------------|-------|-----------------|--------------|
| Registration with email📝 | Guest | Registration works with valid input | 1. Complete registration form, 2. Select sign up button  | User created; redirected to confirm email page, display alert message| Pass ✅ |
| Duplicate | Guest | Registration with existing email/existing username | 1. Complete registration form with existing email, 2. Select sign up button | Validation message displayed indicating email already registered | Pass ✅ |
| Facebook OAuth | Guest | Registration/Login via Facebook OAuth works | 1. Click 'Sign up with Facebook' button, 2. Complete Facebook OAuth flow | User created/logged in; redirected appropriately; no errors | Pass ✅ |
| Google OAuth | Guest | Registration/Login via Google OAuth works | 1. Click 'Sign up with Google' button, 2. Complete Google OAuth flow | User created/logged in; redirected appropriately; no errors | Pass ✅ |
| Successful sign up/login 🔓 | Guest | User can log in with valid credentials | 1. Enter valid username/email and password, 2. Click login/sign up | User logged in; redirected to homepage; success message displayed | Pass ✅ |
| Unsuccessful login ⛔️ | Guest | User cannot log in with invalid credentials | 1. Enter invalid username/email or password, 2. Click login/sign up | Validation message displayed indicating invalid credentials | Pass ✅ |
| Logout 🔒 | User | Logout works correctly | 1. Click logout button, 2. Redirected to confirmation, 3. Sign out/cancel button selected | Redirected to homepage with success message/no message if cancel selected | Pass ✅ |

OAuth authentication was tested using live Google and Facebook developer credentials to ensure real-world login flows function correctly.

#### All Products/Category Pages
| Area | User Role | Test Scenario | Steps | Expected Result | Actual Result |
|------|-----------|---------------|-------|-----------------|--------------|
| Products index | All users | Products page loads correctly with all sections visible | 1. Open products page | All sections visible (category filter, product grid, sorting options) | Pass ✅ |
| Page links | All users | Product card links work correctly | 1. Click on any product image in product grid, 2. Click on category tag, 3. Click on 'Products Home' | Correct product detail page loads without errors, 2. Directed to 'All products' page, 3. Directed to the relevant category page | Pass ✅ |
| Sort by | All users | Sorting options work correctly | 1. Select different sorting options from dropdown | Products sorted correctly based on selected option | Pass ✅ |
| No products in category | All users | If no products in category, appropriate message displayed | 1. Navigate to empty category page | Message displayed indicating no products available in this category | Pass ✅ |

#### Product Detail Page
| Area | User Role | Test Scenario | Steps | Expected Result | Actual Result |
|------|-----------|---------------|-------|-----------------|--------------|
| Product detail page | All users | Product detail page loads correctly with all sections visible | 1. Open any product detail page from products page | All sections visible (product images, name, price, description, add to basket button, reviews) | Pass ✅ |
| Navigation | All users | Keep shopping link works | 1. Click 'Keep shopping' link | Redirected to products page without errors | Pass ✅ |
| Category link | All users | Category tag link works | 1. Click on category tag | Redirected to relevant category page without errors | Pass ✅ |
| Rating link | All users | displays star rating, rating link works | 1. Click on rating link | Page scrolls down to reviews section | Pass ✅ |
| Product options | All users | Product options (size, quantity) work correctly | 1. Select different size/quantity options, hover effect when passing over and selection effect when once is selected | Selected options changes colour, and becomes obvious its selected  | Pass ✅ |
| Out of stock | All users | Out of stock products display appropriate message and selection disabled | 1. Open out of stock product detail page | Message displayed indicating product is out of stock, user unable to select | Pass ✅ |
| Quantity selector | All users | Quantity selector works correctly | 1. Increase/decrease quantity using buttons/input field | Quantity updates correctly based on user input, doesn't go below 1 | Pass ✅ |
| Add to basket - no selection | All users | Add to basket without selecting required options | 1. Try to click add to basket button without selecting required options | Validation message displayed indicating required options must be selected and button disabled | Pass ✅ |
| Add to basket - successful | All users | Add to basket with valid selections | 1. Select required options, 2. Click add to basket button | Product added to basket, success message displayed, basket preview displayed | Pass ✅ |
| Toast functionality |
| Success Toast | All users | Success toast displays correctly after adding to basket | 1. Add product to basket, 2. Success toast displayed showing the product, size, wty and total of basket | Toast appears with correct message | Pass ✅ |
| Go to basket button | All users | Go to basket button in toast works correctly | 1. Click go to basket button in success toast | Redirected to basket page without errors | Pass ✅ |
| Close toast button | All users | Close button in toast works correctly | 1. Click close button in success toast | Toast disappears smoothly | Pass ✅ |
| Product info accordion | All users | Product info accordion works correctly | 1. Click on each accordion header | Accordion expands/collapses correctly, content visible when expanded | Pass ✅ |
| Reviews |
| Review count | All users | Review count displays correctly | 1. Open product detail page with reviews | Review count displayed correctly based on number of reviews, matches number displayed at top of the page in brackets | Pass ✅ |
| Approved reviews | All users | Only approved reviews displayed | 1. Open product detail page with reviews | Only reviews that have been approved by admin are visible | Pass ✅ |
| No reviews | All users | Appropriate message displayed when no reviews | 1. Open product detail page with no reviews | Message displayed indicating no reviews yet | Pass ✅ |
| Your review | Guest | Log in link displayed for guest users | 1. Open product detail page as guest user | Log in link displayed in 'Your review' section, clicking link redirects to login page | Pass ✅ |
| Your review | User | Review form displayed for logged in users if they have purchased the item previously | 1. Open product detail page as logged in user who has purchased the item | Review form displayed correctly | Pass ✅ |
| Your review | User | Review form displayed for logged in users who have not purchased the product previously | 1. Open product detail page as logged in user who has not purchased the item | Message displayed indicating only users who have purchased the product can leave a review | Pass ✅ |
| Submit review | User | Submit review and rating with valid input | 1. Complete review form with valid input and select a rating, 2. Click submit review button | Review submitted successfully, success message displayed indicating review is pending approval | Pass ✅ |
| Review pending approval | User | Submitted review displayed as pending approval, edit and delete options available | 1. Submit review as logged in user, 2. Open product detail page again | Submitted review displayed with 'Pending approval' message,  | Pass ✅ |
| Edit review | User | Edit submitted review | 1. Submit review as logged in user, 2. Click edit button on pending review, 3. Update review content and rating, 4. Click save button | Page reloads and scrolls to review section, displays editable text in your reviews field, enter amendment, Review updated successfully, save changes button - success message displayed indicating review is pending approval, cancel button back to previous screen | Pass ✅ |
| Delete review | User | Delete submitted review | 1. Submit review as logged in user, 2. Click delete button in your reviews section, 3. Confirm modal displaying the review/rating being deleted | Review deleted successfully, success message displayed indicating review has been deleted | Pass ✅ |



#### Misc Pages
| Area | User Role | Test Scenario | Steps | Expected Result | Actual Result |
|------|-----------|---------------|-------|-----------------|--------------|
| About us page | All users | About us page loads correctly with all sections visible | 1. Open about us page | All sections visible, 2. Test external links open in a new tab by clicking on the link, 3. Test buttons, hover effect and link to the appropriate page, 4. test origin story cards, links to relevant story page | Pass ✅ |
|Product origins intro page | All users | Product origins intro page loads correctly with all sections visible | 1. Open product origins intro page | All sections visible, 2. Test buttons, hover effect and link to the appropriate page, 3. test origin story cards, links to relevant story page | Pass ✅ | 
| Story detail pages | All users | Story detail pages load correctly with all sections visible | 1. Open each story detail page from product origins intro page, 2. check Geoapify displays the correct country, 3. Ensure view button links to search view of products containing ' ' | All sections visible, custom content displayed as expected and button links to search result page with the product title populated | Pass ✅ |
| FAQs page | All users | FAQs page loads correctly with all sections visible | 1. Open FAQs page, 2. test accordion dropdowns, 3. test links and buttons | All sections visible, accordion functions correctly, links and buttons link to the correct pages | Pass ✅ |
| Privacy/TOS/Shipping/R&R pages | All users | Privacy/TOS/Shipping/R&R pages loads correctly with all sections visible | 1. Open Privacy/TOS page | All sections visible, no console errors, internal links to correct pages | Pass ✅ |
| Contact us page | All users | Contact us page loads correctly with all sections visible | 1. Open contact us page, 2. test form validation (empty fields, invalid email), 3. test successful submission | All sections visible, form validation works correctly, success message displayed on submission | Pass ✅ |
| | User | Name and email panel prepopulated for logged in users | 1. Open contact us page as logged in user | Name and email fields prepopulated with user's info | Pass ✅ |
| | Admin | Contact us form submission records message in admin panel | 1. Submit contact us form as user, 2. Check admin panel for new message | Message recorded in admin panel with correct details | Pass ✅ |
| | All users | Contact success message displayed after submission | 1. Submit contact us form | Success message displayed confirming receipt of message | Pass ✅ |

### Testing User Stories

In summary, the application implements a B2C direct-to-consumer e-commerce model, where individual customers can browse products, make secure online purchases, and manage their orders through a user-focused web platform. The system architecture, checkout flow, and feature set directly support this business model.

### Bugs & Fixes
I have encountered a few bugs during the development of this project. Below are some of the notable ones along with their fixes. In addition some further minor bugs were identified during the validation process and these have been documented in the [Lighthouse](#lighthouse) section of this README.

<details>
<summary> <strong> Checkout form data missing on Submit - Disabled fields are not posted </strong> </summary>

**Bug:**
During checkout, the order form was consistently failing validation with errors like:

```
full_name: This field is required.
email: This field is required.
phone_number: This field is required.
```

etc.
This was occurring even when the user had filled in the fields.

**Evidence:**
A debug log confirmed the issue: `Order form invalid ... This field is required.`, indicating that the backend was receiving empty required fields on `POST`.

**Cause:**
The issue was created by the checkout JavaScript code disabling the entire form during the Stripe payment processing:
- `toggleFormDisabled(true);`
- `card.update({ 'disabled': true });`
This prevented disabled fields from being included in the form submission, leading to missing data on the server side.

This caused the disabled fields to not be posted to the server, resulting in validation errors for required fields. When Stripe returned a successful payment, and a native submit is triggered on the form, the disabled fields were not included in the POST data and Django only received the `CSRFmiddlewaretoken`.

**Fix:**
To resolve this, I modified the JavaScript to re-enable the form fields immediately before submitting the form:

```javascript
if (paymentIntent && paymentIntent.status === "succeeded") {
        toggleFormDisabled(false);
        const form = document.getElementById("payment-form");
        HTMLFormElement.prototype.submit.call(form);
    } else {
        showError("Payment did not complete. Please try again.");
        resetProcessingState();
    }
  ```

  This means the form is still locked out during payment processing, but is re-enabled just before submission, ensuring all fields are included in the POST data.

  Django is able to validate and create the order successfully once all required fields are present, allowing the checkout flow to complete. The user is successfully redirected to the order confirmation - `checkout_success` page after payment.

</details>

<details>
<summary><strong>Stripe payment processing issue</strong></summary>

**Bug and Evidence:**
When the Stripe payment processing was initiated during checkout, the page would become stuck on the loading spinner indefinitely, and the order would not complete, although the payment was successfully processed by Stripe when checking the Stripe dashboard.

In addition the order was not created in the database, and the user was not redirected to the order confirmation page. The network tab in dev chrome tools showed that the the form POST was never sent and JavaScript console errors showed:
```JavaScript
TypeError: form.submit is not a function
```

The caused a major disruption to the checkout flow, preventing users from completing their purchases.

When putting a fix in place to deal with this an additional issue was identified where the order form data was missing on submit. 

`403 Forbidden CSRF verification failed.`

**Cause**
form.submit was being overwritten by the element named "submit" in the form, causing the TypeError. As the submit button had the `id="submit"` attribute, it conflicted with the form's submit method and so the form was unable to be submitted resulting in the endless loading spinner.

**Fix**
To resolve this, I changed the way the form is submitted in the JavaScript code. Instead of calling `form.submit()`, I used:

```JavaScript
HTMLFormElement.prototype.submit.call(form);
```

This exposed a secondary related issue, where form fields were disabled during payment processing and therefore not included in the POST data. This is documented in detail in the Checkout form data missing on submit bug above. 

After implementing these changes, the checkout flow worked correctly. The form was successfully submitted, the order was created in the database, and the user was redirected to the order confirmation page after payment. The Console and network logs confirmed that there were no errors and the form POST was sent successfully:

```Console
ORDER CREATED: 44F685DF1EF64CCCA068DF93A5148E3A
POST /checkout/ 302
GET /checkout/success/.../ 200
```

</details>

<details>
<summary><strong>Delivery charge being applied to an empty basket</strong></summary>

**Bug and Evidence:**
When a user visited the site for the first time, where nothing would have been added to the basket yet, a delivery charge of £4.99 was being applied to the basket total. This created confusion and an incorrect total being displayed to the user can negatively impact user experience and trust.

![Basket with delivery charge applied to empty basket](/documentation/images/delivery_empty_basket.png)

**Cause:** The basket context processor applied the standard delivery charge whenever the basket total was below the free delivery threshold. If the basket total was £0.00 (empty basket), it would incorrectly meet this condition and apply the delivery charge. In addition the delivery and price calculations were mixing `float` and `Decimal` types which created rounding inconsistencies.

**Fix** 
I updated the basket context processor to explicitly check if the basket is empty before applying the delivery charge. If the basket total is £0.00, no delivery charge is applied, this was ensured by adding a guard condition to ensure that the delivery does not apply when the `product_count == 0`. The basket calculations were also refactored to use `Decimal` types consistently for all monetary values, preventing rounding errors. This aligns with Django `DecimalField` usage and ensures accurate financial calculations throughout the application.

</details>

<details>
<summary><strong>Bootstrap gutters - Unwanted white gaps at page edges</strong></summary>

**Bug and Evidence:**
When using the Bootstrap grid system, unwanted white gaps (gutters) were appearing at the edges of the page content. This created an inconsistent layout and detracted from the overall design aesthetic - particularly affecting the newsletter, banner and footer sections on desktop.

**Cause:**
The issue was caused by Bootstrap's default `.row` gutter behaviour, negative margins on `.row` elements created spacing between the row and its fluid parent container. This caused the content to overflow beyond the viewport edges, resulting in visible white gaps.

**Fix:**
By using bootstraps `g-0` class on the `.row` elements, the default gutter spacing was removed. This ensured that the row's content aligned flush with the parent container edges, eliminating the unwanted white gaps. The layout now appears consistent and visually appealing across different screen sizes.

</details>

<details>
<summary><strong>Country Flag Accessibility & HTML Validation Fix</strong></summary>

**Bug and Evidence:**
During HTML validation of the checkout page, the W3C validator flagged an error related to the use of the `img` element for displaying country flags in the country selection dropdown. The error indicated that the `img` tag was missing an `alt` attribute, which is required for accessibility compliance.

The image flag icon is the country flag icon which is automatically rendered by the `django-countries` package in the country select field. Although the flag is purely decorative and does not convey essential information, the absence of an `alt` attribute violates HTML standards and accessibility guidelines.

**Cause:**
At this stage of development of this project, the business only ships to the UK. Therefore displaying flags for other countries is not necessary and so this feature added very little value to the user experience. 

**Fix:**
The `django-countries` package does not provide a built-in way to customize or remove the flag icons from the country select field. 

To resolve this, the country field was hidden at form level. It is still present in the data model, but rendered as hidden on the user interface. The country is then set to "GB" (United Kingdom) by default in the checkout view when the form is instantiated.

This is to ensure the value is still submitted with the form, database integrity is maintained, and the HTML validation error is resolved. It also allows for future expansion to other countries if and when needed.

The final result means that with the `<img>` being hidden, the HTML validation error is resolved and the checkout page passes W3C validation without any accessibility issues.

</details>

<details>
<summary><strong>Newsletter banner – Removal of `localStorage` persistence</strong></summary>

**Bug and Cause**
During the initial implementation of the newsletter banner, I used `localStorage` to persist the user's dismissal of the banner across sessions. Once an email had been entered and submitted the banner was dismissed and would not reappear on subsequent visits.

When discussing this feature with my mentor Moritz, it was highlighted that this approach could lead to privacy concerns, as `localStorage` data persists across browser sessions, meaning a different user on the same device could be affected by the previous user's interaction with the banner. This could prevent new users from seeing the newsletter signup option, potentially reducing engagement and signups.

**Fix:**
To address this, I removed the `localStorage` persistence logic from the newsletter banner JavaScript code. Now, the banner will reappear on each new session or visit to the site, allowing all users to see and interact with it regardless of previous dismissals.

To hide the lower banner, I've added a simple close button that users can click to minimise the banner. This resolves the `localStorage` concern, whilst still providing a user-friendly way to manage the banner's visibility during their visit and enhance the overall view of the site.

In addition email subscription handling was implemented to store submitted emails in the database for future marketing use.

</details>

### Lighthouse

Lighthouse audits were conducted using Chrome DevTools on the deployed application to assess performance, accessibility, best practices, and SEO. The following table summarizes the Lighthouse scores for key page types on both desktop and mobile devices:

| Page Type | Performance | Accessibility | Best Practices | SEO |
|-----------|------------|---------------|----------------|-----|
| Home - Desktop | 94   | 84 | 96 | 100 |
| Home - Mobile | 81 | 84 | 92 | 100 |
| Products - Desktop |  |  |  |  |
| Products - Mobile  |  |  | | |
| Product Detail - Desktop| | | | |
| Product Detail - Mobile | | | | |
| Basket - Desktop|  |  |  |  |
| Basket - Mobile|  |  |  |  |
| Checkout - Desktop |  |  |  |  |
| Checkout - Mobile |  |  |  |  |


As this project is an e-commerce application, it is expected to be a an image-led and content heavy Django store frontend application. Therefore the performance scores are lower than a typical content-focused website. However, I have implemented several optimizations to improve load times and responsiveness, particularly on mobile devices.

All images are uploaded in WebP format to reduce file sizes without compromising quality. Lazy loading is implemented for product images to defer loading until they are in the viewport, improving initial load times. 

To improve accessibility scores, I have ensured that all images have descriptive alt attributes - relating to the name of the product it depicts, sufficient colour contrast is maintained throughout the site, and ARIA labels are used where appropriate to enhance screen reader compatibility.

**Accessibility Fix - ARIA labels for Newsletter Banner Toggle Caret**
A fix was put in place in the base template to improve accessibility by adding `aria-label` attributes to the toggle caret to collapse and expand the newsletter signup banner. I have set this dynamically in JavaScript to update based on the current state of the banner (expanded or collapsed). This provides screen reader users with clear context about the button's function and current state. As this element is present on all pages, this fix improves accessibility site-wide.

**CSS Minification**

To improve performance, CSS and JS files were minified to reduce file size and load times.
Original stylesheets were retained for readability and development, while minified versions were created for production use:

- `base.css` → `base.min.css`
- `home.css` → `home.min.css`
- `base.js` → `base.min.js`
- `checkout.js` → `checkout.min.js`

Minification was performed using a CSS minification tool from GitHub extensions - [MinifyAll](https://github.com/Josee9988/MinifyAll). This removes unnecessary whitespace, comments, and optimizes code structure without altering functionality.


### Validators

#### HTML Validation
All HTML files in this project have been validated using the [W3C Markup Validation Service](https://validator.w3.org/). Numerous iterations of validation and fixes were performed during development to ensure compliance with HTML5 standards. The final validation results show that all pages pass without any errors.

![screenshot of W3C validation results](/documentation/images/html-validation.png)

#### CSS Validation
All CSS used in this project has been validated using the [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) and all files passed without any errors.
<p>
    <a href="https://jigsaw.w3.org/css-validator/check/referer">
        <img style="border:0;width:88px;height:31px"
            src="https://jigsaw.w3.org/css-validator/images/vcss-blue"
            alt="Valid CSS!" />
    </a>
</p>

#### Python Validation
All Python code used in this project has been validated using the [Flake8 extension](https://flake8.pycqa.org/) in Visual Studio Code to ensure compliance with PEP 8 standards. This tool checks for style guide enforcement, code complexity, and potential errors and highlights issues immediately so can be dealt with during the development process.

I have also run the Python code through the [CI Python linter](https://pep8ci.herokuapp.com/). The final validation results show that all Python files pass without any errors.

#### JavaScript Validation
All JavaScript code used in this project has been validated using the [JSHint](https://jshint.com/) online tool to ensure compliance with JavaScript coding standards. This tool checks for potential errors and highlights issues immediately so can be dealt with during the development process. The final validation results show that all JavaScript files pass without any errors.

## Final Summary & Future Implementations



## Credits
### 
- [Chatgpt](https://chatgpt.com/) 
- [Google fonts](https://fonts.google.com/) 
- [Favicon.io](https://favicon.io/emoji-favicons/) - to create an emoji favicon
- [Leaflet JS](https://leafletjs.com) - to create the interactive map on origin stories pages
- [Geoapify](https://www.geoapify.com/) - to source map tiles and geocoding services for the interactive map
- [XML Sitemaps](https://www.xml-sitemaps.com/) - to create the sitemap for SEO purposes

### Media
- [AWS S3](https://aws.amazon.com/s3/) - to store static and media files
- [chatgpt](https://chatgpt.com/) - to create AI images
- [Font Awesome](https://fontawesome.com/)
- [befunky.com](https://www.befunky.com/dashboard/) - to resize images
- [Cloudconvert](https://cloudconvert.com/jpg-to-webp) - to convert images to different file types. 
- [toWebP](https://towebp.io/) - to convert different file types

### Documentation and Testing 
- [color-hex.com](https://www.color-hex.com/) - to display and compare colour palettes for the logo and website design.
- [Colourcontrast.cc](https://colourcontrast.cc/) - to check colour contrast ratios for accessibility compliance.
- [befunky.com](https://www.befunky.com/) - to edit and enhance images used in the project documentation.
I have used the following sources to help guide and structure the documentation of this project.
- [The love running readme template](https://github.com/Code-Institute-Solutions/readme-template?tab=readme-ov-file) 
- [A markdown cheat sheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#tables)
- [Kera Cudmore's readme template](https://github.com/kera-cudmore/readme-examples/blob/main/milestone1-readme.md) - shared on slack
- [Diffchecker](https://www.diffchecker.com/)
- [W3C](https://validator.w3.org/)
-[Autoprefixer](https://autoprefixer.github.io/)
- [Gyazo](https://gyazo.com/en) plugin- to create gifs to use in the testing documentation
- [Web Disability Simulator](https://chromewebstore.google.com/detail/web-disability-simulator/olioanlbgbpmdlgjnnampnnlohigkjla) 
- [Amiresponsive](https://ui.dev/amiresponsive) - to show the website on a range of device screens
- [Canva](https://www.canva.com/) - to create wireframes
- [Miro](https://miro.com/) - to create ERD diagram
- [wordtracker.com](https://www.wordtracker.com/)
- [Ubersuggest](https://neilpatel.com/ubersuggest/)  
- [Google Keyword Planner](https://ads.google.com/home/tools/keyword-planner/).
- [Mailchimp](https://mailchimp.com/)


### Resources

## Acknowledgements
- I would like to thank my mentor, Moritz, for their invaluable guidance and support throughout the development of this project. Their expertise and encouragement have been instrumental in helping me achieve my goals.

