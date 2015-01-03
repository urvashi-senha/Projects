function prepareList() {
    $('#expList').find('li:has(ul)')
    .click( function(event) {
         
        if (this == event.target) {
            $(this).toggleClass('expanded');
            $(this).children('ul').toggle('medium');
		var target_1 = event.target || event.srcElement;
        alert(event.target_1.innerHTML);
        }
        return false;
    })
    .addClass('collapsed')
    .children('ul').hide();

   
    
};


$(document).ready( function() {
    prepareList()
});
