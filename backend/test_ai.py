import os
import django
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Test OpenAI
print("="*50)
print("Testing OpenAI Connection")
print("="*50)

try:
    import openai
    from openai import OpenAI
    
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    
    # Simple test
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Say 'Hello, OpenAI is working!'"}],
        max_tokens=20
    )
    print("✅ OpenAI Success:", response.choices[0].message.content)
except Exception as e:
    print("❌ OpenAI Error:", str(e))
    print("Type:", type(e).__name__)

# Test Google Gemini
print("\n" + "="*50)
print("Testing Google Gemini Connection")
print("="*50)

try:
    import google.generativeai as genai
    
    genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
    
    # List available models first
    print("Available models:")
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"  - {m.name}")
    
    # Try with correct model name
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content("Say 'Hello, Gemini is working!'")
    print("✅ Gemini Success:", response.text)
except Exception as e:
    print("❌ Gemini Error:", str(e))
    print("Type:", type(e).__name__)