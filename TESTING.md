## [HTML W3 Code Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)
The 11 HTML pages in this project were each tested for validation to ensure there were no HTML syntax errors in the project.

 - [Add Dog](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/html-val-add-dog.JPG)
 - [Admin](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/html-val-admin.JPG)
 - [All Dogs](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/html-val-all-dogs.JPG)
 - [Breed Groups](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/html-val-breed.JPG)
 - [Contact](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/html-val-contact.JPG)
 - [Edit Dog](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/html-val-edit-dog.JPG)
 - [Home Page](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/html-val-home.JPG)
 - [Log In](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/html-val-log-in.JPG)
 - [Profile](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/html-val-profile.JPG)
 - [Register](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/html-val-register.JPG)
 - [View Dog](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/html-val-view-dog.JPG)

---
## [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
The style.css file was tested for validation to ensure there were no CSS syntax errors in the project.

The [direct input test](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/css-val.JPG) of the style.css file returned no errors so the project syntax is good.

---
## [JS Hint](https://jshint.com/)
JavaScript files were tested throughout the project to detect any errors and potential problems in JavaScript code.

The [email.js](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/js-val-2.JPG) and [script.js](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/js-val-1.JPG) scripts were clear of any warnings and only referenced a couple of variables that were called in HTML files.

---

## [PEP8 Online](http://pep8online.com/)
The app.py file was tested regularly throughout the project to check for any errors and to ensure that the Python code was PEP8 compliant.
[The PEP8 online check](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/pep8-val.JPG) confirms that the code meets all requirements

---
## [WAVE](https://wave.webaim.org/)
The Web Accessibility Evaluation Tool was used to check the accessibility standards of the site. 

I was only able to check the pages available to users that are not logged in as the site could not access pages that require a password.
 
The pages that could be checked all scored well. There were no errors returned, just a few contrast issues. However, most of these were down to the page rendering Materialize default colours rather than the colours actually used, particularly on the navigation bar and footer. 

The checks confirmed that elements were all suitably labelled with ARIA tags. 

