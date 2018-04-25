# Binary Search TREE


class Node:
    def __init__(self, key=None):
        self.next = None
        self.key = key


class LinkList(object):
    def __init__(self, head=None):
        self.head = head

    def printList(self):
        ptr=self.head
        if ptr is None:
            print('Link List is Empty !!!')
            return
        print('head',end='')
        while ptr is not None:
            print(' ->', ptr.key, end='')
            ptr = ptr.next
        print()
    def insert_at_begin(self, key):
        #create new Node
        new_node = Node(key)
        # adding new node at beginning
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, key):
        # create new node
        new_node = Node(key)
        # Set pointer to first node then move till last node
        ptr = self.head
        while ptr.next is not None:
            ptr = ptr.next

        ptr.next = new_node

    def insert_at_given_position(self, key, position=None):
        if position is None:
            self.insert_at_end(key)
            return
        if position == 1:
            self.insert_at_begin(key)
            return
        count = 1
        ptr = self.head
        while count != position or ptr.next is None:
            ptr = ptr.next
            count += 1
        new_node = Node(key)
        new_node.next = ptr.next
        ptr.next = new_node

    def delete_from_beginning(self):
        if self.head is None:
            print("LinkList is Empty !")
            return

        ptr = self.head
        self.head = self.head.next
        del ptr

    def delete_from_end(self):
        if self.head is None:
            print("Link List is Empty !")
            return
        if self.head.next is None:
            self.delete_from_beginning()
            return
        ptr = self.head
        ptr_back = ptr
        while ptr.next is not None:
            ptr_back = ptr
            ptr = ptr.next

        ptr_back.next = None
        del ptr

    def delete_at_given_position(self, position):
        ptr = self.head
        count = 1

        # previous node of node to be deleted
        if position == 1:
            self.head = self.head.next
            del ptr
            return
        if position < 1:
            print(' Not a Valid Position !!')
            return

        # Fine node just before node to delete
        while ptr is not None and count < position-1:
            ptr = ptr.next
            count += 1
        if ptr is None or ptr.next is None:
            print("Position is not available !")
            return

        node_to_delete = ptr.next
        ptr.next = node_to_delete.next

        del node_to_delete


if __name__ == '__main__':
    # insert few Nodes and print
    oneWayList = LinkList()
    # Insert At begining
    oneWayList.insert_at_begin(3)
    oneWayList.insert_at_begin(2)
    oneWayList.insert_at_begin(1)
    oneWayList.printList()

    # insert at end
    oneWayList.insert_at_end(6)
    oneWayList.insert_at_end(7)
    oneWayList.insert_at_end(8)
    oneWayList.printList()

    # Insert at given position
    oneWayList.insert_at_given_position(4, 3)
    oneWayList.insert_at_given_position(5, 4)
    oneWayList.printList()

    print('Delete functionality !')
    # delete from the end
    oneWayList.delete_from_end()
    oneWayList.printList()

    # delete from given position
    oneWayList.delete_at_given_position(7)
    oneWayList.printList()

    # Delete from the beginning
    oneWayList.delete_from_beginning()
    oneWayList.printList()
    oneWayList.delete_from_beginning()
    oneWayList.printList()
