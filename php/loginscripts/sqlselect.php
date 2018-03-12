<?php
//class to send sql select queries to database and return info


class database
{

  //function to get data from a table in the database

  //function returns an array of values

  function select($field,$table){
  
    //create the database connection object
    $dbobj = new mysqli("dbhost.cs.man.ac.uk","p34897st","databasepa5s","2017_comp10120_z8");

    //check if connection worked without errors, and cancel if there was
    if($dbobj -> connect_error) {
      die('Connect Error ('.$dbobj -> connect_errno.') '.$dbobj -> connect_error);
    }


    //sanitise inputs
    $field = $dbobj -> real_escape_string($field);
    $table = $dbobj -> real_escape_string($table);
    

    //set up array for retrieved outputs
    
    $row = null;

    //select values from table
    if($result = $dbobj -> query("SELECT ".$field." FROM ".$table)) {
      
      //save array of values to return
      $row = $result -> fetch_array(MYSQLI_NUM);

      $result -> close(); // Remember to release the result set
      $dbobj -> close(); //close db object
    }

    //return the values (or null) retrieved from select query
    return $row;

  }
}
?>
