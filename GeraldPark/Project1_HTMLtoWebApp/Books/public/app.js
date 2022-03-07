
var title = $('#title');
var author = $('#author');
var save = $('#save');
var list = $('#list');

function getBooks(){
    $.getJSON('/books')
    .done(function(books){
        list.empty();
        for (var book of books){
            var li = $("<li />");
            li.data('book', book);
            li.text(book.title + '(' + book.author + ')');
            li.click(function(event){
                var book = $(event.target).data('book');
                deleteBook(book.id);
            });
            list.append(li)
        }
    });
}

function createBook(){
    $.ajax('/books',{
        type : 'POST',
        data : JSON.stringify({
            title: title.val(),
            author: author.val()
        }),
        contentType: "application/json; charset=utf-8"
    })
    .done(getBooks)
}

function deleteBook(id){
    $.ajax('/books/'+id,{
        type: 'DELETE'
    })
    .done(getBooks)
}

save.click(createBook);
getBooks();