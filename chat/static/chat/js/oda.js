//json.stringify - javascript nesnesini json dizesine dönüştürme
//json.parse - json dizesini javascript nesnesine dönüştürme
const chatsocket = new WebSocket(
	'ws://' + window.location.host + '/ws/sohbet/' + 1 + '/'
)

	
chatsocket.onmessage = function (e) {
  const message = JSON.parse(e.data);
  handleMessage(message);
};


//karakter alanından mesajları alıyor javascript dizisine dönüştürme
chatsocket.onmessage = function(e){
	const data = JSON.parse(e.data);
	const minisend = document.querySelector("#textareasend");
	document.querySelector("#chatarea").value += (data.user + ":" + data.message + '\n');
	minisend.innerHTML = (data.message + '\n');
	console.log(minisend.value);
};
//Girilen mesajı deger olarak jsona dönüştürme
document.getElementById("chatbtn").onclick = function(e){
	const msg = document.getElementById("chatinput").value;
	chatsocket.send(JSON.stringify({'message':msg}));
	document.querySelector("#chatinput").value ='';
};

//İleti gönderme olayı
document.querySelector("#chatinput").focus();
document.querySelector("#chatinput").onkeyup = function(e){
	if (e.keyCode === 13) {// Enter tuşu ile gönderme 
		document.querySelector("#chatbtn").click();
		document.querySelector("#liveToastBtn").click();
	}
};
