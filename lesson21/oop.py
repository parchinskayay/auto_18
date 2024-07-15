class Element:
    def __init__(self, name):
        self.name = name

    def click(self):
        print("Click on element: ", self.name)

    def _css_code(self):
        print("CSS code for", self.name)

    def __remove_element(self):
        print("Remove", self.name)


class ButtonElement(Element):
    def __init__(self, name, status):
        super().__init__(name)
        self.status = status

    def double_click(self):
        print("Double click on", self.name)

    def click(self):
        print("Click on button:", self.name)


element = Element('field')
button = ButtonElement('button', 'active')

element.click()
button.click()
button.double_click()
