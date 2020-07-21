from time import sleep
from selenium.webdriver import ActionChains
from Pages.indexPage import IndexPage
from Utilities.Masterclass import Masterclass


class Test1(Masterclass):
    def test_user_case1(self):
        log = self.getLogger()
        action = ActionChains(self.driver)
        page = IndexPage(self.driver)
        try:
            page.getpopularText().click()
            log.info("Clicked on Popular Item")
        except Exception as e:
            self.driver.get_screenshot_as_file("..//Screenshot//PopularItem.png")
            log.error("Popular Item is not Found")
        log.info("Capturing all the product price")
        price = page.getPrice()
        try:
            i = -1
            list = []
            for lowPrice in price:
                i = i + 1
                productPrice = list.append(lowPrice.text)
            log.info("Price displayed are: " + str(list))
            log.info("Lowest price is " + min(list))
        except Exception as e:
            self.driver.get_screenshot_as_file("..//Screenshot//ProductList.png")
            log.error("Condition does not matched or Element not found")
        try:
            if lowPrice.text == min(list):
                action.move_to_element(page.getPrice()[i]).perform()
                page.getAddButton()[i].click()
                sleep(2)
                self.driver.get_screenshot_as_file("..//Screenshot//ProductAddedSuccessfully.png")
                log.info("Product added to the cart successfully.")
        except Exception as e:
            self.driver.get_screenshot_as_file("..//Screenshot//ProductAddedToTheCart_fail.png")
            log.error("Condition does not matched or Element not found")
            raise

        ConfirmMessage = page.getconfCart()
        try:
            assert ConfirmMessage == "Product successfully added to your shopping cart", "Text not matched"
            log.info("Confirm message displayed is : " + ConfirmMessage)
        except Exception as e:
            self.driver.get_screenshot_as_file("..//Screenshot//textmatch_fail.png")
            log.error("Condition does not matched or Element not found")
            raise
        productName = page.getproductName()
        log.info("Lowest Price product name displayed is : " + productName)
        productColor = page.getproductColor()
        log.info("Added product color, size displayed is : " + productColor)
        productQuantity = page.getproductQuantity()
        log.info("Added product quantity displayed is : " + productQuantity)
        productPrice = page.getproductPrice()
        log.info("Verifying lowest price product has been added to cart")
        try:
            assert min(list) == productPrice
            log.info("Product price is " + productPrice + " and lowest price is " + min(list))
            log.info("Added product price displayed is : " + productPrice)
        except Exception as e:
            self.driver.get_screenshot_as_file("..//Screenshot//priceMatchFailed_fail.png")
            log.error("Condition does not matched or Element not found")
            raise
        log.info("Clicking on close window button")
        try:
            page.getWindowClosed().click()
            log.info("Window closed successfully ")
        except Exception as e:
            self.driver.get_screenshot_as_file("..//Screenshot//ClosedButton.png")
            log.error("Condition does not matched or Element not found")
            raise
        try:
            log.info("Mouse hover on cart icon")
            page.getViewCart()
            log.info("Cart dialog box opened successfully")
        except Exception as e:
            self.driver.get_screenshot_as_file("..//Screenshot//CartWindowError.png")
            log.error("Condition does not matched or Element not found")
            raise
        cartDialogBoxQuantity = page.getverifyCartQuantity()
        try:
            assert productQuantity == cartDialogBoxQuantity, "Product Quantity not matched with added quantity"
            log.info("Quantity on cart dialog box displayed is : " +cartDialogBoxQuantity+"Matched with added product quantity"+productQuantity)
        except Exception as e:
            self.driver.get_screenshot_as_file("..//Screenshot//productQuantity_failed.png")
            log.error("Product Quantity not matched with added quantity")
            raise
        cartDialogBoxProductName = page.getVerifyProductName()
        log.info("Product name on cart dialog box displayed is : " + cartDialogBoxProductName)
        cartDialogBoxColor = page.getverifyCartColor()
        try:
            assert cartDialogBoxColor == productColor, "Color and Size not Matched with added product"
            log.info("Color, Size on cart dialog box displayed is : " + cartDialogBoxColor)
        except Exception as e:
            self.driver.get_screenshot_as_file("..//Screenshot//ColorSizeMatch_Fail.png")
            log.error("Color and Size not Matched with added product")
            raise
        cartDialogBoxShippingPrice = page.getVerifyShippingPrice()
        try:
            assert cartDialogBoxShippingPrice == "$2.00", "Shipping cost is not matched"
            log.info("Shipping price on cart dialog box displayed is : " + cartDialogBoxShippingPrice)
        except Exception as e:
            self.driver.get_screenshot_as_file("..//Screenshot//ShippingCostMatch_failed.png")
            log.error("Shipping cost is not matched")
            raise
        cartDialogBoxFinalTotalPrice = page.getVerifyAllTotalPrice()
        log.info("Final price on cart dialog box displayed is : " + cartDialogBoxFinalTotalPrice)
        try:
            log.info("Clicking on Checkout Button")
            cart = page.getClickOnCart()
            cartCurrentTab = cart.getTab()
            summaryPageTitle=self.driver.title
            assert summaryPageTitle=="Order - My Store", "Page navigation failed"
            log.info("Navigated successfully on " + cartCurrentTab + " Page")
        except Exception as e:
            self.driver.get_screenshot_as_file("..//Screenshot//Navigation_failed.png")
            log.error("Page navigation failed")
            raise
        log.info(cartCurrentTab + " tab is selected")
        cartProductName = cart.getProductName()
        try:
            assert productName == cartProductName, "Product name not matched"
            log.info("Product name displayed on the cart is: " +cartProductName+ " matched with added product " +productName)
            self.driver.execute_script("window.scrollTo(0, 450)")
            self.driver.get_screenshot_as_file("..//Screenshot//ProductSummaryCart.png")
        except Exception as e:
            self.driver.get_screenshot_as_file("..//Screenshot//NameMatch_Fail.png")
            log.error("Product name not matched")
            raise
        cartProductColor = cart.getProductColor()
        log.info("Product Color, size displayed on the cart is: " +str(cartProductColor)+ " matched with added product color and size  "+str(productColor))

        cartProductPrice = cart.getProductPrice()
        try:
            assert cartProductPrice == productPrice, "Price not matched with added product"
            log.info("Product Unit price displayed on the cart is: " +cartProductPrice+ " Price not matched with added product "+productPrice)
        except Exception as e:
            self.driver.get_screenshot_as_file("..//Screenshot//productPriceMatch_Failed.png")
            log.error("Product name not matched")
        print(cart.getWithoutShippingTotalPrice())
        print(cart.getProductShippingPrice())
        print(cart.getWithShippingTotalPrice())
        print(cart.getAllTotalPrice())

        sleep(5)
