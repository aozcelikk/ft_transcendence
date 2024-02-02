const toastTrigger = document.getElementById('liveToastBtn')
const toastLiveExample = document.getElementById('liveToast')
//Sağ alt köşeden ileti bilgi ekranı
if (toastTrigger) {
	const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toastLiveExample)
	toastTrigger.addEventListener('click', () => {
		toastBootstrap.show()
	})
};



const chatsocket = new WebSocket(
	'ws://' + window.location.host + '/ws/sohbet/' + 1 + '/'
)
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


//Şimdiki zamanı gösterme
function time() {
    var date = new Date().toLocaleTimeString('tr-TR');
    document.querySelector("#time").innerHTML = date;
};
// her 1 saniyede tarihSaat fonksiyonunu yeniden çalıştır
setInterval(time, 1000); 
