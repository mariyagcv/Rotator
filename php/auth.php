<?php

//check if has valid cookie

require 'token.php';

//if the validateToken() returns false
if(!validateToken())
{
  header('Location: login.php');
}

?>
