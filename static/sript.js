document.addEventListener("DOMContentLoaded", () => {
    const input = document.querySelector("input");

    input.addEventListener("focus", () => {
        input.style.boxShadow = "0 0 8px rgba(74,144,226,0.5)";
    });

    input.addEventListener("blur", () => {
        input.style.boxShadow = "none";
    });
});