<?php
if(isset($_GET['s'])){
$u=$_GET['u']	;
$p=$_GET['p'];
echo shell_exec('python a1.py'.$u.$p);
}

?>
<!DOCTYPE html>
<html>
<head>
	<title>my</title>
</head>
<body>
<form name ="a">
	u<input type="text" name="u">
	p<input type="text" name="p">
    <input type="submit" name="s">
 </form>
</body>
</html>