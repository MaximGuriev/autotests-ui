from elements.base_elements import BaseElement
from playwright.sync_api import Page, expect, Locator

class Button(BaseElement):
    def check_enabled(self, **kwargs):
        locator = self.get_locator(**kwargs)
        expect(locator).to_be_enabled()


    def check_disabled(self, **kwargs):
        locator = self.get_locator(**kwargs)
        expect(locator).to_be_disabled()