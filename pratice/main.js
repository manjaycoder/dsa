class Node{
    constructor(value){
        this.head=value
        this.tail=null
    }

}
class Linked_list{
    constructor(value){
        this.head=new Node(value)
        this.tail=this.head
        this.length=1
    }
}
const myLinked=new Linked_list(1)
console.log(myLinked)