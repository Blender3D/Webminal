$(function() {
  $('.flash-message, .flash-error').each(function() {
    $(this).hide();
    
    $(this).addClass('notification');
    $(this).on('click', function() {
      $(this).slideUp('fast', function() { $(this).remove(); });
    });
    
    $(this).slideDown('fast');
    setTimeout(function() { $(this).trigger('click'); }, 5000);
  });
  
  if ($('body').hasClass('terminal')) {
    $('#terminal iframe').load(function() {
      $('#terminal iframe').get(0).contentWindow.document.keydown(function() {
        alert('a');
      });
    });
    
    function resizeTerminal(width) {
      if (($(document).width() - width > 300) && (width > 300)) {
        $('#terminal').width(width);
        $('#side').width($('body').innerWidth() - width - 40);
        $('body').css({paddingLeft: width});
      }
    }
    
    $(window).on('resize', function() {
      var $terminal = $('#terminal');
      
      $terminal.height($(this).height() - $terminal.outerHeight() + $terminal.height() - 4);
    }).trigger('resize');
    
    $('#terminal').append($('<div />').prop('id', 'splitter'));
    $('body').append($('<div />').prop('id', 'overlay').hide());
    
    $('#overlay').on('mousemove', function(e) {
      resizeTerminal(e.pageX);
    }).on('mouseup', function() {
      $(this).hide();
    });
    
    $('#splitter').on('mousedown', function() {
      $('#overlay').show();
    });
    
    resizeTerminal(301);
  }
});
