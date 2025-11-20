#include <iostream>
using namespace std;

// Node class representing a single element in the linked list
class Node {
public:
    int Value;
    Node* Next;
};

// Function to print the linked list
void printList(Node* n) {
    while (n != NULL) {
        cout << n->Value << " -> ";
        n = n->Next;
    }
    cout << "NULL" << endl;
}

// Insert a new node at the beginning (Head) of the list
// We use Node** (pointer to pointer) because we need to modify the actual head pointer
void insertAtTheFront(Node** head, int newValue) {
    // 1. Prepare a new node
    Node* newNode = new Node();
    newNode->Value = newValue;
    
    // 2. Link the new node to the current head
    newNode->Next = *head;

    // 3. Move the head to point to the new node
    *head = newNode;
}

// Insert a new node at the end of the list
void insertAtTheEnd(Node** head, int newValue) {
    // 1. Prepare the new node
    Node* newNode = new Node();
    newNode->Value = newValue;
    newNode->Next = NULL; // Since it will be the last node, next is NULL

    // 2. If the list is empty, make the new node the head
    if (*head == NULL) {
        *head = newNode;
        return;
    }

    // 3. Traverse to the last node
    Node* last = *head;
    while (last->Next != NULL) {
        last = last->Next;
    }

    // 4. Change the next of the last node
    last->Next = newNode;
}

// Insert a new node after a specific node
void insertAfter(Node* previous, int newValue) {
    // 1. Check if the given previous node is NULL
    if (previous == NULL) {
        cout << "Previous node cannot be NULL!" << endl;
        return;
    }

    // 2. Prepare the new node
    Node* newNode = new Node();
    newNode->Value = newValue;

    // 3. Make next of new node as next of previous node
    newNode->Next = previous->Next;

    // 4. Move the next of previous node as new node
    previous->Next = newNode;
}

// Function to delete the last node of the linked list
void deleteLast(Node** head) {
    // Case 1: If the list is empty
    if (*head == NULL) {
        cout << "The list is already empty." << endl;
        return;
    }

    // Case 2: If the list has only one node
    if ((*head)->Next == NULL) {
        delete *head; // Free memory
        *head = NULL; // Set head to NULL
        return;
    }

    // Case 3: If the list has more than one node
    Node* travel = *head;

    // Traverse to the second to last node
    while (travel->Next->Next != NULL) {
        travel = travel->Next;
    }

    // Now 'travel' points to the second to last node
    Node* temp = travel->Next; // This is the last node we want to delete
    delete temp;               // Free memory
    travel->Next = NULL;       // Update the next pointer of the new last node
}

// Print the list recursively
void printRecursion(Node* n) {
    if (n == NULL) {
        return;
    }
    cout << n->Value << endl;
    printRecursion(n->Next);
}

// Print the list in reverse order using recursion
void printReverseRecursion(Node* n) {
    if (n == NULL) {
        return;
    }
    printReverseRecursion(n->Next);
    cout << n->Value << endl;
}

int main() {
    // Creating nodes
    Node* head = new Node();
    Node* second = new Node();
    Node* third = new Node();

    // Linking nodes and assigning values
    head->Value = 100;
    head->Next = second;

    second->Value = 200;
    second->Next = third;

    third->Value = 300;
    third->Next = NULL;

    cout << "--- Initial List ---" << endl;
    printList(head);

    // Testing deleteLast function
    cout << "\n--- Deleting the last element ---" << endl;
    deleteLast(&head);
    printList(head);

    cout << "\n--- Deleting another element ---" << endl;
    deleteLast(&head);
    printList(head);

    // Memory Cleanup: Delete all remaining nodes to prevent memory leaks
    while (head != nullptr) {
        Node* temp = head;
        head = head->Next;
        delete temp;
    }
    cout << "\nAll nodes deleted. Memory cleaned up." << endl;

    return 0;
}
