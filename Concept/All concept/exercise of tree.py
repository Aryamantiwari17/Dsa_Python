class Treenode:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.children = []

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        spaces = " " * self.get_level() * 4
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

def build_tree():
    root = Treenode("Nilpul (CEO)")

    cto = Treenode("Chinmay (CTO)")
    infra_head = Treenode("Vishwa (Infrastructure Head)")
    app_head = Treenode("Aamir (Application Head)")
    
    infra_head.add_child(Treenode("Dhaval (Cloud Manager)"))
    infra_head.add_child(Treenode("Abhijit (App Manager)"))
    
    cto.add_child(infra_head)
    cto.add_child(app_head)

    hr_head = Treenode("Gels (HR Head)")
    hr_head.add_child(Treenode("Peter (Recruitment Manager)"))
    hr_head.add_child(Treenode("Waqas (Policy Manager)"))

    root.add_child(cto)
    root.add_child(hr_head)

    return root

if __name__ == "__main__":
    root = build_tree()
    root.print_tree()
