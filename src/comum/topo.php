<?php 
require_once 'model/usuario.php';

    $usuario = new Usuario();
    $logado = $usuario->verificarSessao();
    $usuario_logado = "";
    $email_usuario = "";

    if($logado)
    {
        $usuario_logado = $_SESSION['usuario'];
        $email_usuario = $_SESSION['email'];

        $filename_foto = 'img/usuario/'.$_SESSION['foto'];

        if (!file_exists($filename_foto)) {
            $filename_foto = "img/default.jpg";
        }
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
    include_once 'comum/barra_topo.php';
    echo '</header>';
?>