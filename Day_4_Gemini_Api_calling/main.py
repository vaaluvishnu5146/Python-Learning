from google import genai
from dotenv import load_dotenv

# Load the env variables into venv
load_dotenv()

client = genai.Client()

response = client.models.generate_content(
    model="gemini-flash-latest",
    # config= {
    #     "temperature": 1
    # },
    contents="Explain why indian parents spend more on marriages? Also find and tell me how many marriage happens only because of loans as only source of money. Also tell me list of gifts they buy using mariage loans?",
)

print(response.text)