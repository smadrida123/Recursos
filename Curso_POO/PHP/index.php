<?php
require_once("Car.php");
require_once("Account.php");
require_once("UberX.php");
require_once("UberPool.php");
require_once("User.php");
require_once("Driver.php");
require_once("UberVan.php");


$uberX1=new UberX("EZS32F",new Account("OREO","1053869189","smadrida","123456789"),"AUDI","Cualquiera");
$uberX1->printDataCar();
$uberPool1=new UberPool("ABC123",new Account("OREO2","1111111","santiago","1111"),"Suzuki","Cualquiera");
$uberPool1->printDataCar();
$user1=new User("OREO2","123456789","oreo@hotmail.com","lallal");
$user1->printData();
$uberVan = new UberVan("OJL395", new Account("Raúl Ramírez", "AND456","sma","1233456"), "Nissan", "Versa");
$uberVan->setPassenger(4);
$uberVan->printDataCar();


?>