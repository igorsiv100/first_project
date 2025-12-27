print('Hello from repository!')

def print_author():
# Допишите здесь ваш код
    from dotenv import load_dotenv
    import os
    load_dotenv()
    author = os.getenv('AUTHOR')
    print(f"Автор проекта: {author}")

print_author()
