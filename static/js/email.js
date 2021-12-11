/* jshint esversion: 6, jquery: true */
/* Guidance on setting up the email service provided by EmailJS - https://www.emailjs.com/ */
/*Credit: code snippet taken from my previous project but modified to work with Materialize - 
https://github.com/SteveKennyUK/around-the-grounds/blob/main/assets/js/email.js */

const contactForm = document.getElementById("form");

contactForm.addEventListener("submit", function (event) {
    event.preventDefault(); // prevent reload

    const serviceID = "gmail";
    const templateID = "pooch-pals";

    emailjs.sendForm(serviceID, templateID, this).then(
        // modal for successful email submission
        function (response) {
            console.log("Success", response.status, response.text);
            $("#email-success").modal("open");            
            resetForm();
        },
        // modal for failed email submission
        function (error) {
            console.log(JSON.stringify(error));
            $("#email-fail").modal("open");            
        }
    );

    return false; // prevents the page from refreshing when the form is submitted
});
// Reset the form fields to original default values
// (although Contact page is also refreshed when modal is closed)
function resetForm() {
    document.getElementById("name").value = "";   
    document.getElementById("email").value = "";
    document.getElementById("reference").value = "";
    document.getElementById("message").value = "";
}