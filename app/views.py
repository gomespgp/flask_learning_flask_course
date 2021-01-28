from app import app

from flask import render_template

@app.route('/')
def index():
    return render_template('public/index.html')

@app.route('/jinja')
def jinja():

    my_name = 'Gabriel'

    age = 19

    langs = ['Python', 'JavaScript', 'PHP', 'Node.js', 'C']

    friends = {
        'Tom': 30,
        'Amy': 60,
        'Tony': 56,
        'Clarissa': 23
    }

    colours = ('Red', 'Greem')

    cool = True

    class GitRemote:
        def __init__(self, name, description, url):
            self.name = name
            self.description = description
            self.url = url
        
        def pull(self):
            return f'Pullin repo {self.name}'
        
        def clone(self):
            return f'Cloning into {self.url}'
    
    my_remote = GitRemote(
        name='Flask Jinja',
        description='Template design tutorial',
        url='https://github.com/gomespgp/jinja.git'
    )
    
    def repeat(x, qty):
        return x * qty

    return render_template(
        'public/jinja.html',
        my_name=my_name,
        age=age,
        langs=langs,
        friends=friends,
        colours=colours,
        cool=cool,
        my_remote=my_remote,
        repeat=repeat
    )

@app.route('/about')
def about():
    return '<h1 style="color: red">About!!!!!</h1>'
