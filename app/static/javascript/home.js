function turnOffEverything(){

    $('.tablinks').removeClass('active');
    $('.tab-content').hide();

};

$('.tablinks').click(function(){

    turnOffEverything();
    $("#" + this.id).addClass('active');
    $('#' + this.id + '-content').show();

});