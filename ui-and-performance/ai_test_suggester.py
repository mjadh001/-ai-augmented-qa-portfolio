from google import genai

client = genai.Client()

page_description = """
This is a login page for an ecommerce site (Sauce Demo).
It has a username field, a password field, and a login button.
Known accepted username: standard_user, locked_out_user, problem_user.
"""

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=f"""Given this page description, suggest 3 additional edge-case test scenarios
    a QA engineer might miss. Be specific and concise.
    
    Page desctiption:{page_description}"""
)

print(response.text)

