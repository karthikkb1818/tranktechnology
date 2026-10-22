import pytest

from pages.contactus import contactus

@pytest.mark.smoke
def test_contactus(page):
    obj=contactus(page)
    obj.contactus_options_clicking() 