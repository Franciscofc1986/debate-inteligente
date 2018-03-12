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
    header('location:principal.php');
}
else{
    unset ($_SESSION['usuario']);
    header('location:index.html');
     
}
 
?>