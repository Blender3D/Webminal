$(function() {
  $('#command').hide();
  
  $('.flash-message, .flash-error, .flash-warning, .flash-success').each(function() {
    $(this).hide().addClass('notification');
    
    $(this).on('click', function() {
      $(this).slideUp('fast', function() { $(this).remove(); });
    });
    
    $(this).slideDown('fast');
    setTimeout(function() { $(this).trigger('click'); }, 5000);
  });
  
  if ($('body').hasClass('terminal')) {
    $('<div />').prop('id', 'overlay').hide().appendTo('#side');
  }
  
  last_command('404');
});

function last_command(command) {
  $('#overlay').show();
  
  $.get('/help/' + command.split(' ')[0] + '/plain/').success(function(data) {
    $('#side-content').html(data);
    $('#overlay').stop().fadeOut();
  });
}
