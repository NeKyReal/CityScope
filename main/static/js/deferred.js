    const dfd1 = $.Deferred();
    const dfd2 = $.Deferred();
    const dfd3 = $.Deferred();
    $(".white1").fadeOut(1000, dfd1.resolve);
    $(".white2").fadeOut(2000, dfd2.resolve);
    $(".white3").fadeOut(3000, dfd3.resolve);
    dfd1.done(function ()
    {
        console.log("Загрузка завершена на 30%");
    });
    dfd1.fail(function ()
    {
        console.log("Загрузка прервана на 30%");
    });
    dfd2.done(function ()
    {
        console.log("Загрузка завершена на 60%");
    });
    dfd2.fail(function ()
    {
        console.log("Загрузка прервана на 60%");
    });
    dfd3.done(function ()
    {
        console.log("Загрузка завершена на 90%");
    });
    dfd3.fail(function ()
    {
        console.log("Загрузка прервана на 90%");
    });
    dfd3.always(function ()
    {
        console.log("Progress-bar закончил свою работу")
    });
    $.when(dfd1, dfd2, dfd3).done(function ()
    {
        $(".alert-success").fadeOut(1000, dfd3.resolve);
        console.log('Загрузка завершена на 100%. Объявление скрыто.');
    });