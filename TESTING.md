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