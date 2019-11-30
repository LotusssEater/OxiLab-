function AbrirMenu(){
    document.getElementById('sidebar').classList.toggle('active');
    document.getElementById('lateral_derecho').classList.toggle('active');
}
function myFunction(x) {
    x.classList.toggle("change");
}

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

function ValidarUsuario(){
  var pass = document.getElementById("psw").value;
  var Pass_inv = document.getElementById("pass_error");

  var usuario = document.getElementById("user").value;
  var Usuario_Inv = document.getElementById("user_error");
	if(usuario == null || usuario.length == 0){
    Usuario_Inv.style.display = "block";
    Pass_inv.style.display = "block";
	}else{
    Usuario_Inv.style.display = "none";
    ValidarPassword();
  }
}
function ValidarPassword(){
  var pass = document.getElementById("psw").value;
  var Pass_inv = document.getElementById("pass_error");
	if(pass == null || pass.length == 0 || pass.length < 8){
    Pass_inv.style.display = "block";
    
	}else{
    Pass_inv.style.display ="none";
    alert("Inicio de sesion exitoso");
    
  }
}