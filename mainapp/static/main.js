// Password toggle
const togglePassword = document.getElementById("togglePassword");
const password = document.getElementById("password");

togglePassword.addEventListener("click", function () {
    const type = password.getAttribute("type") === "password" ? "text" : "password";
    password.setAttribute("type", type);
    this.classList.toggle("fa-eye-slash");
});

// Theme switch
const themeIcon = document.getElementById("themeIcon");

themeIcon.addEventListener("click", function () {
    document.body.classList.toggle("light");

    if (document.body.classList.contains("light")) {
        this.classList.remove("fa-moon");
        this.classList.add("fa-sun");
    } else {
        this.classList.remove("fa-sun");
        this.classList.add("fa-moon");
    }
});