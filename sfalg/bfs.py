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
		if len(queue):
			current = queue[0]
	return path
