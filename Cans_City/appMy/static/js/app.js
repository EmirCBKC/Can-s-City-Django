
//! NAVBAR user and basket click
let basket = document.querySelector("#basket");
let basketContent = document.querySelector(".basket-content");
basketContent.style.display = "none";

let user = document.querySelector("#user");
let userContent = document.querySelector(".user-content");
userContent.style.display = "none";

basket.addEventListener("click", () => {
    if (basketContent.style.display === "none") {
        basketContent.style.display = "block";
        userContent.style.display = "none";
    } else {
        basketContent.style.display = "none";
    }
});

user.addEventListener("click", () => {
    if (userContent.style.display === "none") {
        userContent.style.display = "block";
        basketContent.style.display = "none";
    } else {
        userContent.style.display = "none";
    }
});
