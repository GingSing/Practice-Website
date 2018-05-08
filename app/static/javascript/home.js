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

//$('.posts').click(function(){
//
//    turnOffSelectedTabs();
//    $('#' + this.id).addClass('selected');
//    let post_id = this.id;
//    $('#show-area-' + current_tab).load("/static/text/a.html", function(){
//        $.getJSON($SCRIPT_ROOT + '/get_weekly_posts/' + post_id
//        , function(data){
//            console.log(data.post_title);
//            $("#header").html(data.post_title);
//            $("#subheader").html(data.post_subtitle);
//            $("#content").html(data.post_content);
//        });
//    });
//});

$('.posts').click(function(){

    turnOffSelectedTabs();
    $('#' + this.id).addClass('selected');
    let post_id = this.id;
    $.ajax({
        url: "../static/text/a.html",
        dataType: 'html',
        cache: false,
        success: function(data){
            //$('#show-area-' + current_tab)).html(data);
            for(let i = 0; i < $weekly.length; i++){
                if($weekly[i]['post_id'] == post_id){
                    $("#header", $(data)).html($weekly[i]['title']);
                    console.log(data);
                    $("#show-area2").html(data);
                    break;
                }
            }
        }
    });
});

//function loadSecondDoc(){
//    $ajax({
//        url: '../static/text/b.html',
//        dataType : 'html',
//        cache : false,
//        success: function (data) {
//            ${'#show-area2'}.html(data);
//        }
//    });
//}