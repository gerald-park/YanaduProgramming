
$("#red-btn").click(function(){
    $("div.demo-box").removeClass('yellow');
    $("div.demo-box").addClass('red');
});
$("#yellow-btn").click(function(){
    $("div.demo-box").removeClass('red');
    $("div.demo-box").addClass('yellow');
});