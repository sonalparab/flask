from flask import Flask

my_app = Flask(__name__)

@my_app.route('/')
def root():
    return "<h2>Welcome</h2>"
@my_app.route('/two')
def two():
    return "<h3>A second route</h3>"
@my_app.route('/three')
def three():
    return "<h3>A third route</h3>"
	
if __name__ == '__main__':
	my_app.run()
