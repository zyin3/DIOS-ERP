$(document).ready(function(){
	/*-----------Approve-Queue-Table-----------*/
    jQuery("#Approve-Queue-Table").jqGrid({
    datatype: "local",       
    autowidth: true,
    altRows: true,
    shrinkToFit: true,
    forceFit: true,
    altclass:'myAltRowClass',
    colNames:['Report Name', 'Employee', 'Report Date', 'Requested Amount'],
    colModel:[
    {name:'reportName',index:'reportName',width:100},
    {name:'Employee',index:'Employee', width:50},
    {name:'reportDate',index:'reportDate', width:100},
    {name:'requestedAmount',index:'requestedAmount', width:100}
    ],
    pager: '#Approve-Queue-Table-pager',
    viewrecords: true,
    height: "auto",
    caption:"Approve Queue" });
    jQuery("#Approve-Queue-Table").jqGrid('navGrid','#Approve-Queue-Table-pager',{edit:false,add:false,del:false});
        var mydata = [
		{reportName:"Report0001",Employee:"Qin Sun",reportDate:"2012-01-01",requestedAmount:"5000.00"},
		{reportName:"Report0002",Employee:"Ray Qian",reportDate:"2012-01-01",requestedAmount:"1234.00"},
		{reportName:"Report0003",Employee:"Jay Guan",reportDate:"2012-01-01",requestedAmount:"9999.00"},
		{reportName:"Report0004",Employee:"Qin Sun",reportDate:"2012-01-01",requestedAmount:"54566.00"},

		];
		
	/*------------My Expense Report Table-----------*/
    jQuery("#MyExpense-Report-Table").jqGrid({
    datatype: "local",       
    autowidth: true,
    altRows: true,
    shrinkToFit: true,
    forceFit: true,
    altclass:'myAltRowClass',
    colNames:['Report Name', 'Report Date', 'Amount', 'Status'],
    colModel:[
    {name:'reportName',index:'reportName',width:100},
    {name:'reportDate',index:'reportDate', width:100},
    {name:'requestedAmount',index:'requestedAmount', width:100},
    {name:'status',index:'status',width:100},
    ],
    pager: '#MyExpense-Report-Table-pager',
    viewrecords: true,
    height: "auto",
    caption:"My Expense Report Table" });
    jQuery("#MyExpense-Report-Table").jqGrid('navGrid','#MyExpense-Report-Table-pager',{edit:false,add:false,del:false});
    
    
    var mydata = [
		{reportName:"Report0001",Employee:"Qin Sun",reportDate:"2012-01-01",requestedAmount:"5000.00"},
		{reportName:"Report0002",Employee:"Ray Qian",reportDate:"2012-01-01",requestedAmount:"1234.00"},
		{reportName:"Report0003",Employee:"Jay Guan",reportDate:"2012-01-01",requestedAmount:"9999.00"},
		{reportName:"Report0004",Employee:"Qin Sun",reportDate:"2012-01-01",requestedAmount:"54566.00"},
	];
		
	var mydata1 = [
		{reportName:"Report0001",reportDate:"2012-01-01",requestedAmount:"5000.00",status:"saved"},
		{reportName:"Report0002",reportDate:"2012-01-01",requestedAmount:"5000.00",status:"waitting for approval"},
		{reportName:"Report0003",reportDate:"2012-01-01",requestedAmount:"5000.00",status:"approved"},
		{reportName:"Report0004",reportDate:"2012-01-01",requestedAmount:"5000.00",status:"Paid"},
	];
	


	/*add dummy data to table*/
	for(var i=0;i<=mydata.length;i++)
	jQuery("#Approve-Queue-Table").jqGrid('addRowData',i+1,mydata[i]);
	
	for(var i=0;i<=mydata1.length;i++)
	jQuery("#MyExpense-Report-Table").jqGrid('addRowData',i+1,mydata1[i]);
	}
    )


	$(window).bind('resize', function() {
	    // Get width of parent container
	    var width = $("#approveQueue").width();
	    jQuery("#Approve-Queue-Table").setGridWidth(width*0.95);
	    jQuery("#MyExpense-Report-Table").setGridWidth(width*0.95);
	}).trigger('resize');