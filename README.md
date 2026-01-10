# Munch Crunch Pantry 

![Screenshot of amiresponsive design on various devices](/documentation/images/amiresponsive-display.png)

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

<details>
<summary><strong>Epic 1: User Account & Authentication</strong></summary>

| Requirement | User Story | AC Numbers | Story Points | Complexity |
|------------|------------|------------|--------------|------------|
| 🟥 Must have | **1.1** Email Registration | AC1–AC5 | 5 | 🟡 Medium |
| 🟩 Could have | **1.2** Social Media Registration | AC1–AC3 | 5 | 🟡 Medium |
| 🟥 Must have | **1.3** Login / Logout | AC1–AC5 | 3 | 🟢 Low |
| 🟥 Must have | **1.4** Password Reset | AC1–AC6 | 5 | 🟡 Medium |
| 🟥 Must have | **1.5** Confirmation Emails | AC1–AC2 | 3 | 🟢 Low |
| 🟥 Must have | **1.6** User Profile Management | AC1–AC5 | 8 | 🔴 High |

</details>

<details>
<summary><strong>Epic 2: Product Discovery & Shopping Experience</strong></summary>

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

</details>

<details>
<summary><strong>Epic 3: Basket & Checkout</strong></summary>

| Requirement | User Story | AC Numbers | Story Points | Complexity |
|------------|------------|------------|--------------|------------|
| 🟥 Must have | **3.1** Shopping Bag Summary | AC1–AC5 | 5 | 🟡 Medium |
| 🟥 Must have | **3.2** Adjust Bag Items | AC1–AC3 | 3 | 🟢 Low |
| 🟥 Must have | **3.3** Secure Checkout | AC1–AC3 | 8 | 🔴 High |
| 🟥 Must have | **3.4** Order Confirmation | AC1–AC2 | 3 | 🟢 Low |

</details>

<details>
<summary><strong>Epic 4: Content, Marketing & Engagement</strong></summary>

| Requirement | User Story | AC Numbers | Story Points | Complexity |
|------------|------------|------------|--------------|------------|
| 🟧 Should have | **4.1** About & Educational Content | AC1–AC2 | 3 | 🟢 Low |
| 🟩 Could have | **4.2** Certifications | AC1 | 2 | 🟢 Low |
| 🟩 Could have | **4.3** Admin Content Management | AC1–AC3 | 5 | 🟡 Medium |
| 🟩 Could have | **4.4** Newsletter Signup | AC1–AC2 | 2 | 🟢 Low |
| 🟩 Could have | **4.5** Newsletter Admin | AC1–AC2 | 3 | 🟢 Low |
| 🟧 Should have | **4.6** Contact Form | AC1–AC4 | 3 | 🟢 Low |

</details>

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

### [Wireframes](/documentation/wireframes.md)
Wireframes were created for desktop, tablet and mobile layouts in Canva. Full wireframes can be viewed [here](/documentation/wireframes.md).


## Features
### Universal Features
 These features are present on all pages of the website to ensure a consistent user experience and easy navigation throughout the site.

<details>
<summary><strong>Navigation Bar</strong></summary>

The navigation bar is designed to be responsive and user-friendly, providing easy access to key sections of the website. It includes links to the home page, product categories, user account management, shopping cart, and other important pages. There is also a search bar for quick product searches. The desktop version includes the categories as accessible links below the main navigation bar for improved usability.

Finally the scrolling info banner is the subsequent part to the navigation bar, providing users with important updates and promotions without taking up excessive space.

![Navigation Bar Desktop](/documentation/images/features/universal/nav-desktop.gif) 

The brand logo is prominently displayed on the left side of the navigation bar, serving as a clickable link that redirects users to the home page from any section of the website. This enhances brand recognition and provides a convenient way for users to return to the main page.

The menu icon on the right side of the navigation bar provides access to additional information pages - About us, Product Origins, Contact us and FAQs 

![Navigation Bar Menu](/documentation/images/features/universal/menu-desktop.png)

The account icon provides access to user account management features such as login, logout, registration and profile management.

![Navigation Bar Account - Logged out](/documentation/images/features/universal/account-desktop1.png)
![Navigation Bar Account - Logged in](/documentation/images/features/universal/account-desktop2.png)

The basket icon displays the current running total of items in the user's shopping cart, providing a quick overview of their selected products and facilitating easy access to the checkout process.

![Navigation Bar Mobile](/documentation/images/features/universal/nav-mobile.gif)

The navigation bar adapts to different screen sizes, ensuring a seamless experience on both desktop and mobile devices. On smaller screens, the navigation links collapse into a hamburger menu for easy access. To reduce the amount of space taken up on smaller screens, the category links are only visible on desktop viewports and so on smaller screens users can access categories via the main menu only. 

![Navigation burger menu mobile](/documentation/images/features/universal/burger-menu-features.png)

The search bar is also accessible from the navigation bar on all screen sizes, allowing users to quickly find products regardless of the device they are using. Further details of the search bar functionality can be found in the next section.

#### Related User Stories:
- **Epic 1 – User Accounts & Authentication**
  - 1.1 Email Registration
  - 1.2 Social Media Registration
  - 1.3 Login / Logout
  - 1.6 User Profile Management

- **Epic 2 – Product Discovery & Shopping Experience**
  - 2.1 Browse Categories

- **Epic 3 – Basket & Checkout**
  - 3.1 Shopping Bag Summary

</details>

<details>
<summary><strong>Search Bar</strong></summary>

The search bar is prominently located in the navigation bar, allowing users to quickly and easily search for products across the entire website. It features an input field where users can type their search queries and a search button to initiate the search.

The mobile version of the search bar is accessible via a search icon in the navigation bar. When clicked, it expands to a full page modal with a search input field and button, providing a user-friendly experience on smaller screens.

![Search bar modal on smaller screens](/documentation/images/features/universal/search-mobile-features.png)

The search functionality is designed to be intuitive and efficient, returning relevant results based on the user's input. It supports partial matches and is case-insensitive, ensuring that users can find products even if they do not know the exact name or spelling.

The search results page displays a list of products that match the search query, along with relevant details such as product images, names and prices. The page is headed to refer to the word being searched for, in addition a visual is displayed to confirm the number of products found containing that word. Initially the search results would also include products that contained the search word in the description, however after user testing it was found that this was returning too many irrelevant results. Therefore I have adjusted the search functionality to only return products that contain the search word in the product name.

![Search Results Page](/documentation/images/features/universal/search-result.png)

The search bar is also designed to provide validation feedback to users. If a user attempts to submit an empty search query, an error message is displayed prompting them to enter a valid search term. If there are no products matching the search query, a message is shown informing the user that no results were found.

#### Related User Stories:
- **Epic 2 – Product Discovery & Shopping Experience**
  - 2.6 Search Functionality

</details>

<details>
<summary><strong>Footer</strong></summary>
The footer is designed to provide users with easy access to important information and links, enhancing the overall user experience on the website. It includes several key sections:

- the newsletter signup form
- quick links to important pages
- social media icons linking to the Munch Crunch Pantry Facebook page, instagram and X (formerly Twitter) profiles

![Footer Desktop](/documentation/images/features/universal/footer-desktop.png)

The footer is responsive and adapts to different screen sizes, ensuring a seamless experience on both desktop and mobile devices. On smaller screens, the layout adjusts to stack the sections vertically for better readability and accessibility.

![Footer Mobile](/documentation/images/features/universal/footer-mobile.png)

