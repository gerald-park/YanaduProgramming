var todos = {};

$("#addButton").click(function(){
    var text = $("#inputBox").val();
    todos[text] = false;
    $("#inputBox").val("");
    console.log(todos);

    $(".contents ul").append(liTemplate(text));
})

function inputTemplate(text) {
    var inputTag = $('<input type="checkBox" id="checkBox"></input>');
    inputTag.data("value", text);
    return inputTag;
}

function buttonTemplate(text) {
    var buttonTag = $('<button id="deleteButton">X</button>');
    buttonTag.data("value", text);
    return buttonTag;
}

function liTemplate(text) {
    var li = $("<li></li>");
    li.attr("value", text);
    li.append(inputTemplate(text));
    li.append(text);
    li.append(buttonTemplate(text));

    li.click(function(event){
        var el = $(event.target); //클릭된 타겟의 이벤트를 받아옴 
        console.log(el.data("value")); // 해당 이트가 발생한 태그의 값을 읽어옴 
        if (el.is("button")){
            delete todos[text];
            $('li[value]='${text}']').remove();
            console.log(todos)
        }
    })

    return li;
}