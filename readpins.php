<?php
	header("Location: http://amorginos.ddns.net");
	system("gpio write 29 1");
	sleep(.5); 
	system("gpio write 29 0");
	sleep(.5); 
	system("gpio write 29 1");
	sleep(.25);
	system("gpio write 29 0")   
?>
