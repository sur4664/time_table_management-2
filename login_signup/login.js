// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.11.1/firebase-app.js";

import { getAuth, signInWithEmailAndPassword } from "https://www.gstatic.com/firebasejs/10.11.1/firebase-auth.js";

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
const loginbtn = document.getElementById('loginbtn');
loginbtn.addEventListener("click", function (event) {
    event.preventDefault();

    //inputs
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    // console.log(email.value, password);
    // alert("sign up button working");
    const auth = getAuth();
    signInWithEmailAndPassword(auth, email, password)
        .then((userCredential) => {
            // Signed in 
            const user = userCredential.user;
            alert("Signed in successfully");
            // window.location.href = "/main/game/index.html";
            // ...
        })
        .catch((error) => {
            const errorCode = error.code;
            const errorMessage = error.message;
            alert(errorMessage);//alerting the error message
        });
});
