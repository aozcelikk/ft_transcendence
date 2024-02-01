const toastTrigger = document.getElementById('liveToastBtn')
const toastLiveExample = document.getElementById('liveToast')
//Sağ alt köşeden ileti bilgi ekranı
if (toastTrigger) {
	const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toastLiveExample)
	toastTrigger.addEventListener('click', () => {
		toastBootstrap.show()
	})
};

//Şimdiki zamanı gösterme
function time() {
    var date = new Date().toLocaleTimeString('tr-TR');
    document.querySelector("#time").innerHTML = date;
};
// her 1 saniyede tarihSaat fonksiyonunu yeniden çalıştır
setInterval(time, 1000); 
