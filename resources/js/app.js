const estaciones = {
    28079004: {
        nombre: "Plaza de España",
        nivelNO2: {
            valor: -1,
            hora: ""
        },
        posisMap: {
            top: "63",
            left: "48.6"
        }
    },
    28079008: {nombre: "Escuelas Aguirre", nivelNO2: {valor: -1, hora: ""}, posisMap: {top: "63.4", left: "51.2"}},
    28079011: {nombre: "Avda. Ramón y Cajal", nivelNO2: {valor: -1, hora: ""}, posisMap: {top: "55.5", left: "52.2"}},

    28079016: {nombre: "Arturo Soria", nivelNO2: {valor: -1, hora: ""}, posisMap: {top: "59", left: "57"}},
    28079017: {nombre: "Villaverde", nivelNO2: {valor: -1, hora: ""}, posisMap: {top: "81.5", left: "48.4"}},
    28079018: {nombre: "Farolillo", nivelNO2: {valor: -1, hora: ""}, posisMap: {top: "69.6", left: "46.7"}},

    28079024: {nombre: "Casa de Campo", nivelNO2: {valor: -1, hora: ""}, posisMap: {top: "63.5", left: "45"}},
    28079027: {nombre: "Barajas Pueblo", nivelNO2: {valor: -1, hora: ""}, posisMap: {top: "49.3", left: "61.4"}},
    28079035: {nombre: "Pza. del Carmen", nivelNO2: {valor: -1, hora: ""}, posisMap: {top: "64", left: "49.5"}},

    28079036: {nombre: "Moratalaz", nivelNO2: {valor: -1, hora: ""}, posisMap: {top: "67", left: "55.3"}},
    28079038: {nombre: "Cuatro Caminos", nivelNO2: {valor: -1, hora: ""}, posisMap: {top: "57.5", left: "49"}},
    28079039: {nombre: "Barrio del Pilar", nivelNO2: {valor: -1, hora: ""}, posisMap: {top: "49", left: "48.8"}},

    28079040: {nombre: "Vallecas", nivelNO2: {valor: -1, hora: ""}, posisMap: {top: "71.7", left: "54.6"}},
    28079047: {nombre: "Mendez Álvaro", nivelNO2: {valor: -1, hora: ""}, posisMap: {top: "69", left: "51.2"}},
    28079048: {nombre: "Castellana", nivelNO2: {valor: -1, hora: ""}, posisMap: {top: "58.5", left: "51"}},

    28079049: {nombre: "Parque del Retiro", nivelNO2: {valor: -1, hora: ""}, posisMap: {top: "65.4", left: "51.5"}},
    28079050: {nombre: "Plaza Castilla", nivelNO2: {valor: -1, hora: ""}, posisMap: {top: "52", left: "50.8"}},
    28079054: {nombre: "Ensanche de Vallecas", nivelNO2: {valor: -1, hora: ""}, posisMap: {top: "75.2", left: "58.6"}},

    28079055: {nombre: "Urb. Embajada", nivelNO2: {valor: -1, hora: ""}, posisMap: {top: "53", left: "61.6"}},
    28079056: {
        nombre: "Pza. Fernández Ladreda",
        nivelNO2: {valor: -1, hora: ""},
        posisMap: {top: "72.5", left: "47.5"}
    },
    28079057: {nombre: "Sanchinarro", nivelNO2: {valor: -1, hora: ""}, posisMap: {top: "45", left: "53.8"}},

    28079058: {nombre: "El Pardo", nivelNO2: {valor: -1, hora: ""}, posisMap: {top: "39.3", left: "42.7"}},
    28079059: {nombre: "Juan Carlos I", nivelNO2: {valor: -1, hora: ""}, posisMap: {top: "52.6", left: "58.9"}},
    28079060: {nombre: "Tres Olivos", nivelNO2: {valor: -1, hora: ""}, posisMap: {top: "43.5", left: "51"}}
}


