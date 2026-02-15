from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children,props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Error: parent node must have a tag")
        if not self.children:
            raise ValueError("Error: parent node must have children")
        res = f"<{self.tag}"        
        if self.props:
            for x in self.props:
                res += f" {x}=\"{self.props[x]}\""
        res += ">"
        for child in self.children:
            res += f"{child.to_html()}"
        res += f"</{self.tag}>"
        return res