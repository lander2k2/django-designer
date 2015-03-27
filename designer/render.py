import sys
import os

from django.template import Context, Template

def template(template_name):

    c = Context({})

    with open(template_name, 'r') as f:
        t = Template(f.read())

    write_path = template_name.replace('.html', '_rendered.html')

    with open(write_path, 'w') as f:
        f.write(t.render(c))

    rendered_path = os.path.abspath(write_path)
    
    print 'file://{0}'.format(rendered_path)

