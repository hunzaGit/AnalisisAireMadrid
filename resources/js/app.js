$(document).ready(function() {


    $.ajax({
        type: 'GET',
        url: 'https://s3.amazonaws.com/bucketcloud18/Datos+Proyecto/Tiempo_real/horario.json',
        dataType: 'json',
        success: function(data, textStatus, jqXHR) {

            const unidadMedida = '<span>µ/m³ NO<sub>2</sub></span>';


            console.log(data);


            Object.keys(data).forEach((idNum)=>{
                //$('#'+ id + 'p').text(parseFloat(data[id].valor))
                const id = '#'+ idNum + 'p';
                const valor = parseFloat(data[idNum].valor);
                console.log(id +' --> ' + valor);
                $(id).text(valor + ' ');
                $(id).append(unidadMedida)

                if(valor >= 60){
                    debugger;
                    console.log(true);
                    $('#'+ idNum).css('border-color','#F2350B');
                }
            });


            //$('#28079004p').text(parseFloat(data[28079004].valor) + ' ');
            //$('#28079004p').append(unidadMedida)
            //150 Mg/CO2




        },
        error: function(jqXHR, statusText, errorThrown) {
            alertify.error("Error al buscar datos en S3");
        }
    });


});