//menu lateral
$('.menu-1').sideNav({
    menuWidth: 300, // Default is 300
    edge: 'left', // Choose the horizontal origin
    closeOnClick: true, // Closes side-nav on <a> clicks, useful for Angular/Meteor
    draggable: true, // Choose whether you can drag to open on touch screens,
    onOpen: function(el) { /* Do Stuff*/ }, // A function to be called when sideNav is opened
    onClose: function(el) { /* Do Stuff*/ }, // A function to be called when sideNav is closed
});

$('.menu-2').sideNav({
    menuWidth: 300, // Default is 300
    edge: 'right', // Choose the horizontal origin
    closeOnClick: true, // Closes side-nav on <a> clicks, useful for Angular/Meteor
    draggable: true, // Choose whether you can drag to open on touch screens,
    onOpen: function(el) { /* Do Stuff*/ }, // A function to be called when sideNav is opened
    onClose: function(el) { /* Do Stuff*/ }, // A function to be called when sideNav is closed
});


$(document).ready(function(){

    $('#myLink').click(function(){ 
        $('.fixed-action-btn.toolbar').openToolbar(); //abrir caixa de edição
        return false; // não expande o item(argumento, ideia, premissa)
     });

    $('.myLink').click(function(){ 
        $('.fixed-action-btn.toolbar').openToolbar(); //abrir caixa de edição
    
        $("#elementoID").val(event.target.id);
        var bla = $("#elementoID").val();
        return false; // não expande o item(argumento, ideia, premissa)
    });

    $('.modal').modal();

    $('.tooltipped').tooltip();

    $('#textarea1').val('Abrir caixa de edição. Abrir caixa de edição. Abrir caixa de edição. Abrir caixa de edição.');

    $('select').formSelect();
});



