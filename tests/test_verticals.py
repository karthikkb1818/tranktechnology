#after creating verticals, we will call it. we need to call the method page. 3rd line. then get the object of that class

import pytest

from pages.verticals import verticals

@pytest.mark.smoke
def test_trading(page):
    obj=verticals(page)
    obj.trading_options_clicking()   # we have called method using object. now we need framework to implement

@pytest.mark.smoke
def test_retail(page):
    obj=verticals(page)
    obj.retail_options_clicking()

@pytest.mark.smoke
def test_health(page):
    obj=verticals(page)
    obj.health_options_clicking()

@pytest.mark.smoke
def test_fintech(page):
    obj=verticals(page)
    obj.fintech_options_clicking()

@pytest.mark.smoke
def test_custom_app(page):
    obj=verticals(page)
    obj.custom_app_options_clicking()