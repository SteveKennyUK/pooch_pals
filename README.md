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

The higher importance/feasibility elements will be incorporated in this first stage of development.		