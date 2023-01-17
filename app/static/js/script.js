'use strict';
var urlEl = document.URL;
document.querySelectorAll('a').forEach(elem => {
    if (urlEl === elem.href) {
        elem.style.fontWeight = 'bold';
    }
    
});
let menuEl = document.querySelectorAll('.lod')
let removedEl = urlEl.split('/');
var news = removedEl.splice(0, 3);
news = removedEl.pop();

var hidEl = document.querySelectorAll('.mask');

if (removedEl.length > 1) {
    hidEl.forEach(elem => {   
        console.log(elem.innerText.trim()); 
        if (elem.innerText.trim() === removedEl[removedEl.length - 1]) {
            elem.classList.remove('entered')
    }
    
})
}



let qwe = document.querySelectorAll('a');
qwe.forEach(elem => {
    elem.parentElement.addEventListener('click', event => {
        if (!(event.target === elem)) {        
            var rs = elem.parentElement.querySelectorAll('.mask');
            if (rs.length > 0) {
                rs.forEach(el => {
                    el.classList.toggle('entered');
                    })
                };
        }
    });
});