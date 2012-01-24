$(function() {
  $('#command').hide();
  
  $('.flash-message, .flash-error').each(function() {
    $(this).hide();
    
    $(this).addClass('notification');
    $(this).on('click', function() {
      $(this).slideUp('fast', function() { $(this).remove(); });
    });
    
    $(this).slideDown('fast');
    setTimeout(function() { $(this).trigger('click'); }, 5000);
  });
  
});

function last_command(command) {
  $('#side-content').load('/help/' + command.split(' ')[0] + '/plain/');
}
