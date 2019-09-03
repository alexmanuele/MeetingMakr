$(function (){
  $(".js-generate").click(function (){
    jQuery.ajax({
      url: '/choose/select/',
      type: 'get',
      dataType: 'json',
      beforeSend: function() {
        $("#uploadModal").modal("show");
      },
      success: function (data) {
        console.log(data.person);
        $("#uploadModal .modal-content").html(data.html_modal);
      }

    });
  });
  $(".js-form-load").click(function () {
    console.log("Sanity check");
    var btn = $(this);
    jQuery.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#editModal").modal("show");
      },
      success: function (data) {
        $("#editModal .modal-content").html(data.html_form);
      }
    });
  });
  $(".js-form-submit").click(function () {
    var btn = $(this);
    console.log('submit check');
    jQuery.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          //$("#person-list").html(data.html_person_list);
          $("#editModal").modal("hide");
        }
        else {
          $("editModal .modal-content").html(data.html_form);
        }
      }
    })
  });
  $(".js-create-member-form").click(function(){
    var btn = $(this);
    console.log('create check');
    jQuery.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function() {
        $("#editModal").modal("show");
      },
      success: function(data){
        $("#editModal .modal-content").html(data.html_form);
      }
    })
  });


});
