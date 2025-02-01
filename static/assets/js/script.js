(function($) {
    "use strict";
    
    var $wrapper = $('.main-wrapper');
    var $slimScrolls = $('.slimscroll');

    // Sidebar Toggle
    $(document).on('click', '#toggle_btn', function() {
        if ($('body').hasClass('mini-sidebar')) {
            $('body').removeClass('mini-sidebar');
            $('.subdrop + ul').slideDown();
        } else {
            $('body').addClass('mini-sidebar');
            $('.subdrop + ul').slideUp();
        }
        return false;
    });

    // Mobile Sidebar Toggle
    $(document).on('click', '#mobile_btn', function() {
        $wrapper.toggleClass('slide-nav');
        $('.sidebar-overlay').toggleClass('opened');
        $('html').toggleClass('menu-opened');
        return false;
    });

    // Sidebar Overlay Close
    $(document).on('click', '.sidebar-overlay', function () {
        $wrapper.removeClass('slide-nav');
        $('.sidebar-overlay').removeClass('opened');
        $('html').removeClass('menu-opened');
    });

    // Initialize sidebar
    function initSidebar() {
        $('#sidebar-menu a').on('click', function(e) {
            if ($(this).parent().hasClass('submenu')) {
                e.preventDefault();
            }
            if (!$(this).hasClass('subdrop')) {
                $('ul', $(this).parents('ul:first')).slideUp(350);
                $('a', $(this).parents('ul:first')).removeClass('subdrop');
                $(this).next('ul').slideDown(350);
                $(this).addClass('subdrop');
            } else {
                $(this).removeClass('subdrop');
                $(this).next('ul').slideUp(350);
            }
        });

        // Active menu open
        $('#sidebar-menu ul li.submenu a.active').parents('li:last').children('a:first').addClass('active').trigger('click');
    }
    initSidebar();

})(jQuery);
