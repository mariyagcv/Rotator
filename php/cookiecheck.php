<?php

//checks if cookies are enabled
function cookiesEnabled(){

  //attemtpts to set a cookie
  setcookie("test_cookie", "test", time() + 3600, '/');

  $cookiesEnabled = false;

  //returns true if there is more than one cookie and false if there isn't
  if(count($_COOKIE) > 0) {
    $cookiesEnabled = true;
  } else {
    $cookiesEnabled = false;
  }

  return $cookiesEnbaled;

}

?>
