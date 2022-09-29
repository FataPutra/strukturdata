class Node:
	'''Node class with two fields'''
	def __init__(self, data):
		self.data = data
		self.next_ptr = None

class Stack:
	'''This class will implement the functionality of Stack'''
	def __init__(self):
		self.top = None
		
	def Push(self, item):
		'''This will add an item to the stack'''
		node = Node(item)
		if self.top is None:
			self.top = node
		else:
			node.next_ptr = self.top
			self.top = node
		
	def Pop(self):
		'''This will remove and return the last inserted item from the stack'''
		if self.top is None:
			return None
		else:
			temp = self.top.data
			temp1 = self.top.next_ptr
			self.top.next_ptr = None
			self.top = temp1
			return temp
			
	def getTop(self):
		'''Returns the top node'''
		return self.top.data
	
	def printStack(self):
		'''This will print the stack'''
		currentNode = self.top
		while currentNode is not None:
			print(currentNode.data)
			currentNode = currentNode.next_ptr
		

if __name__ == '__main__':
	#Creating a stack and inserting items
	stack = Stack()
	stack.Push(5)
	stack.Push(6)
	stack.Push(11)
	stack.Push(1)
	
	print("Original stack")
	stack.printStack()
	
	print("\nTop of the stack")
	print(stack.getTop())
	
	print("\nFirst pop")
	print(stack.Pop())
	
	print("\nSecond pop")
	print(stack.Pop())
	
	print("\nRemaining items in the stack")
	stack.printStack()