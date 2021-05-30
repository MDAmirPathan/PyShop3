<?php
$con=mysql_connect("localhost","peter","abc123");
if(!$con)
{
    die('Could not connect to Server'.mysql_error());
}

mysql_select_db("my_db",$con);

$sql="INSERT INTO ABC (Fname,Phone,Age) VALUES('$_POST[contactname]','$_POST[phone]','$_POST[address]')";


if(!mysql_query($sql,$con))
{
    die('Error:'.mysql_error());
}

mysql_close($con);

echo"Page is Working";
?>