An additional feature has been added to the newsletter signup form to allow the user to collapse and expand the form as needed. This helps to save space in the footer area while still providing easy access to the signup functionality.

![Footer Newsletter Collapse](/documentation/images/features/universal/newsletter-collapsed.png)

The newsletter signup form includes validation to ensure that users enter a valid email address before submitting. If the input is invalid, an error message is displayed prompting them to correct their entry. In addition if a user has already previously subscribed, as their email is stored in the database, they will be informed of this to prevent duplicate subscriptions.

#### Related User Stories:
- **Epic 4 – Content, Marketing & Engagement**
  - **4.4 Newsletter Signup** – allows users to subscribe and receive updates
  - **4.1 About & Educational Content** – quick links provide access to informational pages
  - **4.5 Contact Form** – footer links support access to customer support pages

</details>

<details>
<summary><strong>Toasts</strong></summary>
The application uses **Bootstrap toast notifications** to provide users with real-time feedback on their actions and interactions throughout the website. Toasts are small, non-intrusive messages that appear temporarily on the screen to inform users about the status of their actions, such as successful operations, errors, or important information.

There are four types of toasts implemented throughout the website:
- **Success Toasts**: Indicate that an action was completed successfully, such as adding an item to the cart or successfully logging in.
- **Error Toasts**: Alert users to issues or errors that occurred during an action, such as a failed login attempt or an invalid form submission.
- **Info Toasts**: Provide general information or updates to users, such as informing them about ongoing promotions or changes to the website.
- **Warning Toasts**: Caution users about potential issues or important considerations, such as low stock warnings or unsaved changes.

**Key Features:**
- Auto-Dismissal: Toasts automatically disappear after a set duration (e.g., 4 seconds), ensuring they do not obstruct the user's view for too long.
- Manual Dismissal: Users can manually close toasts by clicking on a close icon, providing control over their experience.
- Consistent Styling: Each type of toast has a distinct color scheme and iconography to quickly convey the nature of the message (e.g., green for success, red for error).
- Accessibility: Toasts are designed to be accessible, with appropriate ARIA roles and attributes to ensure they are announced by screen readers.

Toast notifications enhance the overall UX by delivering timely feedback in a lightweight and accessible way, aligning with modern e-commerce usability best practices.

#### Related User Stories:
- **Epic 1 – User Accounts & Authentication**
  - **1.1 Email Registration** – success and error feedback during account creation
  - **1.3 Login / Logout** – confirmation and error messages on authentication actions
  - **1.4 Password Reset** – feedback for reset requests and validation errors

- **Epic 2 – Product Discovery & Shopping Experience**
  - **2.3 Reviews** – confirmation when reviews are submitted or updated
  - **2.6 Search Functionality** – validation feedback for empty or invalid search queries

- **Epic 3 – Basket & Checkout**
  - **3.1 Shopping Bag Summary** – confirmation when items are added or updated
  - **3.2 Adjust Bag Items** – feedback for quantity updates or item removal
  - **3.3 Secure Checkout** – error and success messaging during checkout flow
</details>

<details>
<summary><strong>Other Universal Features</strong></summary>

#### Back to Top Button
A "Back to Top" button is implemented to enhance user navigation, especially on pages with extensive content. This button appears when the user scrolls down the page, providing a convenient way to quickly return to the top without having to manually scroll back up.

![Back to Top Button](/documentation/images/features/universal/back--to-top.gif)

</details>


### Account Management 

### Page Specific Features

<details>
<summary><strong>Home Page</strong></summary>

The homepage introduces users to Munch Crunch Pantry through a welcoming hero section that clearly communicates the brand’s purpose and values. A welcome message explains the brand philosophy on high-quality, natural wholefoods that are free from additives, helping users immediately understand what the site offers and why it can be trusted. This reinforces the philosophy of simple, honest ingredients and healthy eating, supporting user confidence and brand identity. 

Below the hero content, USPs (Unique Selling Points) are displayed in styled feature panels, drawing attention to important customer benefits such as free delivery thresholds, quality assurance, and sustainable sourcing. These visual cues help users quickly grasp the value proposition without needing to navigate away from the page.

There is also a dynamic button link to the products index page, making it easy for users to start browsing the product catalogue directly from the homepage.

![Homepage hero section](/documentation/images/features/homepage/homepage-hero.png)

The mid section of the page showcases featured product collections through **Best Sellers** and **New Arrivals**. The Best Sellers section displays the most highly rated products, while the New Arrivals section highlights the most recently added products. This provides social proof and helps returning users discover new items, keeping the homepage engaging and relevant.

Currently, the “View all” link directs users to the All Products page. In future development, dedicated collection pages for Best Sellers and New Arrivals could be introduced.

![Homepage featured products](/documentation/images/features/homepage/homepage-products.png)

The final section of the homepage provides links to other areas of the website, particularly the brand’s educational content. The “Browse products” button links to the product index page, “Find out more…” directs users to the About Us page, and “Learn about…” links to the Product Origins page, where users can read stories about the people and communities behind the products. These buttons are styled consistently with the site’s design and include hover effects to enhance interactivity.

![Homepage educational content links](/documentation/images/features/homepage/links-homepage.png)

---

#### Related User Stories:
- **Epic 2 – Product Discovery & Shopping Experience**
  - **2.1 Browse Categories** – clear calls to action guide users into browsing products
  - **2.2 Product Detail Page** – featured products link directly to detailed product pages
  - **2.5 Discounts** – USPs highlight delivery thresholds and value propositions

- **Epic 4 – Content, Marketing & Engagement**
  - **4.1 About & Educational Content** – homepage links to About Us and Product Origins pages
  - **4.4 Newsletter Signup** – homepage supports marketing and engagement goals through clear brand messaging and onward navigation

</details>

<details>
<summary><strong>Product Pages</strong></summary>

The product pages are designed as indexes of the products available on the Munch Crunch Pantry website. They provide users with an organized and visually appealing way to browse and discover products based on their preferences.

These pages can be accessed through the categories menu displayed in the navigation bar on desktop or dropdown menu on smaller screens. Each category page as well as all products pages, displays a grid of products, allowing users to easily find products that match their interests.

Each item is shown with an image, name, price, category tag, and average rating (if available). This provides users with essential information at a glance, helping them make informed decisions about which products to explore further.

The product detail page is accessed by clicking on the image. This display is responsive and the number of items per row adjusts based on the screen size, ensuring a seamless experience across devices. The category tag is also clickable and directs users to the respective category page for further browsing.

Products home link directs the user back to the all products page for easy navigation and the number of items within the specific category page you are on is also displayed for user reference.

Finally the dropdown sort feature allows users to sort the products based on different criteria such as name (A-Z or Z-A), price (low to high or high to low) and category (A-Z or Z-A). This enhances the user experience by allowing users to quickly find products that meet their specific needs and preferences.

![Product Category Page](/documentation/images/features/products-pages/products-grid.png)

![Product Sort Dropdown](/documentation/images/features/products-pages/sorting-dropdown.png)

---

#### Related User Stories:
- **Epic 2 – Product Discovery & Shopping Experience**
  - **2.1 Browse Categories** – category-based product pages support structured browsing
  - **2.6 Search Functionality** – product pages display search results in a clear grid format
  - **2.7 Filters** – sorting options allow users to refine and organise product listings
  - **2.2 Product Detail Page** – products link directly to individual product detail pages

</details>

<details>
<summary><strong>Product Detail Page</strong></summary>

