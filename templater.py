from jinja2 import Environment, PackageLoader, select_autoescape
import os

app_name = 'app'
env = Environment(
	loader=PackageLoader(app_name),
	autoescape=select_autoescape()
)


files = os.listdir('templates')
files.remove('base.html')

titles = {
	'contacts.html': ' - Contacts',
	'equipment.html': ' - Equipment',
	'services.html': ' - Services',
	'index.html': '',
	
	'current_operations.html': ' - Current Operations',
	'data_centers.html': ' - Data Centers',
	'environmental_services.html': ' - Environmental Services'

}


template = None
for file in files:
	template = env.get_template(file)
	with open(file, 'w') as f:
		t = titles[file]
		f.write(template.render(title=t))

#with open('test.html', 'w') as file:
#	file.write(template.render(title='Equipment'))