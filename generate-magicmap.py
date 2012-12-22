from jinja2 import Environment, PackageLoader
env = Environment(loader=PackageLoader('magicmap', 'templates'))
template = env.get_template('template.html')
output = template.render(the='variables', go='here')
with open("template.html", "w") as f:
    f.write(output)
