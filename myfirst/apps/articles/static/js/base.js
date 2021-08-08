var menu = $(".mobile-nav");
var main = $(".main-content");
$(".btn-menu").click(function() {
    if (menu.hasClass("mobile-open")) {
        menu.removeClass("mobile-open");
        main.removeClass("section-open");
    }
    else {
        menu.addClass("mobile-open");
        main.addClass("section-open");
    }
})