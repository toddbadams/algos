class vertex:
    def __init__(self, name: str, adjacent=[]) -> None:
        self.name = name
        self.adjacent = adjacent

    def __eq__(self, obj):
        return self.name == obj.name

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name
        