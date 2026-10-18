from pydantic import BaseModel


class User(BaseModel):
  name: str
  age: int
  email: str

# Validates and coerces types
user = User(name="Alice", age="25", email="alice@example.com")
print(user.model_dump())

user = User(name="Alice", age="25", email="12345")
print(user.model_dump())


from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-flash-latest",
    contents="Explain how AI works in a few words",
)

print(response.text)