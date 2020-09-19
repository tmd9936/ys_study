from jinja2 import Environment, FileSystemLoader

f_loader = FileSystemLoader('templates')
env = Environment(loader=f_loader)
template = env.get_template('child.html')

ren = template.render(title = 'jinja2 연습', body="바디입니다.")
print(ren)