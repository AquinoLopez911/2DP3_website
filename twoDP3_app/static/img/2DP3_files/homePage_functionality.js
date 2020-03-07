

function changeBG(obj) {
    obj.style.transform = "translateY(-1em)";
    // obj.style.backgroundColor = "#485043";
    obj.style.backgroundColor = "#5e6758";
}

function defaultBG(obj) {
    obj.style.transform = "translateY(-1em)";
    obj.style.backgroundColor = "#FFF";
} 

function addShadow(obj) {
    obj.classList.add("shadow-lg");
    obj.style.transform = "translateY(-1em)";
} 

function removeShadow(obj) {
    obj.classList.remove("shadow-lg")
    obj.style.transform = "translateY(1em)";
} 