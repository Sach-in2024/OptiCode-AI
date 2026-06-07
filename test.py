import os
from dotenv import load_dotenv

print("=" * 50)
print("STEP 1: Loading .env file...")
load_dotenv()
key = os.getenv("GROQ_API_KEY")
print(f"Key found: {bool(key)}")
print(f"Key value: {repr(key)}")

print("\nSTEP 2: Importing Groq...")
try:
    from groq import Groq
    print("Groq imported: OK")
except Exception as e:
    print(f"Groq import FAILED: {e}")
    exit()

print("\nSTEP 3: Creating Groq client...")
try:
    client = Groq(api_key=key)
    print("Client created: OK")
except Exception as e:
    print(f"Client FAILED: {e}")
    exit()

print("\nSTEP 4: Sending test message to Groq...")
try:
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": "Say: WORKING"}],
        max_tokens=10,
    )
    print(f"Response: {response.choices[0].message.content}")
    print("\n✅ GROQ IS WORKING!")
except Exception as e:
    print(f"API call FAILED: {e}")

print("=" * 50)