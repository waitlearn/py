from collections import deque
def bfs(graph,start):
	path = []
	queue = deque([start])
	current = start
	explored = [start]
	while len(queue):
		for node in graph[current]:
			if node not in explored:
				queue.append(node)
				explored.append(node)
		path.append(queue.popleft())
		current = path[-1]
	return path

def bfsnq(graph,start):
	path = []
	queue = [start]
	current = start
	explored = [start]
	while len(queue):
		for node in graph[current]:
			if node not in explored:
				queue.append(node)
				explored.append(node)
		path.append(queue.pop(0))
		current = queue[0]
	return path		 

