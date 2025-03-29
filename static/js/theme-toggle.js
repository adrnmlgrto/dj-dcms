const themeToggle = document.getElementById("theme-toggle");
const themeIcon = document.getElementById("theme-icon");
const html = document.documentElement;

function setTheme(theme) {
    html.setAttribute("data-theme", theme);
    localStorage.setItem("theme", theme);
    themeIcon.textContent = theme === "dark" ? "☀️" : "🌙";
}

// Initialize theme
const storedTheme = localStorage.getItem("theme") || "light";
setTheme(storedTheme);

// Toggle theme on button click
themeToggle.addEventListener("click", () => {
    const newTheme = html.getAttribute("data-theme") === "light" ? "dark" : "light";
    setTheme(newTheme);
});