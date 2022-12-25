class User extends Account {
    constructor(name,document){
        super(name,document)

        User.prototype.printData1=function(){
            console.log(this.name)
            console.log(this.document)
    }
}
}