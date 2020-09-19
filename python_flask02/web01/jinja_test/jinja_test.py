from jinja2 import Environment, FileSystemLoader

file_loader = FileSystemLoader('templates')
env = Environment(loader = file_loader)
template = env.get_template('hello.txt')

template = env.get_template('dogs.txt')
ren = template.render(name = '김망떨', animal='고양이')

template = env.get_template('person_info.txt')

person = {}
person['name'] = '김말똥'
person['salary'] = 3000

ren = template.render(data = person)

template = env.get_template('if_structure.txt')
ren = template.render(truth = True)

print(ren)