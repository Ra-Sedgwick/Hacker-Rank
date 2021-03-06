/*
Detect a cycle in a linked list. Note that the head pointer may be 'null' if the list is empty.

A Node is defined as: 
    class Node {
        int data;
        Node next;
    }
*/

boolean hasCycle(Node head) {

    // Case: Empty list.
    if (head == null) {
        return false;
    }
    
    // Floyd's cycle-finding algorithm
    
    Node fast = head;
    Node slow = head;
    
   
    while ((fast != null) && (fast.next != null)) {
        
        fast = fast.next.next;
        slow = slow.next;
        
        if (slow.equals(fast)) {
            return true;
        }
    }
    
    return false;
}
