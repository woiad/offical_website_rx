$(document).ready(function () {

    var winSize = window.innerWidth || document.body.clientWidth

    if (winSize < 991) {

        $('.dropdown-item').on('click', function () {
            var showBlock = this.dataset.show
            if ($(this).hasClass('active')) {
                $('.' + showBlock).slideUp('slow')
                $(this).removeClass('active')
            } else {
                $('.dropdown-item').each(function () {
                    if (this.children[1].classList.contains(showBlock)) {
                        $('.' + showBlock).slideDown('slow')
                        $(this).addClass('active')
                    }
                })
            }
        })

        document.getElementById('product').addEventListener('click', function (ev) {
            var e = ev || window.event
            if (e.target.firstElementChild.classList.contains('active')) {
                e.target.firstElementChild.classList.remove('active')
                e.target.nextElementSibling.style.display = 'none'
            } else {
                e.target.firstElementChild.classList.add('active')
                e.target.nextElementSibling.style.display = 'block'
            }
        })

    }

    function newsAutoRoll () {
        $("#news-roll li").eq(0).animate({'margin-top':'-50px'}, 1000, function () {
            $(this).css({'margin-top': '0px'})
            $(this).appendTo($('#news-roll'))
        })
    }

    var newsRollInt = '';

    newsRollInt = setInterval(newsAutoRoll, 5000)

    $("#news-roll li").on('mouseover', function () {
        clearInterval(newsRollInt)
    })

    $("#news-roll li").on('mouseout', function () {
        newsRollInt = setInterval(newsAutoRoll, 5000)
    })



    // scroll to top
    function scrollToTop() {
        if ($('.scroll-top').length) {

            //Check to see if the window is top if not then display button
            $(window).scroll(function() {
                if ($(this).scrollTop() > 200) {
                    $('.scroll-top').fadeIn();
                } else {
                    $('.scroll-top').fadeOut();
                }
            });

            //Click event to scroll to top
            $('.scroll-top').click(function() {
                $('html, body').animate({ scrollTop: 0 }, 1500);
                return false;
            });
        }
    }
    scrollToTop();
    // Main Menu Function
    function themeMenu() {
        if ($("#main_menu").length) {
            $("#main_menu").menuzord({
                animation: "zoom-out"
            });
        }
    }
    themeMenu()


    function href_to_kf () {
        var kf_href_arr = [
            'http://wpa.qq.com/msgrd?v=3&uin=2880269143&site=qq&menu=yes',
            'http://wpa.qq.com/msgrd?v=3&uin=2880269150&site=qq&menu=yes',
            'http://wpa.qq.com/msgrd?v=3&uin=2880269177&site=qq&menu=yes',
            'http://wpa.qq.com/msgrd?v=3&uin=2880269162&site=qq&menu=yes',
            'http://wpa.qq.com/msgrd?v=3&uin=2880269141&site=qq&menu=ye',
            'http://wpa.qq.com/msgrd?v=3&uin=2880269207&site=qq&menu=yes',
            'http://wpa.qq.com/msgrd?v=3&uin=2880908994&site=qq&menu=yes',
            'http://wpa.qq.com/msgrd?v=3&uin=2880657377&site=qq&menu=yes',
            'http://wpa.qq.com/msgrd?v=3&uin=2880269168&site=qq&menu=yes',
            'http://wpa.qq.com/msgrd?v=3&uin=2880269159&site=qq&menu=yes'
        ]
        var ind = Math.floor(Math.random()*10)
        window.location.href= kf_href_arr[ind]
    }
    $(".flat-window li:nth-child(2)").click(function () {
        window.location.href='tel:0769-22502222'
    })
    if (winSize > 991) {
        $(".flat-window li:last-child").click(function () {
            $(".kf-marsk").css({"display":"block"})
        })
        $(".kf-btn").click(function () {
            $(".kf-marsk").css({"display":"block"})
        })
        $(".kf-marsk .close").click(function () {
            $(".kf-marsk").css({"display":"none"})
        })
    } else {
        $(".flat-window li:last-child").click(function () {
            href_to_kf()
        })
        $(".kf-btn").click(function () {
            href_to_kf()
        })
    }
    $(".account-nav li").on('click', function(){
        var ind = $(this).index()
        $(this).addClass('active')
        $(this).siblings().removeClass('active')
        if (ind == 0) {
            $('.other-account').css({'display':'block'})
            $('.company-account').css({'display': 'none'})
        } else if (ind == 1) {
            $('.other-account').css({'display':'none'})
            $('.company-account').css({'display': 'block'})
        }
    })

    $('.price').click(function () {
        $(this).find('.more-price').slideToggle('normal')
    })

    $('.hot-product .buy').on('click', function () {
        $(".kf-marsk").css({"display":"block"})
    })

    $('.right-column .submit').on('click', function (ev) {
        e  = ev || window.event
        if ($('#searct_text').val() == '') {
          e.stopPropagation()
          e.preventDefault()
        }
    })

    if (winSize < 768) {
        $('.carousel-inner .item').each(function (ind, ev) {
            $('.carousel-inner .item').eq(ind).find('img').attr('src', "/static/images/banner/m_banner" + (ind + 1) + ".jpg")
        })
    }

})
