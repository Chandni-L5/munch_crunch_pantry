# Munch Crunch Pantry 
![Munch Crunch Pantry Logo](/documentation/images/munch-crunch-logo.png)

Munch Crunch pantry is an online ecommerce store dedicated to providing a wide variety of healthy wholefood snacks. Our mission is to promote wellness and healthy living by offering nutritious, delicious, and convenient snack options for people on the go.

The website is a full-stack site based on B2C e-commerce functionality. It features a user-friendly interface, secure payment processing, and a seamless shopping experience. Customers can browse through our catalog of snacks, read detailed product descriptions, and make secure purchases with ease.

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

The philosophy behind Munch Crunch Pantry is to promote healthy living by making nutritious snacks easily accessible to everyone. The website emphasizes the importance of whole foods and natural, sustainable, high quality and ethically sourced ingredients.


### Scope
#### User/Customer Features:
- Responsive design for optimal viewing on various devices (desktops, tablets, smartphones).
- CRUD Functionality - Customers are able to log in, create accounts, view their past orders and leave reviews on products. 
- Authentication and account management - Users can register, log in, reset passwords, and manage their account details.
- Product browsing and search functionality - Users can browse products by categories, search for specific items, and filter results based on preferences.
- Detailed product pages - Each product has a dedicated page with images, descriptions, nutritional information, and customer reviews.
- Shopping cart - Users can add products to their cart, view cart contents, update quantities, and remove items.
- Secure checkout process - Integration with Stripe for secure payment processing, order summary, and confirmation.
- Order history - Customers can view their past orders and order details.
- Customer reviews and ratings - Users can leave reviews and ratings for products they have purchased.

#### Admin Features
- Admin dashboard - A dedicated interface for administrators to manage products, orders, and customer information.
- Product management - Admins can add, edit, and delete products, including images, descriptions, and pricing.

### Agile Development & Planning 
#### User Stories
The development and the planning of this project has been created with the Agile methodologies in mind throughout.

Epics have been condensed to bitesize user stories.

[📚 The epics can be viewed here](/documentation/epics.md)

[📓 The user stories can be viewed here](/documentation/user-stories.md)

#### Estimation
I have used the MoSCoW method to prioritize the user stories into Must have, Should have, Could have and Won't have for this project. These categories are also represented on the KanBan board, with coloured labels for easy reference by the development team. At the start of the project, 'Won't have' items will not be applied, but this will be reviewed at the end of the project for potential future implementations depending on the progress made. 

To support the estimation, I have also used story points based on a Fibonacci methodology to estimate the effort required for each user story. This allows for a more accurate assessment of the complexity and time needed for implementation and helps to guide prioritization and ordering of tasks during the development process.


| Epic 1: User Account & Authentication |
|--------------------------------------------------|

| Requirement | User Story | AC Numbers | Story Points | Complexity |
|------------|------------|------------|--------------|------------|
| 🟥 Must have | **1.1** Email registration | AC1, AC2, AC3, AC4, AC5 | 5 | 🟡 Medium |
| 🟥 Must have | **1.3** Login/Logout | AC1, AC2, AC3, AC4, AC5 | 3 | 🟢 Small |
| 🟥 Must have | **1.5** Confirmation emails | AC1, AC2, AC3 | 3 | 🟢 Small |
| 🟥 Must have | **1.6** User profile management | AC1, AC2, AC3, AC4, AC5 | 8 | 🟠 Large |
| 🟧 Should have | **1.4** Password reset | AC1, AC2, AC3, AC4, AC5, AC6, AC7, AC8, AC9 | 5 | 🟡 Medium |
| 🟩 Could have | **1.2** Social media registration | AC1, AC2, AC3 | 8 | 🟠 Large |

| Epic 2: Product Discovery |
|-----------------------------------------------|

