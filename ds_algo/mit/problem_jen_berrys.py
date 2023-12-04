"""
Problem 1-4. Jen & Berry
https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/resources/mit6_006s20_prob1/
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def __len__(self):
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count

    def __str__(self):
        nodes = []
        current_node = self.head
        while current_node:
            nodes.append(str(current_node.data))
            current_node = current_node.next
        return " -> ".join(nodes)

    def reorder_students(self):
        n = len(self) // 2
        a = self.head
        for _ in range(n):
            a = a.next
        b = a.next
        x_p, x = a, b
        for _ in range(n):
            x_n = x.next
            x.next = x_p
            x_p, x = x, x_n
        c = x_p
        a.next = c
        b.next = None
        return


if __name__ == "__main__":
    # Create a linked list with student numbers
    student_list = LinkedList()
    student_list.append(1)
    student_list.append(2)
    student_list.append(3)
    student_list.append(4)
    student_list.append(5)

    print("Original student list:")
    print(student_list)

    # Reorder the student list
    student_list.reorder_students()

    print("Reordered student list:")
    print(student_list)
