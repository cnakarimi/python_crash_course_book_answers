from pathlib import Path

path = Path('learning_python.txt')
content = path.read_text()
print(content)
new_content=content.replace('Python', 'C')
print(new_content)