<?php
echo '<link rel="stylesheet" href="menuStyle.css">';
echo '<div id="mySidenav" class="sidenav">';
echo '  <a href="javascript:void(0)" class="closebtn" onclick="closeNav()">&times;</a>';
echo '  <a href="timetable.php">Timetable</a>';
echo ' <a href="newsfeed.php">Newsfeed</a>';
echo ' <a href="settings.php">Settings</a>';
echo ' <a href="about.php">About</a>';
echo '</div>';
echo ' <script src="menuScript.js"></script> ';
echo '<div id="rest">';
echo ' <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">';
echo ' <span onclick="openNav()">';
echo '  <div class="menu-icon">';
echo '   <a href="#" class="btn"><i class="fa fa-bars"></i></a>';
echo '  </div>';
echo ' </span>';

?>
