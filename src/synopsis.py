import json
import openai
from src.env import Config
import openai
from src.configuration import CONFIG_PATH, SYNOPSIS_PATH
import time

def load_env():
    openai.api_key = Config.OPENAI_API_KEY

class SynopsisGeneration:
    def __init__(self, config_path):
        try:
            with open(config_path, "r") as f:
                self.config = json.load(f)
        except json.JSONDecodeError as e:
            print(f"Error reading {config_path}: {e}")
            raise
        except FileNotFoundError as e:
            print(f"Configuration file not found: {e}")
            raise

    # generate synopsis
    def generate_synopsis(self, retries=3):
        prompt = self.config['synopsis']
        for attempt in range(retries):
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.5,
                    max_tokens= 500
                )
                return response.choices[0].message['content'].strip()
            except openai.error.RateLimitError:
                if attempt < retries - 1:
                    print(f"Rate limit exceeded. Retrying in {2 ** attempt * 30} seconds...")
                    time.sleep(2**attempt *30) #exponential backoff
                else:
                    print("Maximum retry attempts reached. Unable to generate synopsis")
                    raise
                
            except Exception as e:
                print(f"Error generating synopsis: {e}")
                raise 
    

def save_synopsis(config_path, output_path):
    s_gen = SynopsisGeneration(config_path)
    synopsis = s_gen.generate_synopsis()
    with open(output_path, 'w') as f:
        json.dump({"synopsis": synopsis}, f, indent=4)

if __name__ == "__main__":
    save_synopsis(CONFIG_PATH, SYNOPSIS_PATH)
