class Vertex:
	"""class Vertex"""
	def __init__(self, n):
		self.name = n
		self.neighbors = list()
		self.marked = False
		self.visited = False
	
	def add_neighbor(self, v):
		"""function to add a neighbor"""
		if v not in self.neighbors:
			self.neighbors.append(v)
			self.neighbors.sort()

class Graph:
	"""Class graph"""
	def __init__(self):
		self.dfs_list = []

	vertices = {}
	
	def add_vertex(self, vertex):
		"""function to add a vertex"""
		if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
			self.vertices[vertex.name] = vertex
			return True
		else:
			return False
	
	def add_edge(self, u, v):
		"""function to add an edge"""
		if u in self.vertices and v in self.vertices:
			for key, value in self.vertices.items():
				if key == u:
					value.add_neighbor(v)
				# if key == v:
				# 	value.add_neighbor(u)
			return True
		else:
			return False
			
	def print_graph(self):
		"""function to print a graph"""
		for key in sorted(list(self.vertices.keys())):
			print(key + str(self.vertices[key].neighbors))
		
	def dfs(self, node):
		"""dfs"""
		if not node:
			return False;
		node.visited = True
		self.dfs_list.append(node.name)
		for nd in reversed(node.neighbors):
			nd = self.vertices[nd]
			if nd.visited == False:
				self.dfs(nd)
		return self.dfs_list

"""
Adiacent list

A['B', 'C', 'D']
B[]
C['D', 'F']
D[]
E['C']
F['D', 'E']
"""				
g = Graph()
a = Vertex('A')
g.add_vertex(a)
g.add_vertex(Vertex('B'))
for i in range(ord('A'), ord('G')):
	g.add_vertex(Vertex(chr(i)))


edges = ['AB', 'AD', 'AC', 'CD', 'CF', 'FD', 'FE', 'EC']
for edge in edges:
	g.add_edge(edge[:1], edge[1:])


assert g.dfs(a) in [['A', 'B', 'C', 'D', 'F', 'E'], ['A', 'D', 'C', 'F', 'E', 'B']]
g.print_graph()




