$(document).ready(function () {
    'use strict';
    if (JSON.parse(localStorage.getItem('showDashboardSidebar')) && window.innerWidth >= 1200) {
        $(".dashboard-sidebar").addClass("show");
    }

    $(".dashboard-sidebar-toggler").click(function (e) {
        e.preventDefault();
        $(".dashboard-sidebar").toggleClass("show");
        if ($(".dashboard-sidebar").hasClass("show")) {
            localStorage.setItem('showDashboardSidebar', true)
        } else {
            localStorage.setItem('showDashboardSidebar', false)
        }
    });

    $(window).on('resize', function () {
        if (window.innerWidth < 1200) {
            $(".dashboard-sidebar").removeClass("show");
        }
    });
    /**
     * Notification list
     */
    // if ($(".notification-list").length) {
    //     $('.notification-list').slimScroll({
    //         height: '250px'
    //     });
    // }

    /**
     * Menu Slim Scroll List
     */
    // if ($(".menu-list").length) {
    //     $('.menu-list').slimScroll({
    //     });
    // }

    /**
     * Main content wrapper
     */
    // if ($(".dashboard-wrapper").length) {
    //     $('.dashboard-wrapper').slimScroll({
    //     });
    // }

    /**
     * Sidebar scrollnavigation
     */
    if ($(".sidebar-nav-fixed a").length) {
        $('.sidebar-nav-fixed a')
            // Remove links that don't actually link to anything
            .click(function (event) {
                // On-page links
                if (
                    location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') &&
                    location.hostname == this.hostname
                ) {
                    // Figure out element to scroll to
                    var target = $(this.hash);
                    target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
                    // Does a scroll target exist?
                    if (target.length) {
                        // Only prevent default if animation is actually gonna happen
                        event.preventDefault();
                        $('html, body').animate({
                            scrollTop: target.offset().top - 90
                        }, 1000, function () {
                            // Callback after animation
                            // Must change focus!
                            var $target = $(target);
                            $target.focus();
                            if ($target.is(":focus")) { // Checking if the target was focused
                                return false;
                            } else {
                                $target.attr('tabindex', '-1'); // Adding tabindex for elements not focusable
                                $target.focus(); // Set focus again
                            };
                        });
                    }
                };
                $('.sidebar-nav-fixed a').each(function () {
                    $(this).removeClass('active');
                })
                $(this).addClass('active');
            });
    }

    // ==============================================================
    // tooltip
    // ==============================================================
    if ($('[data-toggle="tooltip"]').length) {
        $('[data-toggle="tooltip"]').tooltip()
    }

    // ==============================================================
    // popover
    // ==============================================================
    if ($('[data-toggle="popover"]').length) {
        $('[data-toggle="popover"]').popover()
    }

    // ==============================================================
    // Chat List Slim Scroll
    // ==============================================================
    // if ($('.chat-list').length) {
    //     $('.chat-list').slimScroll({
    //         color: 'false',
    //         width: '100%'
    //     });
    // }

    // ==============================================================
    // dropzone script
    // ==============================================================
});
// AND OF JQUERY
