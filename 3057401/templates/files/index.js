"use strict";
(() => {
    const e = document.querySelector(".menu__button"), t = document.querySelector(".menu__list");
    e.addEventListener("click", () => {
        let i = "true" === e.getAttribute("aria-expanded");
        e.setAttribute("aria-expanded", !i), e.classList.toggle("menu__button--open"), t.classList.toggle("menu__list--open")
    })
})();