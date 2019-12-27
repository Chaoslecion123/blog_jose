// delete modal snipet
$('[data-toggle="modal"]').click(function (event) {
    var $link = $(event.target);
    if(event.target.tagName.toLowerCase() != 'a') {
        $link = $(event.target).parents('a');
    };

    var modalId = $link.data('target').slice(1);
    var promptId = modalId + '-prompt';
    var formId = 'id_' + modalId + '-form';

    var $prompt = $('#' + promptId)
    var $form = $('#' + formId);

    var name = $link.data('label');
    if (!name) {
        var $tableRow = $(event.target).parents('tr');
        name = $tableRow.children('td:first-child').html();
    };
    console.log($link);
    console.log($prompt);
    console.log($form);
    $prompt.html(name);
    $form.attr('action', $link.attr('href'));
})
