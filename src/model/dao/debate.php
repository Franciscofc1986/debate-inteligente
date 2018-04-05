<?php 

class DebateDAO {

    public function salvarDebate($debate) {
        include 'comum/conectarBD.php';

        try {
            $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
            $sql = "INSERT INTO debate (debate_id, titulo_debate, descricao_debate, autor_id_debate, foto_debate) 
            VALUES (null, :titulo, :descricao, :autor, :foto)";

            $statement = $pdo->prepare($sql) or die ("Sem conexao com o servidor.");
            $statement->bindValue(":titulo",$debate->getTitulo());
            $statement->bindValue(":descricao",$debate->getDescricao());
            $statement->bindValue(":autor",$_SESSION['usuario_id']);
            $statement->bindValue(":foto",$debate->getFoto());
            $result = $statement->execute();
            $pdo = null;

            return $result;
        } 
        catch(PDOException $e)
        {
            $pdo = null;
            echo $sql . "<br>" . $e->getMessage();
        }
        
    }

    public function receberDebatesDoUsuario($usuarioId){
        include 'comum/conectarBD.php';

        // $query = "SELECT * FROM usuario WHERE email_usuario=:email AND senha_usuario=:senha";

        // $statement = $pdo->prepare($query) or die ("Sem conexao com o servidor.");
        // $statement->bindValue(":email",$email);
        // $statement->bindValue(":senha",$senha);
        // $statement->execute();

        // $result = $statement->fetch(\PDO::FETCH_ASSOC);
        // if($result)
        // {
        //     $_SESSION['usuario'] = $result['nome_usuario'];
        //     $_SESSION['email'] = $result['email_usuario'];
        //     $_SESSION['usuario_id'] = $result['usuario_id'];
        //     header('location:../index.php');
        // }
    }

    public function receberTodosDebates(){
        include 'comum/conectarBD.php';
        require_once 'model/debate.php';
        require_once 'model/usuario.php';

        $query = "SELECT * FROM debate, usuario where debate.autor_id_debate = usuario.usuario_id LIMIT 20";
        $statement = $pdo->prepare($query);
        $statement->execute();

        $result = $statement->fetchAll();
        $listaDebates = array();

        foreach( $result as $row ) {
            $debate = new Debate();
            $debate->setId($row['debate_id']);
            $debate->setTitulo($row['titulo_debate']);
            $debate->setDescricao($row['descricao_debate']);
            $debate->setDataCriacao($row['data_cadastro_debate']);
            $debate->setFoto($row['foto_debate']);

            $usuario = new Usuario();
            $usuario->setId($row['usuario_id']);
            $usuario->setNome($row['nome_usuario']);
            $usuario->setEmail($row['email_usuario']);
            $usuario->setTipo($row['tipo_usuario']);
            $usuario->setFoto($row['foto_usuario']);
            $usuario->setDataCadastro($row['data_cadastro_usuario']);
            $debate->setAutor($usuario);
            $listaDebates[] = $debate;
        }

        return $listaDebates;
    }
}

?>