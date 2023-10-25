$(document).ready(function() {
    var table = $('.tabla table');
    table.on('click', 'tr', function() {
        var target = $(this);
        $('tr', table).removeClass('selected');
        target.addClass('selected');

        var estado = target.find('.estado').data(); // Obtiene el valor del estado de la fila seleccionada
        console.log(estado);

        if (estado) {
            $('.boton .botonqr').addClass('botonDeshabilitado'); // Deshabilita el botón QR si estado es true
            $('.boton .botonreporte').removeClass('botonDeshabilitado'); // Deshabilita el botón QR si estado es true
        } else {
            $('.boton .botonqr').removeClass('botonDeshabilitado'); // Habilita el botón QR si estado es false
            $('.boton .botonreporte').addClass('botonDeshabilitado'); // Deshabilita el botón QR si estado es true
        }
    });
});

