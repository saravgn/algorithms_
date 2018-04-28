"""Class to implement BST"""

class Node:
	"""class Node"""
	def __init__(self, value):
		self.right = None
		self.left = None
		self.data = value


class Tree:
	"""class Tree"""
	def __init__(self):
		self.in_order_list = []
		self.pre_order_list = []
		self.post_order_list = []

	def insert(self, node, data):
		"""Insert"""
		if not node:
			return Node(data)

		if data <= node.data:
			node.left = self.insert(node.left, data)

		else:
			node.right = self.insert(node.right, data)

		return node


	def search(self, node, data):
		"""Search"""
		if node is not None and data is not None:
			if node.data == data:
				return True

			if data <= node.data:
				return self.search(node.left, data)
			else:
				return self.search(node.right, data)
		return False

	def delete(self, node, data):
		"""Delete"""
		# Base case
		if node is None:
			return node
		# go left if data is less than root
		if data < node.data:
			node.left = self.delete(node.left, data)
		# if data is greater then root go right
		elif data > node.data:
			node.right = self.delete(node.right, data)
		else:
			# if found node to delete

			# if node has one child 
			if node.left is None:
				temp = node.right 
				node = None
				return temp

			elif node.right is None:
				import pdb; pdb.set_trace()
				temp = node.left
				node = None
				return temp

			# two children - get inorder successor 
			# (which is smallest in right subtree)
			temp = self.get_min(node.right)
			# copy min in node to delete
			node.data = temp.data
			# delete inorder successor
			node.right = self.delete(node.right, temp.data)

		return node

	def get_min(self, node):
		"""Get min inorder successor """
		current = node
		while(current.left is not None):
			current = current.left 
		return current 

	def in_order(self, node):
		"""Visit in_order"""
		if node:
			self.in_order(node.left)
			self.in_order_list.append(node.data)
			self.in_order(node.right)


	def pre_order(self, node):
		"""Visit pre_order"""
		if node:
			self.pre_order_list.append(node.data)
			self.pre_order(node.left)
			self.pre_order(node.right)

		 
	def post_order(self, node):
		"""Visit post_order"""
		if node:
			self.post_order(node.left)
			self.post_order(node.right)
			self.post_order_list.append(node.data)



if __name__ == "__main__":
	# Driver program to test above functions
	""" BST used
				   25
				/      \
			  15        50
			 /  \      /   \
		   10   22    35    70 
		   / \  / \   / \   / \
		  4 12 18 24 31 44 66 90
	"""

	# Populate the tree
	root = None
	tree = Tree()
	root = tree.insert(root, 25)
	root = tree.insert(root, 15)
	root = tree.insert(root, 50)
	root = tree.insert(root, 10)
	root = tree.insert(root, 22)
	root = tree.insert(root, 4)
	root = tree.insert(root, 12)
	root = tree.insert(root, 18)
	root = tree.insert(root, 24)
	root = tree.insert(root, 35)
	root = tree.insert(root, 31)
	root = tree.insert(root, 44)
	root = tree.insert(root, 70)
	root = tree.insert(root, 66)
	root = tree.insert(root, 90)

	print('Testing in_order visit...')
	tree.in_order(root)
	expected_in_order_list = [4, 10,12, 15, 18,22,24,25,31,35,44,50,66,70,90]
	assert expected_in_order_list == tree.in_order_list
	print('Tested in_order visit')

	print('Testing pre_order visit...')
	tree.pre_order(root)
	expected_pre_order_list = [25,15,10,4,12,22,18,24, 50,35,31,44,70,66,90]
	assert expected_pre_order_list == tree.pre_order_list
	print('Tested pre_order visit')

	print('Testing post_order visit...')
	tree.post_order(root)
	expected_post_order_list = [4,12,10,18,24,22,15,31,44,35,66,90,70,50,25]
	assert expected_post_order_list == tree.post_order_list
	print('Tested post_order visit')

	print('Testing search function...')
	assert tree.search(root, 15) == True
	assert tree.search(root, 333) == False
	assert tree.search(root, None) == False
	assert tree.search(None, 15) == False
	print('Tested search function')

	print('Testing delete function...')
	assert tree.search(root, 15) == True
	tree.delete(root, 15)
	tree.in_order_list = []
	tree.in_order(root)
	print(tree.in_order_list)
	assert tree.search(root, 15) == False
	root = tree.insert(root, 15)
	print('Tested delete function')

