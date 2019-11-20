(function($){

	// Main code
	$(document).ready(function(){

		// Initialize the object on dom load
		var navigator = new Navigator({
			carousel: '#carousel',
			nextButton: '.arrow.next',
			prevButton: '.arrow.prev',
			shuffle: true
		});

		navigator.init();

	});


	// A Navigator "class" responsible for navigating through the carousel.
	function Navigator(config) {

		this.carousel = $(config.carousel); //the carousel element
		this.nextButton = $(config.nextButton); //the next button element
		this.prevButton = $(config.prevButton); //the previous button element
		this.chunkSize = config.chunkSize || 5; //how many items to show at a time (maximum)
		this.shuffle = config.shuffle || false; //should the list be shuffled first? Default is false.

		//private variables
		this._items = $(config.carousel + ' li'); //all the items in the carousel
		this._chunks = []; //the li elements will be split into chunks.
		this._visibleChunkIndex = 0; //identifies the index from the this._chunks array that is currently being shown


		this.init = function () {

			//Shuffle the array if neccessary
			if (this.shuffle) {
				//remove visible tags
				this._items.removeClass('visible');

				//shuffle list
				this._items.sort(function() { return 0.5 - Math.random() });

				//add visible class to first "chunkSize" items
				this._items.slice(0, this.chunkSize).addClass('visible');
			}

			//split array of items into chunks
			this._chunks = this._splitItems(this._items, this.chunkSize);

			var self = this;

			//Set up the event handlers for previous and next button click
			self.nextButton.on('click', function(e) {
				self.handleNextClick(e);
			}).show();

			self.prevButton.on('click', function(e) {
				self.handlePrevClick(e);
			});

			// Showing the carousel on load
			self.carousel.addClass('active');
		}

		//handle all code when previous button is clicked
	  this.handlePrevClick = function (e) {

			e.preventDefault();

			//as long as there are some items before the current visible ones, show the previous ones
			if (this._chunks[this._visibleChunkIndex - 1] !== undefined) {
				this.showPrevItems();
			}
		};

		//handle all code when next button is clicked
		this.handleNextClick = function(e) {

			e.preventDefault();

			//as long as there are some items after the current visible ones, show the next ones
			if (this._chunks[this._visibleChunkIndex + 1] !== undefined) {
				this.showNextItems();
			}
		};

		//show the next 3 items
		this.showNextItems = function() {

			//remove visible class from current visible chunk
			$(this._chunks[this._visibleChunkIndex]).removeClass('visible');

			//add visible class to the next chunk
			$(this._chunks[this._visibleChunkIndex + 1]).addClass('visible');

			//update the current visible chunk
			this._visibleChunkIndex++;

			//see if the end of the list has been reached.
			this._checkForEnd();

		};

		//show the previous 3 items
		this.showPrevItems = function() {

			//remove visible class from current visible chunk
			$(this._chunks[this._visibleChunkIndex]).removeClass('visible');

			//add visible class to the previous chunk
			$(this._chunks[this._visibleChunkIndex - 1]).addClass('visible');

			//update the current visible chunk
			this._visibleChunkIndex--;

			//see if the beginning of the carousel has been reached.
			this._checkForBeginning();

		};


		//Determine if the previous button should be shown or not.
		this._checkForBeginning = function() {
			this.nextButton.show(); //the prev button was clicked, so the next button can show.

			if (this._chunks[this._visibleChunkIndex - 1] === undefined) {
				this.prevButton.hide();
			}
			else {
				this.prevButton.show();
			}
		};

		//Determine if the next button should be shown or not.
		this._checkForEnd = function() {
			this.prevButton.show(); //the next button was clicked, so the previous button can show.

			if (this._chunks[this._visibleChunkIndex + 1] === undefined) {
				this.nextButton.hide();
			}
			else {
				this.nextButton.show();
			}
		};


		//This function takes an array "items" and splits it into subArrays each with a maximum length of "chunk".
		this._splitItems = function(items, chunk) {

			var splitItems = [],
			i = 0;

			while (items.length > 0) {
				splitItems[i] = items.splice(0, chunk);
				i++;
			}

			return splitItems;

		};

	}

})(jQuery);


		/*Dropdown Menu*/
$('.dropdown').click(function () {
		        $(this).attr('tabindex', 1).focus();
		        $(this).toggleClass('active');
		        $(this).find('.dropdown-menu').slideToggle(300);
		    });
		    $('.dropdown').focusout(function () {
		        $(this).removeClass('active');
		        $(this).find('.dropdown-menu').slideUp(300);
		    });
		    $('.dropdown .dropdown-menu li').click(function () {
		        $(this).parents('.dropdown').find('span').text($(this).text());
		        $(this).parents('.dropdown').find('input').attr('value', $(this).attr('id'));
});
		/*End Dropdown Menu


		$('.dropdown-menu li').click(function () {
		  var input = '<strong>' + $(this).parents('.dropdown').find('input').val() + '</strong>',
		      msg = '<span class="msg">Hidden input value: ';
		  $('.msg').html(msg + input + '</span>');
		});
		*/


