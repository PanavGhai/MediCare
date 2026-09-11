document.addEventListener("DOMContentLoaded", () => {
    const passwordInput = document.getElementById("password");
    const passwordToggle = document.getElementById("passwordToggle");
    const passwordIcon = document.getElementById("passwordIcon");

    if (passwordInput && passwordToggle && passwordIcon) {
        passwordToggle.addEventListener("click", () => {
            const isVisible = passwordInput.type === "text";

            passwordInput.type = isVisible ? "password" : "text";

            passwordIcon.classList.toggle("fa-eye", isVisible);
            passwordIcon.classList.toggle("fa-eye-slash", !isVisible);

            passwordToggle.setAttribute(
                "aria-label",
                isVisible ? "Show password" : "Hide password"
            );

            passwordToggle.setAttribute(
                "aria-pressed",
                String(!isVisible)
            );
        });
    }

    const loginForm = document.getElementById("loginForm");

    if (loginForm) {
        loginForm.addEventListener("submit", (event) => {
            event.preventDefault();
        });
    }
});