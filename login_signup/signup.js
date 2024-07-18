// Purpose: To sign up the user using firebase authentication
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.11.1/firebase-app.js";
import { getAuth, createUserWithEmailAndPassword } from "https://www.gstatic.com/firebasejs/10.11.1/firebase-auth.js";

// Your web app's Firebase configuration
//credentials.js
// import { firebaseConfig } from './credentials';
const firebaseConfig = {
    apiKey: "AIzaSyBw0tzVyMSMkYUpuF-5-t9E7dtdRGobIUY",
    authDomain: "loginpage-17f73.firebaseapp.com",
    projectId: "loginpage-17f73",
    storageBucket: "loginpage-17f73.appspot.com",
    messagingSenderId: "252461437438",
    appId: "1:252461437438:web:1ecbfdc4afeab4ad0330af"

};

// Initialize Firebase
const app = initializeApp(firebaseConfig);


//signup
const signupbtn = document.getElementById('signupbtn');
signupbtn.addEventListener("click", function (event) {

    event.preventDefault();//
    //inputs
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    // console.log(email.value, password);
    // alert("sign up button working");
    const auth = getAuth();
    createUserWithEmailAndPassword(auth, email, password)
        .then((userCredential) => {
            // Signed up 
            const user = userCredential.user;
            alert("Signed up successfully");
            // ...
        })
        .catch((error) => {
            const errorCode = error.code;
            const errorMessage = error.message;
            alert(errorMessage);
        });
})