<?php

//encode and decode jwt token

function genToken($user_id){

  //ensures there's a secretKey active
  activateSecret();

  //creates header
  $header = base64_encode('{"alg": "HS256","typ": "JWT"}');

  //creates payload
  $payload = base64_encode('{"user_id": "'.$user_id.'"}');

  //creates signature
  $signature = base64_encode(hash_hmac('sha256', $header.'.'.$payload, $_SESSION['secret'], true));

  //create token
  $jwt = $header.'.'.$payload.'.'.$signature;

  //save token in cookies
  setcookie("RotatrLogin", $jwt, time() + (86400 * 30), "/");//1 day cookie


}

function validateToken(){

  //ensure secret is active
  activateSecret();

  //if the cookie exists
  if(isset($_COOKIE["RotatrLogin"]))
  {

    //save the jwt to an array
    $jwtArray=explode('.',$_COOKIE["RotatrLogin"]);

    //create signature based on token
    $jwtSignature = base64_encode(hash_hmac('sha256', $jwtArray[0].'.'.$jwtArray[1], $_SESSION['secret'], true));


    //if the signature is valid return true, else return false
    if($jwtSignature == $jwtArray[2])
    {
      return true;
    }else{
      return false;
    }
  
  }else{
  //if the cookie doesn't exist return false
  return false;
  }

}

function getToken(){

  //set return variable to null
  $token = null;

  if(isset($_COOKIE["RotatrLogin"]))
  {

    $jwtArray=explode('.',$_COOKIE["RotatrLogin"]);

    $token = json_decode($jwtArray[1]);

  }

  return $token;
}

function activateSecret(){

  //checks if there's a secret
  if(!isset($_SESSION['secret'])){

    //sets secret if there is none
    $_SESSION['secret']=random_bytes(32);
  }

}

?>
