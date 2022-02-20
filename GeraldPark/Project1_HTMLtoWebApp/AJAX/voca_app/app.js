var dict = $('ul');
var title = $('h2');
var p = $('p');

$.getJSON('dict.json')
    .done(function(data){
        for(let word of data){
            var li = $('<li></li>');
            li.text(word.title);
            li.data('word',word);
            li.click(function(event){
                var el = $(event.target);
                var word = el.data('word');
                title.text(word.title);
                p.text(word.description);
            });
            dict.append(li);
        }
    })