let topHeader = document.querySelector(".top-header");
let logo = document.querySelector(".logo p");
let searchForm = document.querySelector(".search-form");
let cartForm = document.querySelector(".cart-form")
window.onscroll = () => {
    let height = window.pageYOffset;
    searchForm.classList.remove("is-active");
    cartForm.classList.remove("is-active");
    if(height > 10){
        topHeader.style.height = "8rem";
        logo.style.fontSize = "3rem";
    }else{
        topHeader.style.height = "10rem";
        logo.style.fontSize = "3.6rem";
    }
}

let searchBtn = document.querySelector(".search-btn");
searchBtn.onclick = ()=>{
    searchForm.classList.toggle("is-active");
    cartForm.classList.remove("is-active");
}

let cartBtn = document.querySelector(".cart-btn");
cartBtn.onclick =()=>{
    cartForm.classList.toggle("is-active");
    searchForm.classList.remove("is-active");
}

let menuBtn = document.querySelector(".menu-btn");
let menuSection = document.querySelector(".menu-btn div");
let nav = document.querySelector(".nav-links")

menuBtn.onclick = () => {
    menuSection.classList.toggle("change");
    nav.classList.toggle("is-active")
}
