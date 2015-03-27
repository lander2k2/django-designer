===============
django-designer
===============

Allow designers to work on your templates without having to run
the Django development server, database etc.

Designer's workflow:

#. Pulls repo
#. Edits template, makes it look pretty
#. Runs django-designer function to render template and produce html file
#. Points browser to file
#. Views pretty rendered template in browser
#. Repeats steps 2 and 3, refreshes browser
#. Commits and pushes pretty templates

Note: To state the obvious, context variables are not rendered on page.
View functions are not called.  Context variables are often not needed
when a desinger is viewing templates for design purposes.

-------
Install
-------
Install package::

    pip install django-designer

-----
Usage
-----
Run::

    $ ./manage.py shell
    >>> from designer.render import template
    >>> template('your_app/templates/home.html')
    file:///Users/you/Projects/your_project/your_app/templates/home_rendered.html

Copy-paste output into browser address bar and view rendered template.

Recommend you add ``*_rendered.html`` to your .gitignore.

