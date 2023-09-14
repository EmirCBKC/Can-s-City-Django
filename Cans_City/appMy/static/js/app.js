
//! NAVBAR => user and basket click
let basket = document.querySelector("#basket");
let basketContent = document.querySelector(".basket-content");
basketContent.style.display = "none";

let user = document.querySelector("#user");
let userContent = document.querySelector(".user-content");
userContent.style.display = "none";

function basketClick() {
    if (basketContent.style.display === "none") {
        basketContent.style.display = "block";
        if (userContent) {
            userContent.style.display = "none";
        }
    } else {
        basketContent.style.display = "none";
    }
}

function userClick() {
    if (userContent.style.display === "none") {
        userContent.style.display = "block";
        if (basketContent) {
            basketContent.style.display = "none";
        }
    } else {
        userContent.style.display = "none";
    }
}

//! PROFILE => profile edit
function aktiflestir() {
    document.querySelectorAll(".edit-profil").forEach((i) => { i.disabled = false });
    document.querySelector(".save").style.display = "block";
    document.querySelectorAll(".profile-img-save").forEach((i) => { i.style.display = "block" });
}