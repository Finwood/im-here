function updateLog() {
    console.log("updating log...");

    var newestEntry = $('.feed-container div.card:not(#card-template)').first().data('time');
    var data = newestEntry !== undefined ? {where: '{"_created": {"$gt": "' + newestEntry + '"}}'} : null;

    $.get({
        url: "/api/feedback/",
        dataType: "json",
        data: data,
        success: function(data, status, xhr) {
            // console.log(data._items);
            for (var item of data._items)
                processRecord(item);
        },
        error: function(xhr, status, error) {
            console.warn("AJAX came back with status " + status + ":\n" + error);
        }
    });
}

function processRecord(rec) {
    console.log(rec);

    if ($('#' + rec._id).length == 0) {
        var $card = $('#card-template').clone();

        $card.attr('id', rec._id);
        $card.find('p.ip').text(rec.user);
        $card.find('p.timestamp').text(rec._created);
        $card.find('p.lat span').text(rec.lat);
        $card.find('p.lon span').text(rec.lon);
        $card.data('time', rec._created);

        $('.feed-container').prepend($card);
    }
}

$(document).ready(function(){
    updateLog();
    var updateTimer = window.setInterval(updateLog, 2000);
});