
"use strict"; // Start of use strict

// 1. revolution slider
function revolutionSliderActiver () {
	if ($('.rev_slider_wrapper #slider1').length) {
		jQuery("#slider1").revolution({
			sliderType:"standard",
			sliderLayout:"auto",
			dottedOverlay:"yes",
			delay:5000,
			navigation: {
				arrows:{enable:true,
						left: {
                        h_align: "left",
                        v_align: "center",
                        h_offset: 60,
                        v_offset: 0
                    },
                    right: {
                        h_align: "right",
                        v_align: "center",
                        h_offset: 60,
                        v_offset: 0
                    }

				}
			},
            gridwidth: [1200, 940, 720, 480],
            gridheight: [550, 550, 550, 500],
            lazyType: "none",
            parallax: {
                type: "mouse",
                origo: "slidercenter",
                speed: 2000,
                levels: [2, 3, 4, 5, 6, 7, 12, 16, 10, 50],
            },
            shadow: 0,
            spinner: "off",
            stopLoop: "off",
            stopAfterLoops: -1,
            stopAtSlide: -1,
            shuffle: "off",
            autoHeight: "off",
            hideThumbsOnMobile: "off",
            hideSliderAtLimit: 0,
            hideCaptionAtLimit: 0,
            hideAllCaptionAtLilmit: 0,
            debugMode: false,
            fallbacks: {
                simplifyAll: "off",
                nextSlideOnWindowFocus: "off",
                disableFocusListener: false,
            }
		});
	};
}



function stickyHeader () {
	if ($('.stricky').length) {
		var strickyScrollPos = 100;
		if($(window).scrollTop() > strickyScrollPos) {
			$('.stricky').removeClass('fadeIn animated');
	      	$('.stricky').addClass('stricky-fixed fadeInDown animated');
	      	$('.scroll-to-top').fadeIn(500);
		}
		else if($(this).scrollTop() <= strickyScrollPos) {
			$('.stricky').removeClass('stricky-fixed fadeInDown animated');
	      	$('.stricky').addClass('slideIn animated');
	      	$('.scroll-to-top').fadeOut(500);
		}
	};
}




// 3. gallery fancybox activator
function GalleryFancyboxActivator () {
  var galleryFcb = $('.fancybox');
  if(galleryFcb.length){
    galleryFcb.fancybox({
      openEffect  : 'elastic',
      closeEffect : 'elastic',
      helpers : {
        media : {}
      }
    });
  }
}
// 4. select menu
function selectMenu () {
	if ($('.select-menu').length) {
		$('.select-menu').selectmenu();
	};
}

// 4. select menu
function tooltip () {
	if ($('.tool_tip').length) {
			$('.tool_tip').tooltip();
		};
	$
}




// 11. testimonails carousel
function testimonialsCarosuleGardener() {
	if ($('.testimonials-slider').length) {
		$('.testimonials-slider').owlCarousel({
		    loop: true,
		    margin: 30,
		    nav: true,
	        navText: [
	            '<i class="fa fa-angle-left"></i>',
	            '<i class="fa fa-angle-right"></i>'
	        ],
	        dots: false,
		    autoplay:true,
		    responsive: {
		        0:{
		            items:1,
		            loop:true,
					dots:false
		        },
		        480:{
					items:2,
					loop:true,
					dots:false
				},
				640:{
                    items:2,
                    loop:true,
                    dots:false
				},
		        768:{
		            items:2,
		            loop:true,
					dots:false
		        },
		        1000:{
		            items:3,
		            loop:true
		        }
		    }
		});
	}
}



// 5. client carousel
function clientCarousel () {
	if ($('.client-carousel').length) {
		$('.client-carousel.owl-carousel').owlCarousel({
		    loop: true,
		    margin: 30,
		    nav: true,
	        navText: [
	            '<i class="fa fa-angle-left"></i>',
	            '<i class="fa fa-angle-right"></i>'
	        ],
	        dots: false,
		    autoWidth: false,
		    autoplay:true,
		    autoplayTimeout:3000,
		    autoplayHoverPause:true,
		    responsive: {
		        0:{
		            items:1,
		            autoWidth: false
		        },
		        380:{
		            items:2,
		            autoWidth: false
		        },
		        540:{
		            items:3,
		            autoWidth: false
		        },
		        740:{
		            items:4,
		            autoWidth: false
		        },
		        1000:{
		            items:5,
		            autoWidth: false
		        }
		    }
		});
	};
}
// 5. client carousel
function gallerycarousel () {
	if ($('.gallery_carousel').length) {
		$('.gallery_carousel').owlCarousel({
		    loop: true,
		    margin: 0,
		    nav: false,
		    dots: false,
		    autoWidth: false,
		    autoplay:true,
		    autoplayTimeout:3000,
		    autoplayHoverPause:true,
		    responsive: {
		        0:{
		            items:1,
		            autoWidth: false
		        },
		        380:{
		            items:2,
		            autoWidth: false
		        },
		        540:{
		            items:3,
		            autoWidth: false
		        },
		        740:{
		            items:4,
		            autoWidth: false
		        },
		        1000:{
		            items:5,
		            autoWidth: false
		        }
		    }
		});
	};
}


