import pytest

from pages.technologies import technologies

@pytest.mark.smoke
def test_ecommerce(page):
    obj=technologies(page)
    obj.ecommerce_options_clicking()


@pytest.mark.smoke
def test_mobile(page):
    obj=technologies(page)
    obj.mobile_options_clicking()

@pytest.mark.smoke
def test_ai_clicking(page):
    obj=technologies(page)
    obj.ai_clicking()

