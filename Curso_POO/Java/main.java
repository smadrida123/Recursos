// Your First Program

class main {
    public static void main(String[] args) {
        System.out.println("Hello, World!"); 
        UberX uberx=new UberX("EZS32F",new Account("Oreo","OREO123")
        ,"Kia","2017");
        uberx.setPassenger(4);
        uberx.printDataCar();
        Driver driver=new Driver("OREOSITO","11112223444");
        driver.printData();
         //Polimorfismo con la variable passenger (distinta entre clases)
         UberVan uberVan=new UberVan("QWR123",new Account("SapoPa","123456"));
         uberVan.setPassenger(6);
         uberVan.printDataCar();


    }
}