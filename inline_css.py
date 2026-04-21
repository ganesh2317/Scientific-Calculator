with open('static/calculator/style.css', 'r', encoding='utf-8') as f:
    css = f.read()
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('<link rel="stylesheet" href="/static/calculator/style.css?v=1.2">', f'<style>\n{css}\n</style>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
with open('calculator/templates/calculator/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
