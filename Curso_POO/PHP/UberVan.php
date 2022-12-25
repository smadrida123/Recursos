<?php
require_once("Car.php");
class UberVan extends Car {
    public $typeCarAccepted;
    public $seatsmaterial;

public function __construct($license,$driver,$typeCarAccepted,$seatsmaterial){
    parent::__construct($license,$driver);
    $this->typeCarAccepted=$typeCarAccepted;
    $this->seatsmaterial=$seatsmaterial;
}
public function setPassenger($passenger) {
    
    if ($passenger == 6) {
        $this->passenger = $passenger;
    }
    else {
        echo "Necesitas asignar 6 pasajeros ";
    }

}
public function printDataCar() {
    echo "
        Licencia: $this->license 
        Driver: {$this->driver->name} 
        Número de pasajeros: $this->passenger
        Tipo de carro aceptado: $this->typeCarAccepted";
}

}
?>