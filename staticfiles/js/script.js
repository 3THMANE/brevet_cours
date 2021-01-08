let tim = document.querySelector('.time');
let bar = document.querySelector(".bar");
let op = document.querySelector(".scrol");
let link = document.querySelector(".nav-list");
// let items = document.querySelector(".nav-link");
// function() {
//     $("#library").toggleClass("opened-menu"),
//         $("#library_box").slideToggle("fast"),
//         $("#search").removeClass("opened-menu"),
//         $("#search_box").css("display", "none")
// }
//toggle side bar options
bar.onclick = () => {

    link.classList.toggle("open");
    op.classList.toggle("open");

};

// 
tim.onclick = () => {

    link.classList.toggle("open");
    op.classList.toggle("open");


};

//add active links in navigation bar
// var links = document.getElementsByClassName("nav-list");
// var items = document.getElementsByClassName("nav-link");
// for (var i = 0; i < items.length; i++) {
//     items[i].addEventListener("click", function() {
//         var acti = document.getElementsByClassName("active");
//         acti[0].className = acti[0].className.replace(" active", "");
//         this.className += " active";
//     });}