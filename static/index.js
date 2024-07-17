//effects added on scroll

document.addEventListener("DOMContentLoaded", function(){
    const navbar = document.getElementById('navbar');

    window.addEventListener('scroll', function(){
        if (this.window.scrollY > 50) {
            navbar.classList.add('scrolled');

        } else {
            navbar.classList.remove('scrolled');

        }
    });

});