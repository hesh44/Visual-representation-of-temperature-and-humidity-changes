otvoreno = false 

// funkcija koja pali sistem
function upali() {
  // varijabli dodeljujemo checkbox
  var checkBox = document.getElementById("toggle-upaljeno");

  // if uslov koji nas baca na rutu koja pokrece odnosno gasi uredjaj
  if (checkBox.checked == false){
    $.getJSON('http://172.20.222.231:5000/uredjajON', function(data) {   
      console.log("upali");
    });
  } 
  else {
    $.getJSON('http://172.20.222.231:5000/uredjajOFF', function(data) {   
    console.log("ugasi");
  });
}
}

function upaliTreperenje() {
  var checkBox = document.getElementById("toggle-treperenje");

  if (checkBox.checked == false){
    $.getJSON('http://172.20.222.231:5000/treperenjeON', function(data) {   
    });
  } 
  else {
    $.getJSON('http://172.20.222.231:5000/uredjajOFF', function(data) {   
  });
}
}

// Funkcija koja cita temperaturu i na osnovu nje menja boju okvira polja u kome se ona ispisuje
$(function citaj(){
  $.ajaxSetup ({
    cache: false,
    complete: function() {
    // Ucitavanje temperature na svaku sekundu
      setTimeout(citaj, 1000);
    }
  });
  if(!otvoreno){
    $.getJSON('http://172.20.222.231:5000/getVrednosti', function(data) {
        $('#poljetext').html(data.temperatura);

        if (data.temperatura>30) {
            $("#polje").css("border-color",	"#DC3232");
        }else if (data.temperatura<21) {
            $("#polje").css("border-color",	"#3271DC");
        } else {
            $("#polje").css("border-color",	"#d7c79e");
        }
        console.log(data.temperatura);
       
    });
  } 
});
