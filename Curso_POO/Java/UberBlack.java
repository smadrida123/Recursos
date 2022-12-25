import java.util.ArrayList;
import java.util.Map;

class UberBlack extends Car {
    Map<String, Map<String,Integer>> typeCarAccepted;
    ArrayList<String> seatsMaterial;
    private Integer passenger;

    public UberBlack(String license, Account driver,Map<String, Map<String,Integer>> typeCarAccepted,ArrayList<String> seatsMaterial){
        super(license, driver);
        this.typeCarAccepted=typeCarAccepted;
        this.seatsMaterial=seatsMaterial;
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
