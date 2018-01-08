$(document).ready(function() {


    $.ajax({
        type: 'GET',
        url: 'https://s3.amazonaws.com/bucketcloud18/Datos+Proyecto/Tiempo_real/horario.json',
        dataType: 'json',
        success: function(data, textStatus, jqXHR) {


            console.log(data);

            console.log(parseFloat(data[28079004].valor));

            console.log($('#28079004p'))
            $('#28079004p').text(parseFloat(data[28079004].valor) + ' Mg/CO2')
            //150 Mg/CO2


        },
        error: function(jqXHR, statusText, errorThrown) {
            alertify.error("Error al buscar datos en S3");
        }
    });


});