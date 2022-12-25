<?php
require_once("Account.php");
class Car {
public $id=integer;
public $license=string;
public $driver=string;
protected $passenger=integer;

public function __construct($license,$driver){
    $this->license=$license;
    $this->driver=$driver;
}
public function printDataCar(){
    echo "license: $this->license,
    conductor:.{$this->driver->name},
    document:{$this->driver->document}";
}

public function getPassenger() {
    return $this->passenger;
}

public function setPassenger($passenger) {
        
    if ($passenger == 4) {
        $this->passenger = $passenger;
    }
    else {
        echo "Necesitas asignar 4 pasajeros";
    }

}
}