class Node():
    def __init__(self, star_id, parent, movie_id):
        self.parent = parent
        self.star_id = star_id
        self.movie_id = movie_id


class Queue():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_movie(self, movie_id):
        return any(node.movie_id == movie_id for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node
