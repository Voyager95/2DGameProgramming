
class Key:
    def __init__(self, *adj):
        self.leftTop = adj[0]
        self.top = adj[1]
        self.rightTop = adj[2]
        self.left = adj[3]
        self.self = adj[4]
        self.right = adj[5]
        self.bottomLeft = adj[6]
        self.bottom = adj[7]
        self.bottom = adj[8]
        pass

dic_key = {}
dic_key['A'] = Key('Null', 'Q', 'W', 'Null', 'A', 'S', 'Null', 'Z', 'X')
