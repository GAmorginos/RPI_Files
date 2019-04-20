<?php 
	header("Location: http://amorginos.ddns.net"); 
	system("sudo python /var/www/test.py"); 
	system("gpio write 16 1"); 
	exit();
?>
