$(window).scroll(function () {
if ($(window).scrollTop() >= 50) {
$('.header').addClass('solid-nav');
$('.header li a').addClass('solid-nav');
} else {
$('.header').removeClass('solid-nav');
$('.header li a').removeClass('solid-nav');
}
});