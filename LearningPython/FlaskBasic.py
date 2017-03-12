from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'This is a homepage. Method used: {}'.format(request.method)

@app.route('/contact')
def contact():
    return '<h2>email me at: mjaviatornike@gmail.com</h2>'

@app.route('/profile/<username>')
def profile(username):
    return '<h1>hello {}</h1>'.format(username)

@app.route('/post/int:post_id')
def show_post(post_id):
    return '<h1>Here is the post with id: {}</h1>'.format(post_id)

# only start the app when file is called directly
if __name__ == '__main__':
    app.run(debug=True)