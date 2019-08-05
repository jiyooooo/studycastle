function dialog() {

    var dialogBox = $('.dialog'),
        dialogTrigger = $('.dialog__trigger'),
        dialogClose = $('.dialog__close'),
        dialogTitle = $('.dialog__title'),
        dialogContent = $('.dialog__content'),
        dialogAction = $('.dialog__action');

    // Open the dialog
    dialogTrigger.on('click', function(e) {
        dialogBox.toggleClass('dialog--active');
        e.stopPropagation()
    });

    // Close the dialog - click close button
    dialogClose.on('click', function() {
        dialogBox.removeClass('dialog--active');
    });

    // Close the dialog - press escape key // key#27
    $(document).keyup(function(e) {
        if (e.keyCode === 27) {
            dialogBox.removeClass('dialog--active');
        }
    });

    // Close dialog - click outside
    $(document).on("click", function(e) {
        if ($(e.target).is(dialogBox) === false &&
            $(e.target).is(dialogTitle) === false &&
            $(e.target).is(dialogContent) === false &&
            $(e.target).is(dialogAction) === false) {
            dialogBox.removeClass("dialog--active");
        }
    });

};

// Run function when the document has loaded
$(function() {
    dialog();
});