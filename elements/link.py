from elements.base_elements import BaseElement


class Link(BaseElement):
    @property
    def type_of(self) -> str:
        return "link"