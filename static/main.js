function updateLog(animate) {
    console.log("updating log...");

    if (animate === undefined) animate = true;

    var newestEntry = $('.feed-container div.card:not(#card-template)').first().data('time');
    var data = {sort: '-_created'};
    if (newestEntry !== undefined)
        data.where = '{"_created": {"$gt": "' + newestEntry + '"}}';

    $.get({
        url: "/api/feedback/",
        dataType: "json",
        data: data,
        success: function(data, status, xhr) {
            // console.log(data._items);
            for (var item of data._items.sort(function(a, b) {
                return a._created > b._created;
            }))
                processRecord(item, animate);
        },
        error: function(xhr, status, error) {
            console.warn("AJAX came back with status " + status + ":\n" + error);
        }
    });
}

function processRecord(rec, animate) {
    console.log(rec);

    if ($('#' + rec._id).length == 0) {
        var $card = $('#card-template').clone();

        $card.attr('id', rec._id);
        $card.find('p.ip').text(rec.user);
        $card.find('p.timestamp').text(rec._created);
        $card.find('p.lat span').text(rec.lat.toFixed(3));
        $card.find('p.lon span').text(rec.lon.toFixed(3));
        $card.data('time', rec._created);

        if (animate) {
            $top = $('.card:first-child');
            $top.animate({
                'margin-top': $top.height()
            }, 300, function () {
                $top.css('margin-top', 0);
                $('.feed-container').prepend($card);
            });
        } else {
            $('.feed-container').prepend($card);
        }
    }
}

$(document).ready(function(){
    updateLog(false);
    var updateTimer = window.setInterval(updateLog, 2000);
});
