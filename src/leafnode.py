from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, children=None, props=None):
        super(LeafNode, self).__init__(tag, value, children, props)
        self.children = None
        self.props = props

    def to_html(self):
        if self.value == None:
            raise ValueError("Error")
        if self.tag == None:
            return f'{self.value}'
        return f'<{self.tag}>{self.value}</{self.tag}>'

    def __eq__(self, other):
        return (
                self.tag == other.tag and
                self.value == other.value and
                self.props == other.props
        )

    def __repr__(self):
        return (
                f'LeafNode('
                f'{self.tag}, '
                f'{self.value}, '
                f'{self.props})'
        )
        