![Product Detail Page - desktop](/documentation/images/features/products-pages/product-detail-desktop.png) 
The product detail page provides comprehensive information about a specific product, allowing users to make informed purchasing decisions. The page is designed to be visually appealing and user-friendly, with a focus on showcasing the product's features and benefits.

The main product image is a main focus on the page, to showcase the product visually. The name of the product is prominently displayed along with a category tag that links back to the respective category page for easy navigation and a star rating with the number of reviews received for social proof - this also links to the reviews section which is at the bottom of this page. Not all products have ratings and reviews so this link is conditionally displayed only when reviews exist.

Some USP descriptions are also displayed to highlight key benefits of the product, such as being organic, ethically sourced, or free from additives. In addition, A brief description is displayed to describe the product further.

The selection of prices and quantities available for the product are presented in selectable 'cards', allowing users to easily choose their preferred option. These cards are dynamic as they show a hover effect including pointer cursor when hovered over and when an option is selected the colour changes and a bright border is added, to clearly indicate the user's choice.

![Selecting a product gif](/documentation/images/features/products-pages/select-opt.gif)

Before an item has been selected, the add to basket button is disabled to prevent users from adding an item without specifying their desired quantity. Once a selection is made, the button becomes active, allowing users to add the product to their shopping cart. A tool tip is also provided when hovering over the disabled button to guide users to select a quantity first as displayed in the gif above. 

Where a product is out of stock, this is clearly indicated on the relevant price/quantity card and the add to basket button remains disabled to prevent users from attempting to purchase unavailable items. the out of stock option is styled differently and is not selectable. 

![Product Out of Stock](/documentation/images/features/products-pages/zero-stock.png)

The quantity selector is also dynamic, allowing users to adjust the quantity of the selected product they wish to purchase. The total price is automatically updated based on the selected quantity and price option, and this is displayed in the success message. 

The success message displayed after adding an item to the basket includes the product name, selected quantity, and total price. This provides users with clear feedback on their action and helps them keep track of their shopping cart contents. The pop-up also displays a brief summary of the shopping cart, including the total number of items and the overall cost. This allows users to quickly assess their cart status without navigating away from the product page.

![Add to Basket Success Toast](/documentation/images/features/products-pages/success-bskt.png).

The product detail page is also optimized for smaller screens to ensure a seamless user experience across devices. The layout adjusts to fit the screen size, with elements stacking vertically for better readability and accessibility on mobile devices.

![Product Detail Page - mobile](/documentation/images/features/products-pages/product-detail-mobile.png)

The 'Keep Shopping' link at the top of the page links the user back easily to the 'All Products' page to continue browsing.

The product information area of this page contains dropdown sections for additional details: ingredients list, nutritional information, storage instructions and Country of Origin. This keeps the page organized and allows users to access the information they need without overwhelming them with too much content at once.

![Product Detail Page Additional Info](/documentation/images/features/products-pages/info-dropdowns.png)
![Product Detail Page Additional Info Open](/documentation/images/features/products-pages/expanded-info.png)

If the details are not available for a specific product, a message is displayed to inform the user that the information is not currently provided.

![Product Detail Page Additional Info Not Available](/documentation/images/features/products-pages/info-no-data.png)

The reviews feature is also viewable on this page, allowing users to read feedback from other customers and share their own experiences. This social proof helps build trust and confidence in the product, encouraging users to make a purchase.

The number of total reviews is provided with the title of the section.

The reviews are listed along with the reviewer's username, their star rating and date of submission. Only approved reviews are displayed on the public platform - Admin are required to approve reviews via the admin interface before they are visible to other users.

![Product Detail Page Reviews](/documentation/images/features/products-pages/reviews.png)

The user is also invited to submit their own review, however this is only accessible if the user is logged in and also if they have previously purchased the product. This ensures that reviews are genuine and based on actual customer experiences. The submit button is disabled until a star rating is selected or text is entered into the review box.

 A user must leave a comment and rating, in order to enable the submit button and submit their review for moderation. A validation message is also displayed if the user attempts to submit without meeting these conditions and this message changes when they can proceed to submit.

![Product Detail Page Submit Review](/documentation/images/features/products-pages/review-entry-user.png)

![Product Detail Page Submit Review Enabled](/documentation/images/features/products-pages/review-submit.png)

Once submitted the page is reloaded and scrolled back to the review section, a toast notification is also displayed to inform the user that their review has been submitted for approval. The user can now see their review listed as 'Pending approval' until an admin approves it via the admin interface.

![Product Detail Page Review Pending](/documentation/images/features/products-pages/review-moderation.png)

The user is also able to edit or delete their review. This is accessible on both approved and unapproved reviews. When editing a review, the existing rating and comment are pre-populated in the form to make it easier for the user to make changes. Once the review is updated, it goes back into pending status for admin approval before being visible again on the public platform.

![Product Detail Page Edit Review](/documentation/images/features/products-pages/review-edit.png)

If the user decides to delete their review, a confirmation modal is displayed to prevent accidental deletions. Once confirmed, the review is removed from the product page and a toast notification is shown to inform the user that their review has been successfully deleted.

![Product Detail Page Delete Review Confirmation](/documentation/images/features/products-pages/review-delete.png)

As guest, the prompt shown in 'Your Review' section encourage the user to log in to submit a review. This helps to ensure that reviews are authentic and tied to real customer experiences. If a user does not have an account a further prompt on the login page encourages them to register for an account. 

![Product Detail Page Guest Review Prompt](/documentation/images/features/products-pages/review-guest.png)

As mentioned previously, a user must have purchased the product in order to leave a review. If a logged-in user has not purchased the product and attempts to leave a review, a message is displayed informing them they can only review products they have purchased.

![Product Detail Page No Purchase Review Prompt](/documentation/images/features/products-pages/review-user.png)

Finally where a product has zero reviews, a message is displayed to inform the user that there are no reviews yet for this product.

![Product Detail Page No Reviews](/documentation/images/features/products-pages/zero-reviews.png)


#### Related User Stories:

- **Epic 2 – Product Discovery & Shopping Experience**
  - **2.2 Product Detail Page** – users can view comprehensive product information, pricing options, availability, and additional details to make informed purchasing decisions
  - **2.3 Reviews** – users can read reviews and ratings from other customers to support decision-making
  - **2.6 Search Functionality** – users are directed to this page when selecting a product from search results
  - **2.5 Discounts** – USPs and pricing visibility support promotional messaging and value awareness

- **Epic 3 – Basket & Checkout**
  - **3.1 Shopping Bag Summary** – users receive confirmation and basket summary feedback when adding items to the basket
  - **3.2 Adjust Bag Items** – quantity selection and dynamic pricing updates allow users to control their purchase before checkout

- **Epic 1 – User Accounts & Authentication**
  - **1.3 Login / Logout** – authentication status determines access to review submission
  - **1.6 User Profile Management** – only authenticated users who have purchased a product can create, edit, or delete reviews

- **Epic 2 – Admin & Moderation (Reviews)**
  - **2.4 Admin Approves Reviews** – submitted reviews enter a moderation state and require admin approval before public display

</details>

<details>
<summary><strong>Shopping Basket Page</strong></summary>
When accessing the basket without adding any items, a friendly message is displayed to inform the user that their basket is currently empty. This encourages users to continue shopping and explore the available products.

![Empty Basket Message](/documentation/images/features/basket/empty-bskt.png)

