class Node():
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = None
class LinkList():
    def __init__(self):
        self.first=None
    def add_node(self, data):
        new_node = Node(data)
        if self.first is None:
            new_node.next = self.first
            self.first = new_node 
        else:
            node = self.first 
            while node.next is not None:
                node = node.next
            new_node.next= node.next
            node.next= new_node
    def list_print(self):
        node = self.first 
        while node:
            if(node.next==None):
                print(node.data)
            else:
                print(node.data,sep="=", end="->")
            node = node.next
    def count(self):
        node = self.first 
        count =0
        while node:
            count= count +1
            node = node.next
        return count
    def search(self, a):
        node = self.first 
        index =0
        while index < a :
            index = index +1
            node = node.next
        return node.data
    def tranlate(self, index):
        for i in range(index):
            node = self.first 
            while node.next is not None:
                node = node.next
            temp = Node(self.first.data)
            self.first= self.first.next
            temp.next= node.next
            node.next= temp            
ll = LinkList()
number = int(input("Nhap so luong phan tu: "))
for index in range(1,number+1):
    ll.add_node(input("value: "))
print("Danh sách liên kết:")
ll.list_print()
mid_node = int(ll.count()/2)
print("Giá trị ở giữa: ", ll.search(mid_node))
index = int(input("Dich sang phai K phan tu, K= "))
print(f"Danh sách liên kết sau khi dịch {index} phần tử:")
ll.tranlate(index%(ll.count()))
ll.list_print()

