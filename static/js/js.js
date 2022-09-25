
	


		function responsiveTable (table){

				var RowNum = 1;										// to append row number before each data

		 		$(table+' tr:gt(0)').each(function(){				// select all table rows except table header row

		 			// append the header for row number to the small table 
		 			$('.table-xs').append('<div class="row-header"> <h5> Row Number : '+RowNum+'</h5> </div>');

					$(this).find('td').each(function(){		// select all table data 

						// for each td get it's equivalent header and append header text to the small table header div
						$('.table-xs').append('<div class="col-xs-6 header">'+$('th').eq($(this).index()).text()+'</div>');
					
						// for each td get it's text and append it to the small table data div
						$('.table-xs').append('<div class="col-xs-6 data">'+$(this).text()+'</div>');
				
					});
					
					RowNum++;
				
		 		});

		 	}
				 balanceSize();



		 		// IMPORTANT on resize fun will be excessive load on your processor if you have many rows 

		
		 	$(window).resize(function(){			
		 	 if ($(window).width() < 1000 ){					// to work when shown the small table 	
		 						balanceSize();				// balance the size on resize 
		 						}
		 	})
		 


	
		// balance size will make all headers height equal data height !!! Just to fill the BG color ><

 	function balanceSize(){
				var i = 0 ;		
				$('.header').each(function(){

					$(this).height($('.data').eq(i).height());

					i++;
				});
			}
			