When items are added to the basket, they are displayed in a structured table format, providing users with a clear overview of their selected products. Each item is shown with its name, selected quantity, SKU product number, price per unit, and total price for that item. This allows users to easily review their selections before proceeding to checkout.

![Shopping basket with multiple items](/documentation/images/features/basket/bskt-multiple-items.png)

There is also functionality to adjust the quantity of each item directly within the basket. Users can increase or decrease the quantity using plus and minus buttons. Once the update link is clicked, the total price for that item is updated based on the selected quantity. On success a toast notification is displayed to confirm the update.

![Adjusting item quantity in basket](/documentation/images/features/basket/update-bskt.gif)

 As well as updating the quantity there is a feature to 'trash' the item. When clicked on a particular item, a confirmation modal appears to prevent accidental deletions. Once confirmed the item is removed from the basket and the totals are updated accordingly. This provides a convenient way for users to modify their order without needing to navigate back to the product page.

 ![Removing item from basket](/documentation/images/features/basket/trash.gif)

The application offers free delivery for orders over £20. If the total amount in the basket is below this threshold, a message is displayed informing the user of the remaining amount needed to qualify for free delivery. This encourages users to add more items to their basket to take advantage of the free delivery offer.

This message is displayed in the toast notification when an item is added to the basket as well as in the basket summary section on the right side of the page.

![Free Delivery Message - Toast - threshold not met](/documentation/images/features/basket/threshold-not-met.png)

![Free Delivery Message - Basket Summary - threshold not met](/documentation/images/features/basket/bskt-threshold-not-met.png)

The application also offers a discount of 10% for new customers on their first order. The code is displayed in the yellow info banner at the top of the page to encourage users to take advantage of this offer.

As shown in the screenshot above, discount codes can be applied in the basket summary section on the right side of the page. When a valid discount code is entered and applied, the total amount is updated to reflect the discount. A toast notification is also displayed to confirm that the discount has been successfully applied. If an invalid code is entered, an error toast is displayed to inform the user that the code is not valid.

![Invalid Discount Code Toast](/documentation/images/features/basket/invalid-discount.png)
![Valid Discount Code Toast](/documentation/images/features/basket/discount-success-toast.png)
![Discount Applied in Basket Summary](/documentation/images/features/basket/discount-applied.png)

As this current discount is a one-time use only code, once it has been applied successfully the user or guest cannot reuse the same code again. If they attempt to do so, an error toast is displayed to inform them that the code has already been used. The functionality behind this uses the email address used in relation to the order, so this error will either display in the basket or at checkout. 

![Discount Code Already Used Toast](/documentation/images/features/basket/discount-duplication.png)

The summary of totals covers the subtotal (Basket total), discount (if any), subtotal after discount, delivery (if any) and the Grand total. If the free delivery threshold has not been met, a message is displayed informing the user of the remaining amount needed to qualify for free delivery.

The user is then either prompted to continue shopping, or proceed to checkout via clearly styled buttons. The buttons are styled with hover effects to enhance interactivity and improve the user experience.

---

#### Related User Stories:

- **Epic 3 – Basket & Checkout**
  - **3.1 Shopping Bag Summary** – users can view a clear summary of basket contents, including item details, totals, discounts, and delivery information
  - **3.2 Adjust Bag Items** – users can update quantities or remove items directly from the basket with confirmation feedback
  - **3.3 Secure Checkout** – users are guided toward checkout through clear calls to action once the basket is reviewed

- **Epic 2 – Product Discovery & Shopping Experience**
  - **2.5 Discounts** – users can apply promotional discount codes and view updated totals in real time

- **Epic 1 – User Accounts & Authentication**
  - **1.6 User Profile Management** – discount usage logic is tied to user or guest email to prevent duplicate use of one-time codes

</details>

<details>
<summary><strong>Checkout Page</strong></summary>

![Checkout Page - Guest](/documentation/images/features/checkout/checkout-guest.png)
![Checkout Page - Guest 2](/documentation/images/features/checkout/checkout-guest2.png)

The checkout page displays a summary of the items in the user's basket, including product names, quantities, individual prices, and the total amount due. This allows users to once more review their order before proceeding with payment.

The user is then prompted to complete their details and shipping information through a structured form. The form includes fields for personal information, shipping address, and payment details. Each field is clearly labeled to guide users through the process.

Mostly all of the fields are required to be filled in except for Apartments/flat/suite - which is marked as optional.

The email field and phone number fields include instant validation to ensure valid input. For example, the email field checks for a valid email format, while the phone number field ensures that only numeric input is accepted. If the input is invalid, an error message is displayed to inform the user of the issue.

![Validation for email](/documentation/images/features/checkout/details-validation.png) 
![Validation for phone number](/documentation/images/features/checkout/details-validation2.png)

The shipping details form includes an external application Geoapify API integration to provide address autocomplete functionality. As the user begins typing their address, suggestions are displayed to help them complete the form quickly and accurately. This feature enhances the user experience by reducing the time taken to enter address details manually and minimizing errors.

The form fields are automatically populated based on the selected suggestion, but users can still manually edit the fields if needed.

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

![Geoapify Address Autocomplete](/documentation/images/features/checkout/geoapify-preview.gif)

If a guest is accessing checkout, without an account they are prompted to create an account or log in for a improved checkout experience, logged in users are able to select to save their details to their profile for future purchases. This is achieved through a simple checkbox option.

![logged in user checkout](/documentation/images/features/checkout/checkout-loggedin.png)
![save details checkbox](/documentation/images/features/checkout/checkout-loggedin2.png)

If the user is a returning customer, when accessing the checkout page their saved details are pre-populated in the form fields to streamline the checkout process. This reduces the time taken to complete the form and enhances the overall user experience.

The payment section of the checkout page integrates with Stripe to securely process payments. Users can enter their card details directly on the page, and the payment is processed through Stripe's secure servers. This ensures that sensitive payment information is handled safely and in compliance with industry standards.

Validations are built in to ensure that all required fields are completed correctly before allowing the user to submit the form. If any fields are missing or contain invalid data, error messages are displayed to guide the user in correcting the issues.

![Invalid card number](/documentation/images/features/checkout/invalid-card.png)
![Expired card](/documentation/images/features/checkout/expired-card.png)
![Declined card](/documentation/images/features/checkout/card-declined.png)
![Card failed 3DS](/documentation/images/features/checkout/payment-not-verified.png)

The 'Complete Purchase' button is disabled until all the required fields are valid and the payment information is correctly entered. This prevents users from submitting incomplete or incorrect information, reducing the likelihood of errors during the checkout process. If the user was to accidentally refresh the page whilst the payment is processing or if there is a network issue, the user is directed to payment processing page, which informs the user that their payment is being processed. 

![Payment Processing Page](/documentation/images/features/checkout/processing_payment.png)

This page automatically checks the status of the payment and redirects the user to the appropriate page based on the outcome. This ensures that users are kept informed about the status of their payment and provides a seamless experience even in the event of interruptions. 

Once the payment is successfully processed, the user is redirected to the order confirmation page where they can view the details of their order and receive confirmation of their purchase. In addition a confirmation toast is also displayed to inform the user that their order has been placed successfully.

![Order Success Toast](/documentation/images/features/checkout/successful-order-toast.png)
![Order Confirmation Page](/documentation/images/features/checkout/successful-order.png)

Once the payment is completed, an order confirmation email is automatically sent to the user's provided email address. This email contains a brief summary of the order total, delivery cost (if applicable), Grand Total and a link to the full details of the order, providing users with a record of their purchase and helps to build trust and confidence in the transaction.