function galleryslide () {
	if ($('.gallery_slide').length) {
		$('.gallery_slide').owlCarousel({
		    loop: true,
		    margin: 0,
		    items: 1,
		    nav: false,
		    dots: true,
		    autoWidth: false,
		    autoplay:true,
		    autoplayTimeout:3000,
		    autoplayHoverPause:true
		});
	};
}


function testimonialsarousel () {
	if ($('.testimonial-carousel').length) {
		$('.testimonial-carousel').owlCarousel({
		    loop: true,
		    margin: 0,
		    items: 1,
		    nav: true,
		    navText: [ '<span class="fa fa-angle-left"></span>', '<span class="fa fa-angle-right"></span>' ],
		    dots: true,
		    autoWidth: false,
		    autoplay:true,
		    autoplayTimeout:3000,
		    autoplayHoverPause:true
		});
	};
}
function testimonialsarousel2 () {
	if ($('.testimonial-carousel2').length) {
		$('.testimonial-carousel2').owlCarousel({
		    loop: true,
		    margin: 0,
		    items: 1,
		    nav: true,
		    navText: [ '<span class="fa fa-angle-left"></span>', '<span class="fa fa-angle-right"></span>' ],
		    dots: true,
		    autoWidth: false,
		    autoplay:true,
		    autoplayTimeout:3000,
		    autoplayHoverPause:true
		});
	};
}


function feedbackcarousel () {
	if ($('.feedback-carousel').length) {
		$('.feedback-carousel').owlCarousel({
		    loop: true,
		    margin: 0,
		    items: 1,
		    nav: false,
		    dots: true,
		    autoWidth: false,
		    autoplay:true,
		    autoplayTimeout:3000,
		    autoplayHoverPause:true
		});
	};
}

function teamcarousel () {
	if ($('.team_carousel').length) {
		$('.team_carousel').owlCarousel({
		    loop: true,
		    margin: 30,
		    nav: true,
		    navText: [ '<span class="fa fa-angle-left"></span>', '<span class="fa fa-angle-right"></span>' ],
		    dots: false,
		    autoWidth: false,
		    autoplay:true,
		    autoplayTimeout:3000,
		    autoplayHoverPause:true,
		    responsive: {
		        0:{
		            items:1,
		            autoWidth: false
		        },
		        540:{
		            items:2,
		            autoWidth: false
		        },
		        740:{
		            items:3,
		            autoWidth: false
		        },
		        992:{
		            items:4,
		            autoWidth: false
		        }
		    }
		});
	};
}
function twocolumncarousel () {
	if ($('.two-column-carousel').length) {
		$('.two-column-carousel').owlCarousel({
		    loop: true,
		    margin: 30,
		    nav: false,
		    dots: true,
		    autoWidth: false,
		    autoplay:true,
		    autoplayTimeout:3000,
		    autoplayHoverPause:true,
		    responsive: {
		        0:{
		            items:1,
		            dots: false,
		            autoWidth: false
		        },
		        540:{
		            items:1,
		            dots: false,
		            autoWidth: false
		        },
		        740:{
		            items:1,
		            dots: false,
		            autoWidth: false
		        },
		        992:{
		            items:2,
		            autoWidth: false
		        }
		    }
		});
	};
}


// Fact Counter
function factCounter() {
	if($('.fact-counter').length){
		$('.fact-counter .counter-column.animated').each(function() {

			var $t = $(this),
				n = $t.find(".count-text").attr("data-stop"),
				r = parseInt($t.find(".count-text").attr("data-speed"), 10);

			if (!$t.hasClass("counted")) {
				$t.addClass("counted");
				$({
					countNum: $t.find(".count-text").text()
				}).animate({
					countNum: n
				}, {
					duration: r,
					easing: "linear",
					step: function() {
						$t.find(".count-text").text(Math.floor(this.countNum));
					},
					complete: function() {
						$t.find(".count-text").text(this.countNum);
					}
				});
			}

		});
	}
}



// 9. gallery
function fleetGallery () {
	if ($('.mixit-gallery').length) {
		$('.mixit-gallery').mixItUp();
	};
}



