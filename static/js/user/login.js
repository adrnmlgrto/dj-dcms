document.querySelector("form").addEventListener("submit", function () {
    const btn = document.getElementById("login-btn");
    const btnText = document.getElementById("btn-text");
    const spinner = document.getElementById("loading-spinner");

    btn.disabled = true;
    btnText.classList.add("hidden");
    spinner.classList.remove("hidden");
});