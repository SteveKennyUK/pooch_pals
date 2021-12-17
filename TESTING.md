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
	    [Landing page](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/user-goals-1.JPG)
    -   As a user, I want to be able to easily identify what I need and navigate the site to get to it.
	    - The navigation bar provides clear and concise direction to all the principal pages on the site. The bar is consistent over all pages and is fixed so that it is always visible. The bar also highlights which page the user is currently viewing. Navigation collapses into a hamburger menu on smaller devices, opening to reveal the same pages. Navigational buttons and links are also visible and intuitive
	    [Navbar - logged out](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/user-goals-2.JPG)
	    [Navbar -logged in](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/user-goals-3.JPG)
	    [Navbar - mobile hamburger menu](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/user-goals-4.JPG)
	    [Navbar - mobile menu open](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/user-goals-5.JPG)
	    [Navigational button](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/user-goals-6.JPG)
    -   As a user, I want concise but informative content, displayed in an aesthetic, intuitive and consistent manner.
	    - Information is displayed using cards throughout, which maintains a consistency in presentation. Rather than overloading users with too much information, users are first presented with a synopsis of the dog profile information, which then allows them to make a decision as to whether they would like to find out more. The detailed profiles are presented in a manner that makes information easy to digest. Buttons, such as edit and delete, are presented in a consistent manner throughout.
	     [Synopsis card](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/user-goals-7.JPG)
	     [Full profile card](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/user-goals-8.JPG)
    -   As a user, I want to be able to view the site clearly and intuitively on different device sizes.
	    - Strict attention has been paid to the principles of responsive design throughout the development process. Screen displays react to changes in resolution and orientation to maintain an optimal visual experience for the user.
	     [Small screen display](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/responsive-1.JPG)
	     [Larger screen display](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/responsive-2.JPG)
	     
    -   As a user, I expect the site to be fully accessible.
	    -  The site uses assistive technology, including aria labelling, alt text for non-textual elements, such as images, and  `sr-only` classes. Semantic  `html`  is used to further assist screen readers.
    
