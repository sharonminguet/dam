<?php
   
    mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
    $mysqli = mysqli_connect("localhost", "shertech_database", "shertech_database", "shertech_database");
    $query = "
            SELECT
            usuario
            FROM usuarios
            WHERE usuario = '".$_POST['usuario']."' 
            AND contrasena = '".$_POST['contrasena']."'
    ";                                                  //Compruebo si existe el usuario enviado existe en la bbdd
    $result = mysqli_query($mysqli, $query);            //Ejecute la petición contra base de datos 
    if ($row = mysqli_fetch_assoc($result)) {           //En casomde existir
            $row['resultado'] = 'ok';                   //Le añado una propiedad resultado y digo que es 'ok'
        echo json_encode($row);                         //Le añado el resto de información de la bbdd
    }else{                                              //en caso de que no exista
        
        echo '{"resultado:":"error"}';                  //devuelvo al cliente un 'error'
    }
        
?>


