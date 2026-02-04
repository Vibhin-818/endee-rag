
import os

# PASTE YOUR NEW KEY BELOW

KEY = "AIzaSyB0BAfopdq8oNJLCIziSoPtNDjmKvHUdv0" 



import google.generativeai as genai

try:

    genai.configure(api_key=KEY)

    model = genai.GenerativeModel('gemini-1.5-flash')

    response = model.generate_content("Say 'Hello'")

    print(f"\n✅ SUCCESS! Key is working. Response: {response.text}")

except Exception as e:

    print(f"\n❌ FAILURE: {e}")

