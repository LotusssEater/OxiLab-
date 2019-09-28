function AbrirMenu(){
    document.getElementById('sidebar').classList.toggle('active');
    document.getElementById('lateral_derecho').classList.toggle('active');
}

function myFunction(x) {
    x.classList.toggle("change");
}

var input = document.getElementById("pass");

var text = document.getElementById("WARNING");

// When the user presses any key on the keyboard, run the function
document.addEventListener("keyup", function(event) {

  // If "caps lock" is pressed, display the warning text
  if (event.getModifierState("CapsLock")) {
    text.style.display = "block";
  } else {
    text.style.display = "none"
  }
});

//validaciones
function Validaciones(){
	ValidarUsuario();
	ValidarPassword();
	ValidarEmail();
	ValidarNumero();
}
function ValidarNumero(){
	var error = document.getElementById("num_error");
	var num = document.getElementById("num").value;
	if(num == null || num.length != 12){
		error.style.display = "block";
  } else {
    error.style.display = "none"
  }
}
function ValidarEmail(){
	var error = document.getElementById("email_error");
  var email = document.getElementById("email").value;
  if(email == null || email.lengh == 0 || !(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/.test(email))) {
		error.style.display = "block";
  } else {
    error.style.display = "none"
  }
}
function ValidarUsuario(){
		var error = document.getElementById("user_error");
	var usuario = document.getElementById("user").value;
	if(usuario == null || usuario.length == 0){
		error.style.display = "block";
  } else {
    error.style.display = "none"
  }
}

function ValidarPasswordIgual(){
	var error_c = document.getElementById("c_pass_error");
	var Conpass = document.getElementById("Cpsw").value;
	var pass = document.getElementById("psw").value;
	if(pass != Conpass){
		error_c.style.display = "block";
	   }else{
		   error_c.style.display = "none";
	   }
}

function ValidarPassword(){
	var error = document.getElementById("pass_error");
	var error_c = document.getElementById("c_pass_error");
	var Conpass = document.getElementById("Cpsw").value;
	var pass = document.getElementById("psw").value;
	if(pass == null || pass.length == 0 || pass.length < 8){
		error.style.display = "block";
		error_c.style.display = "block";
	}else if(pass == Conpass){
		error.style.display = "none";
		error_c.style.display = "none";
	}else if(pass != Conpass){
		error_c.style.display = "block";
	}
}