var pswpElement = document.querySelectorAll('.pswp')[0]

var items1 = [
    {
        src: '../../static/images/about-us/home.jpg',
        w: 1600,
        h: 1200
    },
    {
        src: '../../static/images/about-us/home1.jpg',
        w: 1600,
        h: 1200
    }
],
    items2 = [
        {
            src: '../../static/images/about-us/bg.jpg',
            w: 1600,
            h: 1200
        }
    ],
    items3 = [
        {
            src: '../../static/images/about-us/ch.jpg',
            w: 1600,
            h: 1200
        }
    ],
    items4 = [
        {
            src: '../../static/images/about-us/hy.jpg',
            w: 1600,
            h: 1200
        }
    ],
    items5 = [
        {
            src: '../../static/images/about-us/qt.jpg',
            w: 1600,
            h: 1200
        },
        {
            src: '../../static/images/about-us/qt1.jpg',
            w: 1600,
            h: 1200
        }
    ],
    itemarr = [items1, items2, items3, items4, items5];
// define options (if needed)
var options = {
    // optionName: 'option value'
    // for example:
    index: 0 // start at first slide
};
// Initializes and opens PhotoSwipe

$(document).ready(function () {
    $('.company-image li').on('click', function () {
       var ind = $(this).index()
        var gallery = new PhotoSwipe( pswpElement, PhotoSwipeUI_Default, itemarr[ind], options);
        gallery.init();
    })
})
