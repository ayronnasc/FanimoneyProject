const dropdownGain = document.getElementsByClassName("dropdown-gain");
        if(dropdownGain){
               Array.prototype.forEach.call(dropdownGain, (el) =>{
					const h2 = el.children[0];
					const gainContent = el.children[1];
					const panel = el.getElementsByClassName("panel");
					
					Array.prototype.forEach.call(panel, (el) =>{
						const table = el.children[2]

						el.children[0].addEventListener('click', ()=>{
							let scrollPos = window.scrollY;
							table.classList.toggle('table-visible')
							el.children[0].classList.toggle('panel-heading-transform');
							window.scrollTo(scrollPos);
						});

						h2.addEventListener('transitionend', ()=>{
							if(!h2.classList.contains('dropdown-title-transform')){
								if(table.classList.contains('table-visible') && el.children[0].classList.contains('panel-heading-transform'))
									{
										el.children[0].classList.remove('panel-heading-transform');
										table.classList.remove('table-visible');
									}
							}
						});

					});

					h2.addEventListener('click', ()=>{
						h2.classList.toggle('dropdown-title-transform');
						h2.children[1].classList.toggle('bx-x');

						el.classList.toggle('dropdown-transition');
					}) //click event

					h2.addEventListener('transitionend', ()=>{
						if(h2.classList.contains('dropdown-title-transform')){
							gainContent.style.display =  'block';
							gainContent.classList.add('dropdown-content-transition');
						}else {
							gainContent.classList.remove('dropdown-content-transition');
							gainContent.style.display =  'none';
							
						}
					})

                }); //forEach
				
			}

document.addEventListener("DOMContentLoaded", function(event) {
   
const showNavbar = (toggleId, navId, bodyId, headerId) =>{
const toggle = document.getElementById(toggleId),
nav = document.getElementById(navId),
bodypd = document.getElementById(bodyId),
headerpd = document.getElementById(headerId)

// Validate that all variables exist
if(toggle && nav && bodypd && headerpd){
toggle.addEventListener('click', ()=>{
// show navbar
nav.classList.toggle('show')
// change icon
toggle.classList.toggle('bx-x')
// add padding to body
bodypd.classList.toggle('body-pd')
// add padding to header
headerpd.classList.toggle('body-pd')
})
}
}

showNavbar('header-toggle','nav-bar','body-pd','header')

/*===== LINK ACTIVE =====*/
const linkColor = document.querySelectorAll('.nav_link')

function colorLink(){
if(linkColor){
linkColor.forEach(l=> l.classList.remove('active'))
this.classList.add('active')
	this.classList.add('click-disabled')
}
}
linkColor.forEach(l=> l.addEventListener('click', colorLink))

 // Your code to run since DOM is loaded and ready
});




/**
* TABLES GAIN, OUTGOING AND INVESTMENTS
*
*
* I don't recommend using this plugin on large tables, I just wrote it to make the demo useable. It will work fine for smaller tables 
*   but will likely encounter performance issues on larger tables.
*
*		<input type="text" class="form-control" id="dev-table-filter" data-action="filter" data-filters="#dev-table" placeholder="Filter Developers" />
*		$(input-element).filterTable()
*		
*	The important attributes are 'data-action="filter"' and 'data-filters="#table-selector"'
*/
(function(){
    'use strict';
	var $ = jQuery;
	$.fn.extend({
		filterTable: function(){
			return this.each(function(){
				$(this).on('keyup', function(e){
					$('.filterTable_no_results').remove();
					var $this = $(this), 
                        search = $this.val().toLowerCase(), 
                        target = $this.attr('data-filters'), 
                        $target = $(target), 
                        $rows = $target.find('tbody tr');
                        
					if(search == '') {
						$rows.show(); 
					} else {
						$rows.each(function(){
							var $this = $(this);
							$this.text().toLowerCase().indexOf(search) === -1 ? $this.hide() : $this.show();
						})
						if($target.find('tbody tr:visible').size() === 0) {
							var col_count = $target.find('tr').first().find('td').size();
							var no_results = $('<tr class="filterTable_no_results"><td colspan="'+col_count+'">No results found</td></tr>')
							$target.find('tbody').append(no_results);
						}
					}
				});
			});
		}
	});
	$('[data-action="filter"]').filterTable();
})(jQuery);

$(function(){
    // attach table filter plugin to inputs
	$('[data-action="filter"]').filterTable();
	
	$('.container').on('click', '.panel-heading span.filter', function(e){
		var $this = $(this), 
			$panel = $this.parents('.panel');
		
		$panel.find('.panel-body').slideToggle();
		if($this.css('display') != 'none') {
			$panel.find('.panel-body input').focus();
		}
	});
	$('[data-toggle="tooltip"]').tooltip();
})




