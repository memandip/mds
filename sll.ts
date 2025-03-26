class LinkedListNode<T> {
    value: T;
    next: LinkedListNode<T> | null;

    constructor(value: T){
        this.value = value;
        this.next = null;
    }
}

class SinglyLinkedList<T> {

    head: LinkedListNode<T>;

    insertNode(data: T){
        if(!this.head) {
            this.head = new LinkedListNode(data);
            return this.head;
        }
        
        let current = this.head;
        while(current.next){
            current = current.next;
        }

        current.next = new LinkedListNode(data);

        return current;
    }

    deleteNode(){

    }


}

const sll = new SinglyLinkedList();
sll.insertNode(1);
sll.insertNode(2);
sll.insertNode(3);

let currentNode = sll.head;
while(currentNode.next){
    console.log(currentNode.value);
    currentNode = currentNode.next;
}
console.log(currentNode.value);
