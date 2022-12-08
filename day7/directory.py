from dataclasses import dataclass
import re

class Dir:
    def __init__(self, parent):
        self.parent = parent
        self.children = []
        self.contents = []
    
    def add_child(self, child):
        pass

    def add_file(self, file):
        pass

@dataclass
class File:
    size: int
    name: str