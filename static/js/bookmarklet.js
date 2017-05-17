/**
 * Created by Dave on 2017/4/27.
 */
(function(){
    var jquery_version='3.2.0';
    var site_url= 'http://127.0.0.1:8000/';
    var static_url = site_url+ "static/";
    var min_width = 100;
    var min_height = 100;

    function bookmarklet(msg){
        // here goes the bookmarklet code
        // load css
        var css = jQuery('<link>');
        css.attr({
            rel : "stylesheet",
            type: 'text/css',
            // to avoid browser cache
            href: static_url+ 'css/bookmarklet.css?r='+ Math.floor(Math.random()*99999999999999999999)
        });
        jQuery('head').append(css);

        // load bootstrap
        var bootstrap_css = jQuery('<link>');
        bootstrap_css.attr({
           rel: "stylesheet",
            type: 'text/css',
            href: static_url+ 'css/bootstrap.min.css?r='+Math.floor(Math.random()*99999999999999999999)
        });
        jQuery('head').append(bootstrap_css);
        // load HTML
        box_html = '<div class="alert alert-info" id="bookmarklet"><a href="#" id="close">&times;</a>' +
                              '<div class="modal-dialog">' +
                                   '<div class="container">' +
                                          '<div class="col-md-4>"'+
                                           '<h1>Select an image to bookmark</h1>'+
                                              '<div class="images"></div>' +
                                           '</div>'+
            '                       </div>' +
            '                 </div>' +
            '</div>';

        jQuery('body').append(box_html);

        // close event
        jQuery('#bookmarklet #close').click(function () {
            jQuery('#bookmarklet').remove();
        });
    };

    // find images and display them
    jQuery.each(jQuery('img[src$="jpg"]'), function(index, image){
        if(jQuery(image).width() >= min_width && jQuery(image).height() >= min_height)
        {
            image_url = jQuery(image).attr('src');
            jQuery('#bookmarklet .images').append('<a href="#"><img src="'+image_url+'"/></a>');
        }
    });

    // when an image is clicked open the URL in it
    jQuery('#bookmarklet .images a').click(function(e){
        selected_image = jQuery(this).children('img').attr('src');
        // hide bookmarklet
        jQuery('#bookmarklet').hide();
        // open the new window to submit image
        window.open(site_url + 'images/create/?url='
        + encodeURIComponent(selected_image)
        + '&title='
        +encodeURIComponent(jQuery('title').text()),
        '_blank');
    });
    // check if jQuerry is loaded
    if(typeof window.jQuery != 'undefined'){
        bookmarklet();
    }
    else{
        // check for the conflicts
        var conflict = typeof window.$ != 'undefined';
        // create script and point to GOOGLE API
        var script = document.createElement('script');
        script.setAttribute('src',
        'http://ajax.googleapis.com/ajax/libs/jquery/' + jquery_version + 'jquery.min.js');
        // add the script to the head for processing
        document.getElementsByTagName('head')[0].appendChild(script);
        // create a way to wait until a script is loading
        var attempts = 15;
        (function(){
            // check again if jQuerry is undefined
            if(typeof window.jQuery == 'undefined'){
                if (--attempts > 0){
                    // call himself with a few milleseconds
                    window.setTimeout(arguments.callee, 250)
                }else{
                    // too much attemps to loads call error
                    alert('an error occured while loading jQuery!')
                }
            }else{
                bookmarklet();
            }
        })();
    }
})();
