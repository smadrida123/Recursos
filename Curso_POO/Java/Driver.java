class Driver extends Account {
    public Driver(
    String name,
    String document){
    super(name,document);
    }
    void printData() {
        System.out.println(name+document);
    }
}
