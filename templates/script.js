	$(document).ready(function(){
		    	(function worker() {
				  	$.ajax({
				    url: 'http://md1s0fec:7000/', 
					    success: function(data) {
					      $('#data_input').html(data);
					    },
					    complete: function() {
					      // Schedule the next request when the current one's complete
					      setTimeout(worker, 5000);
					    }
			  		});
				})();
			});