$(document).ready(function() {
    // Cuando se hace clic en un botón del día...
    $(".segment-button").click(function() {
        // Obtiene el valor del día del botón
        var day = $(this).attr("data-value");

        // Realiza una solicitud AJAX a la vista 'index'
        $.ajax({
            url: '',  // Reemplaza esto con la ruta a tu vista 'index'
            data: {
                'day': day  // Envía el día como parámetro
            },
            dataType: 'json',
            success: function (data) {
                // Aquí debes actualizar tu HTML con las clases devueltas por la vista.
                // Esto dependerá de cómo quieras mostrar las clases.

                // Primero, vacía el contenido actual
                $(".content").empty();

                // Luego, para cada clase en los datos devueltos...
                $.each(data.clases, function(i, c) {
                    // Crea una nueva tarjeta de clase y añádela al contenido
                    var card = '<div class="card">' +
                               '<div class="card-content">' +
                               '<div class="color-line"></div>' +
                               '<div class="card-header">' +
                               '<h1 class="card-title">' + c.ramo + '</h1>' +
                               '<span class="label">' + c.bloque + '</span>' +
                               '<span class="label"><h5>' + c.seccion + '</h5></span>' +
                               '<span class="dias" style="display: none;">' + c.dias + '</span>' +
                               '</div></div></div>';
                    $(".content").append(card);
                });
            }
        });
    });
});

