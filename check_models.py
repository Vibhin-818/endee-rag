
import google.generativeai as genai

import os



# --- PASTE YOUR KEY BELOW ---

KEY = "AIzaSyB0BAfopdq8oNJLCIziSoPtNDjmKvHUdv0"



genai.configure(api_key=KEY)



print(f"\n🔍 Checking available models for key: {KEY[:5]}...")



try:

    count = 0

    # List all models your project has access to

    for m in genai.list_models():

        if 'generateContent' in m.supported_generation_methods:

            print(f"   ✅ FOUND: {m.name}")

            count += 1

    

    if count == 0:

        print("\n❌ NO MODELS FOUND.")

        print("   Reason: Your API Key belongs to an old 'gen-lang-client' project.")

        print("   Fix: Create a NEW API Key in a NEW Project at aistudio.google.com")

    else:

        print(f"\n🎉 Success! You have access to {count} models.")

        print("   Update your app.py to use one of the names above (e.g., 'gemini-pro').")



except Exception as e:

    print(f"\n❌ ERROR: {e}")

