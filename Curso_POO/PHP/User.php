<?php
require_once("Account.php");
class User extends Account {

public function __construct($name,$document,$email,$password){
    parent::__construct($name,$document,$email,$password);

}
public function printData(){
    echo "Name: $this->name,
    Document: $this->document,
    Email: $this->email";
}
}

?>