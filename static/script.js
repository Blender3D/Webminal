$(document).ready(function() {
    $('#command').hide();
    
    $('.flash-message, .flash-error, .flash-warning, .flash-success').each(function() {
        var $this = $(this);
        
        $this.click(function() {
            $this.slideUp('fast', $this.remove);
        }).hide().addClass('notification').slideDown('fast');
        
        setTimeout(function() {
            $this.trigger('click');
        }, 5000);
    });
    
    if ($('body').hasClass('terminal')) {
        $('<div />', {
            'id': 'overlay'
        }).hide().appendTo('#side');
    }
    
    show_command_help('404');
});

function show_command_help(command) {
    if (command) {
        var url = '/help/' + command.split(' ')[0] + '/plain/';
        
        $('#overlay').show();
        
        $.get(url).success(function(data) {
            $('#side-content').html(data);
            $('#overlay').stop().fadeOut();
        });
    }
}
