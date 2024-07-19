import json
import openai
from env import Config
from configuration import CONFIG_PATH, REVIEW_PATH

def load_env():
    openai.api_key = Config.OPENAI_API_KEY

class ReviewGeneration:
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

    #generate review
    def generate_review(self):
        prompt = self.config['review']
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.5,
                max_tokens=400
            )
            return response.choices[0].message['content'].strip()
        except Exception as e:
            print(f"Error generating review: {e}")
            raise
        
def save_review(config_path, output_path):
    r_gen = ReviewGeneration(config_path)
    review = r_gen.generate_review()
    with open(output_path, 'w') as f:
        json.dump({"review": review}, f, indent=4)

if __name__ == "__main__":
    save_review(CONFIG_PATH, REVIEW_PATH)