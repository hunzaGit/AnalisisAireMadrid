var scrubberBar = document.getElementsByClassName('scrubber-bar')[0];
var scrubberWindow = document.getElementsByClassName('scrubber-window')[0];
var scrubberDerecha = document.getElementsByClassName('scrubber-derecha')[0];
var scrubberIzquierda = document.getElementsByClassName('scrubber-izquierda')[0];
const anchoImagen =scrubberWindow.clientWidth; //1200


scrubberWindow.onmousemove = function (event) {
    var ajustePunteroBarra = 21; //-13
    // valor para ajustar el puntero con la barra se calcula poniendo el sobre el inicio del frame
    // haciendo coincidir con la barra. (el console.log('resta'...) indica el valor)


    // console.log('winWidth: ' + window.innerWidth);
    // console.log('clientWith: '+ scrubberWindow.clientWidth)

    var windowChangeSize = (window.innerWidth - anchoImagen) / 2

    // event.pageX - 225 = windowChangeSize
    // event.pageX = windowChangeSize + 225
    // event.pageX - windowChangeSize = 225
    // console.log('ajustePunteroBarra: ' + ajustePunteroBarra )
    // console.log('puntero: ' +event.pageX);
    // console.log('windowChangeSize: '+ windowChangeSize);
    // console.log('resta: ' + (event.pageX - windowChangeSize))
    var x = event.pageX - windowChangeSize - ajustePunteroBarra;

    //si sale de los limites
    if (x < 0) {
        x = 0
    }
    if (x > anchoImagen) {
        x = anchoImagen
    }
    // console.log('PosBarra: ' + x);
    scrubberBar.style.left = x + "px";
    scrubberIzquierda.style.width = x + "px";

    scrubberDerecha.style.width = (anchoImagen - x) + "px";

}
