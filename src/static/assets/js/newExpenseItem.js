/*function expenseItemFormSubmit() {
	//disable button
    //$('#expenseItemSubmitBtn').addClass('disabled');
    
    var ser = $('#expenseItemForm').serialize();
    $.ajax({
            type: "POST",
            data: $('#expenseItemForm').serialize(),
            url: "/eclaim/newExpenseAjax/",
            dataType:"text",
            success: function(data) {
			alert('sucess!');
            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
            alert('failed!');

            }
        });
}*/
  	var cssClassNames = {
	    'headerRow': 'datatable_th',
	    'tableRow': 'datatable_tr',
	    'oddTableRow': 'datatable_tr',
	    'selectedTableRow': '',
	    'hoverTableRow': 'datatable_tr_hover',
	    'headerCell': 'datatable_tr',
	    'tableCell': 'datatable_tr',
	    'rowNumberCell': ''};

  var options = {'cssClassNames': cssClassNames,
	  'page' :  'enable',
	  'pageSize' : '5',
	  'allowHtml' : true
  };


function getExpenseItem(expense_slug) {
    $.ajax({
            type: "GET",
            url: "/eclaim/expense/" + expense_slug + "/item/all/",
            dataType:"text",
            success: function(data) {
				google.load('visualization', '1', {packages:['table']});
				var json_table = new google.visualization.Table(document.getElementById('expenseListTable'));
				

				
				var json_data = new google.visualization.DataTable(data);
				var formatter = new google.visualization.TablePatternFormat('<div class="btn-group"><a class="btn btn-mini" onclick="deleteItem({0})"><i class="icon-trash"></i></a><a class="btn btn-mini" onclick="editItem({0})"><i class="icon-pencil"></i></a></div>');
  				formatter.format(json_data,[0,0]);

				json_table.draw(json_data,options);
				clean();
			  google.visualization.events.addListener(json_table, 'sort',
			      function(event) {
			      	clean();
			      });
			 google.visualization.events.addListener(json_table, 'select', 
				function(event) {
					clean();
					updateExpenseItemForm();
				});
			  google.visualization.events.addListener(json_table, 'page',
			      function(event) {
			      	clean();
			      });

				
   			$('#expenseListTable td').hover(function(){clean();});
            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
            }
        });
}
function deleteItem(expenseItemId){
    expense_slug = $('#expenseName').val();
    $.ajax({
	    type: "POST",
	    url: "/eclaim/expense/" + expense_slug + "/delete_expense_item/" + expenseItemId + "/",
	    dataType:"text",
	    success: function() {
	  		getExpenseItem(expense_slug);
	    }
	   }
	   );
}

function editItem(expenseItemId){
	alert("edit!  " + expenseItemId);
	expense_slug = $('#expenseName').val();
	$.ajax({
	    type: "GET",
	    url: "/eclaim/expense/" + expense_slug + "/edit_expense_item/" + expenseItemId + "/",
	    dataType:"html",
	    success: function(data) {
	  		$('#expenseRight').html(data);
	    }
	   }
	   );
	//$('#itemId').val(expenseItemId);

}


function updateExpenseItemForm(){
	
	
}


function clean(){
	$('#expenseListTable table').removeClass();
	//$('#expenseListTable tr').removeClass();
	//$('#expenseListTable td').removeClass();
	$('#expenseListTable table').addClass("table table-striped");

}

$(document).ready(function(){
	//$('#expenseItemSubmitBtn').bind('click',function(){expenseItemFormSubmit()});
	//$('#expenseItemSubmitBtn').submit(function(){expenseItemFormSubmit()});
	//add cookie needed for django
	$(document).ajaxSend(function(event, xhr, settings) {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    function sameOrigin(url) {
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }
    function safeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    if (!safeMethod(settings.type) && sameOrigin(settings.url)) {
        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    }
});

$.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                // Only send the token to relative URLs i.e. locally.
                xhr.setRequestHeader("X-CSRFToken",
                                     $('input[name="csrfmiddlewaretoken"]').val());
            }
        }
    });
	getExpenseItem($('#expenseName').val());
	clean();

}

);
