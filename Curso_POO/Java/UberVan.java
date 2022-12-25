import java.util.ArrayList;
import java.util.Map;

class UberVan extends Car {
    Map<String, Map<String,Integer>> typeCarAccepted;
    ArrayList<String> seatsMaterial; Integer passenger;

    public UberVan(String license, Account driver){
        super(license, driver);
    
    }

    
    
    void printDataCar() {
        if(passenger !=null){
            System.out.println("License: "+license+" Driver: "+driver.name + " Passenger: "+passenger); 
        }
        
    }
    public void setPassenger(Integer passenger){
        if(passenger==6){
         this.passenger=passenger;
        }else{
         System.out.println("Necesitas asignar 6 pasajeros");
        }  
    }
    
   
   
   
   
   
    public Integer getPassenger(){
        return passenger;
    }
    
}