$(document).ready(function() {
    $('#form').on('submit',function(e){
      $.ajax({
        data : {
          firstname : $('#firstname').val(),
          lastname : $('#lastname').val(),
        },
        type : 'POST',
        url : '/'
      })
      .done(function(data){
        $('#output').text(data.output).show();
        alert(hi);
      });
      e.preventDefault();
    });
  });