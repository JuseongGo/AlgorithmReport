class Node:
    def __init__(self, value):
        # double linked list
        self.value = value
        self.left = None
        self.right = None


class NodeMgmt:
    def __init__(self, head):
        self.head = head  # 루트노드

    # 삽입
    def insert(self, value):
        self.current_node = self.head
        while True:
            if value < self.current_node.value:
                if self.current_node.left != None:  # 이미 가지고 있다면
                    self.current_node = self.current_node.left  # 비교대상을 바꾼다.
                else:
                    self.current_node.left = Node(value)  # 없다면 새로 만들어 연결시킨다.
                    break
            else:
                if self.current_node.right != None:  # 이미 가지고 있다면
                    self.current_node = self.current_node.right  # 비교대상을 바꾼다.
                else:
                    self.current_node.right = Node(value)
                    break

    # 이진 탐색 트리 출력
    def search(self, value):
        self.current_node = self.head

        while self.current_node:
            if self.current_node.value == value:  # 찾았다
                return True
            elif value < self.current_node.value:
                self.current_node = self.current_node.left  # 비교대상 바꾸기
            else:
                self.current_node = self.current_node.right  # 비교대상 바꾸기
        return False  # 다 찾아봤는데 없다.
    
    def delete(self, value):
        # 삭제할 노드 탐색
        self.current_node = self.head  # 삭제할 노드
        self.parent = self.head  # 삭제할 노드의 부모 노드

        # 일단 해당 노드가 있는지를 찾는다
        while self.current_node:
            if self.current_node.value == value:
                searched = True
                break
            elif value < self.current_node.value:
                self.parent = self.current_node
                self.curent_node = self.current_node.left  # 비교대상 변경
            else:
                self.parent = self.current_node
                self.current_node = self.current_node.right  # 비교대상 변경

        if searched == False:  # 그런 값을 가진 노드가 없다 = 삭제할 노드가 없다
            return False

        ## 해당노드를 찾았다. 이제 삭제를 하자!
        # case1
        if self.current_node.left == None and self.current_node.right == None:
            if value < self.parent.value:
                self.parent.left = None
            else:
                self.parent.right = None
        # case2
        # 왼쪽 노드만 가지고 있다.
        elif self.current_node.left != None and self.current_node.right == None:
            # 삭제할 노드가 parent의 오른쪽에 있냐 왼쪽에 있냐
            if value < self.parent.value:
                self.parent.left = self.current_node.left
            else:
                self.parent.right = self.current_node.left
        # 오른쪽 노드만 가지고 있다.
        elif self.current_node.left == None and self.current_node.right != None:
            if value < self.parent.value:
                self.parent.left = self.current_node.right
            else:
                self.parent.right = self.current_node.right

        # case3 : 삭제할 노드가 두개의 자식을 가진다
        if self.current_node.left != None and self.current_node.right != None:

            # case3-1 : 삭제할 노드가 부모 노드의 왼쪽에 있다
            if value < self.parent.value:
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right

                # 가장 작은값은 무조건 left에 있다 = 일단 left 끝까지 가게
                while self.change_node.left != None:
                    self.change_node_parent = self.change_node
                self.change_node = self.change_node.left

                # 3-1-2
                if self.change_node.right != None:
                    self.change_node_parent.left = self.change_node.right
                else:  # 3-1-1
                    self.change_node_parent.left = None

                # 위로 옮기기
                self.parent.left = self.change_node
                self.change_node.right = self.current_node.right
                self.change_node.left = self.current_node.left
            # case3-2 : 삭제할 노드가 부모 노드의 오른쪽에 있다
            else:
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right
                while self.change_node.left != None:
                    self.change_node_parent = self.change_node
                    self.chage_node = self.change_node.left  # 비교 대상 변경
                # 3-2-2
                if self.chage_node.right != None:
                    self.change_node_parent.left = self.change_node.right
                else:  # 3-2-1
                    self.change_node_parent.left = None

                # 위로 옮긴다.
                self.parent.right = self.change_node
                self.change_node.left = self.current_node.left
                self.chage_node.right = self.current_node.right
# 실행
head = Node(1)
BST = NodeMgmt(head)
BST.insert(2)
BST.insert(3)
BST.delete(2)

print(BST.search(2))
print(BST.search(5))