<html>
<?php
	$value = $argv[1]
	setcookie("Rotator",$value,time() + (60*30), "/");
?>
</html>
