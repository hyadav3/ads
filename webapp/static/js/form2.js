$(document).ready(function () {
    $("#form").submit(function (event) {
      var formData = {
		Age: $('#Age').val(),
		BloodPressure: $('#BloodPressure').val(),
		BMI: $('#BMI').val(),
		DiabetesPedigreeFunction: $('#DiabetesPedigreeFunction').val(),
		Glucose: $('#Glucose').val(),
		Insulin: $('#Insulin').val(),
		Pregnancies: $('#Pregnancies').val(),
		SkinThickness: $('#SkinThickness').val(),

      };
      
  
      $.ajax({
        type: "GET",
        url: "../predictor",
        data: formData,
        dataType: "json",
        encode: true,
      }).done(function (data) {
        console.log(data);
      });
  
      if (!data.success) {
        if (data.errors.Age) {
          $("#Age-group").addClass("has-error");
          $("#Age-group").append(
            '<div class="help-block">' + data.errors.Age + "</div>"
          );
        }

        if (data.errors.BloodPressure) {
          $("#BloodPressure-group").addClass("has-error");
          $("#BloodPressure-group").append(
            '<div class="help-block">' + data.errors.BloodPressure + "</div>"
          );
        }

        if (data.errors.BMI) {
          $("#BMI-group").addClass("has-error");
          $("#BMI-group").append(
            '<div class="help-block">' + data.errors.BMI + "</div>"
          );
        }
        if (data.errors.DiabetesPedigreeFunction) {
            $("#DiabetesPedigreeFunction-group").addClass("has-error");
            $("#DiabetesPedigreeFunction-group").append(
              '<div class="help-block">' + data.errors.DiabetesPedigreeFunction + "</div>"
            );
          }
          if (data.errors.Glucose) {
            $("#Glucose-group").addClass("has-error");
            $("#Glucose-group").append(
              '<div class="help-block">' + data.errors.Glucose + "</div>"
            );
          }
          if (data.errors.Insulin) {
            $("#Insulin-group").addClass("has-error");
            $("#Insulin-group").append(
              '<div class="help-block">' + data.errors.Insulin + "</div>"
            );
          }
          if (data.errors.Pregnancies) {
            $("#Pregnancies-group").addClass("has-error");
            $("#Pregnancies-group").append(
              '<div class="help-block">' + data.errors.Pregnancies + "</div>"
            );
          }
        if (data.errors.SkinThickness) {
                $("#SkinThickness-group").addClass("has-error");
                $("#SkinThickness-group").append(
                  '<div class="help-block">' + data.errors.SkinThickness + "</div>"
                );
          }

      } else {
        $("#results").html(
          '<div class="alert alert-success"> Your probability of diabetes is:' + data.message + "%.</div>"
        );
      }

    });

    event.preventDefault();
  });
