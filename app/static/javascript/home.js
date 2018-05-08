var current_tab = document.getElementsByClassName("active")[0].id;
var counter = 0;

function turnOffActiveTabs(){

    $('.tablinks').removeClass('active');
    $('.tab-content').hide();

};

function turnOffSelectedTabs(){
    $('.posts').removeClass('selected');
}

$('.tablinks').click(function(){

    turnOffActiveTabs();
    $('#' + this.id).addClass('active');
    current_tab = document.getElementsByClassName("active")[0].id;
    $('#' + this.id + '-content').show();

});

$('.posts').click(function(){

    turnOffSelectedTabs();
    $('#' + this.id).addClass('selected');
    let post_id = this.id.substring(0,1);
    $.ajax({
        url: "../static/text/a.html",
        dataType: 'html',
        cache: false,
        success: function(data){
            for(let i = 0; i < $weekly.length; i++){
                if($weekly[i]['post_id'] == post_id){
                    var div = jQuery("<div/>"); // changes the contents before adding (faster)
                    div.html(data);
                    div.find("#header").html($weekly[i]['post_title']);
                    div.find("#subheader").html($weekly[i]['post_subtitle']);
                    div.find("#content").html($weekly[i]['post_content']);
                    $("#show-area-" + current_tab).html(div.html())
                    break;
                }
            }
        }
    });
});