import pytest
# from ..page_objects.login_page import LoginPage
# from ..page_objects.profile_page import ProfilePage
from ..page_objects.info_page import InfoPage

@pytest.mark.sanity
def test_number_of_items_menu(open_info_page):  # it will be 5
    page = InfoPage(open_info_page)
    items = page.get_menu_items()
    assert len(items) == 5

@pytest.mark.sanity
def test_items_are_unique_menu(open_info_page):
    page = InfoPage(open_info_page)
    items = page.get_menu_items()
    assert len(items) == len(set(items)), 'You have non-unique elements'

