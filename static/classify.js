$( document ).ready(function(){

    var tweet_id = $("#tweet_id").text();
    var tweet = $("#tweet").text();

    $('#yes').click(function(){
        $.ajax({
        type: "POST",
        url: "/rate",
        data: { tweet_id : tweet_id, relevant : 1 }
          })
        .done(function( msg ) {
            location.reload()
        });
    }) 

    $('#no').click(function(){
        $.ajax({
            type: "POST",
            url: "/rate",
            data: { tweet_id : tweet_id, relevant : 0 }
              })
            .done(function( msg ) {
                location.reload()
            });
    }) 

});