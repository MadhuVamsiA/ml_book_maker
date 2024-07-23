from env import Config
import prompts
import json
import openai 
from configuration import CONFIG_PATH, CHAPTERS_CONTENT_PATH

model = "gpt-4"
temperature = 0.5
max_tokens =3500
prompt = prompts.generate_prompt(book="book",book_title="book_title")

def load_env():
    openai.api_key = Config.OPENAI_API_KEY

class BookGenerator:
    def __init__(self,config_path):
        try:
            with open(config_path, "r") as f:
                self.config = json.load(f)
        except json.JSONDecodeError as e:
            print(f"Error reading {config_path}: {e}")
            raise
        except FileNotFoundError as e:
            print(f"Configuration file not found: {e}")
            raise
    
    #generate content
    def generate_content(self, prompt):
        try:
            response = openai.ChatCompletion.create(
                model=model,
                messages=[
                    {"role": "system", "content": prompts.system_prompt},
                    {"role": "user", "content": prompt}
                ],
                temperature=temperature,
                max_tokens=max_tokens
            )
            return response.choices[0].message['content'].strip()
        except Exception as e:
            print(f"Error generating content: {e}")
            raise

    def generate_chapters(self):
        chapters_content = {}
        for chapter in self.config['chapters']:
            chapters_content[chapter['title']] = ""
            for prompt in chapter['prompts']:
                content = self.generate_content(prompt)
                chapters_content[chapter['title']] += content + "\n\n"
        return chapters_content

def save_chapters_content(config_path, output_path):
    content_gen = BookGenerator(config_path)
    chapters_content = content_gen.generate_chapters()
    with open(output_path, 'w') as f:
        json.dump(chapters_content, f, indent=4)

if __name__ == "__main__":
    save_chapters_content(CONFIG_PATH, CHAPTERS_CONTENT_PATH)