---
## [Google Chrome Developers Tools](https://developer.chrome.com/docs/devtools/)
 - Google Dev Tools was used extensively during project development to help identify and solve any syntax and styling issues.
 - The Dev Tools [Lighthouse tool](https://developers.google.com/web/tools/lighthouse) is useful to check the performance quality of the site. The site scored well overall in all categories. The only score below 90 was the Best Practices on desktop. However, this score appeared to be down to the site not using HTTPS, which is something beyond my control.
   
	 - [Mobile performance](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/lighthouse-mobile-report.JPG)
	 - [Desktop performance](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/lighthouse-desktop-report.JPG)
   
- Responsiveness of different screen sizes was continually checked during the development process to ensure that the site rendered as well as possible on differing screen sizes and orientations. Although helpful, this is not foolproof so further responsiveness testing was required.

---
## Responsiveness Testing
-   The site design adheres to a mobile-first philosophy and was tested throughout development to ensure that it satisfies the requirements of all screen sizes through Google Dev Tools. The decision to use [Materialize](https://materializecss.com/) as a design framework, particularly the use of Materialize cards, meant that responsiveness was automatically at the forefront of page layouts. 

- The original intention of keeping the site clean and uncluttered helped with responsiveness as the potential for content overflow was reduced. Where there was any degree of textual content, the Materialize `flow-text` class was added to maintain text readability. The Breed Groups page was the page with most textual content and some media queries were added to remedy any overflow, particularly in landscape mode.

- [Responsinator](https://www.responsinator.com/) was used to test the completed project on different devices  - please see [link](http://www.responsinator.com/?url=http%3A%2F%2Fpooch-pals-ms3.herokuapp.com%2Findex) for results.

- In addition to automated tests, using real devices is desirable. Thanks to friends and family, I was able to test the site on various devices, including Samsung Galaxy S8, Samsung Galaxy S9, various iPhones, iPads, Samsung Galaxy Tabs, Asus Zenbook and Lenovo ThinkPad. Results were very positive. 

---
## Browser Compatibility
[Autoprefixer](https://autoprefixer.github.io/) was used to add vendor browser prefixes. Manual testing was also carried out.

The site was tested on a ASUS Zenbook desktop, Samsung Galaxy mobile and iPhone 11 using various browsers.
- **Chrome** The site was developed using Chrome so works well. See [desktop screenshot](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/chrome.JPG). Mobile view was good in portrait and landscape.
- **Mozilla Firefox** [Desktop](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/firefox.JPG). Mobile view was good in portrait and landscape.
- **Edge** [Desktop](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/edge.JPG). Mobile view was good in portrait and landscape.
- **Opera** [Desktop](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/opera.JPG). Mobile view was good in portrait and landscape.

---

## Testing User Stories 

-   #### User Goals (general)
    
    -   As a user, I want to be immediately drawn into the site and understand its main purpose.
	    - The site's landing page immediately engages with the user. The background wallpaper, title image and introductory text let users know that this site is about meeting dogs. The images and typography project a fun and welcoming ambience. 

	    	- [Landing page](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/user-goals-1.JPG)
    -   As a user, I want to be able to easily identify what I need and navigate the site to get to it.
	    - The navigation bar provides clear and concise direction to all the principal pages on the site. The bar is consistent over all pages and is fixed so that it is always visible. The bar also highlights which page the user is currently viewing. Navigation collapses into a hamburger menu on smaller devices, opening to reveal the same pages. Navigational buttons and links are also visible and intuitive
	    	- [Navbar - logged out](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/user-goals-2.JPG)
	    	- [Navbar -logged in](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/user-goals-3.JPG)
	    	- [Navbar - mobile hamburger menu](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/user-goals-4.JPG)
	    	- [Navbar - mobile menu open](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/user-goals-5.JPG)
	    	- [Navigational button](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/user-goals-6.JPG)
    -   As a user, I want concise but informative content, displayed in an aesthetic, intuitive and consistent manner.
	    - Information is displayed using cards throughout, which maintains a consistency in presentation. Rather than overloading users with too much information, users are first presented with a synopsis of the dog profile information, which then allows them to make a decision as to whether they would like to find out more. The detailed profiles are presented in a manner that makes information easy to digest. Buttons, such as edit and delete, are presented in a consistent manner throughout.
	    	- [Synopsis card](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/user-goals-7.JPG)
	    	- [Full profile card](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/user-goals-8.JPG)
    -   As a user, I want to be able to view the site clearly and intuitively on different device sizes.
	    - Strict attention has been paid to the principles of responsive design throughout the development process. Screen displays react to changes in resolution and orientation to maintain an optimal visual experience for the user.
	    	- [Small screen display](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/responsive-1.JPG)
	    	- [Larger screen display](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/responsive-2.JPG)
	     
    -   As a user, I expect the site to be fully accessible.
	    -  The site uses assistive technology, including aria labelling, alt text for non-textual elements, such as images, and  `sr-only` classes. Semantic  `html`  is used to further assist screen readers.
    
-   #### [](https://github.com/SteveKennyUK/pooch_pals#site-owner-goals)Site Owner Goals
    
    -   As the site owner, I want features and content that will engage new users quickly, encourage them to explore the site and draw them back in the future.
	    - The landing page is very welcoming in terms of colour, imagery and typography. It immediately entices users by providing a synopsis of the most recent additions to the site. Navigational links throughout the landing page encourage users to explore further. The breed group page provides some educational material and encourages current dog owners or potential dog owners to register in order to continue to learn about which dogs may be suitable for their dogs or for themselves. 
	      - [Landing page recent additions and nav links](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/owner-goals-1.JPG)
	      - [Breed groups information](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/owner-goals-2.JPG)
    -   As the site owner, I want users to feel comfortable that their data is secure.
	    - Users are informed on both the landing page and the contact page that only verified users will be allowed to contact other users. Security checks would need to take place before admin grants verified status to a user. Dogs belonging to verified users can be identified by a green tick on their profile page. Any pages that contain more detailed information about the dog profiles are only accessible to registered and logged in users. These pages are protected to prevent non-logged in users forcing access or other users accessing an individual's profile page.
	    	- [Verification notice](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/owner-goals-3.JPG)
	    	- [Verification confirmed](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/owner-goals-5.JPG)
	    	- [User must be logged in to view](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/owner-goals-4.JPG)	    
    -   As the site owner, I want to be able to moderate the site content.
	    - Admin users have control over the site content, with the ability to add, edit and delete any data added by users. A dedicated admin page also allows admin users to view, verify and delete users. This page is protected so that non-admin users cannot access it by force.
	    	- [Admin page](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/owner-goals-7.JPG)
	    	- [Admin user can edit and delete all profiles](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/owner-goals-6.JPG)
	    	- [Access restricted to admin user only](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/owner-goals-8.JPG)
    -   As the site owner, I want the site to be accessible to all users.
	    - See User Goals (General) above.
	    
    -   As the site owner, I want to be able to use the site myself to find playmates for my own dogs.
	    - Owners can set up their own profile pages and interact with other users to find playmates for their own dogs.
	    	- [Site owner's own profile](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/owner-goals-9.JPG)
    -   As the site owner, I want to also be able to develop the site to promote dog accessories and services (either my own or those of a business partner).
	    - There are currently links in the page footer which take users to other organisations and businesses. These could be tracked to register when users click the links and visit the pages. There is also scope to add a dedicated page to promote accessories and services in the future. 
			- [Footer links](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/owner-goals-10.JPG)

-   #### [](https://github.com/SteveKennyUK/pooch_pals#user-stories)User Stories
    
    -   **(Unregistered/logged out user)**
        
        -   I want to be quickly reassured that this site will be of interest to me.
	        - The landing page makes it very clear what the site is about (see User Goals (General) above). Logged out users can browse the breed group and contact pages to gather more information to inform their decision on whether to register.
	        
        -   I want to be able to identify the content of the site and be able to navigate to areas of interest e.g. view dogs on the site.
	        - Navigation links are clear and unambiguous (see User Goals (General) above). As a user, if I am interested in viewing dog profiles on the site, I will need to first register. This helps to attract genuinely interested users only.
	         
        -   I want to be able to register to join the site effortlessly and with minimal information required.
	        - There are clear navigational links to the registration page, located both on the navigation bar and on the landing page (also at the foot of the login page - see below). The registration form is simple and clear, requiring users to supply only a username, password and email address. There are helpers on the form should the user supply any invalid entries. 
	        	- [Nav links to registration page](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/logged-out-1.JPG)
	        	- [Registration form](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/logged-out-2.JPG)
	        	- [Registration form validation helpers](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/logged-out-3.JPG)	         
        -   I want to be able to contact the site owners with any questions.
	        - There is a contact page accessible from the navigation bar. This page contains a form that users may complete to make any enquiries to the site owners/admin. Users do not need to be registered to use this service.
	        	- [Contact page](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/logged-out-4.JPG)
    -   **(Registered/logged in user)**
        
        -   I want to be able to login and logout easily.
	        -  There are clear navigational links to the login page, located both on the navigation bar and on the landing page (also at the foot of the registration page - see above). The login form is simple and clear, requiring username and password only. There is feedback in the event of invalid entries. The logout button is clearly and predictably located in the 'Account' dropdown navigation link (as part of all links in mobile dropdown menu).
	        	- [Log in form](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/logged-in-1.JPG)
	        	- [Logout button desktop](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/logged-in-2.JPG)
	        	- [Logout button mobile](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/logged-in-3.JPG)
        -   I want to be able to view my profile and see my dog's profile and any reviews I have left for other dogs.
	        - There is a link to the profile page in the 'Account' dropdown navigation link for logged in users.
	        	- [Profile page](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/logged-in-4.JPG)
        -   I want to be able to add a profile for my dog(s) with relative ease.
	        - An intuitive and tooltip labelled 'Add New Dog' button is located in a user's profile page. This takes the user to a form for adding a dog profile to the site. This form has textual instructions, iconography and feedback helpers to assist the user in adding a profile with minimal fuss.
	        	- [Add New Dog button](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/logged-in-5.JPG)
	        	- [Add Dog form](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/logged-in-6.JPG)
        -   I want to be able to leave reviews for other dogs on the site.
	        - An intuitive and tooltip labelled 'Add Review' button is located in a dog's profile page. This opens a modal where a user may leave a review.
	       	    - [Add Review button](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/logged-in-7.JPG)
	        	- [Add Review modal](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/logged-in-8.JPG)
        -   I want to be able to edit and/or delete my contributions.
	        - Dog profiles and reviews have buttons providing the user who created them the option to edit or delete.
	        	- [Edit Dog Profile button](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/logged-in-9.JPG)
	        	- [Edit Dog Profile form](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/logged-in-10.JPG)
	        	- [Delete Dog Profile confirmation request](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/logged-in-11.JPG)
	        	- [Edit review modal](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/logged-in-12.JPG)
	        	- [Delete review modal](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/logged-in-13.JPG)	        	        
        -   I want to be able to search for dogs that meet certain criteria e.g. breed, location.
	        - There is a search function on the All Dogs page allowing users to search the dog profiles by breed name, sex, size, location and personality. Button links from the Breed Groups page also return results by breed group.
	        	- [Search bar](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/logged-in-14.JPG)
	        	- [Breed group filter buttons](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/logged-in-15.JPG)
        -   I want to be able to understand more about different dog breeds.
	        - The Breed Groups page provides useful background information about the different dog groups and links to research further.	 
	        	- [Breed Groups page](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/logged-in-16.JPG)       
        -   I want to be able to interact with other site users.
	        - There is a Contact page, allowing users to enquire about other users' dog profiles. This can be further developed for a more direct method - see Future Features. 
	        	- [Contact page for logged in users](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/logged-in-17.JPG)
        -   I want to know that other site users are trustworthy.
	        - Site users are informed that other users need to undergo safety checks prior to any contact being allowed with other users. Dogs belonging to verified users have a green tick on their profile page. See Site Owner Goals above for screenshots.
	          
        -   I would like to be able to save profiles of interest to go back to later.
	        - This is a feature that was deemed out of scope for the first development phase. In future, users will be able to 'favourite' dog profiles to save - see Future Features.
	        
    -   **(Admin/site owner user)**
        
        -   I want to be able to validate users to improve trust in the site.
	        - All users are automatically unverified when registering. Admin can update their status to verified after security checks, with verification status displayed on dog profiles. See Site Owner Goals above.
	        
        -   I want to be able to view, edit and delete all users and entries on the site.
	        - The Admin page is only available to users with admin privileges. This page has additional security features to prevent unauthorised access. Admin users may also edit and delete other user contributions. See Site Owner Goals above.

---

## Further Testing

-   Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

- Peer reviews by fellow Code Institute students, mentors and tutors helped to identify areas I may have overlooked.

-   A large amount of testing was done to ensure that all buttons, links and click events have the desired function. 

All links to external sites should open in a new tab.

**Sitewide**
| | Location | Type | Expected Outcome | Pass/Fail|
-----|-----|-----|-----|-------|
All Users | Navbar | Logo | Navigate to index.html| Pass
|| Navbar | Home Link | Navigate to index.html | Pass
|| Navbar | Breeds Link | Navigate to breed_groups.html | Pass
|| Navbar | Contact Link | Navigate to contact.html | Pass
|| Navbar | Account Link | Open dropdown menu | Pass
|| Navbar | Hamburger (mobile only) | Open dropdown menu | Pass
|| Footer | Kennel Club Link | Open Kennel Club | Pass
|| Footer | PDSA Club Link | Open PDSA | Pass
|| Footer | Dog Accessories Link | Open Pets At Home | Pass
|| Footer | Pet Insurance Link | Open Petplan | Pass
|| Footer | Dog Friendly Holidays Link | Open Canine Cottages | Pass
|| Footer | Contact Form Link | Navigate to contact.html | Pass
|| Footer | Email Link | Open email account with contact@poochpals.com address  | Pass
|| Footer | Telephone Link | Open phone keypad with 02085555555 | Pass
|| Footer | Social Media Link | Open Facebook | Pass
|| Footer | Social Media Link | Open Instagram | Pass
|| Footer | GitHub Link | Open github.com/SteveKennyUK | Pass
|| Floating | Navigational button | Return to top of page | Pass
Users not logged in| Navbar | Dogs Link | Navigate to login.html| Pass
|| Navbar | Register Link | Navigate to register.html | Pass
|| Navbar | Log In Link | Navigate to login.html | Pass
|| All Pages | Attempts to access pages authorised for logged in users only e.g. via manual URL input | Redirect to login page with 'Please Log In To View This Page' flash message | Pass
|Users logged in| Navbar | Dogs Link | Navigate to all_dogs.html | Pass
|| Navbar | Profile Link | Navigate to session user's profile page | Pass
|| Navbar | Logout Link | Log out user and redirect to login.html | Pass
Admin users only| Navbar | Admin Link | Navigate to admin.html| Pass
|Users logged in without admin status| All Pages | Attempts to access pages authorised for admin users only e.g. via manual URL input | Redirect to home page with 'This Page Is Restricted To Admin Access' flash message | Pass

**Home Page**
| | Location | Type | Expected Outcome | Pass/Fail|
-----|-----|-----|-----|-------|
Users not logged in | Main Body | Image | Display login title image | Pass
|| Main Body | Log In Button | Navigate to login.html | Pass
|| Main Body | Register Button | Navigate to register.html | Pass
|| Newest Pals Cards | View Dog Link | Redirect to login page with 'Please Log In To View This Page' flash message | Pass
Users logged in | Main Body | Image | Display profile title image | Pass
|| Main Body | Profile Button | Navigate to session user's profile page | Pass
|| Main Body | All Dogs Button | Navigate to all_dogs.html | Pass
|| Newest Pals Cards | View Dog Link Button | Navigate to view_dog page of the dog on the card | Pass

**Login Page**
| | Location | Type | Expected Outcome | Pass/Fail|
-----|-----|-----|-----|-------|
|| Form | Register Link | Navigate to register.html | Pass
|| Form | Log In Button | Valid input - redirect to session user's profile page with 'Arooo! Welcome back {username}' flash message   | Pass
|| Form | Log In Button | Required field not filled in - 'Please fill in this field' tooltip | Pass
|| Form  | Log In Button | Invalid input - Change to red and inform user of requirements for valid input for username and password if requirements not met | Pass

**Register Page**
| | Location | Type | Expected Outcome | Pass/Fail|
-----|-----|-----|-----|-------|
|| Form | Log In Link | Navigate to login.html | Pass
|| Form | Register Button | Valid input - redirect to session user's profile page with 'Registration Successful' flash message   | Pass
|| Form | Register Button | Required field not filled in - 'Please fill in this field' tooltip plus valid email format required tooltip  | Pass
|| Form  | Register Button | Invalid input - Change input field colour to red and inform user of requirements for valid input for username and password if requirements not met | Pass
|| Form  | Register Button | Username already exists - 'Username already exists, please select another' flash message | Pass
|| Form  | Register Button | Password and Confirm Password fields don't match - 'Passwords Must Match' flash message | Pass

**Profile Page**
| | Location | Type | Expected Outcome | Pass/Fail|
-----|-----|-----|-----|-------|
|| Title Card | Back Button | Navigate to previous page | Pass
|| 'My Dogs' Card | Add Dog Button | 'Add New Dog' tooltip and navigate to add_dog.html   | Pass
|| 'My Dogs' Card  | View Dog Button  | 'View Dog' tooltip and navigate to view_dog page of the dog on the card | Pass
|| 'My Dogs' Card  | Edit Button  | Visible to session user and to admin user. Navigates to edit_dog page for the dog on the card | Pass
|| 'My Dogs' Card  | Delete Button  | Visible to session user and to admin user. Triggers a card reveal asking user to confirm that they wish to delete the dog profile. Clicking 'Cancel' or 'x' closes the card reveal with no action taken. Clicking 'Delete' deletes the dog profile with user redirected to home page and 'Dog Profile Removed' flash message | Pass
|| 'Reviews I've Left'  | Text and Button  | If a reviewed dog has been deleted, it will appear as "Reviewed for '*deleted dog*'" and the 'View {dog_name}' button will not appear  | Pass
|| 'Reviews I've Left'  | View {dog_name} Button  | Navigate to profile page of the reviewed dog  | Pass
|| 'Reviews I've Left'  | Link to view dog profiles   | Shows if user has not left any reviews. Navigate to all_dogs.html  | Pass

**Breed Groups Page**
| | Location | Type | Expected Outcome | Pass/Fail|
-----|-----|-----|-----|-------|
|| Title Card | Back Button | Navigate to previous page | Pass
|| Information Card | Kennel Club Link | Open Kennel Club | Pass
|| Breed Group Cards  | View {Breed Group} Button  | Navigate to All Dogs page where only dogs from the selected breed group will be displayed | Pass

**Add Dog Page**
| | Location | Type | Expected Outcome | Pass/Fail|
-----|-----|-----|-----|-------|
|| Title Card | Profile Button | Navigate to session user's profile page | Pass
|| Form | Cancel Button | Return to session user's profile page | Pass
|| Form | Breeds Link | Navigate to breed_groups.html | Pass
|| Form | Add Dog Button | Required field not filled in - tooltips advising the user of required fields  | Pass
|| Form  | Add Dog Button | Invalid input - Change input field colour to red and inform user of requirements for valid input for fields if requirements not met | Pass
|| Form  | Add Dog Button | Successful submission - redirect to session user's profile page with 'Welcome to the pack {dog_name}' flash message | Pass

**Edit Dog Page**
| | Location | Type | Expected Outcome | Pass/Fail|
-----|-----|-----|-----|-------|
|| Title Card | Back Button | Navigate to previous page | Pass
|| Form | Cancel Button | Return to previous page | Pass
|| Form | Breeds Link | Navigate to breed_groups.html | Pass
|| Form | Form Fields | Fields populated with data currently held in database | Pass
|| Form | Edit Dog Button | Required field not filled in - tooltips advising the user of required fields  | Pass
|| Form  | Edit Dog Button | Invalid input - Change input field colour to red and inform user of requirements for valid input for fields if requirements not met | Pass
|| Form  | Edit Dog Button | Successful submission - redirect to session user's profile page with '{dog_name}'s profile updated!' flash message | Pass

**Dogs Page**
| | Location | Type | Expected Outcome | Pass/Fail|
-----|-----|-----|-----|-------|
|| Title Card | Back Button | Navigate to previous page | Pass
|| Dog Cards  | View Dog Button  | 'View Dog' tooltip and navigate to view_dog page of the dog on the card | Pass
|| Dog Cards  | Edit Button  | Visible to session user and to admin user. Navigates to edit_dog page for the dog on the card | Pass
|| Dog Cards  | Delete Button  | Visible to session user and to admin user. Triggers a card reveal asking user to confirm that they wish to delete the dog profile. Clicking 'x' closes the card reveal and clicking 'Cancel' redirects the user to their profile page, with no action taken. Clicking 'Delete' deletes the dog profile with user redirected to home page and 'Dog Profile Removed' flash message | Pass
|| Search Bar  | Search Button  | If the input field is left empty - tooltip requesting the user to fill in the field. If there are fewer than three characters - tooltip requesting more than three characters are provided.   | Pass
|| Search Bar  | Reset Button  | Refresh the page without submitting any data | Pass
|| Search Bar  | Search Button  | 'See results for {query} below' flash message displays | Pass
|| Search Bar  | Search Button  | If no results returned - 'No results found! Please search again!' returned. Includes a link to refresh the page.  | Pass
|| Search Bar  | Search Button  | If results returned - profile cards of only the profiles matching the search are displayed  | Pass
|| Dog Cards  | Pagination  | Only a maximum of six cards will be displayed on the screen. If there are more than six dog profiles (including those returned for search results), a pagination index will display. Clicking the pagination numbers will search through the results by pages of six profiles.  | Pass

**View Dog Page**
| | Location | Type | Expected Outcome | Pass/Fail|
-----|-----|-----|-----|-------|
|| Title | Back Button | Navigate to previous page | Pass
|| Title  | Verification Icon  | Green tick and 'Verified User' tooltip appears next to dog name only if the user who created profile is verified | Pass
|| Profile | Image  | If the user did not provide an image when adding the dog profile, the designated default image will display instead | Pass
|| Reviews  | Add Review Button  | 'Add Review' tooltip. Button triggers 'Add Review' modal to appear | Pass
|| Add Review Modal  | Modal | 'Cancel' closes modal with no action taken. 'Submit' adds review, closes modal and 'Thank You For Your Review' flash message displays at head of page. | Pass
|| Reviews  | Review Text  | If the user who left a review has been deleted, they will display as "deleted user" | Pass
|| Reviews  | Edit Review Button  | Visible to session user and to admin user, with an 'Edit Review' tooltip . Opens a modal where the user can edit the review. | Pass
|| Reviews  | Edit Review Modal  | Original review populates the textarea. 'Cancel' closes the modal. 'Submit' updates the review, closes the modal and displays 'Review Updated' flash message.  | Pass
|| Reviews | Delete Button  | Visible to session user and to admin user. Triggers a modal asking user to confirm that they wish to delete the review. Clicking 'Cancel' closes the modal with no action taken. Clicking 'Delete' deletes the review, redirects the user to All Dogs page and 'Review Removed' flash message is displayed | Pass

**Contact Page**
| | Location | Type | Expected Outcome | Pass/Fail|
-----|-----|-----|-----|-------|
|| Title Card | Back Button | Navigate to previous page | Pass
|| Form | Cancel Button | Return to previous page | Pass
|| Form | Form Fields | Only display 'Dog Ref:' field to logged in users | Pass
|| Form | Submit Button | Required field not filled in - tooltips and helper text advising the user of required fields  | Pass
|| Form  | Submit Button | Invalid input - Change input field colour to red and inform user of requirements for valid input for fields if requirements not met, including valid email format  | Pass
|| Form  | Submit Button | Display modal providing feedback to the user as to whether or not their message was submitted successfully. Refresh Contact page with all fields cleared. If the message was submitted successfully, a copy will be sent to the email address supplied by the user. | Pass

**Admin Page**
| | Location | Type | Expected Outcome | Pass/Fail|
-----|-----|-----|-----|-------|
|| Title Card | Back Button | Navigate to previous page | Pass
|| User Cards | View User Button | Navigate to the profile page of the user on the card | Pass
|| User Cards | Verify User Button | Update the user's record to show `is_verified: true` and display '{username} Has Been Verified!' flash message. If the user has already been verified there will be a '{username} Is Already Verified' flash message. | Pass
|| User Cards | Delete Button | Triggers a card reveal asking admin user to confirm that they wish to delete the user profile. Clicking 'Cancel' or 'x' closes the card reveal with no action taken. Clicking 'Delete' deletes the user profile, refreshes the Admin page and a 'User Profile Removed' flash message is displayed. | Pass

---

## Bugs
### Resolved Bugs

 -   Several bugs were encountered as a result of using Materialize styling, particularly as I had previously been used to using the Bootstrap framework. The first issue arose when styling the navbar. The brand logo and brand text would not sit horizontally inside the navbar, rather the text would sit beneath the logo, over the main body. I thought that this could be due to the flex settings but I could not resolve the issue by altering the styling settings. I was finally able to resolve the bug by placing the text inside a `span`  element, which brought it inside the navbar, with vertical alignment placing it in the correct position.

 - I was having a few issues with keeping the footer in place on screens with content that does not fill the page. I had encountered this on a previous collaborative project, where the fixed footer would also sometimes cover the page's lower content. I eventually found a way to set up a sticky footer  using simple CSS (see credit in `css.style` under 'Footer'), which circumvented these issues. However, when I added content to the page, it would sit inside the footer. This was a simple oversight on my part - the `{% block content %}` in `base.html` simply sat between the `<nav>` and `<footer>` elements. I had to place the `{% block content %}` inside a container element - in this case the `<main>` element.

 - Registration page - I encountered a bug when setting up the functionality to confirm the user password input on the Register form. I wanted a flash message to appear if the passwords did not match and to refresh the form page to start again. I had a number of bugs, including coding errors (incorrect indentation and syntax), a 'Registration Successful' message appearing with the 'Passwords Not Matching' message and registration going through despite the confirmation password not matching. 
I managed to resolve it in the end by focusing on what to do if the passwords did not match rather than if they did. In placing  `if request.form.get("password") != request.form.get("password-confirm"):` before the form input dictionary values, the flash message and page refresh would trigger before the input values could be added to the database.

 - I wanted to use the 'is_admin' field in the user collection to control access to admin-only functions. I could have used the admin's username (Admin123) to set restrictions e.g. `{% if session.user|lower == "admin123"|lower %}`. However, this would have some restrictions as it would no longer work if admin changed username. There could also be the situation where more than one admin user may be required, which is why using the 'is_admin' field is better. However, I encountered a bug whereby initially non-admin users could not access the Admin nav link but it would then become available to them. After some investigation, I noticed that it became available to all users once the admin user had logged in and logged out again. The problem was the logout set up. The solution was to replace `session.pop("user")` with `session.clear()`as the pop setting only cleared `session["user"]` and not `session["admin"]`. 
 
- I used the `title` filter to capitalise each word where most user inputs on the database are to be displayed. The exception was the textarea 'personality' field, as I did not want every word to be capitalised. Instead, I used `capitalize`so that the first letter of the first word at least would be capitalised. The problem is that if the user inputs more than one sentence into the textarea, only the first sentence will start with a capital letter. I figured that the solution would be to build a function that splits the sentences at " . ", capitalises each sentence then joins them with a " . " . I spent some time experimenting but decided to leave the 'personality' display as the user had input in the textarea. However, I went back to the issue and found some code that would enable me to capitalise each sentence before writing to the database, whether adding or editing a dog profile. Code can be seen [here](https://codehandbook.org/python-capitalize-first-letter-of-all-sentences/). A caveat is that any capitalised words other than those following a full stop, e.g. after a '!', would not be capitalised in the output. The solution would be to add regular expressions to the code. However, I did not have time for this so that is something to go back to in the future.

- I opted to insert a template to display the edit and delete buttons beneath the dog profile for users who had created the profile. These buttons would be used in more than one place, the first being on the profile cards on the 'all dogs' page, where they were inserted into another template containing the dog cards. When I then inserted the buttons into the 'view dog' profile card, I encountered a bug when the delete card reveal was enacted. The 'view dog' profile was created on one base card, which meant that the entire dog profile would make way for the 'delete confirmation' card reveal. Consequently, the confirmation text and buttons would go to the top of the card, outside the viewport. This creates a poor UX as the user would need to scroll to the top of the page to confirm or cancel deletion. I tried a number of ways to keep the reveal within the viewport, including putting the buttons within their own card. All attempts resulted in poor positioning or overflow. The issue was finally resolved by adding a class to the container card in the 'view dog' page, then using that to target the `card-reveal` class within the `edit_delete.html` template.  Applying `position: relative` and `bottom: 0` kept the card reveal content at the bottom of the card, without any overflow or positional problems.

- Having set up the email.js functionality for the contact page form, I wanted to provide feedback to the user, including adding a modal to pop up and confirm that the form had been submitted successfully. I had done this previously using a Bootstrap framework so attempted to use similar code. However, the fact that this project uses Materialize rather than Bootstrap caused some issues. Firstly, the submit button in Materialize does not use a `value` attribute so I could not simply set the value of the button to change to "Sending..." and "Sent" to provide feedback. Similarly, I could not get the modal to pop up. I finally noticed that whereas Bootstrap uses `modal("show")` to activate the modal, Materialize uses `modal("open")`. Once I made this change, the modal worked and provided suitable feedback to the user. I also set the close modal button to route back to the contact page so all fields would be cleared in any case.

- In the admin page, I wanted a button to take the admin user to view other user profiles. As the profile view is set up to show the page to the session user only, this meant that the admin user would always be redirected to their own profile page, as they are also a session user. I tried including `if session["admin"]:` instructions in the profile view, taking the username fed through when clicking the 'View User' button on the admin page, rather than the session user. This succeeded in redirecting the user to the user profile page. However, this then prevented other users from accessing their own profile page. The ultimate solution was to build a separate `@app.route("/profile/admin/<username>" )` containing the `session["admin"]` code.

- Users are able to edit or delete any reviews that they have left for other dogs. I thought that it would be easiest to enable this functionality to be actioned by way of modals. I hit a major bug in that when there was more than one review on a page, the edit modal would always target the first record only. I tried various ways to target each review in the backend (in the view_dog view) but had to seek Tutor Support. The issue I had overlooked was that although only one edit modal is created in the html, it will be a different modal generated for each review. I therefore needed to give each edit modal a different `id` . The solution was therefore to have `id="edit-review-modal-{{ review._id }}"` and `href="#edit-review-modal-{{ review._id }}"`.

- There was an issue whereby the 'Dogs' page width was overflowing on mobile and tablet screen sizes such that users needed to scroll to the right to see the full page. This was the only page that was having this issue. I tried various CSS stylings, such as on `body` and `html` plus adding a container element to the page. None of these worked so upon inspection on Dev Tools, I realised that it was the pagination container settings that were pushing the page to the left. I had set these as I was having trouble centring the pagination links ( adding `text-align: center` to `.pagination`was having no effect). After some further research, I realised that the answer was to use flexbox. I was therefore able to centre the pagination links on all screen sizes and have no width overflow.

- I encountered a major bug with the search functionality. Firstly, once the search had been made and returned the relevant dog profiles, clicking the back button after viewing the profile would throw an error. Similarly, clicking the back button on the main page twice would return the same error - essentially the search function is now searching for data that no longer exists. Secondly, if a search returned enough results to warrant pagination, clicking on a page link would throw the same error. I could see that the issue was no information being passed when the buttons were clicked. With the help of Tutor Support, the resolution was to use JS `goBack()`  function instead of `request.referrer` for going back a page (this requires a user to resubmit when going back from the profile page but it is functional). The pagination was a bit more tricky but was resolved by making the search route GET only and using `query = request.args.get("query")` instead of `query = request.form.get("query")`.

- After setting up the reviews function, if a dog has received a review and the dog is subsequently deleted, an error was thrown when the user who left the review goes onto their profile page. This was caused by the fact that the dog name is referenced in the 'Reviews I've Left' section at the foot of the profile page. The resolution was to add a conditional statement in the `profile` view such that if there is no such dog on the database then the dog name will simply be returned as "deleted dog". Similarly, the button link to view the dog would throw an error so a conditional statement was required in `profile.html` to only display the button if the dog profile is not deleted. This led me to notice that a user's name is referenced on a dog's profile when a review is left so the same issue would occur if a user is deleted by admin. A similar conditional statement was therefore required in the `view_dog` view so that if there is no such user on the database, the name would simply be "deleted user".

- Another bug discovered while testing is the need to be careful where more than one user has editing rights over the same object. In this case, the user who created a dog profile or review plus admin user can edit either. I had set the review `created_by` user to stay the same when editing reviews but had overlooked this when setting up the `edit_dog` function.  In this case, `created_by` remained as the session user (as set when creating the profile). The problem here is that when admin edits the profile, the dog profile would then be set as created by the admin user and appear in their profile page. I therefore set the `created_by` field to remain the same as originally set when any profile editing takes place.
 

### Unresolved Bugs
---
- A bug arose surrounding the session user when I added most recently added dog profiles to the home page. I tried to use the `dog_card` template to inject the dog profile card. This template also contains the `edit_delete`template, which has conditional settings to display the buttons dependent on whether or not the user is in session. This works fine if a user is in session. However, if a user is not logged in and tries to view the home page, an error is thrown regarding an undefined 'user' variable. This is the case even when the session user is defined in the home page view. As I want all users to be able to view the latest profile cards (not the full profiles) on the home page and time was at a premium, I decided to include the full `dog_card` code in `index.html` and remove the parts which contained references to 'user' - these were not required anyway. Only parts of the code were therefore necessarily repeated and this is something to come back to in the future. 

- A relatively minor bug was discovered late in the testing stage. Having resolved the issues surrounding deleted dog profiles and users where they are referenced in reviews, I checked if there were any other ways that deleting one record may affect the site elsewhere. One bug that I did discover is that if a user is in session at the time that admin deletes them from the users collection, the user will still be in session. However, if they attempt to view their profile or try to make an action that would amend the database, an error is thrown. Essentially, where the code would be searching for their session user details that no longer exist. I'm not sure if it's possible to remove a user from session at the same time as removing them from the database. I don't have the time to investigate this in any depth and as the user would not be able to make any changes to the database and would not be able to login again once the session ends, I don't consider this a major concern at this stage.  