import sys
import os

from django.template import Context, Template

def render(template_name):

    c = Context({})

    with open(template_name, 'r') as f:
        t = Template(f.read())

    with open('rendered_template.html', 'w') as f:
        f.write(t.render(c))

    this_dir = os.path.dirname(os.path.abspath(__file__))

    print 'file://{0}/rendered_template.html'.format(this_dir)