![Order Confirmation Email](/documentation/images/features/checkout/email-order-conf.png)

If the user clicks on the link in the email, they are directed back to the order confirmation page which displays the full details of their order including itemised list of products purchased, quantities and prices.

---

#### Related User Stories:

- **Epic 3 – Basket & Checkout**
  - **3.1 Shopping Bag Summary** – users can review basket contents, totals, delivery costs, and discounts before completing their purchase
  - **3.3 Secure Checkout** – users can securely enter personal, shipping, and payment details using Stripe, with validation and error handling throughout the process
  - **3.4 Order Confirmation** – users are redirected to an order confirmation page and receive an order confirmation email after successful payment

- **Epic 1 – User Accounts & Authentication**
  - **1.1 Email Registration** – guest users are encouraged to register during checkout to improve future purchasing experiences
  - **1.3 Login / Logout** – returning users can log in to access saved details
  - **1.6 User Profile Management** – logged-in users can save delivery information and have it automatically pre-populated on future checkouts

- **Epic 2 – Product Discovery & Shopping Experience**
  - **2.5 Discounts** – applied discounts and delivery thresholds are reflected in checkout totals and confirmation summaries

- **Epic 4 – Content, Marketing & Engagement**
  - **1.5 Confirmation Emails** – automated order confirmation emails provide users with a record of their purchase and reinforce trust in the platform

</details>

<details>
<summary><strong>About us Page</strong></summary>
The About Us page provides users with information about the Munch Crunch Pantry brand, its mission, values, and commitment to quality. The page is designed to build trust and credibility with users by highlighting the brand's dedication to sourcing high-quality, natural wholefoods that are free from additives.

![About Us Page](/documentation/images/features/misc/about-us-intro.png)

As mentioned in the user stories, certifications was something that was important to the potential users of the site. Although this story has not been completed fully, I have included a section on the About us page to showcase some of the bodies that Munch Crunch Pantry is associated with. This helps to reinforce the brand's commitment to quality and ethical sourcing, which is a key value proposition for the target audience.

![About Us Certifications](/documentation/images/features/misc/certifications.png)

The final part of the page provides access to the 'Origin Stories' page, where users can learn more about the people and communities behind the products. A small preview of the content of these pages is displayed to entice users to explore further.

![About Us Origin Stories](/documentation/images/features/misc/origin-stories-about.png)

---

#### Related User Stories:

- **Epic 4 – Content, Marketing & Engagement**
  - **4.1 About & Educational Content** – users can learn about the brand’s values, sourcing practices, and philosophy
  - **4.2 Certifications** – certification bodies and affiliations are displayed to support ethical and quality-focused purchasing decisions
  - **4.3 Admin Content Management** – educational content is structured to allow future expansion and management via the admin interface

</details>

<details>
<summary><strong>Origin Stories</strong></summary>
The link from the About Us page and the navigation menu leads to the Origin Stories index page, which provides users with links to individual stories about the people and communities behind the products offered by Munch Crunch Pantry. This page is designed to educate users about the brand's sourcing practices and the positive impact it has on producers.

![Origin Stories Index Page](/documentation/images/features/misc/origin-stories.gif)

Each origin story page features a hero image that visually represents the story being told. The content is structured to provide a comprehensive overview of the producer, their practices, and the impact of their work. This includes sections on sustainable farming methods, community benefits, and personal anecdotes from the producers themselves.

![Origin Story - Amina](/documentation/images/features/misc/amina1.png)

