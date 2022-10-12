import vertex

class edge:
    def __init__(self, a:vertex, b:vertex, weight=0) -> None:
        self.b = b
        self.a = a
        self.weight = weight

    def __eq__(self, obj):
        return self.weight == obj.weight

    def __str__(self) -> str:
        return f'{self.a.name} to {self.b.name} w={self.weight}'

    def __repr__(self) -> str:
        return f'{self.a.name} to {self.b.name} w={self.weight}'

        