class UberX extends Car {
    String brand;
    String model;
    private Integer passenger;

    public UberX(String license, Account driver,String brand,String model){
        super(license, driver);
        this.brand=brand;
        this.model=model;
    }

    void printDataCar() {
        if(passenger !=null){
            System.out.println("License: "+license+" Driver: "+driver.name + " Passenger: "+passenger); 
        }
        
    }

    public Integer getPassenger(){
        return passenger;
    }

    public void setPassenger(Integer passenger){
        if(passenger==4){
         this.passenger=passenger;
        }else{
         System.out.println("Necesitas asignar 4 pasajeros");
        }  
    }
}
