<?php

include 'loginscripts/sqlselect.php';
include 'loginscripts/hash.php';


//retrieves username and password from the form entered
$username = $_POST["uname"];
$password = $_POST["password"];

//converts password to hashed version for database comparison
$password = pwHash($password);

//make a database object and use it to get password
$db = new Database;

//get the password for the username given
$realPasswod = $db -> select()

?>
