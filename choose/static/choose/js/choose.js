/*
$(function (){
  $(".js-generate").click(function (){
    var btn = $(this);
    jQuery.ajax({
      url: btn.attr("data-url"),
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
    alert("CLICK");
    console.log('submit check');
    jQuery.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          alert("This here right here");
          $("#person-list").html(data.html_person_list);
          $("#editModal").modal("hide");
        }
        else {
          alert("no it was this one");
          $("editModal .modal-content").html(data.html_form);
        }
      }
    })
  });
  $(".js-create-member-form").click(function(){
    var btn = $(this);
    alert('create check');
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
*/
$(function (){
  var generate = function () {
    var btn = $(this);
    jQuery.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function() {
        $("#uploadModal .modal-content").html("");
        $("#uploadModal").modal("show");
      },
      success: function (data) {
        console.log(data.person);
        $("#uploadModal .modal-content").html(data.html_modal);
      }
    });
  };
  var loadForm = function () {
    console.log("Sanity check");
    var btn = $(this);
    jQuery.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#editModal .modal-content").html("");
        $("#editModal").modal("show");
      },
      success: function (data) {
        $("#editModal .modal-content").html(data.html_form);
      }
    });
  };
  var submitForm = function () {
    var form = $(this);
    jQuery.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#person-list").html(data.html_person_list);
          $("#editModal .modal-content").html("");
          $("#editModal").modal("hide");
        }
        else {
          $("editModal .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };
  //Binding
  /*
  $(".js-generate").click(generate);
  $(".js-form-load").click(loadForm);
  */
  $("#editModal").on("submit", ".js-person-update", submitForm);
  $("#editModal").on("submit", ".js-person-create", submitForm);

  $(document).on('click', '.js-generate', generate);
  $(document).on('click', '.js-form-load', loadForm);



});
