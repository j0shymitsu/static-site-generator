class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Error")

    def props_to_html(self):
        if self.props is None:
            return ''
        for k, v in props.items():
            return f'{k}={v}'

    def __eq__(self, other):
        return (
                self.tag == other.tag and
                self.value == other.value and
                self.children == other.children and
                self.props == other.props
        )

    def __repr__(self):
        return (
            f'HTMLNode('
            f'{self.tag}, '
            f'{self.value}, '
            f'{self.children}, '
            f'{self.props})'
        ) 
        
