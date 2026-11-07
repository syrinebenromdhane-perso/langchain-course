from dotenv import load_dotenv
import os

load_dotenv()
#load en var

def main():
    print("Hello Syrine, you're doing a good job")
    print(os.environ.get("OPENAI_API_KEY"))
    
if __name__ == '__main__':
    main()