//alert('Привет');
//var result = confirm('Пока');
//if (result) {
//    console.log('Привет, JavaScript');
//}
//else {
//    console.log('Пока, JavaScript');
//}
//document.write('Здесь я практикую JavaScript')

document.addEventListener('DOMContentLoader', function(){});

function innerHTMLMessage() {
    var textElement = document.getElementsByClassName('text');
    var newText = 'Это бебра 2';
    newText += '<br>';
    textElement[0].innerHTML = newText;
}
