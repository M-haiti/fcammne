(function ($) {
  function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != "") {
      var cookies = document.cookie.split(";");
      for (var i = 0; i < cookies.length; i++) {
        var cookie = $.trim(cookies[i]);
        if (cookie.substring(0, name.length + 1) == name + "=") {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    //RETORNANDO EL TOKEN
    return cookieValue;
  } //end function getCookie
  function generarCodigo() {
    console.log("Generar Codigo 2");

    $(".field-pais select").change(function () {
      console.log("Generar Codigo 3");
      let count = "";
      let url = "/countcopartepais/";
      let paiscode = "";
      paiscode = $(this).val();
      url += paiscode;

      console.log("url", url);

      let csrftoken = getCookie("csrftoken");

      $.ajax({
        type: "POST",
        url: url,
        data: {
          csrfmiddlewaretoken: csrftoken,
        },
        success: function (data) {
          count = parseInt(data);
          count++;
          codigoOrg = paiscode + "-" + count;
          $(".field-codigo_org input").val(codigoOrg);
        },
        error: function (jqXHR, textStatus, errorThrown) {
          if (jqXHR.status === 0) {
            alert(
              "Error al intentar Conectarse: Verifique su conexion a Internet."
            );
          } else if (jqXHR.status == 404) {
            alert("La Pagina solicitada no fue encontrada [404]");
          } else if (jqXHR.status == 500) {
            alert("Erro Interno [500]");
          } else if (textStatus === "parsererror") {
            alert("Error en el retorno de Datos. [parseJson]");
          } else if (textStatus === "timeout") {
            alert("Tiempo de Espera agotado");
          } else if (textStatus === "abort") {
            alert("Solicitud Abortada. [Ajax Request]");
          } else {
            alert("Error desconocido: " + jqXHR.responseText);
          } //end if
        }, //end error
      });
    });
  }
  $(document).ready(function () {
    console.log("Coparte Create");
    $('.field-codigo_org input' ).prop( 'disabled', true );
    $('[id^=id_programa-comment]').prop( 'disabled', true );
    
    generarCodigo();

    if ($('.errornote').length ) {
      $('.field-pais select').trigger('change');
    }
    $('.submit-row input').click(function(){
      console.log('remove disabled!')
      $('.field-codigo_org input' ).prop( 'disabled', false );
      $('[id^=id_programa-comment]').prop( 'disabled', false );
    })
  });
})(django.jQuery);
