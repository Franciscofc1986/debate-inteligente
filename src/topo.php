<?php 
    session_start();
    $logado = false;
    $usuario_logado = "";
    if(!isset ($_SESSION['usuario']) == true)
    {
        unset($_SESSION['usuario']);
    }else{
        $logado = true;
        $usuario_logado = $_SESSION['usuario'];
    }
    
    echo '<!DOCTYPE html>
        <html lang="pt-BR">
        <head>
        <meta charset="utf-8">
        <title >Tem Lógica</title>
        <!--Import Google Icon Font-->
        <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
        <!--Import materialize.css-->
        <link type="text/css" rel="stylesheet" href="css/materialize.min.css"  media="screen,projection"/>
        <link type="text/css" rel="stylesheet" href="css/style.css"/>
        <!--Let browser know website is optimized for mobile-->
        <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
        </head>

        <body>
        <header>';
    include_once 'barra_topo.php';
    echo '</header>';
?>