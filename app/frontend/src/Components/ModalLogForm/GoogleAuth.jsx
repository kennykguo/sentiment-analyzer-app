import { useEffect } from "react";

const GoogleAuth = () => {
    const handlerCallbackResponse = (response) => {
        console.log("Encoded JWT ID token: " + response.credential);
    };

    useEffect(() => {
        if (window.google) {
            window.google.accounts.id.initialize({
                client_id: "542197543670-5m2vib2an69ha70d47q5b8je8hfnufmd.apps.googleusercontent.com",
                callback: handlerCallbackResponse,
                language: 'en'
            });

            window.google.accounts.id.renderButton(
                document.getElementById("signInDiv"),
                { theme: "outline", size: "large", type: "standard", text: "sign_in_with", shape: "rectangular" }
            );

            try {
                window.google.accounts.id.prompt();
            } catch (error) {
                console.error('Prompt error: ', error);
            }
        } else {
            console.error('Google API not loaded');
        }
    }, []);

    return <div id="signInDiv"></div>;
};

export default GoogleAuth;
