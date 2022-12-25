class Car {
    private Integer id;
    public String license;
    public Account driver;
    protected Integer passenger;
    
    public Car(String license,Account driver){
        this.license=license;
        this.driver=driver;
    
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public Integer getPassenger(){
        return passenger;
    }
    
    public void setPassenger(Integer passenger){
        if(passenger==4){
         this.passenger=passenger;
        }else{
         System.out.println("Necesitas asignar 6 pasajeros");
        }  
    }
    

}

