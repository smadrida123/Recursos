function Account(name,document) {
    this.id;
    this.name=name;
    this.document=document;
    this.email;
    this.password;

    Account.prototype.printData=function(){
        console.log(this.name)
        console.log(this.document)
}
}