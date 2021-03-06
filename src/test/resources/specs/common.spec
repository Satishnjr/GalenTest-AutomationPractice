
@objects
    header-img.responsive     css      img[class='img-responsive'] 
    header-div.row            xpath    //*[@id="header"]/div[2]/div/div
    header-logo               css      img[class='logo img-responsive']
    search_box                id       search_query_top
    cart                      css      a[title='View my shopping cart']                      
    cart-text                 css      .shopping_cart a b  
    cart-empty-text           css	   .ajax_cart_no_product
    menu                      css      .sf-menu
    home-page-steps           id	   home-page-tabs
    carousel                  css	   .bx-viewport
    footer                    css      .footer-container
    #newsletter		          id        newsletter-input
    


= Header =
    @on *
    	header-img.responsive:
			inside screen 0px top
			centered horizontally inside screen 1px
			
            
		header-div.row:
			height ~ 38px
			inside header-div.row 0px top
			centered horizontally inside screen 1px
			
	
    	cart:
    		height 45px
    		css font-weight is "700"
    		
    	
    	cart-text:
    	    inside cart 5 to 10px top
    	    
    	cart-empty-text:
    	    inside cart 10 to 15px top
    	        
            
    @on desktop
    	header-img.responsive:
    		width < 1200px 
    		height < 70px
    		
		header-logo:
			below header-div.row ~ 15px
			width < 351px                                                                           
			height < 101px
			css font-family is  "Arial, Helvetica, sans-serif"
			css font-size is "13px" 
			
		header-div.row:
			width < 1200px
			
			 
		search_box:
			below header-div.row 50px
			width < 371px                                                                           
			height ~ 45px
		
		cart:
		    width < 300px
		    below header-div.row 50px	
		
		menu:	        
            width < 1200px
            height 59px
            below search_box < 45px
            below cart < 45px
        
        home-page-steps: 	
    	    width < 1200px 
    		height 46px
		
		carousel:
            width < 780px
            height < 450px
            below menu ~ 30px
            	
	@on mobile
		header-img.responsive:	
			width < 400px 
			height 22px
			
		header-div.row:
			width < 400px
			
		header-logo:
			below header-div.row ~ 15px
			width < 400px                                                                           
			height < 101px
			css font-family is  "Arial, Helvetica, sans-serif"
			css font-size is "13px" 
			
			 
		search_box:
			below header-div.row 164px
			width < 400px                                                                           
			height ~ 45px
		
		cart:
		    width < 400px
		    below header-div.row 259px
		
		home-page-steps: 	
    	    width < 400px 
    		height 88px    
		
		carousel:
            width < 400px
            height < 250px
             
               	
	@on tablet
		header-img.responsive:
			width < 700px
			height ~ 38px
			
		header-div.row:
			width < 700px  
			
		header-logo:
			below header-div.row ~ 15px		
			width < 700px 						                                                                         
			height < 101px
			css font-family is  "Arial, Helvetica, sans-serif"
			css font-size is "13px" 
			
			 
		search_box:
			below header-div.row 164px
			width < 700px                                                                           
			height ~ 45px
        
        cart:
		    width < 700px
		    below header-div.row 259px
		
		home-page-steps: 	
    	    width < 700px 
    		height 44px 
    	
    	carousel:
            width < 700px
            height < 400px
            
            
            
= footer =
    @on desktop
	    footer:
	        width > 1000px 
    		height > 400px
    		
    	#newsletter-input:
    	    #width ~ 300px 
    		#height ~ 45px
    	
    		
    @on mobile
	    footer:
	        width > 400px 
    		height > 400px
    		
    @on tablet
	    footer:
	        width > 700px 
    		height > 400px