| Requirement | User Story | AC Numbers | Story Points | Complexity |
|------------|------------|------------|--------------|------------|
| 🟥 Must have | **2.1** Browse categories | AC1, AC2, | 3 | 🟢 Small |
| 🟥 Must have | **2.2** Product detail page | AC1, AC2, AC3 | 5 | 🟡 Medium |
| 🟥 Must have | **2.6** Search functionality | AC1, AC2, AC3 | 8 | 🟠 Large |
| 🟥 Must have | **2.8** Admin CRUD | AC1, AC2, AC3 | 5 | 🟡 Medium |
| 🟥 Must have | **2.9** Admin product management | AC1, AC2, AC3 | 5 | 🟡 Medium |
| 🟧 Should have | **2.3** Reviews | AC1, AC2, AC3 | 8 | 🟠 Large |
| 🟧 Should have | **2.4** Admin approves reviews | AC1, AC2, AC3 | 5 | 🟡 Medium |
| 🟧 Should have | **2.7** Filters | AC1, AC2, AC3 | 8 | 🟠 Large |
| 🟩 Could have | **2.5** Discounts | AC1, AC2 | 8 | 🟠 Large |

| Epic 3: Shopping Bag & Checkout Process|
|---------------------------------------|

| Requirement | User Story | AC Numbers | Story Points | Complexity |
|------------|------------|------------|--------------|------------|
| 🟥 Must have | **3.1** Shopping bag summary | AC1, AC2, AC3, AC4, AC5 | 5 | 🟡 Medium | 
| 🟥 Must have | **3.2** Adjust bag items | AC1, AC2, AC3 | 8 | 🟠 Large |
| 🟥 Must have | **3.3** Secure checkout | AC1, AC2, AC3 | 13 | 🟠 Large |
| 🟥 Must have | **3.4** Order confirmation | AC1, AC2 | 3 | 🟢 Small |

| Epic 4: Brand Experience & Engagement |
|--------------------------------------|

| Requirement | User Story | AC Numbers | Story Points | Complexity |
|------------|------------|------------|--------------|------------|
| 🟧 Should have | **4.1** About + educational content | AC1, AC2 | 2 | 🟢 Small |
| 🟧 Should have | **4.6** Contact form | AC1, AC2, AC3, AC4 | 3 | 🟢 Small |
| 🟩 Could have | **4.2** Certifications | AC1 | 2 | 🟢 Small |
| 🟩 Could have | **4.3** Admin content management | AC1, AC2, AC3 | 5 | 🟡 Medium |
| 🟩 Could have | **4.4** Newsletter signup | AC1, AC2, AC3, AC4 | 5 | 🟡 Medium |
| 🟩 Could have | **4.5** Newsletter admin | AC1, AC2 | 5 | 🟡 Medium |

During the planning stages, the MoSCoW priorities were distributed as 52% Must have, 24% Should have and 24% Could have. The total number of story points estimated for the project was 130 including the Could have features.

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

#### Relational Data Model
#### Database Schema

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

<!-- create a screenshot of the fonts used and add here -->

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
### Languages
### Hosting Platforms
### Development Tools:
### Django Packages

## Deployment

## Testing
### Automated Testing
Products App Tests
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
### Testing User Stories
### Bugs & Fixes
### Lighthouse
### Validators

## Final Summary & Future Implementations

## Credits
### 
- [Chatgpt](https://chatgpt.com/) 
- [Google fonts](https://fonts.google.com/) 
- [Favicon.io](https://favicon.io/emoji-favicons/) - to create an emoji favicon

### Media
- [Font Awesome](https://fontawesome.com/)
- [befunky.com](https://www.befunky.com/dashboard/) - to resize images
- [pexels.com](https://www.pexels.com/) - to source images
- [Sora](https://sora.chatgpt.com/explore) - to create AI images
- [Cloudconvert](https://cloudconvert.com/jpg-to-webp) - to convert images to different file types. 
- [toWebP](https://towebp.io/) - to convert different file types

### Documentation and Testing 
- [color-hex.com] (https://www.color-hex.com/) - to display and compare colour palettes for the logo and website design.
- [Colourcontrast.cc](https://colourcontrast.cc/) - to check colour contrast ratios for accessibility compliance.
-[befunky.com](https://www.befunky.com/) - to edit and enhance images used in the project documentation.
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
- [Canva](https://www.canva.com/) - to create wireframes and ERD
- [wordtracker.com](https://www.wordtracker.com/)
- [Ubersuggest](https://neilpatel.com/ubersuggest/)  
- [Google Keyword Planner](https://ads.google.com/home/tools/keyword-planner/).
- [Mailchimp](https://mailchimp.com/)


### Resources

## Acknowledgements
- I would like to thank my mentor, Moritz, for their invaluable guidance and support throughout the development of this project. Their expertise and encouragement have been instrumental in helping me achieve my goals.

