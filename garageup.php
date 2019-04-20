<?php
	header("Location: http://amorginos.ddns.net"); 
	system("gpio write 29 1");
	sleep(15); 
	system("gpio write 29 0"); 
	exit();
?>
