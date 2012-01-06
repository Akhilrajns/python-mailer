<?php
/* CONNECTION VARIABLES */
$db_hostname = "127.0.0.1"; // Usually "127.0.0.1"
$db_username = "root";
$db_password = "";
$db_name = "demo_dk";

$conn = mysql_connect($db_hostname, $db_username, $db_password);
if($conn){
  mysql_select_db($db_name, $conn);
 echo "Hai Success veendum";
}
else{ die(mysql_error());}
?>

<?php header('Location: http://myapptest.localhost/home.php')?>
