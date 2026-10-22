from conftest import page


class portfoliopage:
    def __init__(self, page):
        self.page=page
        self.portfolio=page.locator('//a[text()="Portfolio"]')

        self.ics=page.locator('//a[@href="https://www.icshomework.in/"]')
        self.wings=page.locator('//a[@href="https://www.wingspharma.com/"]')
        self.arena=page.locator('//a[@href="https://arenasonipat.com/"]')
        self.home360=page.locator('//a[@href="https://home360stores.com/"]')
        #self.club=page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/services/portfolio/pic5.png"]')
        self.cords=page.locator('//a[@href="https://cordscable.tranktechnologies.com/"]')

        # self.web=page.locator('//a[@href="https://www.tranktechnologies.com/web-development-company"]')
        # self.cms=page.locator('//a[@href="https://www.tranktechnologies.com/cms-website-development-company"]')
        # self.ecom=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[1]')
        # self.web2=page.locator('//a[@href="https://www.tranktechnologies.com/website-development-company"]')
        # self.cust=page.locator('//a[@href="https://www.tranktechnologies.com/custom-web-portal-development-company"]')

        # self.uiux=page.locator('//a[@href="https://www.tranktechnologies.com/ui-ux-design-company"]')
        # self.mob=page.locator('//a[@href="https://www.tranktechnologies.com/mobile-app-design-company"]')
        # self.resp=page.locator('//a[@href="https://www.tranktechnologies.com/responsive-web-design-company"]')
        # self.brand=page.locator('//a[@href="https://www.tranktechnologies.com/brand-identity-design-services-company"]')

        # self.appdev=page.locator('(//a[@href="https://www.tranktechnologies.com/app-development-company"])[1]')
        # self.ios=page.locator('//a[@href="https://www.tranktechnologies.com/ios-mobile-app-development-company"]')
        # self.andapp=page.locator('//a[@href="https://www.tranktechnologies.com/android-mobile-app-development-company"]')
        # self.anddev=page.locator('//a[@href="https://www.tranktechnologies.com/android-app-development-company"]')
        # self.appment=page.locator('(//a[@href="https://www.tranktechnologies.com/app-development-company"])[2]')

        # self.hyb=page.locator('//a[@href="https://www.tranktechnologies.com/hybrid-mobile-app-development-company"]')
        # self.cross=page.locator('//a[@href="https://www.tranktechnologies.com/cross-platform-mobile-app-development-company"]')
        # self.prog=page.locator('//a[@href="https://www.tranktechnologies.com/progressive-web-app-development-company"]')

        # self.graph=page.locator('//a[@href="https://www.tranktechnologies.com/graphic-design-company"]')
        # self.logo=page.locator('//a[@href="https://www.tranktechnologies.com/logo-design-company"]')
        # self.bann=page.locator('//a[@href="https://www.tranktechnologies.com/banner-design-company"]')
        # self.pack=page.locator('//a[@href="https://www.tranktechnologies.com/packaging-design-company"]')
        # self.bus=page.locator('//a[@href="https://www.tranktechnologies.com/business-cards-design-company"]')

    def portfolio_options_clicking(self):
        self.portfolio.click()
        self.page.wait_for_load_state("load")
        self.portfolio_options=[self.ics,self.wings,self.arena,self.home360,self.cords]
        for portfolio in self.portfolio_options:
            with self.page.context.expect_page() as new_page_info:
                portfolio.click()
            new_tab = new_page_info.value
            new_tab.wait_for_load_state("load")
            new_tab.close()        