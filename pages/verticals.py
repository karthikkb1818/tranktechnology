from conftest import page


class verticals:
    def __init__(self, page):
        self.page=page
        self.verticals=page.locator('(//a[text()="Verticals"])[1]') 

        #Trading
        self.trading=page.locator('(//img[@alt="trading"])[1]')
        self.tra1=page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-mobile-app-development-company"])[1]')
        self.tra2=page.locator('(//a[@href="https://www.tranktechnologies.com/algo-trading-app-development-company"])[1]')
        self.tra3=page.locator('(//a[@href="https://www.tranktechnologies.com/paper-trading-app-development-company"])[1]')
        self.tra4=page.locator('(//a[@href="https://www.tranktechnologies.com/custom-trading-software-development-company"])[1]')
        self.tra5=page.locator('(//a[@href="https://www.tranktechnologies.com/cfd-trading-app-development-company"])[1]')
        self.tra6=page.locator('(//a[@href="https://www.tranktechnologies.com/webportal-trading-development"])[1]')
        self.tra7=page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-development-in-massachusetts"])[1]')
        self.trading_options=[self.tra1,self.tra2,self.tra3, self.tra4, self.tra5, self.tra6,self.tra7]


        #retailandecommerce
        self.retail=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[1]')
        self.ret1=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[1]')
        self.ret2=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-app-development"])[1]')
        self.retail_options=[self.ret1, self.ret2]


        #health
        self.health_care=page.locator('(//a[@href="https://www.tranktechnologies.com/healthcare-mobile-app-development-company"])[1]')
        self.hea1=page.locator('(//a[@href="https://www.tranktechnologies.com/diet-and-nutrition-app-developement"])[1]')
        self.hea2=page.locator('(//a[@href="https://www.tranktechnologies.com/health-tracking-app"])[1]')
        self.health_options=[self.hea1, self.hea2]

        #Fintech
        self.fintech=page.locator('(//a[@href="https://www.tranktechnologies.com/fintech-mobile-app-development-company"])[1]')
        self.fin1=page.locator('(//a[@href="https://www.tranktechnologies.com/pos-software-development-company"])[1]')
        self.fin2=page.locator('(//a[@href="https://www.tranktechnologies.com/cryptocurrency-mobile-app-development-company"])[1]')
        self.fintech_options=[self.fin1,self.fin2]

        #customapp
        self.custom_app=page.locator('//strong[text()="Custom App"]')
        self.cus1=page.locator('(//a[@href="https://www.tranktechnologies.com/desktop-application-development-company"])[1]')
        self.cus2=page.locator('(//a[@href="https://www.tranktechnologies.com/custom-crm-development-company"])[1]')
        self.cus3=page.locator('(//a[@href="https://www.tranktechnologies.com/hrm-application-development-company"])[1]')
        self.cus4=page.locator('(//a[@href="https://www.tranktechnologies.com/erp-app-development-company"])[1]')
        self.cus5=page.locator('(//a[@href="https://www.tranktechnologies.com/travel-mobile-app-development-company"])[1]')
        self.cus6=page.locator('(//a[@href="https://www.tranktechnologies.com/e-learning-mobile-app-development-company"])[1]')
        self.cus7=page.locator('(//a[@href="https://www.tranktechnologies.com/dating-app-development-company"])[1]')
        self.cus8=page.locator('(//a[@href="https://www.tranktechnologies.com/real-estate-mobile-app-development-company"])[1]')
        self.cus9=page.locator('(//a[@href="https://www.tranktechnologies.com/usa/custom-crm-development-company-usa"])[1]')    
        self.custom_app_options=[self.cus1,self.cus2,self.cus3,self.cus4,self.cus5,
                                 self.cus6,self.cus7,self.cus8,self.cus9]

        



    def trading_options_clicking(self):
        for i in self.trading_options:
            self.verticals.hover()
            self.trading.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def retail_options_clicking(self):
        for i in self.retail_options:
            self.verticals.hover()
            self.retail.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def health_options_clicking(self):
        for i in self.health_options:
            self.verticals.hover()
            self.health_care.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def fintech_options_clicking(self):
        for i in self.fintech_options:
            self.verticals.hover()
            self.fintech.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def custom_app_options_clicking(self):
        for i in self.custom_app_options:
            self.verticals.hover()
            self.custom_app.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()
 
        