$(document).ready(function () {

    $('#datosMetereologicos')
        .css('width', '300px')
        .css('height', 'auto'); //115px

    $('#leyenda')
        .css('width', '300px')
        .css('height', 'auto'); //175px

    $.ajax({
        type: 'GET',
        url: 'https://s3.amazonaws.com/bucketcloud18/Datos+Proyecto/Tiempo_real/horario.json',
        dataType: 'json',
        success: function (data, textStatus, jqXHR) {

            const valorTopVerde = 100,
                valorTopAmarillo = 160,
                valorTopNaranja = 180;

            /*Object.keys(data).forEach((id) => {
                console.log(id + ':{ nombre: "", nivelNO2: {    valor: -1, hora: "" }, posisMap:    { top:"", left     : ""            }},')
            });*/

            Object.keys(data).forEach((idNum) => {

                const valor = parseFloat(data[idNum].valor);
                estaciones[idNum].nivelNO2.valor = valor;
                estaciones[idNum].nivelNO2.hora = data[idNum].hora;


                crearHTMLPuntoEstacion(idNum, estaciones[idNum], (html) => {

                    $('.interactive-map').after(html);

                    if (valor <= valorTopVerde) { // [...,100]
                        $('#' + idNum).css('border-color', '#00f263');
                    } else if (valor > valorTopVerde && valor <= valorTopAmarillo) { // (100, 160]
                        $('#' + idNum).css('border-color', '#f2c931');
                    } else if (valor > valorTopAmarillo && valor <= valorTopNaranja) { // (160,180]
                        $('#' + idNum).css('border-color', '#f26c00');
                    } else if (valor > valorTopNaranja) { // [160, ...]
                        $('#' + idNum).css('border-color', '#FA0001');
                    }
                });

            });

            $.ajax({
                type: 'GET',
                url: 'https://s3.amazonaws.com/bucketcloud18/Datos+Proyecto/Tiempo_real/fechaActualizacion.json',
                dataType: 'json',
                success: function (horaUpdate, textStatus, jqXHR) {

                    if(horaUpdate){
                        $('#fechaActualizacion').append(horaUpdate.dia);
                        $('#horaActualizacion').append(horaUpdate.hora);
                    }else{
                        $('#fechaActualizacion').append('-');
                        $('#horaActualizacion').append('-');
                    }

                },
                error: function (jqXHR, statusText, errorThrown) {
                    console.error("Error al buscar hora actualizacion en S3");
                }
            });


        },
        error:

            function (jqXHR, statusText, errorThrown) {
                console.error("Error al buscar datos en S3");
            }
    });

    //http://api.openweathermap.org/data/2.5/weather?q=London,uk&appid=da800b2b6787ebdc3b4a4ce7422f48a8

    $.ajax({
        //url: "http://api.openweathermap.org/data/2.5/weather?q=Madrid&lang=es&units=metric&appid=da800b2b6787ebdc3b4a4ce7422f48a8",
        url: "https://api.openweathermap.org/data/2.5/weather?q=Madrid,es&lang=es&units=metric&appid=da800b2b6787ebdc3b4a4ce7422f48a8",
        method: "GET",
        success: function (data, textStatus, jqXHR) {

            console.log('*** actual **************');

            //console.log('RESPUESTA: ');
            console.log(data);


            $('#EstadoCielo').text("Estado del cielo: "/* + data.weather[0].description*/);
            if(data.weather[0].icon)
                $('#EstadoCielo').after("<img src='http://openweathermap.org/img/w/"+data.weather[0].icon +".png' style='margin: -15px 0;' title='"+data.weather[0].description +"'>");
            else
                $('#EstadoCielo').after(data.weather[0].description);
            $('#viento').text("Viento: " + data.wind.speed + "m/s " + convertDir(data.wind.deg));
            //$('#dirViento').text("Dir. viento: " );
            $('#temperatura').text("Temperatura: " + data.main.temp + "ºC");


            const fechaMET = convertTimestamp(data.dt);
            if(data.dt) {
                $('#fechaActuMet').append(fechaMET.dia);
                $('#horaActuMet').append(fechaMET.hora);
            }else{
                $('#fechaActuMet').append('-');
                $('#horaActuMet').append('-');
            }


        },
        error: function (jqXHR, statusText, errorThrown) {
            console.log("Error en AEMET");
        }
    });



    $.ajax({
        //url: "http://api.openweathermap.org/data/2.5/weather?q=Madrid&lang=es&units=metric&appid=da800b2b6787ebdc3b4a4ce7422f48a8",
        url: "https://api.openweathermap.org/data/2.5/forecast?q=Madrid,es&lang=es&units=metric&cnt=2&appid=da800b2b6787ebdc3b4a4ce7422f48a8",
        method: "GET",
        success: function (data, textStatus, jqXHR) {
            console.log('*** prediccion **************');

            //console.log('RESPUESTA: ');
            console.dir(data);


            if(data.list[0].rain['3h']){
               $('#predicLluvia').text('Precipitaciones: '+data.list[0].rain['3h'] + 'mm');
            }else{
                $('#predicLluvia').text('Precipitaciones: No se preveen');
            }


            //console.log();

        },
        error: function (jqXHR, statusText, errorThrown) {
            console.log("Error en openweathermap");
        }
    });


});


function crearHTMLPuntoEstacion(id, infoEstacion, callback = Function()) {

    let html = '<button id=' + id.toString() + ' class="map-point" style="top:' + infoEstacion.posisMap.top + '%;left:' + infoEstacion.posisMap.left + '%">' +
        '<div class="content">' +
        '<div class="">' +
        '<h3 class="titulo-content">' + infoEstacion.nombre + '</h3>' +
        '<div class="middle-line" ></div>' +
        '<p id="' + id.toString() + 'p" class="info-content"><strong>' + infoEstacion.nivelNO2.valor + '</strong><span> µg/m³ NO<sub>2</sub></span></p>' +
        '</div>' +
        '</div>' +
        '</button>'

    callback(html);
}


function convertDir (deg){
    let val = '';
    if(deg >=337.5 && deg <= 22.5) val = 'Norte';
    if(deg <=337.5 && deg >= 292.5) val = 'Noroeste';
    if(deg <=292.5 && deg >= 247.5) val = 'Oeste';
    if(deg <=247.5 && deg >= 202.5) val = 'Suroeste';
    if(deg <=202.5 && deg >= 157.5) val = 'Sur';
    if(deg <=157.5 && deg >= 112.5) val = 'Sureste';
    if(deg <=112.5 && deg >= 67.5) val = 'Este';
    if(deg <=67.5 && deg >= 22.5) val = 'Noreste';
    return val;
}


function convertTimestamp(timestamp) {
    var d = new Date(timestamp * 1000),	// Convert the passed timestamp to milliseconds
        yyyy = d.getFullYear(),
        mm = ('0' + (d.getMonth() + 1)).slice(-2),	// Months are zero based. Add leading 0.
        dd = ('0' + d.getDate()).slice(-2),			// Add leading 0.
        hh = d.getHours(),
        h = hh,
        min = ('0' + d.getMinutes()).slice(-2),		// Add leading 0.
        ampm = 'AM',
        time;

    if (hh > 12) {
        h = hh - 12;
        ampm = 'PM';
    } else if (hh === 12) {
        h = 12;
        ampm = 'PM';
    } else if (hh == 0) {
        h = 12;
    }

    // ie: 20/01/2018, 14:35
    time = {
        dia:dd + '/' + mm + '/' + yyyy,
        hora: hh + ':' + min
    }

    return time;
}