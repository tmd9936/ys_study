from jinja2 import Environment, FileSystemLoader

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
template = env.get_template('for_structure.txt')

colors = ['red', 'blue', 'yellow']
ren = template.render(colors=colors)

