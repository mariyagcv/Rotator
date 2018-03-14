<!DOCTYPE html>
<html>
<!-- imports main font -->
<link href="https://fonts.googleapis.com/css?family=Open+Sans&amp;subset=cyrillic-ext" rel="stylesheet">   <meta charset="UTF-8">
  <link rel="stylesheet" href="styles.css">
<title>RotatoR</title>
</head>
<body class = "inside">
  <div class = "centeredTimeTable">

  <h1>YOUR SCHEDULE</h1> <!-- WHY ISJN'T ROTATOR RESPONSIVE !??? -->

  <?php include 'menu2.php'; ?>
<!-- BTW TIMETABLE IS NOT YET RESPONSIVE AND LOOKS SHIT ON PHONES
     BUT TRY TO FIX LATER ON -->

  <table>
  <tr>
    <th class = "weekDays">Weekday</th>
    <th class = "weekDays">Task1</th>
    <th class = "weekDays">Task2</th>
  </tr>

  <tr>
    <td class = "weekDays">Monday</td>
    <td class = "task">Task1</td>
    <td class = "noTask">No task</td>
  </tr>
  <tr>
    <td class = "weekDays">Tuesday</td>
    <td class = "noTask">No task</td>
    <td class = "task">Task2</td>
  </tr>
  <tr>
    <td class = "weekDays">Wednesday</td>
    <td class = "task">Task1</td>
    <td class = "task">Task2</td>
  </tr>
  <tr>
    <td class = "weekDays">Thursday</td>
    <td class = "noTask">No task</td>
    <td class = "noTask">No task</td>
  </tr>
  <tr>
    <td class = "weekDays">Friday</td>
    <td class = "task">Task1</td>
    <td class = "task">Task2</td>
  </tr>
  <tr>
    <td class = "weekDays">Saturday</td>
    <td class = "task">Task1</td>
    <td class = "task">Task2</td>
  </tr>
  <tr>
    <td class = "weekDays">Sunday</td>
    <td class = "task">Task1</td>
    <td class = "task">Task2</td>
  </tr>

  </table>



</div>
</body>
</html>
