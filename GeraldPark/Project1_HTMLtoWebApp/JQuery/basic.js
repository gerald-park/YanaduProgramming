$("#alert").click(function() {
    alert("Button clicked!");
});

$("#button2").click(function(){
    $('#alert').click();
});

alert($('div.demo-container').html());

$("#btn").click(function(){
    $("div.demo-container").html("<div>Button Clicked!</div>");
});