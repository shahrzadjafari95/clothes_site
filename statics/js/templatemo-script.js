/*
 *	www.templatemo.com
 *******************************************************/

 /* Google map
------------------------------------------------*/
var map = '';
var center;

function initialize() {
    var mapOptions = {
      zoom: 16,
      center: new google.maps.LatLng(13.758468,100.567481),
      scrollwheel: false
    };
  
    map = new google.maps.Map(document.getElementById('google-map'),  mapOptions);

    google.maps.event.addDomListener(map, 'idle', function() {
        calculateCenter();
    });
  
    google.maps.event.addDomListener(window, 'resize', function() {
        map.setCenter(center);
    });
}

function calculateCenter() {
  center = map.getCenter();
}

function loadGoogleMap(){
    var script = document.createElement('script');
    script.type = 'text/javascript';
    script.src = 'https://maps.googleapis.com/maps/api/js?v=3.exp&sensor=false&' + 'callback=initialize';
    document.body.appendChild(script);
}

/* HTML document is loaded. DOM is ready. 
-----------------------------------------*/
$(document).ready(function(){

	/* Mobile menu */
	$('.mobile-menu-icon').click(function(){
		$('.templatemo-nav').slideToggle();				
	});

	$( window ).resize(function() {
		if($( window ).width() > 767) {
			$('.templatemo-nav').show();	
		} else {
			$('.templatemo-nav').hide();	
		} 
	});

  // http://stackoverflow.com/questions/2851663/how-do-i-simulate-a-hover-with-a-touch-in-touch-enabled-browsers
  $('body').bind('touchstart', function() {});

});

$(document).ready(function () {
    // Add refresh button after the captcha image
    $('img.captcha').after(
        $('<a href="#void" class="captcha-refresh" style="font-size: 20px; margin-left: 10px; margin-right: 10px"><i class="fa fa-refresh"></i></a>')
    );

    // Click-handler for the refresh link
    $('.captcha-refresh').click(function () {
        var $form = $(this).parents('form');
        var url = location.protocol + "//" + window.location.hostname + ":" + location.port + "/captcha/refresh/";

        // Make the AJAX call
        $.getJSON(url, {}, function (json) {
            $form.find('input[name="captcha_0"]').val(json.key);
            $form.find('img.captcha').attr('src', json.image_url);
        });

        return false;
    });
});


<!-- JavaScript for validating the password dynamically -->
document.getElementById('password1').addEventListener('input', function() {
        const password = this.value;
        const username = document.querySelector('input[name="username"]').value;

        // Conditions to check
        const lengthCondition = document.getElementById('condition-length');
        const similarCondition = document.getElementById('condition-similar');
        const commonCondition = document.getElementById('condition-common');
        const numericCondition = document.getElementById('condition-numeric');

        // Password must be at least 8 characters long
        if (password.length >= 8) {
            lengthCondition.classList.add('valid');
            lengthCondition.classList.remove('invalid');
        } else {
            lengthCondition.classList.add('invalid');
            lengthCondition.classList.remove('valid');
        }

        // Password should not be too similar to the username (simplified)
        if (!password.toLowerCase().includes(username.toLowerCase())) {
            similarCondition.classList.add('valid');
            similarCondition.classList.remove('invalid');
        } else {
            similarCondition.classList.add('invalid');
            similarCondition.classList.remove('valid');
        }

        // Password should not be entirely numeric
        if (!/^\d+$/.test(password)) {
            numericCondition.classList.add('valid');
            numericCondition.classList.remove('invalid');
        } else {
            numericCondition.classList.add('invalid');
            numericCondition.classList.remove('valid');
        }

        // For "commonly used passwords", in a real app you would have a list to compare
        const commonPasswords = ['password', '123456', 'qwerty']; // example list
        if (!commonPasswords.includes(password.toLowerCase())) {
            commonCondition.classList.add('valid');
            commonCondition.classList.remove('invalid');
        } else {
            commonCondition.classList.add('invalid');
            commonCondition.classList.remove('valid');
        }
    });
