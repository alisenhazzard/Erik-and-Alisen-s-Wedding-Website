$(document).ready(function() {
    try{
        $('.slideshow').cycle({
            fx: 'fade' // choose your transition type, ex: fade, scrollUp, shuffle, etc...
        });
    }catch(err){}
});
