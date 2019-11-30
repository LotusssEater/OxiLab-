$(document).ready(function(){
    $('[data-toggle="tooltip"]').tooltip();
});

function AbrirMenu(){
    document.getElementById('sidebar').classList.toggle('active');
    document.getElementById('lateral_derecho').classList.toggle('active');
}

const btnRemix = document.querySelector('.toggler-btn');
btnRemix.addEventListener('click', function () {
    document.getElementById('remixes').classList.toggle('active');
});

const btnCoaching = document.querySelector('.togglec-btn');
btnCoaching.addEventListener('click', function () {
    document.getElementById('coaching').classList.toggle('active');
});
// esto hace q se cambie las 3 rayas' a x
function myFunction(x) {
    x.classList.toggle("change");
}


