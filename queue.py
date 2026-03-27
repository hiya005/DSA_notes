queue = []

def insert():
    item = int(input("enter element to insert: "))
    queue.append(item)
    print(item,"inserted to queue")

def delete():
    if len(queue)==0:
        print("queue is empty , cannot delete")
        removed_item = queue.pop(0)
        print(removed_item,"deleted the queue")
    
def transversal():
    if len(queue)==0:
        print("queue is empty")
    else:
        print("queue elements are:")

        for element in queue:
            print(element)