#include <iostream>
using namespace std;

// Düğüm (Node) sınıfının tanımı
class Node{
    public:
        int Value;
        Node* Next;
};

/**
 * @brief Listenin tamamını baştan sona yazdırır (Iterative).
 * @param n Başlangıç düğümü (head).
 */
void printList(Node* n){
    while(n != NULL){
        cout << n->Value << " -> ";
        n = n->Next;
    }
    cout << "NULL" << endl;
}

/**
 * @brief Listenin başına yeni bir düğüm ekler.
 * @param head Listenin 'head' pointer'ına bir pointer (Node**).
 * @param newValue Eklenecek yeni değer.
 */
void insertAtThefront(Node **head, int newValue){ 
    // Yorum: &head'i (head pointer'ının adresini) göndermemizin nedeni,
    // ASIL head'i değiştirmek istememizdir. Diğer türlü bir kopya üzerinde çalışırdık.
    
    // 1. Yeni düğümü hazırla
    Node* newNode = new Node();
    newNode->Value = newValue;
    
    // 2. Yeni düğümün 'Next'ini mevcut head yap
    newNode->Next = *head;  
    
    // 3. 'head' pointer'ını güncelleyerek yeni düğümü göster
    *head = newNode;
}

/**
 * @brief Listenin sonuna yeni bir düğüm ekler.
 * @param head Listenin 'head' pointer'ına bir pointer (Node**).
 * @param newValue Eklenecek yeni değer.
 */
void insertAtThend(Node **head, int newValue){
    // 1. Yeni düğümü hazırla ve son düğüm olacağı için Next'ini NULL yap
    Node *newNode = new Node();
    newNode ->Value = newValue;
    newNode ->Next = NULL;

    // 2. Liste boşsa, 'head'i bu yeni düğüm yap
    if(*head == NULL){
        *head = newNode;
        return; 
    }

    // 3. Liste boş değilse, son düğümü bul
    Node *last = *head;
    while(last->Next != NULL){
        last = last ->Next;
    }

    // 4. Son düğümün 'Next'ini yeni düğüm olarak ayarla
    last -> Next = newNode;
}

/**
 * @brief Belirli bir düğümden ('previous') sonraya yeni bir düğüm ekler.
 * @param previous Yeni düğümün ekleneceği yerin bir önceki düğümü.
 * @param NewValue Eklenecek yeni değer.
 */
void InsertAt(Node *previous, int NewValue){
    // Hata kontrolü: 'previous' NULL olamaz
    if(previous == NULL){
        cout << "HATA: 'previous' dugumu NULL olamaz!" << endl;
        return;
    }
    
    // 1. Yeni düğümü hazırla
    Node *newNode = new Node();
    newNode -> Value = NewValue;
    
    // 2. Yeni düğümün 'Next'ini, 'previous'ın 'Next'i yap
    newNode -> Next = previous -> Next;
    
    // 3. 'previous'ın 'Next'ini yeni düğüm yap
    previous -> Next = newNode;
}

/**
 * @brief Listenin tamamını baştan sona yazdırır (Recursive).
 * @param n Başlangıç düğümü (head).
 */
void PrintRecursion(Node* n){
    // Temel Durum (Base Case): Liste bittiyse dur.
    if(n == NULL){
        return;
    }
    
    // Özyineli Adım (Recursive Step):
    // Önce mevcut değeri yazdır, sonra geri kalanı için fonksiyonu çağır.
    cout << n ->Value << endl;
    PrintRecursion(n ->Next); // 'return' gereksiz
}

/**
 * @brief Listenin tamamını sondan başa (ters) yazdırır (Recursive).
 * @param n Başlangıç düğümü (head).
 */
void PrintReverseRecursion(Node * n){
    // Temel Durum (Base Case): Liste bittiyse dur.
    if(n == NULL)
        return;

    // Özyineli Adım (Recursive Step):
    // ÖNCE listenin geri kalanı için fonksiyonu çağır (ve bitmesini bekle).
    PrintReverseRecursion(n -> Next);
    
    // Geri kalan her şey yazdırıldıktan SONRA mevcut değeri yazdır.
    cout << n->Value <<  endl;
}

int main(){

    // Listeyi boş başlat
    Node* head = NULL;

    // Listeyi doldur
    insertAtThend(&head, 100);
    insertAtThend(&head, 200);
    insertAtThend(&head, 300);
    
    cout << "Orijinal Liste:" << endl;
    printList(head); // 100 -> 200 -> 300 -> NULL
    
    cout << "\nBaşa -1 eklendi:" << endl;
    insertAtThefront(&head, -1);
    printList(head); // -1 -> 100 -> 200 -> 300 -> NULL
    
    cout << "\nSona 400 eklendi:" << endl;
    insertAtThend(&head, 400);
    printList(head); // -1 -> 100 -> 200 -> 300 -> 400 -> NULL

    // '200' düğümünü bulup (bu head->Next->Next olur) ondan sonraya 250 ekleyelim
    cout << "\n200'den sonraya 250 eklendi:" << endl;
    if(head != NULL && head->Next != NULL && head->Next->Next != NULL){
         InsertAt(head->Next->Next, 250); // head->Next->Next = 200'lük düğüm
    }
    printList(head); // -1 -> 100 -> 200 -> 250 -> 300 -> 400 -> NULL

    cout << "\nListe Tersten Yazdirma (Recursive):" << endl;
    PrintReverseRecursion(head);


    // ÖNEMLİ: Hafızayı temizle
    cout << "\nProgram bitti, hafiza temizleniyor..." << endl;
    while (head != NULL) {
        Node* tmp = head;
        head = head->Next;
        delete tmp;
    }
    cout << "Tum dugumler (pointer) hafizadan silindi." << endl;

    return 0;
}