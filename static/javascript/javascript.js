//Javascript
function cadastro(){ 
		var nome = document.getElementById("nome").value;
		var email = document.getElementById("email").value;
		var senha = document.getElementById("senha").value;
		var pais = document.getElementById("pais").value;
		var idioma = document.getElementById("idioma").value;
		var confsenha = document.getElementById("confsenha").value;
		if(nome ==""){
			alert("Preecha o campo, por favor.");
			return false;
		}
		
		if( (email.indexOf("@")==-1)||(email=="")(email.indexOf(".")==-1)){
			alert("Preecha o campo, por favor.");
			return false;
		}
		
		if(senha ==""){
			alert("Preecha o campo, por favor.");
			return false;
		}
		if(confsenha ==""){
			alert("Preecha o campo, por favor.");
			return false;
		}
		
		if(confsenha != senha){
			alert("Preecha o campo corretamente, por favor.");
			return false;
		}
		
		if(pais ==""){
			alert("Preecha o campo, por favor.");
			return false;
		}
		
		if(idioma ==""){
			alert("Preecha o campo, por favor.");
			return false;
		}
		
		
	}
		


var slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1} 
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none"; 
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block"; 
  dots[slideIndex-1].className += " active";
}
var instance = M.Carousel.init({
    fullWidth: true,
    indicators: true
  });