$('.dropdown-menu li').click(function () {
			document.getElementById("giornata").value = $(this).parents('.dropdown').find('input').val() ;
});






window.requestAnimFrame = (function () {
        return  window.requestAnimationFrame ||
            window.webkitRequestAnimationFrame ||
            window.mozRequestAnimationFrame ||
            window.oRequestAnimationFrame ||
            window.msRequestAnimationFrame ||
            function (callback) {
                window.setTimeout(callback, 1000 / 60);
            };
    })();

    Math.randMinMax = function(min, max, round) {
        var val = min + (Math.random() * (max - min));

        if( round ) val = Math.round( val );

        return val;
    };
    Math.TO_RAD = Math.PI/180;
    Math.getAngle = function( x1, y1, x2, y2 ) {

        var dx = x1 - x2,
            dy = y1 - y2;

        return Math.atan2(dy,dx);
    };
    Math.getDistance = function( x1, y1, x2, y2 ) {

        var     xs = x2 - x1,
            ys = y2 - y1;

        xs *= xs;
        ys *= ys;

        return Math.sqrt( xs + ys );
    };

    var     FX = {};

    (function() {

        var canvas = document.getElementById('myCanvas'),
            ctx = canvas.getContext('2d'),
            lastUpdate = new Date(),
            mouseUpdate = new Date(),
            lastMouse = [],
            width, height;

        FX.particles = [];

        setFullscreen();
        document.getElementById('button').addEventListener('mousedown', buttonEffect);

        function buttonEffect() {

            var button = document.getElementById('button'),
                height = button.offsetHeight,
                left = button.offsetLeft,
                top = button.offsetTop,
                width = button.offsetWidth,
                x, y, degree;

            for(var i=0;i<40;i=i+1) {

                if( Math.random() < 0.5 ) {

                    y = Math.randMinMax(top, top+height);

                    if( Math.random() < 0.5 ) {
                        x = left;
                        degree = Math.randMinMax(-45,45);
                    } else {
                        x = left + width;
                        degree = Math.randMinMax(135,225);
                    }

                } else {

                    x = Math.randMinMax(left, left+width);

                    if( Math.random() < 0.5 ) {
                        y = top;
                        degree = Math.randMinMax(45,135);
                    } else {
                        y = top + height;
                        degree = Math.randMinMax(-135, -45);
                    }

                }
                createParticle({
                    x: x,
                    y: y,
                    degree: degree,
                    speed: Math.randMinMax(100, 150),
                    vs: Math.randMinMax(-4,-1)
                });
            }
        }
        window.setTimeout(buttonEffect, 100);

        loop();

        window.addEventListener('resize', setFullscreen );

        function createParticle( args ) {

            var options = {
                x: width/2,
                y: height/2,
                color: 'hsla('+ Math.randMinMax(160, 290) +', 100%, 50%, '+(Math.random().toFixed(2))+')',
                degree: Math.randMinMax(0, 360),
                speed: Math.randMinMax(300, 350),
                vd: Math.randMinMax(-90,90),
                vs: Math.randMinMax(-8,-5)
            };

            for (key in args) {
              options[key] = args[key];
            }

            FX.particles.push( options );
        }

        function loop() {

            var     thisUpdate = new Date(),
                delta = (lastUpdate - thisUpdate) / 1000,
                amount = FX.particles.length,
                size = 2,
                i = 0,
                p;

            ctx.fillStyle = 'rgba(15,15,15,0.25)';
            ctx.fillRect(0,0,width,height);

            ctx.globalCompositeStyle = 'lighter';

            for(;i<amount;i=i+1) {

                p = FX.particles[ i ];

                p.degree += (p.vd * delta);
                p.speed += (p.vs);// * delta);
                if( p.speed < 0 ) continue;

                p.x += Math.cos(p.degree * Math.TO_RAD) * (p.speed * delta);
                p.y += Math.sin(p.degree * Math.TO_RAD) * (p.speed * delta);

                ctx.save();

                ctx.translate( p.x, p.y );
                ctx.rotate( p.degree * Math.TO_RAD );

                ctx.fillStyle = p.color;
                ctx.fillRect( -size, -size, size*2, size*2 );

                ctx.restore();
            }

            lastUpdate = thisUpdate;

            requestAnimFrame( loop );
        }

        function setFullscreen() {
            width = canvas.width = window.innerWidth;
            height = canvas.height = window.innerHeight;
        };
    })();
