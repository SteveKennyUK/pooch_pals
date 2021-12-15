# Pooch Pals
  
 
This website has been created for my Data Centric Development Milestone 3 project, the third project on the [Code Institute Diploma in Software Development](https://codeinstitute.net/) course.

This project is a full-stack site that focuses on a particular domain and its dataset. The aim is to allow users to share their own data and have convenient access to data provided by other users of the site.  

Interest in dog ownership has increased since the start of the COVID pandemic, with people spending more time at home. 'Pooch Pals' aims to meet the needs of dog owners, especially new owners, who would like their dogs to socialise with other dogs. It can also give potential new owners a chance to understand a particular breed before committing to ownership.

The site allows registered users to provide information to create a profile for their dog, which is stored on a MongoDB database. Users can then search for other user profiles to find a good match for their own dogs, plus modify and delete their own information. The ultimate aim is a happy dog, while also helping dog owners to better understand their best friends.


## User Experience (UX)
---
This application will follow the principles of User Centred Design (UCD), which will focus on placing users at the centre of the design and development process.
 
This site has two principal user goals to consider.

 1.  **Site/Business Owners** - for the site owners, it is both a labour of love and a business opportunity. They are primarily interested in the wellbeing of dogs and wish to help dog owners connect so that dogs can spend quality time together. The site owners may have their own dogs which could benefit from the platform. They can also use this as an opportunity to create a platform to promote dog-related goods and partner with other dog-related organisations. This will only be possible by firstly growing the site, which will require building a user friendly experience.

 1.  **Site Users** - the main focus of the site will be to provide a platform for dog owners (whether they be long standing, new or potential owners) to find potential playmates for their own dog or help understand what would be required to own a particular breed. Users would require a site that is easy to use but would also want reassurances that their information is safe as the welfare of their dogs is paramount.
The site users can be identified as falling within one of the following three categories -
	 - **User category 1:** Unregistered/logged out user
	 - **User category 2:** Registered/logged in user
	 - **User category 3:** Admin/site owner user
	 
### Project Strategy
---
-  #### User Goals (general)

	* As a user, I want to be immediately drawn into the site and understand its main purpose.
	* As a user, I want to be able to easily identify what I need and navigate the site to get to it.
	* As a user, I want concise but informative content, displayed in an aesthetic, intuitive and consistent manner.
	* As a user, I want to be able to view the site clearly and intuitively on different device sizes.
	* As a user, I expect the site to be fully accessible.

-  #### Site Owner/Business Goals

	* As the site owner, I want features and content that will engage new users quickly, encourage them to explore the site and draw them back in the future.
	* As the site owner, I want users to feel comfortable that their data is secure.	
	* As the site owner, I want to be able to moderate the site content.
	* As the site owner, I want the site to be accessible to all users.
	* As the site owner, I want to be able to use the site myself to find playmates for my own dogs.	
	* As the site owner, I want to also be able to develop the site to promote dog accessories and services (either my own or those of a business partner).


-  #### User Stories 
    - **(Unregistered/logged out user)**
		* I want to be quickly reassured that this site will be of interest to me.
		* I want to be able to identify the content of the site and be able to navigate to areas of interest e.g. view dogs on the site.
		* I want to be able to register to join the site effortlessly and with minimal information required. 	
		* I want to be able to contact the site owners with any questions.
		
	- **(Registered/logged in user)**	
		* I want to be able to login and logout easily.
		* I want to be able to view my profile and see my dog's profile and any reviews I have left for other dogs.
		* I want to be able to add a profile for my dog(s) with relative ease.
		* I want to be able to leave reviews for other dogs on the site.
		* I want to be able to edit and/or delete my contributions.
		* I want to be able to search for dogs that meet certain criteria e.g. breed, location.
		* I want to be able to understand more about different dog breeds.
		* I want to be able to interact with other site users.
		* I want to know that other site users are trustworthy.
		* I would like to be able to save profiles of interest to go back to later.		

	- **(Admin/site owner user)**	
		* I want to be able to validate users to improve trust in the site.
		* I want to be able to view, edit and delete all users and entries on the site.

### Project Scope

---

Looking at the User and Owner/Business Goals, there are plenty of features and content which could be included in the site to attempt to satisfy all their needs. However, a number of factors limit what would be possible or desirable to include in the first development stage.

The main constraints are time and the current technological expertise of the developer. The decisions made at this stage are designed to avoid making the scope too large, such that the project becomes overloaded and fails to meet deadlines or making it too small, such that there is an unimpressive end result.

The first development stage aims to create a Minimal Viable Product, providing users with the core requirements that they actually need. Additional features can be added if there is time or at future developmental stages, once feedback has been received from the initial site features.  

The features to include in this first development stage will be determined by creating a strategy trade-off table, drawing on the user goals and needs.

There may also be conflicting needs between the user categories, in which case a decision will be made on which to prioritise. This will be addressed in the Structure and Skeleton phases of development.

 #### Strategy Trade-offs

 Opportunity | Importance | Viability
----------- | ---------- | ---------
Clear and intuitive navigational links | 5 | 5
Responsive for all device sizes | 5 | 5
Secure document-based database | 5 | 5
Registration and login/logout pages with user authentication | 5 | 5
Form for users to create dog profile | 5 | 5
User profile page | 5 | 5 
Individual dog profile pages | 5 | 5
Search facility for users to filter profiles | 5 | 5
CRUD (Create, Read, Update, Delete) functionality across the site | 5 | 5
Admin only facility to verify and moderate users and content | 5 | 4
Footer with site information and links to external sites | 4 | 5
Reviews function for dog profiles | 4 | 4
Breed group page to provide information and filter by group | 4 | 4
Facility for users to contact other users (via admin) | 4 | 4
Facility for users to contact other users (directly) | 4 | 2
'Favourites' function | 3 | 3

#### Content Scope

Using the table above, we can see which are the most valuable features to the user, how much of our resources they would take up and thus which features should be incorporated in the first stage.

It is felt that features should be provided in the following order of importance - 

 - An informative landing page with intuitive navigation.
 - Simple registration, login and logout facilities.
 - General dog profile page with search facility (users will need to register to see more detailed profiles, which both encourages users to register and also provides registered users with a degree of reassurance over who can view the profiles).
 - User profile page.
 - Form to add dog profile information.
 - Detailed dog profile pages.
 - Features to allow user to view, edit and delete their dog profile(s).
 - Admin only features.
 - Review features.
 - Contact page.
 - Breed information and filter page. 
  

### Project Structure
---
The structural design of the site aims to make the user interaction with the site as easy and as comfortable as possible. This is achieved by creating meaningful relationships between the various site elements so that users can intuitively understand their meaning and purpose.

 #### Interactive Design

The principles of Interactive Design (IxD) promote consistency, predictability, visibility, learnability and feedback as central to the above aim. The structure of this site aims to follow these principles.  

 -  **Page Structure**

	- The nature of this site necessarily involves spreading content over several pages. The user expects different functions to have their own pages e.g. registration, login, profile pages. The user will therefore be provided with good, clear and intuitive links to the different pages, either via the navigation bar or through buttons and links.
	
	- In order to keep the site consistent and predictable, elements will follow the same structure across all pages. All pages will have the same background image, navigation bar and footer. Information will be displayed using cards which will be displayed in a consistent manner.

	- The landing page will immediately address some of the user goals, with clear directions to desired content through navigation links, calls to action and meaningful images. These are consistent with previous user experiences on other sites.
	
	- A separate contact section is also expected. The 'Contact' page provides a contact form where users can request further information, particularly if they wish to register interest in contacting another user/dog owner. Input fields will react to user actions, which will provide reassuring feedback to the user. As the site develops and expands, a facility for users to contact each other directly e.g. direct chat, will be added.
	
	- Separate error pages in the event of a broken link or server error will be added. This feedback adds reassurance to the user and provides them with clear instructions on how to return to the site.
  
 -  **Visibility**

	- The location and purpose of elements should be clear to users. Where appropriate, there will be partial overlay of elements on the screens to hint to the user that there is more content below. Additionally, if necessary, a scroll down arrow will be employed to indicate to the user that useful content can be accessed further down. 

	- There will also be a floating scroll up arrow where the page length requires a degree of scrolling down so users can return to the top of the screen with a single click from anywhere on the page. The smooth scroll styling will enable the user to understand the page layout and where the various elements are located. 

	-  Dropdown menus will have an arrow to indicate that there are further options available. This is a common practice to make elements more visible so should be predictable to the user. If not, the consistent use of this practice will help the user to learn what such arrows mean and be comfortable when encountering them.
  
 -  **Navigation**

	- The site navigation will again be consistent and predictable by following the convention of the site logo on the top left with a horizontal navigation bar to the right of the logo. 
	
	- A fixed navigation bar and sticky footer will be employed. This will provide a better visual experience for the user and, in conjunction with the floating scroll up arrow, will reduce the amount of scrolling required by the user.
	
	- The navigation bar will be responsive and will use a hamburger menu for smaller devices. This is consistent and predictable with most sites on mobile devices. The menu will then push the page content down when activated to maximise visibility of the options.  

 -  **Buttons and Links**

	- Buttons and links will be used to create a smoother navigation process for the user. The purpose of these must be made clear to the user. Buttons and links will react when the mouse hovers over them. This conventionally suggests that clicking on the button or link will make something happen. The use of unambiguous text or iconography will make it clear to the user what will happen when the button or link is clicked.
	
	- Styling the buttons and links in a consistent manner and employing the same reaction when e.g. the mouse hovers will help the user to learn and predict what they need to do to achieve their goals.
	
	- When a button is clicked, the user will be provided with some feedback to reassure them that their action has been acknowledged. This will be either a change in the button appearance or a flash message appearing. The flash message will either confirm that the required action has been successful or inform the user that an error has occurred, with instructions on what the user should do next. This builds trust with the user.	
	
	- External links will always open in another page (by adding the `target="_blank"`attribute inside the link's anchor element). This makes for a better user experience as the user will not need to use the back button to return to the site. It is also good practice to add `rel="noopener"` as this adds a security layer by preventing the new page from accessing the original window object.
  

 -  **Iconography**

	- Icons will be used to help users to quickly identify content matter. A visual representation can say more than words and often stands out more. A quick scan of the page will pick out icons and well chosen ones will stand out and immediately assure the user as to the associated content.

	- The site logo acts in a similar fashion and the user quickly learns to associate the image with the site and its purpose. A favicon, using the dog logo image, will be also be added. This is now generally expected by users and helps them to identify the site if they have several pages open.

#### Information Architecture (IA)

 - The navigation paths follow a tree structure with the head branches representing the main features. These feature pages, where appropriate, will contain buttons and links leading the user to any sub features relevant to the main branches, avoiding overloading the navigation bar. Sub features include links to edit, delete and create new content; these will require no more than three clicks to reach. 

 - Once the site evolves, additional branches can be added but the fundamental structure will remain.
 
 - The IA varies slightly, dependent on the current user category - please see below. 

![User 1 - not registered/logged in](https://github.com/SteveKennyUK/pooch_pals/blob/main/static/images/readme/User%20-%20not%20logged%20in.jpeg)
![User 2 - registered & logged in](https://github.com/SteveKennyUK/pooch_pals/blob/main/static/images/readme/User%20-%20registered%20&%20logged%20in.jpeg)
![User 3 - Admin](https://github.com/SteveKennyUK/pooch_pals/blob/main/static/images/readme/Admin.jpeg) 	

#### Database Architecture

 -  **Database Choice**

The non-relational document-based database of [MongoDB](https://www.mongodb.com/) was selected as the best fit for this project. The various data collections only have a few relational elements so the greater flexibility provided by MongoDB (e.g. over a SQL relational database) is preferable.

Where there are relational elements between collections, the ObjectId of one collection will be inserted as a key in the relational collection. This guards against issues arising using key names from a collection as a key in another collection e.g. in the event the key name is changed. The ObjectId will remain constant so is safer to use. These relationships are colour coded in the below schema diagram.

 - **Data Collections**
 
	**Users** - this collection stores user information for registration, login and profile purposes. It also stores admin and verification status as Booleans. The ObjectId will be used as a reference when a user adds a dog profile (in the Dog collection) or leaves a review (in the Reviews collection).
	
	**Breed Group** - this collection stores information regarding the categorisation of dogs by breed group. It will used as a filter and as an informational tool. The breed groups are a set standard so are unlikely to change. Consequently, only admin users will have access to this collection, should the description or image require updating. If the standards are ever changed, it would be simple to enable admin to make any additions or amendments. The ObjectId will be used as a reference when a user adds a new dog profile.
	
	**Dogs** - this is the core collection, storing all information regarding dog profiles, most of which will be provided by user input on the 'Add Dog' profile form. This information will then be used to display information on the 'Dog Profile' pages. The ObjectId will be used as a reference when a review is left on a dog profile (in the Reviews collection).
	
	**Reviews** - this collection stores information when a review is left on a dog profile. It will store the ObjectId of both the user who has left the review and the dog profile that is subject to the review.


![Database schema diagram](https://github.com/SteveKennyUK/pooch_pals/blob/main/static/images/readme/database-ER-diagram.jpeg)

Screenshots of each collection can be seen below -

 - [Breed Groups](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/readme/database-breed-groups.JPG)
 - [Dogs](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/readme/database-dogs.JPG)
 - [Reviews](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/readme/database-reviews.JPG)
 - [Users](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/readme/database-users.JPG)

### Project Design (Skeleton and Surface)
---
The layout and content of the site has been designed with the User Experience at the forefront. The typical user will be someone who owns a dog or is interested in dogs. The site therefore needs to engage with this type of user and make them feel at ease. 
The subject matter of the site, focusing on dogs, lends itself to a fun, playful and lively theme. The design decisions for the site are intended to reflect this theme.  

-  #### General Layout

	- The design will broadly follow the 'rule of thirds' to provide a visually comforting experience to the user. Where appropriate, sections will be divided into thirds or one-third to two-thirds ratios.

	- Sizing of elements will be balanced and proportional to again improve the visual comfort of the site. Where appropriate, measurements will use rem units to help with responsiveness.

	- Layouts will be responsive to different screen sizes, particularly as many users will be expected to view the site on mobile devices. Consequently, the layout will change according to media size e.g. three horizontal columns on a desktop may become three vertical columns on a mobile phone.
	
	- The decision has been made to use [Materialize](https://materializecss.com/) as a framework to create a responsive site. It is felt that in addition to responsiveness, this framework offers myriad options to create features to assist in displaying user content clearly. The use of Materialize also influences some of the other design decisions. 
	
	-  Content will be displayed principally using Materialize card components. These provide a visually appealing and responsive solution. Main outer container cards will have a white opaque background, partially revealing the background wallpaper. Inner cards will sit within the outer container.
	

	- It is the intention to include pagination where a page has a lot of content so as to avoid causing cognitive overload to the user. In particular, a page displaying all the dog profile cards would benefit from such a feature. 

-  #### Colour Scheme

	- The colour scheme for this site is important to help the user feel immediately comfortable. The decision was made to employ the Materialize [base colours](https://materializecss.com/color.html) for much of the site's colour palette. Any additional CSS styling can then use the colour HEX values.
	
	- In the interests of consistency and to help create a fun vibe, the same background wallpaper involving dog-related images will be used across all pages. In order to not create too much of a distraction, a white background with relatively small black images has been chosen. The standard #000 Black and #FFF white will also be used across the site, where appropriate, to complement the background. 
	
	- The decision has also been made to keep the site fairly simple in terms of colours used. This will help focus attention on the content and user interactions. The site will instead rely on the imagery and component colours to add the requisite visual depth. 
	
	- All colours are checked with [WebAIM](https://webaim.org/resources/contrastchecker/) to ensure that the colour contrasts meet accessibility guidelines.
	
	- **Core Elements**		
	
		It is felt that the core elements (e.g. navigation bar and footer) should employ a colour that is warm and reassuring but also complements the background wallpaper. The Materialize #eceff1 blue-grey lighten-5 was first chosen. However, it was felt that something a bit warmer and with a greater contrast capacity was required. After adjusting to a warmer colour with more blue hue added and running through WebAIM to check contrast with black text, the following colour was settled upon -
	
		[#ebf1fa](https://icolorpalette.com/color?q=ebf1fa) - Icy Lilac
	
		The core text elements contained within the body, such as main headings, require a darker colour in order to contrast against the lighter background and meet accessibility guidelines. The following Materialize colour was chosen as it still remains consistent with the core elements' colour -
		
		[#455a64 ](https://icolorpalette.com/color?q=455a64) - blue-grey darken-2 ('San Juan') 		

	- **Buttons**		
	
		The choice of colours for the buttons is important as it should add to the intuitive and learnable design features of the site. Navigational buttons which progress the user through the site (such as 'Search' & Back) will use the same colour employed for core navigation elements i.e. 	[#ebf1fa](https://icolorpalette.com/color?q=ebf1fa) - Icy Lilac. This provides added reassurance to the user as to the button's function.
	
		Button colours will also be consistent with recognised colour standards used elsewhere. These include - 
	
    	[#26a69a](https://icolorpalette.com/color?q=26a69a) - teal lighten-1 ('Baltic'). This Materialize teal colour represents a 'green for go' instruction. This will be used for buttons that initiate an action, such as 'Submit', 'Edit' and 'Register'. This colour will also be used as a border on card elements to provide contrast against the background and complement the action buttons.
    
    	[#f44336](https://icolorpalette.com/color?q=f44336) - red ('Vermilion Bird'). This Materialize red colour represents a negative instruction, such as 'Delete' and 'Cancel'.
    	
    	[#ffab00](https://icolorpalette.com/color?q=ffab00) - amber accent-4 ('Flash of Orange'). This Materialize accent colour will be used to draw attention to certain features such as call to action buttons and any flash messages.

		Buttons will react to user interactions, such as when the mouse hovers over the button, the colour will change or the Materialize `waves-effect` class will be employed to indicate that clicking the button will cause something to happen.

	- **Palette** 
	
		The chosen colours are displayed in the following palette -
		
	![Pooch Pals Palette](https://github.com/SteveKennyUK/pooch_pals/blob/main/static/images/readme/colour-palette.JPG)
	
-  #### Typography

	- The font choices for the site will also adhere to the fun, playful and lively theme outlined previously. Research from other sites with a similar dog theme (see Credits) helped to decide on the best fonts to use to achieve this.

	-  The [Neucha](https://fonts.google.com/specimen/Neucha?query=neucha#standard-styles) font on [Google Fonts](https://fonts.google.com/) has been selected for the main titles and headings. The sleek and clean look of the [Lato](https://fonts.google.com/specimen/Lato?query=lato#standard-styles) font complements Neucha well and will be used for the main body text. 'Sans serif' will act as a fall-back font for Lato and 'cursive' as a fall-back font for Neucha, in case the chosen fonts are not imported correctly.

- #### Imagery

	- The choice of images to use for the site is straightforward in that it will focus on dog imagery. This is what a user would expect from such a site. Principally, the images will come from the dog profile pictures uploaded by the users. If a user does not upload a photo or the link fails, a dedicated default image will be displayed, including a message informing the viewer that no image is available.

	- In addition to the profile photos, the site will include cartoon-style pictures. This is again in keeping with the fun and playful nature of the site. These pictures will also be used to tell a story, indicating the nature of the current page or link button e.g. a picture of a person and dog with a computer indicates login or registration is required.	

- #### Wireframes

	 - Eleven html pages were identified as being required to display the project data in the initial development stages. The wireframes for these pages were developed using [Balsamiq](https://balsamiq.com/) and can be viewed below (please right-click on the mouse to open in an external page).
		 - [Home Page](https://github.com/SteveKennyUK/pooch_pals/blob/main/static/images/wireframes/home_page_pooch_pals.pdf)
		 - [Register Page](https://github.com/SteveKennyUK/pooch_pals/blob/main/static/images/wireframes/register_pooch_pals.pdf)
		 - [Login Page](https://github.com/SteveKennyUK/pooch_pals/blob/main/static/images/wireframes/login_pooch_pals.pdf)
		 - [Profile Page](https://github.com/SteveKennyUK/pooch_pals/blob/main/static/images/wireframes/profile_pooch_pals.pdf)
		 - [All Dogs Page](https://github.com/SteveKennyUK/pooch_pals/blob/main/static/images/wireframes/all_dogs_pooch_pals.pdf)
		 - [View Dog Page](https://github.com/SteveKennyUK/pooch_pals/blob/main/static/images/wireframes/view_dog_pooch_pals.pdf)
		 - [Add Dog Page](https://github.com/SteveKennyUK/pooch_pals/blob/main/static/images/wireframes/add_dog_pooch_pals.pdf)
		 - [Edit Dog Page](https://github.com/SteveKennyUK/pooch_pals/blob/main/static/images/wireframes/edit_dog_pooch_pals.pdf)
		 - [Breed Groups Page](https://github.com/SteveKennyUK/pooch_pals/blob/main/static/images/wireframes/breed_groups_pooch_pals.pdf)
		 - [Contact Page](https://github.com/SteveKennyUK/pooch_pals/blob/main/static/images/wireframes/contact_pooch_pals.pdf)
		 - [Admin Page](https://github.com/SteveKennyUK/pooch_pals/blob/main/static/images/wireframes/admin_pooch_pals.pdf)
	- **EDIT** - There was a slight amendment in the final layout of the View Dog page for medium and large screen sizes. It was decided to place the image at the top of the page, as per the small screen sizes, with the information list below. This is in keeping with the rest of the pages on the site and it was felt that the consistency would provide a better UX. 

## Features
---
### Existing Features

#### Navigation and Footer

 - All pages have the same navigation bar at the top and footer at the bottom. These areas are styled with the same colour scheme and all links react to mouse hover to maintain consistency. Navigation links have a darker background shade, external links have a heavier font weight and social media links buzz when hovered. This indicates to the user that not only will clicking the link take them to a new location but also the type of page that will be opened.

 - The navigation bar has the company logo as a clickable 'Home' button. This reinforces the site's image and makes it more recognisable to the user. Similarly, a favicon has been added to the open page tab. This is expected and helps the user to identify the site amongst several open sites. This brand reinforcement is important for building familiarity and trust.

 - The navigation bar is positioned in an expected position at the head of the page. The navigation links stand out and make their purpose clear. The active page link has a darker background shade to emphasise to the user where they are on the site (the 'Account' link is highlighted on desktop when a page within the dropdown menu is active). 

 - The navigation bar is fixed so the user can have access to navigation links wherever they are on the page. This improves the user experience particularly where the page content scrolls down a long way.
 
 - A floating arrow button appears in the bottom right corner on each page once the user has started to scroll down. This provides the user with an additional convenient way to return to the top of the page without having to scroll up. 
 
 - A 'Back' button is situated in the top left of the card container of all pages except the Home page and Add Dog page (see below). This again assists the user in navigating the site. This was placed in its own template as it will be reused on several pages and injected using the Jinja `{% include %}`statement. 'Cancel' buttons in an indicative red colour are used throughout the site and will take the user back a step.

 - A sticky footer has been employed so that it stays at the bottom of the screen where the page has little content.  It also scrolls up at the bottom of pages with longer content but will still remain at the foot of the screen. The footer contains useful information that encourages the user to investigate further.
 
 #### Register Page

 - A centralised card with an indicative image of a person registering a dog on the site followed by a simple sign-up form. The form employs [Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/) to add a level of security with hashed passwords.
 
 - User authentication - the `input` fields employ the `pattern` attribute to set the length and character types that may be used when choosing usernames and passwords. However, for the email address it was decided that it would be better to use  `<input type="email">` to automatically validate to ensure it is a properly formatted e-mail address.

 - The user's chosen username is checked against the database to check that the name has not already been taken by another user. A confirm password field was added to help ensure that the user has input their chosen password correctly by giving them the chance to repeat it. The two password fields are then checked and only if they match will registration be allowed.
 
 - Following successful registration, the user is redirected to their Profile page and a flash message provides feedback of a successful registration.
 
 - The user's username, password and email are added to the database. There are also two Boolean fields, 'is_admin' and 'is_verified', that are added to the 'users' collection. These are initially set to False so that the user initially has neither admin nor verified status. These fields can be updated by Admin users. 

#### Login Page

 - Same card styling as Register page, with indicative image of person logging in with their dog. As with Register, the input fields have a pattern attribute to prompt the user to enter valid characters and word length. 
 
 - The form checks the database to see if the username input by the user has been registered. It also checks if the password input by the user matches that in the database. If either of these do not match a database record, a flash message informs the user that username and/or password is incorrect. Using **and/or** does not indicate to any unauthorised user attempting brute force login whether they have at least one of username or password correct.
 
 - If the username does exist and the hashed password matches that held in the database for that record, the user is redirected to their Profile page and a flash message provides feedback of a successful login.
 
 - Use of a [login required decorator](https://flask.palletsprojects.com/en/2.0.x/patterns/viewdecorators/#login-required-decorator) provides an additional security feature. If a user attempts to enter a page that has this decorator attached and is not logged in, they will not be able to access the page and will instead be redirected to the login page. 

#### Profile Page
  
- A welcoming image and page title ("username's Den"), using Jinja templating to display the user's name. 

- The main body displays any dog profiles that the user has added, providing instructions and a link on how to add a new dog if they have not yet done so. There is also a floating button with indicative 'plus' sign and a tooltip on desktop so users can add a new dog profile. There is a link to take users to the dog's full profile page plus buttons to edit or delete the dog profile. Defensive design is employed here so that if a user selects the delete button, a card reveal asks them to confirm that they wish to delete.

- There is a list of any reviews that users have left for other dogs. They can follow a link to the dog's full profile so that they can view, edit or delete the review. If no reviews have been left, the user is prompted to leave one if desired, with a link to the All Dogs page.

- Users may only view their own profile page. In addition to the login decorator, a profile page may only be viewed if that user is in session. Otherwise, a flash message will inform the user that they need to log in to view the page and they will be redirected to the login page. 

- The `title` filter is used when displaying data from the database's 'dog' collection. This ensures that names are displayed with the first letter in capitals, even if the user added data in lowercase on the 'add dog' form. This was chosen over `capitalize` as some dog breeds will contain two or more words. It was later decided to use `upper` for locations as only the first letter of a postcode would be capitalised using `title`.

#### Add Dog Form
  
- A welcome image in keeping with the rest of the site plus a button providing the user with the convenient option to return to their profile page without having to use the browser 'back' button. A simple 'Back' button is not used here as the Profile page is the only page that gives access to the Add Dog page

- The form requests all the details required for the dog profile and writes the information to the 'dog' collection in the database when submitted. There is also a 'cancel' button to take the user back to their profile page without submitting any information.

- The form fields provide the user with guidance, including indicative icons and helper text beneath the form field where appropriate. All form fields are required except the image field. The form line turns green with a valid input and red with an invalid input. The image field currently requires a URL link of the image. This is acceptable for the first development stage but a more suitable method of uploading an image will be added - see 'Future Features'. If an image is not supplied, a default image will be displayed where relevant.

- In addition to the form fields, there is a 'reference' field added in the backend. This field is a randomly generated UUID number, truncated to eight characters, that will be used as a reference number for each dog profile. This was selected in favour of using the ObjectId as an eight character reference was required and truncating the ObjectId would leave similar results, whereas the UUID would give more random and differing results.

#### Edit Dog Form
  
- The edit form allows users to amend any of the data they supplied when creating their dog profile. When the form loads, the fields are populated with the data previously supplied so the user knows the current state of ther data. The textarea input in the 'add_dog' view was amended at this point to ensure that the data written to the database would have the first letter of each sentence capitalised. It is then a simple case of injecting the data into the edit form when it loads.

- As an extra security measure, any links to this edit form will only be available to the user who created the dog profile or to the admin user. Once the 'Edit Dog' button is clicked, the database record for that dog profile will be updated with the information submitted in the form. 

#### Delete Functionality
  
- The D element of CRUD functionality is satisfied by giving the user the option to delete any records that they have created. Admin users also have access to delete any records stored on the database. In each case, only the user creator and the admin user will have access to this functionality for each record. 

- As part of the defensive design of the site, any time a delete button is clicked, the user will be prompted to confirm that they wish to proceed with the cancellation before the record is removed from the database.

#### All Dogs Page
  
- This page displays all the dog profiles on the database. Each profile is presented in a card with basic information of image, name and location. This gives users a quick snapshot of each dog to help them to decide whether the dog may be a match for a pal for their own dog. If they would like to investigate further, they can click on the large indicative eye icon to view the full profile.

- The dog profile cards are the same as those used on the profile page so a template of the card code (`dog_cards.html`) is inserted to avoid repeating code. Similarly, the back button is added by inserting the `return.html` template. The same edit and delete options are therefore available to users who created the profile and to admin users.

- The navigation link to the page is available to all users, including those not logged in. However, the `@login_required` decorator has been added so that only logged in users may view the page content. This is to firstly provide registered users with peace of mind that their dogs' information is not exposed to anyone who comes on the site. Secondly, it encourages unregistered users to sign up to explore the site content.

- As this page will display all the dog profiles on the site, pagination has been added to prevent a long downward scroll. The display has been limited to six profile cards so they will sit uniformly on all screen sizes. 

- A search function is provided so that users can narrow down the profiles to be displayed without having to search through all of them. This includes searches for breed, sex and location. Search indices were created using the Python interpreter in the command line to avoid conflicting simultaneous searches that could occur had they been created in the search view in `app.py`.

#### View Dog Page
  
- This page reads the data from the dog collection in the database (that was supplied from the Add Dog form) and displays it in an aesthetic manner so that users can learn about the featured dog. 

- If the user who created the profile has been verified by admin, a green tick with 'Verified User' tooltip appears next to the dog's name. This is to give users some reassurance when selecting which dogs to meet.

- Beneath the dog information, any reviews that the dog has received are displayed . An 'add review' button opens up a modal and allows the user to leave a review for the dog. If the user has left a review, buttons to edit or delete the review are visible. These are also available to admin users.

- Finally, if the user is interested in meeting the dog, there is a button linking to the Contact page. Ideally, a more direct way to contact other users would be employed (see Future Features) but with the developer's current technical knowledge and time available, this method was selected. 
 
#### Contact Page
  
- The Contact page is available to all users as it is open for general enquiries. However, not all fields are available to all users. If a registered user is interested in meeting one of the dogs on the site, there is a field for them to input the dog's reference code (found on the dog profile page). This field is not available to users who are not logged in. 

-  An advisory note that members need to undergo safety checks prior to being verified provides reassurance to users as to the safety of the site.

- Once the message has been submitted, the user will be provided with feedback via a modal that either their message has been received or that there has been a problem sending it. Messages are handled by EmailJS and send a copy to the sender as well as to the nominated admin email address. 

#### Home Page
  
- The site's landing page immediately provides users with a solid understanding of what the site is about. The heading, image of dogs playing together and background text sets the scene. There is an immediate reassurance that the safety of users and dogs is paramount.
 
 - The secondary image and navigation buttons displayed depend on whether or not the user is logged in. A logged in user will have options to navigate to either their profile page or to the All Dogs page so they can search profiles. Non-logged in users are given the option to either log in or register.
 
 - Finally, in order to provide up-to-date information, the general profile cards of the six most recently added dog profiles is displayed. This is also available to non-logged in users as an incentive to either log in or register. Clicking the view dog button will take users to the All Dogs page but only logged in users will be able to view this page. 
 
 #### Breed Groups Page
  
- The breed groups page is educational but also complements the search function. All users can view this page as they are able to learn about the different dog breed groups. This can help to inform a decision for either current owners as to which dog would be suitable to meet their own dog or for prospective owners as to which dog would be suitable to become a part of their home. 

- Some background information is provided for each breed group plus a link to take the user to the All Dogs page. The All Dogs page will display only dogs belonging to that breed group. Again, only logged in users will be able to view the All Dogs page.

 #### Admin Page
  
- The Admin page is only available to users with admin rights (`is_admin: true` in the user record). An `@is_admin` decorator  has been added to all pages where only the admin user should have access. This is to prevent other users from forcing their way onto a restricted page by typing in an admin URL.

- The Admin page displays all the registered users with options to view the user's profile page, verify the user or delete the user from the database. A flash message will advise the admin user that the user has been successfully verified or if they are already verified.  Defensive design again requires confirmation before a user profile is deleted.
 
- As previously mentioned, admin users have rights to edit and delete all profiles and reviews across the site.

**ADMIN AUTHENTICATION DETAILS**
|Username|Password  |
|--|--|
| Admin123 |p00chPal5  |

Other test user profiles can be accessed by both username and password set to user0001, user0002, user0003 etc.

### Future Features

This site is well set up to be further developed, once my knowledge, experience and time allow. Features that I have already identified include -

- A more suitable way for users to add images to the site than the current URL method. In particular for this site, users would most likely want to upload their own photos of their dogs and would not likely have URL image links for them. Uploading to a cloud storage site such as [Amazon AWS](https://aws.amazon.com/media-sharing/) would be a good solution.
- A better way for users to communicate with each other would be favourable. A real time chat function for verified users, such as that provided by [SocketIO](https://socket.io/) would be ideal.
- Use of [Google Maps Geocoding API](https://developers.google.com/maps/documentation/geocoding/overview) to help locate users on a map would be a good addition to the site.
- Extra dog profile features such as star ratings or favourites.
- Additional admin features such as user entries pending admin approval before being published.
- A forgotten username/password function to assist users when logging in.
- A dark theme using JavaScript to improve site accessibility.
- A preloader to display as the pages load to fill in for any page loading delays. 

## Technologies Used

### Languages Used

-  [HTML5](https://en.wikipedia.org/wiki/HTML5) for structuring the site
-  [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) for styling the site
-  [JavaScript](https://en.wikipedia.org/wiki/JavaScript) for site logic
- [Python](https://www.python.org/) for site functionality and accessing the database. [Jinja](https://jinja.palletsprojects.com/en/3.0.x/) was used as a templating engine.

	- Although no specific naming methodology was employed (such as BEM), class and function names are descriptive of their purpose so that they can be easily identifiable to other developers.

	- Comments are placed appropriately within the HTML, CSS, Python and JS code to improve readability.

  

### Frameworks, Libraries & Programs Used

1.  [Materialize:](https://materializecss.com/)

	- Materialize CSS was used to assist with the responsiveness and styling of the website.

1.  [Hover.css:](https://ianlunn.github.io/Hover/)

	- Hover.css was used to add reactive functionality to some links and buttons.

1.  [Google Fonts:](https://fonts.google.com/)

	- Google Fonts was used to import the 'Neucha' and 'Lato' fonts into the style.css file, which is used throughout the project.

1.  [Font Awesome:](https://fontawesome.com/)

	- Font Awesome was used to add icons for aesthetic and UX purposes.

1.  [jQuery:](https://jquery.com/)

	- jQuery was used to assist with manipulation of the Document Object Model to make the site interactive for users.

1.  [Git](https://git-scm.com/)

	- Git was used for version control by utilising the Gitpod terminal to commit to Git and Push to GitHub. Branches were utilised to develop different features before merging into the main branch, once all changes were considered ready to implement.

1.  [GitHub:](https://github.com/)

	- GitHub was used to store the project code after being pushed from Git.

1.  [GitHub Project Board:](https://github.com/SteveKennyUK/pooch_pals/projects)

	- The GitHub Project Board was used to project manage the creation of the site. This uses a kanban board to display all tasks and view progress.

1.  [Lucidchart](https://www.lucidchart.com/pages/)

	- Lucidchart was used to create the site map drawings and database schema during the design process.
	
1.  [Balsamiq:](https://balsamiq.com/)

	- Balsamiq was used to create the [wireframes](https://github.com/SteveKennyUK/pooch_pals/tree/main/static/images/wireframes) during the design process.

1.  [Color-hex](https://www.color-hex.com/user/add-palette.php)

	- Color-hex was used to display the colour palette choice.

1.  [Looka:](https://looka.com/)

	- Looka was used to create the website [Logo](https://github.com/SteveKennyUK/pooch_pals/blob/main/static/images/logo.png) and [Favicon image](https://github.com/SteveKennyUK/pooch_pals/tree/main/static/images/favicon).

1.  [GIMP:](https://www.gimp.org/)

	- GIMP was used to resize images and edit photos for the website.

1.  [favicon.io:](https://favicon.io/favicon-converter/)

	- favicon.io was used to convert the logo to a favicon to enable full web browser compatibility.

1.  [WebAIM](https://webaim.org/resources/contrastchecker/)

	- WebAIM was used to check that foreground and background colour contrasts meet WCAG accessibility requirements.

1.  [Webformatter](https://webformatter.com)

	- Webformatter was used to assist in optimising code readability.

1.  [Autoprefixer](https://autoprefixer.github.io/)

	- Autoprefixer was used to parse CSS and add vendor prefixes.

1.  [TinyPNG](https://tinypng.com/)

	- Tiny PNG was used for image compression.

1.  [W3Schools](https://www.w3schools.com/)

	- W3Schools was used for coding guidance and clarification.

1.  [RandomKeygen](https://randomkeygen.com/)

	- RandomKeygen was used to generate a secure environmental secret key.

1.  [Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/)

	- Werkzeug was used to provide secure user authentication.

1. [EmailJS](https://www.emailjs.com/) 
	- EmailJS was used to create the email service.

## Deployment
---
Although the application has been developed using GitHub, GitHub Pages is only capable of hosting static websites. It is therefore necessary to use a platform capable of hosting backend applications. The chosen platform is [Heroku](https://www.heroku.com/), a container-based cloud Platform as a Service (PaaS).

### Environmental Variables
The application's environmental variables are contained within a file named `env.py`. This file contains sensitive information so should be stored within the application's `.gitignore` file to prevent the information being shared e.g. committed to GitHub.
The default environmental variables are set as follows -

    import os  
    
    os.environ.setdefault("IP", "0.0.0.0")
    os.environ.setdefault("PORT", "5000")
    os.environ.setdefault("SECRET_KEY", "<application's secret key>")

In order to connect to MongoDB, these additional environmental variables are required - 

    os.environ.setdefault("MONGO_URI", "<mongodb connection string>")
    os.environ.setdefault("MONGO_DBNAME", "<database name>")

The connection string is obtained within MongoDB by 

 1. Navigating to 'Databases'.
 2. Within the 'Database Deployments' section, selecting 'Connect'.
 3. Ensuring the correct driver and version is selected e.g. Python 3.6 or later.
 4. Copying the connection string and pasting into the `env.py` file, inserting your own information where there is placeholder text for password and database name.


### Heroku
In order to make the application ready to work in Heroku, the following steps are first necessary -

 1. Provide Heroku with a list of applications and dependencies that are required to run the site. These are stored in the requirements.txt file, which is created using the following command - 
 
	`pip3 freeze --local > requirements.txt`
	
	This command should be run each time a new application is added.

 2. Inform Heroku of the Python file that is used to run the application. This information is stored in the Procfile and the following command is used to include the Python `app.py` file used for this application -    
   
	 `echo web: python app.py > Procfile`
	 
	 Ensure that any extra blank line in the Procfile is deleted as this could 		cause issues when running the app. 
 
 3. Push the files to GitHub and deploy to Heroku using the below steps.

### Deployment Steps

 1. Log in to [Heroku](https://www.heroku.com/), select **New** on the upper right hand side and **Create new app** from the dropdown.
 ![deployment image 1](https://github.com/SteveKennyUK/pooch_pals/blob/main/static/images/deployment/deployment_1.JPG)
 2. Create an original name for the app and select the region closest to your location.
 ![deployment image 2](https://github.com/SteveKennyUK/pooch_pals/blob/main/static/images/deployment/deployment_2.JPG)
 3. Go to the **Deploy** tab and under **Deployment method**, select **GitHub**. 
 4. Enter the repository name ('pooch_pals') in the **Connect to GitHub** search box. When the repository appears beneath, click **Connect**. 
![deployment image 3](https://github.com/SteveKennyUK/pooch_pals/blob/main/static/images/deployment/deployment_3.JPG)
5. Click on **Settings** and under **Config Vars**, select **Reveal Config Vars**. This is where the hidden environmental variables need to be stored so Heroku can read them.
![deployment image 4](https://github.com/SteveKennyUK/pooch_pals/blob/main/static/images/deployment/deployment_4.JPG)
6. Add the environmental variables (matching those inserted into the `env.py` file) to the Config Vars -

|KEY|VALUE  |
|--|--|
| IP | 0.0.0.0 |
| PORT | 5000 |
| SECRET_KEY | < app's secret key > |
| MONGO_URI | < mongodb connection string > |
| MONGO_DBNAME | < database name > |

7. Back in **Deploy**, select **Enable Automatic Deploys** to enable Heroku to automatically update when pushes are made to GitHub.
8. Under **Manual Deploy**, select **Deploy Branch** to start building the app. ![deployment image 5](https://github.com/SteveKennyUK/pooch_pals/blob/main/static/images/deployment/deployment_5.JPG)
'Your app was successfully deployed' will appear once deployment is complete and you may view the live site.   

### Making a Local Clone

It is possible to copy the repository to your local machine so that you can fix merge conflicts, add or remove files and push larger commits without affecting the original repository.  

Cloning a repository pulls down a full copy of all the repository data that GitHub has at that point in time. See [GitHub Docs](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) for further information and below for a summary.

**Please note that the application will only run locally if the environmental variables (including secret keys) used in the original `env.py` file are included in the cloned `env.py` file**.

1. Log in to your GitHub account and locate the [relevant repository](https://github.com/SteveKennyUK/pooch_pals).

2. Click on the 'Code' button, next to the green 'Gitpod' button. This will reveal the 'Clone' option.

3. In order to clone the repository using HTTPS, select HTTPS and copy the link. There is a copy button to the right of the URL.
![deployment image 6](https://github.com/SteveKennyUK/pooch_pals/blob/main/static/images/deployment/deployment_6.JPG)

4. Next, open Git Bash. See [here](https://git-scm.com/downloads) for download options, if required.

5. Change the current working directory on your local machine to the location where you want the cloned directory to be made.

6. Type `git clone` into your IDE terminal followed by the URL you copied in Step 3.
```
$ git clone https://github.com/SteveKennyUK/pooch_pals.git
```
7. Press Enter.

8. Your local clone will be created.
```
$  git clone https://github.com/SteveKennyUK/pooch_pals.git
Cloning into 'pooch_pals'...
remote: Enumerating objects: 97, done.
remote: Counting objects: 100% (97/97), done.
remote: Compressing objects: 100% (73/73), done.
remote: Total 97 (delta 27), reused 82 (delta 16), pack-reused 0
Receiving objects: 100% (97/97), 1.20 MiB | 12.66 MiB/s, done.
Resolving deltas: 100% (27/27), done.
```

## Credits 

### Code 

-  [Code Institute](https://codeinstitute.net/) tutorials provided helpful guidance in creating the code for this project, particularly [Tim Nelson](https://github.com/TravelTimN/2BN-Tim)'s Task Manager Tutorial. 
- The following Code Institute students and alumni provided ideas, guidance, inspiration and general improvement in my coding understanding and development while creating this project -
	- [Ed Bradley](https://github.com/Edb83/self-isolution) 
	- [Proud Unicorns](https://github.com/irasan/hackpride2021)
	- [Melinda Zhang](https://github.com/MelindaZhang2020/CI-MS3-Tutti-Fruitti) - in particular, helped to understand the use of ObjectId.
	- [Suzy Bennett](https://github.com/suzybee1987/the-book-nook-project)
- Code Institute Tutor Igor Basuga provided invaluable assistance when I was having issues using modals to edit reviews.
- Code Institute Tutor Rebecca provided invaluable assistance when I was having issues with links and redirection on the search page.  
- Code for the floating scroll to top button was provided by [W3Schools](https://www.w3schools.com/howto/tryit.asp?filename=tryhow_js_scroll_to_top) and slightly modified by the developer to suit the site.  
- Many helpful hints and guidance were provided by posts by other developers on [Stack Overflow](https://stackoverflow.com/).

  

### Content

- Dog breed group descriptions courtesy of [PDSA](https://www.pdsa.org.uk/pet-help-and-advice/looking-after-your-pet/puppies-dogs/dog-breed-groups). Crossbreed description courtesy of [The Kennel Club](https://www.thekennelclub.org.uk/getting-a-dog/are-you-ready/what-is-a-crossbreed-dog/).
- Information for dog personality descriptions taken from [The Kennel Club](https://www.thekennelclub.org.uk/breed-standards/)	and [dogtime.com](https://dogtime.com/dog-breeds/profiles).

  
  

### Media
 - General
	-  [Background wallpaper](https://github.com/SteveKennyUK/pooch_pals/blob/main/static/images/background-wallpaper.jpg) courtesy of [Julia B](https://www.vecteezy.com/members/julia-b2008383144) at [Vecteezy](https://www.vecteezy.com/vector-art/3485476-black-and-white-pattern-with-a-dog-theme). 
	- [Default dog image](https://github.com/SteveKennyUK/pooch_pals/blob/profile/static/images/default-dog.jpg) courtesy of [pixy.org](https://pixy.org/574674/).
 - Home Page
	 - [Landing image](https://github.com/SteveKennyUK/pooch_pals/blob/contact/static/images/home-img.jpeg) courtesy of [raygina at Cleanpng](https://www.cleanpng.com/users/@raygina.html).
 - Register Page
	 - [Register form image](https://github.com/SteveKennyUK/pooch_pals/blob/main/static/images/register-img.JPG) courtesy of [volyk at VectorStock](https://www.vectorstock.com/royalty-free-vector/working-at-home-men-vector-30492563).
 - Log In Page
	 - [Log In form image](https://github.com/SteveKennyUK/pooch_pals/blob/main/static/images/login-img.JPG) courtesy of [Mentalmind at VectorStock](https://www.vectorstock.com/royalty-free-vector/focused-guy-and-dog-vector-38816185).
- Profile Page
	- [Profile page image](https://github.com/SteveKennyUK/pooch_pals/blob/main/static/images/profile-img.JPG) courtesy of [jemmastock at VectorStock](https://www.vectorstock.com/royalty-free-vector/man-with-dog-cartoon-vector-18933023).
- Add Dog Page
	- [Add Dog page image](https://github.com/SteveKennyUK/pooch_pals/blob/main/static/images/add-dog-img.JPG) courtesy of [fizzgig at VectorStock](https://www.vectorstock.com/royalty-free-vector/happy-dog-vector-258271).
	- Images for dog profiles courtesy of  [Kennel Club](https://www.thekennelclub.org.uk/breed-standards/)	and [dogtime.com](https://dogtime.com/dog-breeds/profiles).
- Edit Dog Page
	- [Edit Dog page image](https://github.com/SteveKennyUK/pooch_pals/blob/edit_dog/static/images/edit-img.jpg) courtesy of [Poul_Carlsen at VectorStock](https://www.vectorstock.com/royalty-free-vector/cartoon-of-two-happy-children-with-a-family-dog-vector-19930935).
- All Dogs Page
   - [All Dogs page image](https://github.com/SteveKennyUK/pooch_pals/blob/main/static/images/dogs-img.JPG) courtesy of [Igor Zakowski at VectorStock](https://www.vectorstock.com/royalty-free-vector/scottish-terrier-purebred-dog-cartoon-vector-35696699).
 - Breed Group Section
   - [Breed Group page image](https://github.com/SteveKennyUK/pooch_pals/blob/main/static/images/breeds-img.JPG) courtesy of [muchmania at VectorStock](https://www.vectorstock.com/royalty-free-vector/group-of-dog-breeds-vector-20466196).
	- Breed group images courtesy of [PDSA](https://www.pdsa.org.uk/pet-help-and-advice/looking-after-your-pet/puppies-dogs/dog-breed-groups). Crossbreed image courtesy of [Trending Breeds](https://www.trendingbreeds.com/wp-content/uploads/2019/07/Cockapoo-Breed-Overview-large.jpg). 
- Contact Page
   - [Contact page image](https://github.com/SteveKennyUK/pooch_pals/blob/main/static/images/contact-img.JPG) courtesy of [Skathi at VectorStock](https://www.vectorstock.com/royalty-free-vector/cartoon-style-of-postal-dog-vector-13611534).
 - Error Pages
   - [400 image](https://github.com/SteveKennyUK/pooch_pals/blob/main/static/images/400.jpg) courtesy of [faster panda kill kill](https://www.flickr.com/photos/chainsawpanda/99058668/) at [HTTP Status Dogs](https://httpstatusdogs.com/400-bad-request). 
   - [401 image](https://github.com/SteveKennyUK/pooch_pals/blob/main/static/images/401.jpg) courtesy of [basykes](https://www.flickr.com/photos/basykes/28995006/) at [HTTP Status Dogs](https://httpstatusdogs.com/401-unauthorized). 
   - [404 image](https://github.com/SteveKennyUK/pooch_pals/blob/main/static/images/404.jpg) courtesy of [HTTP Status Dogs](https://httpstatusdogs.com/404-not-found). 
   - [500 image](https://github.com/SteveKennyUK/pooch_pals/blob/main/static/images/500.jpg) courtesy of [monicaewagner](https://www.flickr.com/photos/11155422@N00/4232049056/) at [HTTP Status Dogs](https://httpstatusdogs.com/500-internal-server-error). 

### Acknowledgements

- My Mentor Antonio Rodriguez for his advice and feedback.

- [BorrowMyDoggy](https://www.borrowmydoggy.com/) provided me with some inspiration and ideas.
  

### Notice

- This site has been created for educational purposes only.  