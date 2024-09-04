
setTimeout(function() {
	document.querySelector('.preloader').style.opacity = 0;
	setTimeout(function() {
		document.querySelector('.preloader').style.display = 'none';
		document.querySelector('.page-1').style.display = 'block';
		document.querySelector('.page-1').style.transform = 'scale(0.5)';
		document.querySelector('.page-1').style.opacity = 0;
		setTimeout(function() {
			document.querySelector('.page-1').style.transform = 'scale(1)';
			document.querySelector('.page-1').style.opacity = 1;
		}, 200);
	}, 500);
}, 2000);

document.getElementById('get-started').addEventListener('click', function() {
	document.querySelector('.page-1').style.opacity = 0;
	setTimeout(function() {
		document.querySelector('.page-1').style.display = 'none';
		document.querySelector('.page-2').style.display = 'flex';
		document.querySelector('.page-2').style.opacity = 1;
	}, 500);
});

// document.getElementById('back-to-start').addEventListener('click', function() {
// 	document.querySelector('.page-2').style.opacity = 0;
// 	setTimeout(function() {
// 		document.querySelector('.page-2').style.display = 'none';
// 		document.querySelector('.page-1').style.display = 'flex';
// 		document.querySelector('.page-1').style.opacity = 1;
// 	}, 500);
// });

function getSolution() {
	// Add your solution logic here
	document.getElementById('solution').innerHTML = 'Your solution goes here';
}


const inputField = document.querySelector(".input");
const temporary = document.querySelector(".temporary")
inputField.addEventListener("focus", () => { temporary.style.display = "none"; });
const visibility = document.querySelector("#visibility");


if ( visibility.innerHTML.trim().length > 0 ){
	document.querySelector('.preloader').style.display = 'none';
	document.querySelector('.page-1').style.display = 'none';
	temporary.style.display = "none";
	document.querySelector('.page-2').style.display = 'flex';
	document.querySelector('.page-2').style.opacity = 1;
	document.querySelector('.hero').style.display = "none";
} 

const animatedText = document.querySelector(".animated-text");
let text = animatedText.innerHTML;
animatedText.innerHTML = "";
let i = 0;

function typeText() {
    if (i < text.length) {
        animatedText.innerHTML += text[i];
        i++;
        setTimeout(typeText, 50);
    }
}

typeText();