var menu = $('#sidemenu li');
var content = $('#content');

menu.click(function(event){
    var url = event.target.innerText + '.html';
    console.log(url);
    $.ajax(url)
        .done(function(html){
            content.html(html);
        });
});