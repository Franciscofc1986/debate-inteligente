<?php 
include 'conectarBD.php';

$email = $_POST['email'];
$senha = $_POST['senha'];


$query = "SELECT * FROM usuario WHERE email_usuario=:email AND senha_usuario=:senha";

$statement = $pdo->prepare($query) or die ("Sem conexao com o servidor.");
$statement->bindValue(":email",$email);
$statement->bindValue(":senha",$senha);
$statement->execute();

$result = $statement->fetch(\PDO::FETCH_ASSOC);
if($result)
{
    $_SESSION['usuario'] = $result['nome_usuario'];
    $_SESSION['email'] = $result['email_usuario'];
    $_SESSION['usuario_id'] = $result['usuario_id'];
    header('location:../index.php');
}
else{
    unset ($_SESSION['usuario']);
    unset ($_SESSION['email']);
    unset ($_SESSION['usuario_id']);
    header('location:../logar.php');
     
}

?>