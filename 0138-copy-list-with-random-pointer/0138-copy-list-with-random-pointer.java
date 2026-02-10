/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {
        Map<Node, Node> existing = new HashMap<>();
        existing.put(null, null);
        Node dummy = new Node(0);
        Node curr = dummy;
        while (head != null) {
            curr.next = getOrCreateNode(existing, head);
            curr = curr.next;
            existing.put(head, curr);
            curr.random = getOrCreateNode(existing, head.random);
            existing.put(head.random, curr.random);
            head = head.next;
        }
        return dummy.next;
    }

    private Node getOrCreateNode(Map<Node, Node> existing, Node key) {
        if (existing.containsKey(key)) {
            return existing.get(key);
        }
        return new Node(key.val);
    }
}