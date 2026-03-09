from elements.base_elements import BaseElement
from playwright.sync_api import Page, expect, Locator

class Button(BaseElement):
    def check_enabled(self, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        expect(locator).to_be_enabled()


    def check_disabled(self, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        expect(locator).to_be_disabled()