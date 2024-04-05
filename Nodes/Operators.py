class OperatorNode(Node):
    def __init__(self, op):
        self.op = op

class UnaryOperatorNode(OperatorNode):
    def __init__(self, op, value):
        self.value = value
        super().__init__(op)

class BinOperatorNode(OperatorNode):
    def __init__(self, op, left, right):
        self.left = left
        self.right = right
        super().__init__(op)

class TernaryOperatorNode(OperatorNode):
    def __init__(self, op, left, center, right):
        self.left = left
        self.center = center
        self.right = right
        super().__init__(op)
