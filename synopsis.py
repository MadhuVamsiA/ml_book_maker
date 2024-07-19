import json
from env import Config
import openai
from configuration import CONFIG_PATH, SYNOPSIS_PATH


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
    def generate_synopsis(self):
        prompt = self.config['synopsis']
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
