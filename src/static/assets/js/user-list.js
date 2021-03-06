/**
 * @author Qin Sun
 */

jQuery(document).ready(function(){ 
	 //for csrf token.....
	  jQuery(document).ajaxSend(function(event, xhr, settings) {
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
  
  jQuery("#userListTable").jqGrid({        
    url:"/eclaim/hr/employee_list/", 
    datatype: "json",
    autowidth: true,
    altRows: true,
    shrinkToFit: true,
    forceFit: true,
    height: "auto",
    altclass:'myAltRowClass',
     jsonReader : {
      root:"row",
      repeatitems: false,
      id: "id"
   },
    colNames:['Employee Id','First Name','Last Name','Is Active'],
    colModel:[
      {name:'employee_id',index:'employee_id', width:200, sorttype:"int"},
      {name:'first_name',index:'first_name', width:200, sorttype:"text"},
      {name:'last_name',index:'last_name', width:200,sorttype:"text"},
      {name:'is_active',index:'is_active', width:300,sorttype:"int"},
       ],
    caption: "User List",
    rowNum:10, 
    rowList:[5,10,15],
    sortname: 'employee_id',
    sortorder: 'asc',
 
    pager: '#userListTablePager', 
    viewrecords: true,	
  });
  	jQuery("#userListTable").jqGrid('navGrid',"#userListTablePager");
});
