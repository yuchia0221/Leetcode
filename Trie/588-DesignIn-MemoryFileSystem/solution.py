from typing import List


class Node:
    def __init__(self):
        self.content = ""
        self.children = dict()


class FileSystem:
    def __init__(self):
        self.root = Node()

    def ls(self, filePath: str) -> List[str]:
        node = self.root
        paths = [path for path in filePath.split("/") if path]
        print(paths)
        for path in paths:
            if path not in node.children:
                node.children[path] = Node()
            node = node.children[path]

        if node.content:
            return [paths[-1]]
        else:
            return sorted(node.children.keys())

    def mkdir(self, filePath: str) -> None:
        node = self.root
        paths = [path for path in filePath.split("/") if path]
        for path in paths:
            if path not in node.children:
                node.children[path] = Node()
            node = node.children[path]

    def addContentToFile(self, filePath: str, content: str) -> None:
        node = self.root
        paths = [path for path in filePath.split("/") if path]
        for path in paths:
            if path not in node.children:
                node.children[path] = Node()
            node = node.children[path]

        node.content += content

    def readContentFromFile(self, filePath: str) -> str:
        node = self.root
        paths = [path for path in filePath.split("/") if path]
        for path in paths:
            if path not in node.children:
                node.children[path] = Node()
            node = node.children[path]

        return node.content