The lower half of the page contains a map integration using the [Leaflet JS library](https://leafletjs.com/). This map displays the geographical location of the producer country - country of origin, providing users with a visual representation of where the products originate. The map includes a marker indicating the exact location, enhancing the storytelling aspect of the page. 

Leaflet is an open source JavaScript library for mobile-friendly interactive maps. By displaying the location of the producers, users can gain a better understanding of the global reach of Munch Crunch Pantry and the diverse communities it supports.

![Origin Story Map Integration](/documentation/images/features/misc/amina2.png)

Finally at the bottom of each origin story page, there is a call-to-action button that encourages users to browse products containing the products mentioned in the article. This button links directly to the search page, with pre-filled search terms of said products to make it easy for users to find and purchase them.

---

#### Related User Stories:

- **Epic 4 – Content, Marketing & Engagement**
  - **4.1 About & Educational Content** – origin stories provide educational insight into sourcing practices, producer communities, and brand values
  - **4.3 Admin Content Management** – origin stories are structured content that can be created, edited, and published by administrators
  - **4.2 Certifications** – storytelling reinforces ethical sourcing and sustainability themes that support certification-focused user expectations

- **Epic 2 – Product Discovery & Shopping Experience**
  - **2.6 Search Functionality** – call-to-action buttons link directly to pre-filtered product searches based on items mentioned in each story
  - **2.1 Browse Categories** – users are encouraged to continue browsing products after engaging with educational content

</details>

<details>
<summary><strong>Other Miscellaneous Pages</strong></summary>
Several other miscellaneous pages have been created to support the overall functionality and user experience of the Munch Crunch Pantry website. These pages include:

- a Contact Us page
- an FAQ page
- Privacy Policy and Terms & Conditions pages
- Shipping Information page
- Return & Refunds Information page
- Error pages (400, 403, 404, 500)

**Contact Us Page**

A contact form is provided for users to reach out with inquiries, feedback, or support requests. The form includes fields for the user's name, email address, order number (if applicable)subject, and message. Upon submission, the form data is sent to the site administrators via the admin dashboard. 

The form includes validation to ensure that all required fields are completed correctly before submission. In addition if the user tries to submit the form with missing or invalid information, an error toast is also displayed.

![Contact Us Page Validation](/documentation/images/features/misc/contact-validation.png)
![Contact Us Page Validation 2](/documentation/images/features/misc/contact-error-toast.png)

When the form is submitted successfully, the user is directed to a confirmation page informing them that their message has been received and will be addressed promptly via email. The user is then provided with a link to return to the homepage or continue browsing the site.

![Contact Us Page Success](/documentation/images/features/misc/message-sent.png)

When the admin receives the contact form submission, they can view the details in the admin interface under the 'Customer Support' section. The admin can then respond to the user's directly in the admin interface and mark the query as resolved, providing assistance or information as needed. The response is then provided to the user via email. 

![Contact Us -Email reply](/documentation/images/features/misc/contact-response-email.png)

A record of a logged in users contact submissions is also stored in their user profile page for reference, including the status of their query and if a reply has been issued by the admin. Read more about this in the User Profile Page section below

**Error Pages**
Custom error pages have been created for common HTTP error codes including 400 (Bad Request), 403 (Forbidden), 404 (Not Found), and 500 (Internal Server Error). These pages provide a user-friendly message informing users of the error and offering guidance on how to proceed. Each error page includes a link to return to the homepage or navigate to other sections of the site, helping to maintain a positive user experience even in the event of an error.

**FAQ Page**
The FAQs page can be accessed via the navigation menu and also in the footer of the site. This page provides users with answers to common questions about the Munch Crunch Pantry services, products, and policies. 

The questions and answers are displayed in an accordion format, allowing users to easily browse and find the information they need without overwhelming them with too much content at once. Each question can be expanded or collapsed to reveal or hide the corresponding answer.

Many answers also include links to other relevant pages on the site, such as the Contact Us page for further assistance or the Shipping Information page for details on delivery options.

The content on this page has been created using AI - chatgpt to ensure comprehensive coverage of common user inquiries and provide accurate information.

![FAQ Page](/documentation/images/features/misc/faqs.png)

**Privacy Policy & Terms & Conditions Pages**
The Privacy Policy and Terms & Conditions pages provide users with important information about their rights and responsibilities when using the Munch Crunch Pantry website. These pages outline the company's policies regarding data collection, usage, and protection, as well as the terms of service for using the site.

The content on this page has been created using AI - chatgpt to ensure comprehensive coverage of legal requirements and provide accurate information.

**Shipping Information and Returns & Refunds Pages**
The Shipping Information and Returns & Refunds pages provide users with detailed information about the company's shipping policies, delivery options, and procedures for returning products or requesting refunds. These pages help to set clear expectations for customers and provide guidance on how to handle any issues that may arise with their orders.

The content on this page has been created using AI - chatgpt to ensure comprehensive coverage of the relevant policies and provide accurate real-world style information.
</details>

<details>
<summary><strong>User Profile Page</strong></summary>
The User Profile page provides logged-in users with a personalized dashboard where they can view and manage their account information, order history, and contact submissions. This page is designed to enhance the user experience by providing easy access to important account-related features.

This page is accessible via the navigation bar when the user is logged in, through the My account dropdown menu.

![User Profile Page1](/documentation/images/features/account/my-profile1.png)
![User Profile Page2](/documentation/images/features/account/my-profile2.png)

The profile page is divided into several sections for easy navigation:
- **User Information:** 

  - This section displays the user's basic account information, including their name, username and default delivery information. 
  - Users can update these sections by amending the infills and then selecting update profile button. A toast notification is displayed to confirm the update was successful.

  ![User Profile Update Toast](/documentation/images/features/account/profile-update-toast.png)

  - The manage email button takes the user to new page `/accounts/email/` where they can update their email address associated with their account. - More details about this page and its functionality can be found in the Defensive Design and Permissions section below.
  - Similarly, the change password button takes the user to the standard Django Allauth change password page where they can update their password securely. - More details about this page and its functionality can be found in the Defensive Design and Permissions section below.
- **Order History:**

  - This section lists all previous orders placed by the user, including order numbers, dates, and total amounts. 
  - Each order number is a clickable link that takes the user to the order confirmation page for that specific order, allowing them to view detailed information about their purchase.
- **Your Queries**
  - This section displays a list of contact form submissions made by the user, including the subject, date submitted, and status (e.g., pending, resolved).
  - Each item includes a dropdown to view the message the user submitted.
  - If the admin has responded to the query, a message is displayed to reflect this.
  - If no response has been issued yet, a message is displayed to inform the user that their query is still being processed.

  ![User Profile Contact Submissions](/documentation/images/features/account/queries-profile.png)

---

#### Related User Stories:

- **Epic 4 – Content, Marketing & Engagement**
  - **4.5 Contact Form** – users can submit enquiries and receive responses from site administrators
  - **4.1 About & Educational Content** – FAQ, Shipping, Returns, Privacy Policy, and Terms pages provide supporting information and guidance
  - **4.3 Admin Content Management** – informational content is structured to allow future updates via the admin interface

- **Epic 1 – User Accounts & Authentication**
  - **1.6 User Profile Management** – logged-in users can view their contact submissions and response status

- **Epic 3 – Basket & Checkout**
  - **3.3 Secure Checkout** – Shipping and Returns information supports informed purchasing decisions

</details>

Admin Interface

**Admin Interface Customisation**

The Django admin interface was customised to improve clarity and usability.
The default **Groups** model was intentionally hidden, as group-based permissions
are not used in this project. This prevents unnecessary complexity for admin users
while retaining Django’s built-in authentication system.

### Defensive Design & Permissions

### Accessibility

### Features Left to Implement

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

**Frontend Languages:** - HTML, CSS, JavaScript

**Backend Technologies:** - Python, Django, PostgreSQL

**Version Control:** - Git, GitHub

**Deployment Platform:** - Heroku

**Payment Processing:** - Stripe

**Cloud Storage:** - AWS S3 for static and media file storage

**Administrative Interface:** - Django Admin

**Additional Libraries & Packages:** - Bootstrap 5, Font Awesome, Geoapify API, Google Fonts, Django Allauth and Socialaccount, Crispy Forms, Pillow, Boto3, Django Storages, Psycopg2, Gunicorn, Django CKEditor, Django Countries, Leaflet JS library

## Deployment

This project has been developed using Django and deployed to Heroku, using PostgreSQL for the backend database and AWS S3 for static and media file storage. The static and media files are hosted on AWS S3 for efficient delivery. 

The deployment process involves several steps, including setting up the Heroku app, configuring environment variables, and ensuring that all dependencies are properly managed.

The following steps describe how another developer can recreate the project locally and deploy it to Heroku:

### 1 - Fork the Repository:

  Forking creates your own copy of the project repository on GitHub, allowing you to make changes without affecting the original project.

  1. Log in to your GitHub account.
  2. Navigate to the [repository page](https://github.com/Chandni-L5/munch_crunch_pantry).
  3. Click the **Fork** button in the upper right corner of the page.
  4. Select your GitHub account as the destination for the fork.

### 2 - Clone the Repository:
  Cloning the repository downloads a copy of the project to your local machine, allowing you to work on it offline.
  1. Open your terminal or command prompt.
  2. Navigate to the directory where you want to clone the project.
  3. Run the following command, replacing `your-username` with your GitHub username:
     ```bash
     git clone https://github.com/your-username/munch_crunch_pantry.git
     cd munch_crunch_pantry
     ```

### 3 - Create and Activate a Virtual Environment:
  A virtual environment isolates your project's dependencies from other Python projects on your machine.
  1. Create a virtual environment by running:
     ```bash
     python3 -m venv venv
     ```
  2. Activate the virtual environment:
     - On macOS/Linux:
       ```bash
       source venv/bin/activate
       ```
     - On Windows:
       ```bash
       venv\Scripts\activate
       ```

### 4 - Install Dependencies:
  Install the required Python packages listed in the `requirements.txt` file:
  ```bash
  pip install -r requirements.txt
  ```
  If `requirements.txt` is not present, you can create it by running:
  ```bash
  pip freeze > requirements.txt
  ```

### 5 - Set Up a Local Environment File:
  Sensitive information such as API keys and database credentials should not be hardcoded in the codebase. Instead, they should be stored in environment variables which are **not** committed to Github.

  Create a `.env` file in the root directory of the project to store environment variables securely. Add the following variables, replacing the placeholder values with your own:

  ```plaintext
  SECRET_KEY=your_secret_key
  DEBUG=True

  DATABASE_URL=your_database_url

  STRIPE_PUBLIC_KEY=your_stripe_public_key
  STRIPE_SECRET_KEY=your_stripe_secret_key
  STRIPE_WH_SECRET=your_stripe_webhook_secret

  USE_AWS=True
  AWS_ACCESS_KEY_ID=your_aws_access_key_id
  AWS_SECRET_ACCESS_KEY=your_aws_secret_access_key
  AWS_STORAGE_BUCKET_NAME=your_aws_s3_bucket_name
  AWS_S3_REGION_NAME=your_aws_s3_region_name
  AWS_S3_CUSTOM_DOMAIN=your_aws_s3_custom_domain
  ```

  ⚠️ **Important:** Do not commit the `.env` file to version control. Add it to your `.gitignore` file to prevent accidental exposure of sensitive information.

### 6 - Apply Database Migrations and Create a Superuser:
  1. Apply database migrations:
     ```bash
     python3 manage.py migrate
     ```
  2. (Optional) If using fixtures, load them into the database:
     ```bash
     python3 manage.py loaddata your_fixture_file.json
     ```
  3. Create a superuser account for accessing the Django admin:
     ```bash
     python3 manage.py createsuperuser
     ```

### 7 - Run the Development Server:
  1. Start the Django development server to test the application locally:
  ```bash
  python3 manage.py runserver
  ```
  2. Open your web browser and navigate to `http://127.0.0.1:8000/` to view the application.

### 8 - Set up AWS S3 for Static and Media Files:
  1. Create an AWS account if you don't already have one. 
  2. set up an S3 bucket for storing static and media files. 
  3. Choose a unique name for your bucket and select the appropriate region. 
  4. Make sure the **uncheck** "Block all public access" option to allow public read access to your files.
  5. Enable static webhosting on the bucket.
  6. **Permission** - Add a bucket policy to allow public read access to objects in the bucket. Here is an example policy:
     ```json
     {
       "Version": "2012-10-17",
       "Statement": [
         {
           "Sid": "PublicReadGetObject",
           "Effect": "Allow",
           "Principal": "*",
           "Action": "s3:GetObject",
           "Resource": "arn:aws:s3:::your-bucket-name/*"
         }
       ]
     }
     ```
  7. Create an IAM user with programmatic access and attach a policy that grants the necessary permissions to access the S3 bucket:
      1. Go to **IAM → Users → Add users**. 
      2. Create a user
      3. Enable programmatic access
      4. Attach a policy which allows S3 access to your bucket.
      5. Save the **Access Key ID** and **Secret Access Key** for use in your `.env` file. These will also be added to Heroku Config Vars later. 
      6. Update the `.env` file with your AWS credentials and bucket information as shown in Step 5.

### 9 - Prepare for Deployment:
  1. Install Gunicorn, a production-ready web server:
     ```bash
     pip install gunicorn
     ```
  2. Update `requirements.txt`:
     ```bash
     pip freeze > requirements.txt
     ```
  3. Create a `Procfile` in the root directory with the following content:
     ```plaintext
     web: gunicorn munch_crunch_pantry.wsgi
     ```
  4. Update Django settings for production, including allowed hosts and static file handling.

      1. Debug disabled in production:
         ```python
         DEBUG = False
         ```
      2. Set allowed hosts:
         ```python
         ALLOWED_HOSTS = ['your-heroku-app-name.herokuapp.com', 'localhost', '127.0.0.1']
         ```
      3. Static configurations for collectstatic:
          ```python
          STATIC_URL = '/static/'
          STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
          ```
      4. Configure AWS S3 storage settings for when enabled.
         ```python
          if USE_AWS in os.environ:
              # AWS S3 settings here
          ```

### 10 - Deploy to Heroku:
  1. Log in to your Heroku account and create a new app - **New → Create new app**.
  2. Name the app (must be unique) and select your region.
  3. Go to resources tab and add the **Heroku Postgres** add-on for the database. Heroku will automatically set the `DATABASE_URL` environment variable.
  4. Go to the **Settings** tab and click on **Reveal Config Vars**. Add the environment variables from your `.env` file 

  | Key | Value |
  |-----|-------|
  | SECRET_KEY | your_secret_key |
  | DEBUG | False |
  | DATABASE_URL | Auto (Heroku Postgres) |
  | STRIPE_PUBLIC_KEY | your_stripe_public_key |
  | STRIPE_SECRET_KEY | your_stripe_secret_key |
  | STRIPE_WH_SECRET | your_stripe_webhook_secret |
  | USE_AWS | True |
  | AWS_ACCESS_KEY_ID | your_aws_access_key_id |
  | AWS_SECRET_ACCESS_KEY | your_aws_secret_access_key |
  | AWS_STORAGE_BUCKET_NAME | your_aws_s3_bucket_name |
  | AWS_S3_REGION_NAME | your_aws_s3_region_name |
  | AWS_S3_CUSTOM_DOMAIN | your_aws_s3_custom_domain |

  5. Go to the **Deploy** tab, select **GitHub** as the deployment method, and connect your GitHub repository.
  6. Choose the branch to deploy (usually `main` or `master`) and click **Deploy Branch**.
  7. After deployment, run database migrations on Heroku:
     ```bash
     heroku run python3 manage.py migrate --app your-heroku-app-name
     ```
  8. Create a superuser on Heroku:
     ```bash
     heroku run python3 manage.py createsuperuser --app your-heroku-app-name
     ```
  9. Collect Static files to S3:
  
    If configured correctly, Heroku will automatically run `collectstatic` during deployment. If not, you can run it manually:
     ```bash
     heroku run python3 manage.py collectstatic --a <your-heroku-app-name>
     ```
  10. Open your deployed application in the browser:
     ```bash
     heroku open --app your-heroku-app-name

You have now successfully deployed the Munch Crunch Pantry project to Heroku!

## Testing
### Automated Testing

The Munch Crunch Pantry project includes a comprehensive suite of automated tests to ensure the reliability and correctness of its core functionality. The tests cover various aspects of the application, including utility functions, views, forms, and webhook handling. The tests are implemented using Django's built-in testing framework, which provides a robust and efficient way to validate the application's behaviour.

This output confirms that all 36 automated tests pass successfully, including
error-handling scenarios such as simulated email delivery failure.

```markdown
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

The tests focus on the most critical parts of the purchase flow: ensuring the payments are processed safely, metadata is handled correctly and successful Stripe events result in order creation, without duplicating orders on repeated webhook calls.

- **PaymentIntent Creation**
  - Verifies that an empty basket returns no PaymentIntent. and does not attempt to create one.

- **Cache Checkout Data (View)** 
  - Confirms that valid basket and user profile data are cached correctly in the PaymentIntent metadata for later retrieval during webhook processing.

- **Webhook Endpoint** 
- Confirms the webhook returns a 400 response for invalid JSON and verifies that a valid Stripe webhook event is passed to the correct handler.

- **Webhook Handler** 
  - Using mock metadata, tests confirm that a successful payment event results in order creation with correct details, and that repeated events do not create duplicate orders. 
  - Tested resilience logic where the handler retries up to 5 times to locate an existing order before creating a new one (time.sleep mocked and counted). This helps prevent duplicate orders during delayed/async webhook processing.

- **OrderForm Validation** 
  - Confirmed the checkout form enforces required fields by verifying `full_name` is required and returns validation errors when missing.

- **Mocking approach**
  - Stripe calls were mocked throughout the suite (`PaymentIntent.create`, `PaymentIntent.modify`, `Webhook.construct_event`, `Charge.retrieve`) so tests run quickly, deterministically, and without external API dependence, while still verifying that the integration points are called correctly.

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

**In conclusion** - 
Together, these tests provide confidence that critical business logic, payment processing, and data integrity behave correctly under both normal and failure conditions.

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

#### Manual Testing Summary

- ✅ Navigation, banners, footer, and global UI tested across all pages
- ✅ Authentication tested (email/password, Google OAuth, Facebook OAuth)
- ✅ Account management tested (profile updates, email management, password changes)
- ✅ Product browsing, category filtering, sorting, and searching tested
- ✅ Product detail pages tested (options, stock states, reviews, accordions, toasts)
- ✅ Review system tested (submission, edit, delete, approval and pending states)
- ✅ Basket functionality tested (add/update/remove items, delivery thresholds, discounts)
- ✅ Checkout flow tested (form validation, saved details, guest prompts)
- ✅ Stripe payment integration tested (successful payments, failed payments, webhooks, duplicate prevention)
- ✅ Order confirmation and email notifications tested
- ✅ Informational and content pages tested (About, FAQs, Product Origins, Stories, Contact)
- ✅ Custom error pages tested (400, 404, 500)
- ✅ AWS S3 static and media storage tested (hashed static files, public media access)
- ✅ Admin functionality tested via Django admin (products, orders, users, reviews, newsletters, stories)
- ✅ Responsive behaviour tested on mobile, tablet, and desktop viewports
- ✅ Form validation tested across all user inputs
- ✅ No console errors detected during manual testing

Full manual testing documentation with test cases, steps, expected and actual results can be found in the **[Manual Testing Document](documentation/manual-testing.md)**.

### Testing User Stories
The application has been tested against the user stories defined in the Planning section of this README. Each user story has been manually tested to ensure that the functionality meets the requirements and provides a positive user experience.

You can find the detailed testing of each user story in the **[User Stories Testing Document](documentation/user-stories.md)**.

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

<details>
<summary><strong>Checkout refresh during payment processing</strong></summary>

**Bug:**
During testing of the checkout process, I noticed that if the user refreshed the page while the payment was being processed, it could lead to confusion and potential errors. The page would reload to the checkout again, suggesting the payment had not been completed, and the user might not be sure if their payment was successful or if they needed to resubmit their information.

**Cause:**
The checkout flow relied on the frontend JavaScript to manage the payment process and redirect the user upon successful payment with a single POST/redirect cycle. 

1. `PaymentIntent` is created and confirmed via Stripe, and payment shows as successful in the Stripe dashboard.
2. Javascript submits the checkout form once the payment is confirmed.
3. Django processes the order and redirects to the success page.

However, if the user refreshed the page during step 2 (after payment but before form submission), the browser would lose the inflight JavaScript state and reload the checkout page. On reload a new `PaymentIntent` would be created, but the user would have no indication that a payment was already in progress or completed.

**Fix:**
To deal with this, I used a recovery strategy to make the checkout flow more resilient to page refreshes, interruptions and network issues during payment processing. This is achieved in three co-ordinated steps:

1. Client side recovery using `localStorage` to persist the `payment_intent_id` during payment processing. If the page is refreshed, the JavaScript checks for an existing `payment_intent_id` in `localStorage` and attempts to retrieve its status from Stripe. If the payment was already successful, it proceeds to submit the form automatically.
2. Server side idempotency by checking for existing orders associated with the `payment_intent_id` in the webhook handler. If an order already exists, it avoids creating a duplicate order and simply acknowledges the webhook.
3. Using the Stripe webhook as the source of truth for payment status. Even if the client-side flow is interrupted, the webhook will ensure that successful payments are processed and orders are created correctly. The user is directed to a pending payment page if necessary, which reloads automatically until the webhook confirms the order, finally redirecting to the success page. 

Once checkout is fully and successfully completed all recovery data is cleared from `localStorage` and results with an empty basket, signifying a fresh state for the next purchase.

</details>

<details>
<summary><strong>Order Confirmation email sent with incorrect order number</strong></summary>

**Bug:**
After implementing the bug fix to prevent the checkout process from resetting when the page is refreshed during payment processing, I noticed that the order confirmation email sent to the user contained an incorrect order number. The email displayed a different order number than the one shown on the order confirmation page after checkout, and in some cases the email was not sent out at all.

This issue did not exist prior to the refresh-handling update and only appeared after the changes were introduced.

**Cause:**
The issue occurred as there were multiple execution paths introduced to the checkout flow, as well duplicate order creation logic in the webhook handler. The checkout view would create an Order record once the payment details were submitted, The Stripe webhook handler would also create an Order record if it could not find an existing one for the given `payment_intent_id`. In addition a new recovery flow was added to handle page refreshes during payment processing which meant on some occasions the view rendered the success template directly without going through the normal order creation flow and so the flow to send the confirmation email was skipped.

This meant that two separate Order objects could be created for the same payment, leading to confusion and incorrect order numbers being sent in the email. The success page would display one number and the email another.

**Fix:**
- I refactored the order creation logic to ensure that only one Order record is created per successful payment. The webhook handler was updated to first check for an existing Order using the `payment_intent_id` before creating a new one. This prevents duplicate orders from being created.
- Routed all successful payment flows to the same `checkout_success` view, using the order number from the existing Order record. This ensures consistency between the order confirmation page and the email.
- Ensured that the order confirmation email is sent only after the Order record is created, using the correct order number. The email is now triggered once the checkout_success view is rendered, guaranteeing that the user receives the correct information.

</details>

### Lighthouse

Lighthouse audits were conducted using Chrome DevTools on the deployed application to assess performance, accessibility, best practices, and SEO. Audits were carried out on both desktop and mobile views to reflect real-world user experiences across different devices. The results below summarise the scores obtained for key pages in the application:

| Page Type | Performance | Accessibility | Best Practices | SEO |
|-----------|------------|---------------|----------------|-----|
| Home - Desktop | 94   | 87 | 100 | 100 |
| Home - Mobile | 88 | 87 | 100 | 100 |
| Products - Desktop | 65 | 83 | 100 | 100 |
| Products - Mobile  | 62 | 85 | 96 | 100 |
| Product Detail - Desktop| 90 | 81 | 100 | 100 |
| Product Detail - Mobile | 67 | 77 | 96 | 100 |
| Basket - Desktop| 95 | 81 | 100 | 100 |
| Basket - Mobile| 85 | 78 | 96 | 100 |
| Checkout - Desktop | 93 | 85 | 100 | 100 |
| Checkout - Mobile | 64 | 86 | 96 | 100 |

As this project is an e-commerce application, it is naturally image-led and content heavy particularly when it comes to product and checkout pages. Performance scores on mobile devices are therefore lower than those of a lightweight, content-only site. Additional factors such as third-party services (Stripe, Font Awesome) and externally hosted images via AWS S3 also contribute to increased load times during audits.

 I have implemented several optimizations to improve load times and responsiveness. Product images have been served in WebP format with lazy loading to reduce initial load times.

All images are uploaded in WebP format to reduce file sizes without compromising quality. Lazy loading is implemented for product images to defer loading until they are in the viewport, improving initial load times. 

To improve accessibility scores, I have ensured that all images have descriptive alt attributes - relating to the name of the product it depicts, sufficient colour contrast is maintained throughout the site, and ARIA labels are used where appropriate to enhance screen reader compatibility.

Lighthouse reported a minor font-display advisory for Font Awesome icons loaded via an external CDN. As these fonts are provided by a third-party service and already implement font-display: swap, the warning was noted but not prioritised. This does not impact usability, accessibility, or performance within the project scope.

Occasional Lighthouse trace errors were also encountered during testing due to tooling limitations; rerunning audits and using PageSpeed Insights confirmed consistent and acceptable performance across key metrics.

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
All HTML files in this project have been validated using the [W3C Markup Validation Service](https://validator.w3.org/).

As this is a Django application, validation was performed on rendered HTML output rather than raw template files. Multiple validation iterations were carried out throughout development to identify and resolve issues early. Final validation confirms that all pages pass HTML5 validation with no errors.

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
- I would also like to thank my fellow students in the Code Institute Slack community for their assistance and feedback during the development process. Their insights and suggestions have greatly contributed to the improvement of this project.

