$(function(){

    // esg 메인페이지 fullpage
    $('#fullpage').fullpage({
        afterLoad: function(anchorLink, index){
            if(index >= 6){
                $.fn.fullpage.setAutoScrolling(false);
                $.fn.fullpage.setFitToSection(false);
            }if(index > 1) {
                $('#wrapper').addClass('headFixed');
            }if(index == 1) {
                $('#wrapper').removeClass('headFixed');
            }if(index < 6) {
                $.fn.fullpage.setAutoScrolling(true);
                $.fn.fullpage.setFitToSection(true);
            }
        },
    });


}) //최종괄호