-   #### [](https://github.com/SteveKennyUK/pooch_pals#site-owner-goals)Site Owner Goals
    
    -   As the site owner, I want features and content that will engage new users quickly, encourage them to explore the site and draw them back in the future.
	    - The landing page is very welcoming in terms of colour, imagery and typography. It immediately entices users by providing a synopsis of the most recent additions to the site. Navigational links throughout the landing page encourage users to explore further. The breed group page provides some educational material and encourages current dog owners or potential dog owners to register in order to continue to learn about which dogs may be suitable for their dogs or for themselves. 
	      [Landing page recent additions and nav links](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/owner-goals-1.JPG)
	      [Breed groups information](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/owner-goals-2.JPG)
    -   As the site owner, I want users to feel comfortable that their data is secure.
	    - Users are informed on both the landing page and the contact page that only verified users will be allowed to contact other users. Security checks would need to take place before admin grants verified status to a user. Dogs belonging to verified users can be identified by a green tick on their profile page. Any pages that contain more detailed information about the dog profiles are only accessible to registered and logged in users. These pages are protected to prevent non-logged in users forcing access or other users accessing an individual's profile page.
	    [Verification notice](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/owner-goals-3.JPG)
	    [Verification confirmed](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/owner-goals-5.JPG)
	    [User must be logged in to view](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/owner-goals-4.JPG)	    
    -   As the site owner, I want to be able to moderate the site content.
	    - Admin users have control over the site content, with the ability to add, edit and delete any data added by users. A dedicated admin page also allows admin users to view, verify and delete users. This page is protected so that non-admin users cannot access it by force.
	    [Admin page](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/owner-goals-7.JPG)
	    [Admin user can edit and delete all profiles](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/owner-goals-6.JPG)
	    [Access restricted to admin user only](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/owner-goals-8.JPG)
    -   As the site owner, I want the site to be accessible to all users.
	    - See User Goals (General) above.
	    
    -   As the site owner, I want to be able to use the site myself to find playmates for my own dogs.
	    - Owners can set up their own profile pages and interact with other users to find playmates for their own dogs.
	    [Site owner's own profile](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/owner-goals-9.JPG)
    -   As the site owner, I want to also be able to develop the site to promote dog accessories and services (either my own or those of a business partner).
	    - There are currently links in the page footer which take users to other organisations and businesses. These could be tracked to register when users click the links and visit the pages. There is also scope to add a dedicated page to promote accessories and services in the future. 
	[Footer links](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/owner-goals-10.JPG)

-   #### [](https://github.com/SteveKennyUK/pooch_pals#user-stories)User Stories
    
    -   **(Unregistered/logged out user)**
        
        -   I want to be quickly reassured that this site will be of interest to me.
	        - The landing page makes it very clear what the site is about (see User Goals (General) above). Logged out users can browse the breed group and contact pages to gather more information to inform their decision on whether to register.
	        
        -   I want to be able to identify the content of the site and be able to navigate to areas of interest e.g. view dogs on the site.
	        - Navigation links are clear and unambiguous (see User Goals (General) above). As a user, if I am interested in viewing dog profiles on the site, I will need to first register. This helps to attract genuinely interested users only.
	         
        -   I want to be able to register to join the site effortlessly and with minimal information required.
	        - There are clear navigational links to the registration page, located both on the navigation bar and on the landing page (also at the foot of the login page - see below). The registration form is simple and clear, requiring users to supply only a username, password and email address. There are helpers on the form should the user supply any invalid entries. 
	         [Nav links to registration page](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/logged-out-1.JPG)
	         [Registration form](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/logged-out-2.JPG)
	         [Registration form validation helpers](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/logged-out-3.JPG)	         
        -   I want to be able to contact the site owners with any questions.
	        - There is a contact page accessible from the navigation bar. This page contains a form that users may complete to make any enquiries to the site owners/admin. Users do not need to be registered to use this service.
	         [Contact page](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/logged-out-4.JPG)
    -   **(Registered/logged in user)**
        
        -   I want to be able to login and logout easily.
	        -  There are clear navigational links to the login page, located both on the navigation bar and on the landing page (also at the foot of the registration page - see above). The login form is simple and clear, requiring username and password only. There is feedback in the event of invalid entries. The logout button is clearly and predictably located in the 'Account' dropdown navigation link (as part of all links in mobile dropdown menu).
	        [Log in form](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/logged-in-1.JPG)
	        [Logout button desktop](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/logged-in-2.JPG)
	        [Logout button mobile](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/logged-in-3.JPG)
        -   I want to be able to view my profile and see my dog's profile and any reviews I have left for other dogs.
	        - There is a link to the profile page in the 'Account' dropdown navigation link for logged in users.
	         [Profile page](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/logged-in-4.JPG)
        -   I want to be able to add a profile for my dog(s) with relative ease.
	        - An intuitive and tooltip labelled 'Add New Dog' button is located in a user's profile page. This takes the user to a form for adding a dog profile to the site. This form has textual instructions, iconography and feedback helpers to assist the user in adding a profile with minimal fuss.
	         [Add New Dog button](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/logged-in-5.JPG)
	         [Add Dog form](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/logged-in-6.JPG)
        -   I want to be able to leave reviews for other dogs on the site.
	        - An intuitive and tooltip labelled 'Add Review' button is located in a dog's profile page. This opens a modal where a user may leave a review.
	        [Add Review button](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/logged-in-7.JPG)
	        [Add Review modal](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/logged-in-8.JPG)
        -   I want to be able to edit and/or delete my contributions.
	        - Dog profiles and reviews have buttons providing the user who created them the option to edit or delete.
	        [Edit Dog Profile button](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/logged-in-9.JPG)
	        [Edit Dog Profile form](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/logged-in-10.JPG)
	        [Delete Dog Profile confirmation request](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/logged-in-11.JPG)
	        [Edit review modal](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/logged-in-12.JPG)
	        [Delete review modal](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/logged-in-13.JPG)	        	        
        -   I want to be able to search for dogs that meet certain criteria e.g. breed, location.
	        - There is a search function on the All Dogs page allowing users to search the dog profiles by breed name, sex, size, location and personality. Button links from the Breed Groups page also return results by breed group.
	         [Search bar](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/logged-in-14.JPG)
	         [Breed group filter buttons](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/logged-in-15.JPG)
        -   I want to be able to understand more about different dog breeds.
	        - The Breed Groups page provides useful background information about the different dog groups and links to research further.	 
	         [Breed Groups page](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/logged-in-16.JPG)       
        -   I want to be able to interact with other site users.
	        - There is a Contact page, allowing users to enquire about other users' dog profiles. This can be further developed for a more direct method - see Future Features. 
	        [Contact page for logged in users](https://github.com/SteveKennyUK/pooch_pals/blob/testing/static/images/testing/user-stories/logged-in-17.JPG)
        -   I want to know that other site users are trustworthy.
	        - Site users are informed that other users need to undergo safety checks prior to any contact being allowed with other users. Dogs belonging to verified users have a green tick on their profile page. See Site Owner Goals above for screenshots.
	          
        -   I would like to be able to save profiles of interest to go back to later.
	        - This is a feature that was deemed out of scope for the first development phase. In future, users will be able to 'favourite' dog profiles to save - see Future Features.
	        
    -   **(Admin/site owner user)**
        
        -   I want to be able to validate users to improve trust in the site.
	        - All users are automatically unverified when registering. Admin can update their status to verified after security checks, with verification status displayed on dog profiles. See Site Owner Goals above.
	        
        -   I want to be able to view, edit and delete all users and entries on the site.
	        - The Admin page is only available to users with admin privileges. This page has additional security features to prevent unauthorised access. Admin users may also edit and delete other user contributions. See Site Owner Goals above.