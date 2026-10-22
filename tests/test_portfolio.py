import pytest

from pages.portfolio import portfoliopage

@pytest.mark.smoke
def test_portfolio(page):
    obj=portfoliopage(page)
    obj.portfolio_options_clicking() 