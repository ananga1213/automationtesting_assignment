import re
from time import sleep
from selenium.webdriver import ActionChains
from Pages.indexPage import IndexPage
from Utilities.Masterclass import Masterclass


class Test2(Masterclass):
    def test_user_case2(self):
        log = self.getLogger()
        action = ActionChains(self.driver)
        page = IndexPage(self.driver)
        product = page.getDiscountedProduct()
        i = -1

        for price in product:
            i = i + 1
            x=price.text
            if "%" in x:
                action.move_to_element(page.getPrice()[i]).perform()
                page.getAddButton()[i].click()
                sleep(5)
                page.getWindowClosed().click()
        cart = page.getClickOnCart()
        summaryPageTitle = self.driver.title
        assert summaryPageTitle == "Order - My Store", "Page navigation failed"
        oldPrice = cart.getOldPrice()
        discountPercent = cart.getDiscountPercentage()
        discountedPrice = cart.getDiscountedPrice()
        actualpricelist=[]
        discountPercentlist=[]
        discountedPricelist=[]
        for actualPrice in oldPrice:
            z=actualPrice.text
            trim = z[1:]
            actualpricelist.append(trim)
        for discountpercentage in discountPercent:
            m=discountpercentage.text
            trimminus = m[2:]
            trimpercent=trimminus[:-2]
            discountPercentlist.append(trimpercent)
        for disPrice in discountedPrice:
            p = disPrice.text
            ltrm=p[1:]
            discountedPricelist.append(float(ltrm))

        Mul_discount=[]
        for num1, num2 in zip(actualpricelist, discountPercentlist):
            Mul_discount.append(float(num1) * float(num2))
        roundedResultlist = []
        for div_discount in Mul_discount:
            div_result= div_discount/100
            roundedResult=round(div_result, 2)
            roundedResultlist.append(roundedResult)

        finalprice = []
        for num3, num4 in zip(actualpricelist, roundedResultlist):
            finalprice.append(float(num3) - float(num4))
        #print(finalprice)

        assert finalprice == discountedPricelist, "Discount is not correct"
        log.info("Discount is correct")

        sleep(5)