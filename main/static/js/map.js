ymaps.ready(init);

function init()
{
    var myMap = new ymaps.Map("map",
        {
            center: [55.994415, 92.797464],
            zoom: 19
        },
        {
            searchControlProvider: 'yandex#search'
        });

    myMap.geoObjects.add(new ymaps.Placemark([55.994415, 92.797464],
        {
            balloonContent: 'Мы находимся <strong>здесь</strong>'
        },
        {
            preset: 'islands#icon',
            iconColor: '#ff9065'
        }));
}