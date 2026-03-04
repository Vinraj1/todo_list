// ================= PASSWORD TOGGLE =================
const togglePassword = document.getElementById("togglePassword");
const password = document.getElementById("password");

togglePassword.addEventListener("click", function () {
    const type = password.type === "password" ? "text" : "password";
    password.type = type;
    this.classList.toggle("fa-eye-slash");
});

// ================= LOADING + SUCCESS =================
const loginForm = document.getElementById("loginForm");
const loginBtn = document.getElementById("loginBtn");

loginForm.addEventListener("submit", function () {
    loginBtn.classList.add("loading");

    setTimeout(() => {
        loginBtn.classList.remove("loading");
        loginBtn.classList.add("success");
    }, 1500);
});

// ================= PARTICLES INIT =================
particlesJS("particles-js", {
    particles: {
        number: { value: 60 },
        size: { value: 3 },
        move: { speed: 2 },
        line_linked: { enable: true },
    }
});