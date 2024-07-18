import { initializeApp } from "https://www.gstatic.com/firebasejs/10.11.1/firebase-app.js";
import { getAuth, signInWithPopup, GoogleAuthProvider } from "https://www.gstatic.com/firebasejs/10.11.1/firebase-auth.js";

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

const app = initializeApp(firebaseConfig);

const googlelogin = document.getElementById('google-signin-btn');
googlelogin.addEventListener("click", function (event) {
    // alert("google sign in button working");
    const provider = new GoogleAuthProvider();

    const auth = getAuth();
    signInWithPopup(auth, provider)
        .then((result) => {
            // This gives you a Google Access Token. You can use it to access the Google API.
            const credential = GoogleAuthProvider.credentialFromResult(result);
            const token = credential.accessToken;
            // The signed-in user info.
            const user = result.user;
            // IdP data available using getAdditionalUserInfo(result)
            // window.location.href = "/main/game/index.html";
            alert("Signed in successfully");

            // ...
        }).catch((error) => {
            // Handle Errors here.
            const errorCode = error.code;
            const errorMessage = error.message;
            // The email of the user's account used.
            const email = error.customData.email;
            // The AuthCredential type that was used.
            const credential = GoogleAuthProvider.credentialFromError(error);
            // ...
        });
});
