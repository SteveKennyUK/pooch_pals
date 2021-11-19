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

**Interactive Design**
The principles of Interactive Design (IxD) promote consistency, predictability, visibility, learnability and feedback as central to the above aim. The structure of this site aims to follow these principles.  

 -  #### Page Structure

	- The nature of this site necessarily involves spreading content over several pages. The user expects different functions to have their own pages e.g. registration, login, profile pages. The user will therefore be provided with good, clear and intuitive links to the different pages, either via the navigation bar or through buttons and links.
	
	- In order to keep the site consistent and predictable, elements will follow the same structure across all pages. All pages will have the same background image, navigation bar and footer. Information will be displayed using cards which will be displayed in a consistent manner.

	- The landing page will immediately address some of the user goals, with clear directions to desired content through navigation links, calls to action and meaningful images. These are consistent with previous user experiences on other sites.
	
	- A separate contact section is also expected. The 'Contact' page provides a contact form where users can request further information, particularly if they wish to register interest in contacting another user/dog owner. Input fields will react to user actions, which will provide reassuring feedback to the user. As the site develops and expands, a facility for users to contact each other directly e.g. direct chat, will be added.
	
	- Separate error pages in the event of a broken link or server error will be added. This feedback adds reassurance to the user and provides them with clear instructions on how to return to the site.
  
 -  #### Visibility

	- The location and purpose of elements should be clear to users. Where appropriate, there will be partial overlay of elements on the screens to hint to the user that there is more content below. Additionally, if necessary, a scroll down arrow will be employed to indicate to the user that useful content can be accessed further down. 

	- There will also be a floating scroll up arrow where the page length requires a degree of scrolling down so users can return to the top of the screen with a single click from anywhere on the page. The smooth scroll styling will enable the user to understand the page layout and where the various elements are located. 

	-  Dropdown menus will have an arrow to indicate that there are further options available. This is a common practice to make elements more visible so should be predictable to the user. If not, the consistent use of this practice will help the user to learn what such arrows mean and be comfortable when encountering them.
  
 -  #### Navigation

	- The site navigation will again be consistent and predictable by following the convention of the site logo on the top left with a horizontal navigation bar to the right of the logo. 
	
	- A fixed navigation bar and sticky footer will be employed. This will provide a better visual experience for the user and, in conjunction with the floating scroll up arrow, will reduce the amount of scrolling required by the user.
	
	- The navigation bar will be responsive and will use a hamburger menu for smaller devices. This is consistent and predictable with most sites on mobile devices. The menu will then push the page content down when activated to maximise visibility of the options.  

 -  #### Buttons and Links

	- Buttons and links will be used to create a smoother navigation process for the user. The purpose of these must be made clear to the user. Buttons and links will react when the mouse hovers over them. This conventionally suggests that clicking on the button or link will make something happen. The use of unambiguous text or iconography will make it clear to the user what will happen when the button or link is clicked.
	
	- Styling the buttons and links in a consistent manner and employing the same reaction when e.g. the mouse hovers will help the user to learn and predict what they need to do to achieve their goals.
	
	- When a button is clicked, the user will be provided with some feedback to reassure them that their action has been acknowledged. This will be either a change in the button appearance or a flash message appearing. The flash message will either confirm that the required action has been successful or inform the user that an error has occurred, with instructions on what the user should do next. This builds trust with the user.	
	
	- External links will always open in another page (by adding the `target="_blank"`attribute inside the link's anchor element). This makes for a better user experience as the user will not need to use the back button to return to the site. It is also good practice to add `rel="noopener"` as this adds a security layer by preventing the new page from accessing the original window object.
  

 -  #### Iconography

	- Icons will be used to help users to quickly identify content matter. A visual representation can say more than words and often stands out more. A quick scan of the page will pick out icons and well chosen ones will stand out and immediately assure the user as to the associated content.

	- The site logo acts in a similar fashion and the user quickly learns to associate the image with the site and its purpose. A favicon, using a dog paw print image, will be also be added. This is now generally expected by users and helps them to identify the site if they have several pages open.

**Information Architecture (IA)**

 - The navigation paths follow a tree structure with the head branches representing the main features. These feature pages, where appropriate, will contain buttons and links leading the user to any sub features relevant to the main branches, avoiding overloading the navigation bar. Sub features include links to edit, delete and create new content; these will require no more than three clicks to reach. 

 - Once the site evolves, additional branches can be added but the fundamental structure will remain.
 
 - The IA varies slightly, dependent on the current user category - please see below.

![User 1 - not registered/logged in](https://github.com/SteveKennyUK/pooch_pals/blob/main/static/images/readme/User%20-%20not%20logged%20in.jpeg)

![User 2 - registered & logged in](https://github.com/SteveKennyUK/pooch_pals/blob/main/static/images/readme/User%20-%20registered%20&%20logged%20in.jpeg)

![User 3 - Admin](https://github.com/SteveKennyUK/pooch_pals/blob/main/static/images/readme/Admin.jpeg) 	
	