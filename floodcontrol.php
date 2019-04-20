<?php
	header("Location: http://amorginos.ddns.net");
	system("gpio write 29 1");
	sleep(1); 
	system("gpio write 29 0");
	sleep(2); 
	system("gpio write 29 1");
	sleep(1);
	system("gpio write 29 0")   
?>
