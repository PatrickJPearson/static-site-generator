from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if self.value == None:
            raise ValueError("Error: leaf nodes must have a value")
        if not self.tag:
            return str(self.value)
        if not self.props:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        res = f"<{self.tag}"
        for x in self.props:
            res +=  f" {x}=\"{self.props[x]}\""
        res += f">{self.value}</{self.tag}>"
        return res
        
    def __repr__(self):
        return f"tag: {self.tag}\nvalue: {self.value}\nprops: {self.props}"