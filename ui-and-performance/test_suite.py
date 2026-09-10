import re
from playwright.sync_api import Page, expect
from google import genai


def test_successful_login(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"password\"]").press("Enter")
    #Assertion: confirm login actually succeeded
    expect(page).to_have_url(re.compile(".*inventory.html"))
    expect(page.locator(".title")).to_have_text("Products")

def test_login_with_wrong_password(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").fill("wrongpassword")
    page.locator("[data-test=\"password\"]").press("Enter")

    expect(page.locator("[data-test=\"error\"]")).to_be_visible
    expect(page.locator("[data-test=\"error\"]")).to_contain_text("Username and password do not match")

def test_add_item_to_cart_and_checkout(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"password\"]").press("Enter")
    #Add item to cart
    page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    #assert cart is updated
    expect(page.locator(".shopping_cart_badge")).to_have_text("1")

    #Go to cart
    page.locator("[data-test=\"shopping-cart-link\"]").click()
    expect(page).to_have_url(re.compile(".*cart.html"))

    #Proceed to checkout
    page.locator("[data-test=\"checkout\"]").click()

    #Fill in checkout info
    page.locator("[data-test=\"firstName\"]").fill("test")
    page.locator("[data-test=\"lastName\"]").fill("tester")
    page.locator("[data-test=\"postalCode\"]").fill("07834")
    page.locator("[data-test=\"continue\"]").click()

    #Finish order
    page.locator("[data-test=\"finish\"]").click()

    #confirmation page
    expect(page.locator(".complete-header")).to_have_text("Thank you for your order!")

def test_sort_low_to_high(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"password\"]").press("Enter")

    page.locator("[data-test=\"product-sort-container\"]").click()
    page.locator("[data-test=\"product-sort-container\"]").select_option("lohi")

    expect(page.locator(".inventory_item_price").first).to_have_text("$7.99")

def test_logout(page: Page):
     page.goto("https://www.saucedemo.com/")
     page.locator("[data-test=\"username\"]").fill("standard_user")
     page.locator("[data-test=\"password\"]").fill("secret_sauce")
     page.locator("[data-test=\"password\"]").press("Enter")

     page.locator("#react-burger-menu-btn").click()
     page.locator("[data-test=\"logout-sidebar-link\"]").click()

     expect(page.locator("[data-test=\"login-button\"]")).to_be_visible()

def test_login_with_whitespace_in_username(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").fill("    standard_user     ")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"password\"]").press("Enter")

    # We don't know yet whether the app trims whitespace or not -
    # so we check what ACTUALLY happens, which is the point of this test.
    # If login succeeds despite the spaces, that tells us the app trims input.
    # If it fails, that's a legitimate finding worth noting.
    expect(page.locator("[data-test=\"error\"]")).to_be_visible()
    #Test passed which confirms that login field does not trim leading/trailing whitespaces
    #- an AI-suggested edge case that a manual review might have skipped

def test_checkout_confirmation_message_is_valid(page: Page):
    #Full checkout flow
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"password\"]").press("Enter")
    page.locator("[data-test=\"add-to-cart-sauce-labs-bike-light\"]").click()
    page.locator("[data-test=\"shopping-cart-link\"]").click()
    page.locator("[data-test=\"checkout\"]").click()
    page.locator("[data-test=\"firstName\"]").fill("User")
    page.locator("[data-test=\"lastName\"]").fill("Tester")
    page.locator("[data-test=\"postalCode\"]").fill("10001")
    page.locator("[data-test=\"continue\"]").click()
    page.locator("[data-test=\"finish\"]").click()

    #Capture the actual confirmation test from the page
    confirmation_text = page.locator("[data-test=\"complete-header\"]").text_content()

    #Ask the AI to judge whether this message correctly confirms the order
    client = genai.Client()
    response = client.models.generate_content(
        model = "gemini-3.6-flash",
        contents=f"""A user just completed checkout on an ecommerce site. 
        The page displayed this message: "{confirmation_text}"

        Does this message clearly and correctly confirm that the order was placed successfully?
        Answer with only YES or NO, followed by a one-sentence reason."""
    )

    ai_judgement = response.text.strip()
    print(f"AI judgement: {ai_judgement}")

    assert ai_judgement.upper().startswith("YES"), f"AI flagged the confirmation message as unclear: {ai_judgement} "
     

                                                  
