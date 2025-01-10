
$(document).ready(function () {
    $(".add-note").click(function () {
        $(".popup").removeClass("hidden").addClass("show");
    });

    $(".close-popup").click(function () {
        $(".popup").removeClass("show").addClass("hidden");
    });
});