// 10. typed plugin
function typed () {
	if ($(".typed").length) {
		$(".typed").typed({
	        stringsElement: $('.typed-strings'),
	        typeSpeed: 200,
	        backDelay: 1500,
	        loop: true,
	        contentType: 'html', // or text
	        // defaults to false for infinite loop
	        loopCount: false,
	        callback: function () { null; },
	        resetCallback: function () { newTyped(); }
	    });
    };
}

// 14. single featured hover
function singleFeaturedHover () {
	if ($('.single-our-feature').length) {
		$('.single-our-feature').hover(function () {
			var bgHover = $(this).data('hover-background');
			$(this).css({
				'background-image': 'url('+bgHover+')'
			});
		}, function () {
			$(this).css({
				'background-image': ''
			});
		});
	};
}


// 20. Responsive Video
function respnsiveVideo () {
	if ($('.responsive-video-box').length) {
		$('.responsive-video-box').fitVids();
	}
}




//21 Price Ranger
function priceFilter() {
    if ($('.price-ranger').length) {
        $('.price-ranger #slider-range').slider({
            range: true,
            min: 10,
            max: 200,
            values: [11, 99],
            slide: function(event, ui) {
                $('.price-ranger .ranger-min-max-block .min').val('$' + ui.values[0]);
                $('.price-ranger .ranger-min-max-block .max').val('$' + ui.values[1]);
            }
        });
        $('.price-ranger .ranger-min-max-block .min').val('$' + $('.price-ranger #slider-range').slider('values', 0));
        $('.price-ranger .ranger-min-max-block .max').val('$' + $('.price-ranger #slider-range').slider('values', 1));
    };
}


// 22. Cart Touch Spin
function cartTouchSpin () {
	if($('.quantity-spinner').length){
		$("input.quantity-spinner").TouchSpin({
		  verticalbuttons: true
		});
	}
}


// 23. Video Fancybox
function videoFancybox () {
	if ($("a.video-fancybox").length) {
		$("a.video-fancybox").click(function() {
		    $.fancybox({
		            'padding'       : 0,
		            'autoScale'     : false,
		            'transitionIn'  : 'none',
		            'transitionOut' : 'none',
		            'title'         : this.title,
		            'width'         : 680,
		            'height'        : 495,
		            'href'          : this.href.replace(new RegExp("watch\\?v=", "i"), 'v/'),
		            'type'          : 'swf',
		            openEffect      : 'elastic',
				    closeEffect     : 'elastic',
				    helpers         : {
				    	media : {}
				    },
		            'swf'           : {
		            	'wmode'             : 'transparent',
		                'allowfullscreen'   : 'true'
		            }
		        });

		    return false;
		});
	};
}





// 27. Select menu
function selectDropdown() {
    if ($(".selectmenu").length) {
        $(".selectmenu").selectmenu();

        var changeSelectMenu = function(event, item) {
            $(this).trigger('change', item);
        };
        $(".selectmenu").selectmenu({ change: changeSelectMenu });
    };
}


// 31. Tabs Box
function tabbox() {
	if($('.tabs-box').length){

		//Tabs
		$('.tabs-box .tab-buttons .tab-btn').click(function(e) {

			e.preventDefault();
			var target = $($(this).attr('data-tab'));

			target.parents('.tabs-box').find('.tab-buttons').find('.tab-btn').removeClass('active-btn');
			$(this).addClass('active-btn');
			target.parents('.tabs-box').find('.tabs-content').find('.tab').fadeOut(0);
			target.parents('.tabs-box').find('.tabs-content').find('.tab').removeClass('active-tab');
			$(target).fadeIn(300);
			$(target).addClass('active-tab');
		});

	}

}
// 32. imgbxslider
function imgbxslider() {
	if($('.img-slide-box').length){
		$('.img-slide-box').bxSlider({
			adaptiveHeight: true,
			auto:true,
			controls:false,
			maxSlides: 1,
			minSlides: 1,
			moveSlides: 1,
			pause: 5000,
			speed: 700
		});
	}
}
		// Prealoder
function handlePreloader() {
	if($('.preloader').length){
		$('.preloader').delay(200).fadeOut(500);
	}
}

function singleProduct () {

  $('.flexslider').flexslider({
    animation: "slide",
    controlNav: "thumbnails"
  });


}


