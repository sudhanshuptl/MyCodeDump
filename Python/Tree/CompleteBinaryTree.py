from BinarySearchTree import BinarySearchTree, Node
import copy
'''
1. Insertion Logic
2. Search a node
3. creating Mirror image of tree
4 . delete a Node from tree
5. check tree2 is mirror image of tree1
6. path root to each leaf node
'''
class CompleteBinaryTree(BinarySearchTree):
    '''
        most of tree traversal logic is same just need to update insertion and updation logic
    '''
    def __init__(self, root = None):
        super().__init__(root)

    def insert(self, key):
        '''
        :param key:
        insert node with value key at first available position in level order traversal
        :return:None
        '''
        node = Node(key)
        if self.root is None:
            self.root = node
            return
        queue = [self.get_root()]
        while queue:
            this_node = queue.pop(0)
            if this_node.left is not None:
                queue.append(this_node.left)
            else:
                this_node.left = node
                break
            if this_node.right is not None:
                queue.append(this_node.right)
            else:
                this_node.right = node
                break

    @staticmethod
    def search(this_node, key):
        if this_node is None:
            return False
        elif this_node.key == key:
            return True
        return CompleteBinaryTree.search(this_node.left, key) or CompleteBinaryTree.search(this_node.right, key)

    def create_mirror_image(self, this_node):
        '''
        :param this_node:
        :return: new tree mirror image tree i.e 180 degree rotated from vertical line
        '''
        if this_node:
            self.create_mirror_image(this_node.left)
            self.create_mirror_image(this_node.right)

            # Actual swapping
            this_node.left, this_node.right = this_node.right, this_node.left
        return this_node

    def delete_deepest(self, last_node):
        queue = [self.root]
        while queue:
            this_node = queue.pop(0)
            if this_node.left is not None:
                if this_node.left == last_node:
                    this_node.left = None
                    del last_node
                    return
                else:
                    queue.append(this_node.left)
            if this_node.right is not None:
                if this_node.right == last_node:
                    this_node.right = None
                    del last_node
                    return
                else:
                    queue.append(this_node.right)

    def delete(self, key):
        '''
            find node with value key and deppest node , swap and delete deepest node
        '''
        if self.root is None:
            print('Tree is Empty')
            return
        queue = [self.root]

        while queue:
            this_node = queue.pop(0)
            if this_node.key == key:
                key_node = this_node
            if this_node.left is not None:
                queue.append(this_node.left)
            if this_node.right is not None:
                queue.append(this_node.right)

        key_node.key = this_node.key # here this node is last node or deepest node
        self.delete_deepest(this_node)

    @staticmethod
    def are_mirrors(root1, root2):
        '''
        :param root1:
        :param root2:
        :return return true if these two trees are mirror images of each other:
        '''
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        if root1.key != root2.key:
            return False
        else:
            return CompleteBinaryTree.are_mirrors(root1.left, root2.right)\
                   and CompleteBinaryTree.are_mirrors(root1.right, root2.left)

    @staticmethod
    def print_root_to_leaf(root, path=[]):
        if root is None:
            return
        path.append(root.key)
        if root.left is None and root.right is None:
            print('->'.join([str(x) for x in path]))
        else:
            CompleteBinaryTree.print_root_to_leaf(root.left, copy.copy(path))
            CompleteBinaryTree.print_root_to_leaf(root.right, copy.copy(path))

if  __name__ == '__main__':
    complete_binary_tree = CompleteBinaryTree()
    complete_binary_tree.insert(1)
    complete_binary_tree.insert(2)
    complete_binary_tree.insert(3)
    complete_binary_tree.insert(4)
    complete_binary_tree.insert(5)
    complete_binary_tree.insert(6)
    complete_binary_tree.insert(7)
    complete_binary_tree.insert(8)
    print('_____Level Order Traversal____')
    complete_binary_tree.level_order_traversal([complete_binary_tree.get_root()])
    complete_binary_tree.print('INORDER')

    print('\nMax Depth >> ', end='')
    print(complete_binary_tree.max_depth(complete_binary_tree.root))

    print('Print All leaf Node >>')
    complete_binary_tree.print_all_leaf_node(complete_binary_tree.root)

    print('\n\nSearch a Node 5 :', complete_binary_tree.search(complete_binary_tree.get_root(), 5))
    print('\n\nSearch a Node 9 :', complete_binary_tree.search(complete_binary_tree.get_root(), 9))


    print('____Delete Node __________')
    complete_binary_tree.delete(8)
    print('_____Level Order Traversal____')
    complete_binary_tree.level_order_traversal([complete_binary_tree.get_root()])

    print('________Create mirror image_______')
    complete_binary_tree.create_mirror_image(complete_binary_tree.root)
    print('_____Level Order Traversal____')
    complete_binary_tree.level_order_traversal([complete_binary_tree.get_root()])

    #bt = CompleteBinaryTree()
    #bt.insert(1)
    #bt.insert(2)
    #bt.insert(3)
    #bt.insert(4)
    #bt.insert(5)
    #bt.insert(6)
    #bt.insert(7)
    #bt.insert(8)
    #print('_____Level Order Traversal tree_2 ____')
    #bt.level_order_traversal([bt.get_root()])
    #print('__Check is tree1 and tree2 are mirror image__ :', end='')
    #print(CompleteBinaryTree.are_mirrors(complete_binary_tree.root, bt.root))

    print('__Print all the path from root to leaf__')
    CompleteBinaryTree.print_root_to_leaf(complete_binary_tree.get_root(), [])