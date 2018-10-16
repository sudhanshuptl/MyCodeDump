# Binary Search TREE


class Node():
    def __init__(self, data=None):
        self.data = data
        self.next = None
    def __str__(self):
        return 'data = '+str(self.data)+': Next :='+str(self.next)


class LinkList():
    def __init__(self, head=None):
        self.head = head

    def insertion_at_beginning(self, data):
        if self.head is None:
            self.head = Node(data)

        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def print_list(self):
        if self.head is None:
            print('Link List is Empty')
            return
        ptr = self.head
        print('\nhead', end='')
        while ptr is not None:
            print('->', ptr.data, end='')
            ptr = ptr.next
        print()

    def insertion_at_end(self, data):
        if self.head is None:
            self.insertion_at_beginning(data)
        else:
            # create node
            new_node = Node(data)
            # point next to None
            new_node.next = None

            ptr = self.head
            while ptr.next is not None:
                ptr = ptr.next
            # point ot new node
            ptr.next = new_node

    def insertion_at_given_position(self, data, position):
        if position == 1:
            self.insertion_at_beginning(data)
        else:
            ptr = self.head
            count = 1
            while count < position - 1 and ptr.next is not None:
                ptr = ptr.next
                count += 1
            new_node = Node(data)
            new_node.next = ptr.next
            ptr.next = new_node

    def deletion_from_beginning(self):
        if self.head is None:
            return
        else:
            ptr = self.head
            self.head = self.head.next
            del ptr

    def deletion_from_end(self):
        if self.head is None:
            return
        else:
            if self.head.next is None:
                self.deletion_from_beginning()
            else:
                ptr = self.head
                while ptr.next.next is not None:
                    ptr = ptr.next

                temp = ptr.next
                ptr.next = temp.next
                del temp

    def delete_from_given_position(self, position):
        if position < 1:
            print('Out of range')
            return
        if self.head is None:
            return
        if position == 1:
            self.deletion_from_beginning()
            return

        ptr = self.head
        count = 1
        flag_out_of_range = False
        while count < position - 1:
            ptr = ptr.next
            count += 1
            if ptr.next is None:
                flag_out_of_range = True
                break

        if not flag_out_of_range:
            temp = ptr.next
            ptr.next = temp.next
            del temp

    def reverse_link_list(self):
        if self.head is None or self.head.next is None:
            return

        ptr = self.head.next
        self.head.next = None
        # iterate thought all node and insert at beginning
        while ptr is not None:
            temp = ptr
            ptr = ptr.next

            # insert temp at beginning
            temp.next = self.head
            self.head = temp

    def search(self, key):
        '''
        :param key:
        :return: position if found else -1
        '''
        position = 1
        ptr = self.head
        while ptr is not None:
            if ptr.data == key:
                return position
            position += 1
            ptr = ptr.next
        return -1

    def insert_at_sorted_position(self, data):
        if self.head is None or self.head.data > data:
            self.insertion_at_beginning(data)
            return

        ptr = self.head
        back_ptr = None
        # This move pointer to node after which we have to insert
        while ptr.next is not None and ptr.next.data < data:
            back_ptr = ptr
            ptr = ptr.next

        # If need to insert before first node or need to insert at end of list
        if back_ptr is None or ptr.next is None:
            back_ptr = ptr

        # Now Insert
        new_node = Node(data)
        new_node.next = back_ptr.next
        back_ptr.next = new_node


if __name__ == '__main__':
    # insert few Nodes and print
    oneWayList = LinkList()
    # Insert At begining
    print(' Inserting 3, 2, 1 in beginning ')
    oneWayList.insertion_at_beginning(3)
    oneWayList.insertion_at_beginning(2)
    oneWayList.insertion_at_beginning(1)
    oneWayList.print_list()

    # insert at end
    print('Inserting 6,7,8 at the end')
    oneWayList.insertion_at_end(6)
    oneWayList.insertion_at_end(7)
    oneWayList.insertion_at_end(8)
    oneWayList.print_list()

    # Insert at given position
    print(' insert 4 at 3rd position and 5 at 4rth position')
    oneWayList.insertion_at_given_position(4, 3)
    oneWayList.insertion_at_given_position(5, 4)
    oneWayList.print_list()

    print('Delete functionality !')
    # delete from the end
    print('Delete from the end')
    oneWayList.deletion_from_end()
    oneWayList.print_list()

    # delete from given position
    print('delete from 7th position')
    oneWayList.delete_from_given_position(7)
    oneWayList.print_list()

    # Delete from the beginning
    print('delete from beginning ')
    oneWayList.deletion_from_beginning()
    oneWayList.print_list()
    print('delete from beginning ')
    oneWayList.deletion_from_beginning()
    oneWayList.print_list()

    print('Reverse One Way link list')
    oneWayList.reverse_link_list()
    oneWayList.print_list()

    print('Search 4 in link list if available return position :', oneWayList.search(4))