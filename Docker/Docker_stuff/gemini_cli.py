import google.generativeai as genai
import sys
import os

# Unbuffer output for web terminal
sys.stdout.reconfigure(line_buffering=True)
sys.stderr.reconfigure(line_buffering=True)

# Configure API key
api_key = os.environ.get('GEMINI_API_KEY')
if not api_key:
    print("Error: GEMINI_API_KEY environment variable not set!", flush=True)
    print("Run: export GEMINI_API_KEY='your-api-key-here'", flush=True)
    sys.exit(1)

genai.configure(api_key=api_key)

# Create the model
model = genai.GenerativeModel('gemini-1.5-flash')

print("Gemini CLI - Type your questions (type 'quit' to exit)", flush=True)
print("=" * 50, flush=True)

while True:
    try:
        sys.stdout.write("\nYou: ")
        sys.stdout.flush()
        prompt = sys.stdin.readline().strip()
        
        if prompt.lower() in ['quit', 'exit', 'q']:
            print("Goodbye!", flush=True)
            break
        
        if not prompt:
            continue
            
        print("\nThinking...", flush=True)
        response = model.generate_content(prompt)
        print(f"\nGemini: {response.text}\n", flush=True)
        
    except KeyboardInterrupt:
        print("\n\nGoodbye!", flush=True)
        break
    except Exception as e:
        print(f"\nError: {e}\n", flush=True)
