from components.base_component import BaseComponent
from playwright.sync_api import Page, Playwright, expect

from elements.icon import Icon
from elements.text import Text
from elements.textarea import Textarea


class EmptyViewComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        #self.icon = page.get_by_test_id(f'{identifier}-empty-view-icon')
        #self.title = page.get_by_test_id(f'{identifier}-empty-view-title-text')
        #self.description = page.get_by_test_id(f'{identifier}-empty-view-description-text')

        self.icon = Icon(page, f'{identifier}-empty-view-icon', 'Icon')
        self.title = Text(page,f'{identifier}-empty-view-title-text', 'Text')
        self.description = Text(page,f'{identifier}-empty-view-description-text', 'Description')

    def check_visible(self, title: str, description: str):
        self.icon.check_visible()
        self.title.check_visible()
        self.title.check_have_text(title)
        self.description.check_visible()
        self.description.check_have_text(description)

        #expect(self.icon).to_be_visible()
        #expect(self.title).to_be_visible()
        #expect(self.title).to_have_text(title)
        #expect(self.description).to_be_visible()
        #expect(self.description).to_have_text(description)
