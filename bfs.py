"""class to model graph and reproduce bfs"""

class Vertex:
	"""class vertex"""
	def __init__(self, n):
		self.name = n
		self.neighbors = list()
		self.marked = False
		self.visited = False
	
	def add_neighbor(self, v):
		"""add neighbor"""
		if v not in self.neighbors:
			self.neighbors.append(v)
			self.neighbors.sort()

class Graph:
	"""class graph"""
	def __init__(self):
		self.bfs_list = []

	vertices = {}
	
	def add_vertex(self, vertex):
		"""add vertex"""
		if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
			self.vertices[vertex.name] = vertex
			return True
		else:
			return False
	
	def add_edge(self, u, v):
		"""add edge"""
		if u in self.vertices and v in self.vertices:
			for key, value in self.vertices.items():
				if key == u:
					value.add_neighbor(v)
				# uncomment if graph not direct
				# if key == v:
				# 	value.add_neighbor(u)
			return True
		else:
			return False
			
	def print_graph(self):
		"""print graph"""
		for key in sorted(list(self.vertices.keys())):
			print(key + str(self.vertices[key].neighbors))
		
	def bfs(self, vert):
		"""bfs"""
		queue = []
		queue.append(vert)
		vert.marked = True

		while(queue):
			curr_vert = queue.pop(0)
			self.bfs_list.append(curr_vert.name)
			curr_vert.visited = True
			for ne in reversed(curr_vert.neighbors):
				ne = self.vertices[ne]
				if not ne.marked:
					ne.marked = True
					queue.append(ne)
		return self.bfs_list

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

assert g.bfs(a) == ['A', 'D', 'C', 'B', 'F', 'E']
g.print_graph()







