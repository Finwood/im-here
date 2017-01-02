$(document).ready(function(){
    console.log("Hello World");

    function updateLog() {
        console.log("entered updateLog");
        $.ajax({
            url: "/api/feedback/",
            type: "GET",
            dataType: "json",
            success: function(data, status, xhr) {
                console.log(data._items);
            },
            complete: function(xhr, status) {
                console.log("AJAX is back: " + status);
            }
        });
    }

    updateLog();
});