function thmLightBox() {
    if ($('.img-popup').length) {
        var groups = {};
        $('.img-popup').each(function() {
            var id = parseInt($(this).attr('data-group'), 10);

            if (!groups[id]) {
                groups[id] = [];
            }

            groups[id].push(this);
        });


        $.each(groups, function() {

            $(this).magnificPopup({
                type: 'image',
                closeOnContentClick: true,
                closeBtnInside: false,
                gallery: { enabled: true }
            });

        });

    };
}
function galleryMasonaryLayout() {
    if ($('.masonary-layout').length) {
        $('.masonary-layout').isotope({
            layoutMode: 'masonry'
        });
    }

    if ($('.post-filter').length) {
        $('.post-filter li').children('span').click(function() {
            var Self = $(this);
            var selector = Self.parent().attr('data-filter');
            $('.post-filter li').children('span').parent().removeClass('active');
            Self.parent().addClass('active');


            $('.filter-layout').isotope({
                filter: selector,
                animationOptions: {
                    duration: 500,
                    easing: 'linear',
                    queue: false
                }
            });
            return false;
        });
    }

    if ($('.post-filter.has-dynamic-filter-counter').length) {
        // var allItem = $('.single-filter-item').length;

        var activeFilterItem = $('.post-filter.has-dynamic-filter-counter').find('li');

        activeFilterItem.each(function() {
            var filterElement = $(this).data('filter');
            console.log(filterElement);
            var count = $('.gallery-content').find(filterElement).length;

            $(this).children('span').append('<span class="count"><b>' + count + '</b></span>');
        });
    };
}



//Contact Form Validation
if($("#contact-form").length){
	$("#contact-form").validate({
	    submitHandler: function(form) {
	      var form_btn = $(form).find('button[type="submit"]');
	      var form_result_div = '#form-result';
	      $(form_result_div).remove();
	      form_btn.before('<div id="form-result" class="alert alert-success" role="alert" style="display: none;"></div>');
	      var form_btn_old_msg = form_btn.html();
	      form_btn.html(form_btn.prop('disabled', true).data("loading-text"));
	      $(form).ajaxSubmit({
	        dataType:  'json',
	        success: function(data) {
	          if( data.status == 'true' ) {
	            $(form).find('.form-control').val('');
	          }
	          form_btn.prop('disabled', false).html(form_btn_old_msg);
	          $(form_result_div).html(data.message).fadeIn('slow');
	          setTimeout(function(){ $(form_result_div).fadeOut('slow') }, 6000);
	        }
	      });
	    }
	});
}


if ($('.latest-project-carousel').length) {
    $('.latest-project-carousel').owlCarousel({
        loop: true,
        margin: 30,
        nav: true,
        navText: [
            '<i class="fa fa-angle-left"></i>',
            '<i class="fa fa-angle-right"></i>'
        ],
        dots: false,
        autoWidth: false,
        autoplay: true,
        autoplayTimeout: 3000,
        autoplayHoverPause: true,
        responsive: {
            0: {
                items: 1,
                autoWidth: false
            },
            480: {
                items: 1,
                autoWidth: false
            },
            600: {
                items: 2,
                autoWidth: false
            },
            768: {
                items: 3,
                autoWidth: false
            },
            1000: {
                items: 3,
                autoWidth: false
            }
        }
    });
};



if ($('.accordion-box').length) {
    $('.accordion-box .acc-btn').click(function() {
        if ($(this).hasClass('active') !== true) {
            $('.accordion-box .acc-btn').removeClass('active');
        }

        if ($(this).next('.acc-content').is(':visible')) {
            $(this).removeClass('active');
            $(this).next('.acc-content').slideUp(500);
        } else {
            $(this).addClass('active');
            $('.accordion-box .acc-content').slideUp(500);
            $(this).next('.acc-content').slideDown(500);
        }
    });
}



	// Elements Animation
	if($('.wow').length){
		var wow = new WOW(
		  {
			boxClass:     'wow',      // animated element css class (default is wow)
			animateClass: 'animated', // animation css class (default is animated)
			offset:       0,          // distance to the element when triggering the animation (default is 0)
			mobile:       true,       // trigger animations on mobile devices (default is true)
			live:         true       // act on asynchronously loaded content (default is true)
		  }
		);
		wow.init();
	}






// instance of fuction while Document ready event
jQuery(document).on('ready', function () {
	(function ($) {
		revolutionSliderActiver();
		selectMenu();
		tooltip();
		fleetGallery();
		GalleryFancyboxActivator();
		typed();
		singleFeaturedHover();
		respnsiveVideo();
		priceFilter();
		cartTouchSpin();
		videoFancybox();
		selectDropdown();
		tabbox();
		imgbxslider();
		handlePreloader();
		singleProduct();
		testimonialsCarosuleGardener();
		thmLightBox();
		galleryMasonaryLayout();

	})(jQuery);
});

// instance of fuction while Window Load event
jQuery(window).on('load', function () {
	(function ($) {
		clientCarousel();
		gallerycarousel();
		galleryslide();
		testimonialsarousel();
		testimonialsarousel2();
		feedbackcarousel();
		teamcarousel();
		twocolumncarousel();
	})(jQuery);
});

// instance of fuction while Window Scroll event
jQuery(window).on('scroll', function () {
	(function ($) {
		stickyHeader();
		factCounter();
	})(jQuery);
});
