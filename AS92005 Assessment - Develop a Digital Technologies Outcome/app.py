from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/make', methods=['GET', 'POST'])
def make():
    if request.method == 'POST':
        # Get form values, checking if skip buttons were pressed
        pepeha = {
            'name': request.form.get('name') if 'skip_name' not in request.form else None,
            'mountain': request.form.get('mountain') if 'skip_mountain' not in request.form else None,
            'river': request.form.get('river') if 'skip_river' not in request.form else None,
            'sea': request.form.get('sea') if 'skip_sea' not in request.form else None,
            'tribe': request.form.get('tribe') if 'skip_tribe' not in request.form else None,
            'sub_tribe': request.form.get('sub_tribe') if 'skip_sub_tribe' not in request.form else None,
            'meeting_ground': request.form.get('meeting_ground') if 'skip_meeting_ground' not in request.form else None,
            'meeting_house': request.form.get('meeting_house') if 'skip_meeting_house' not in request.form else None,
            'ancestor': request.form.get('ancestor') if 'skip_ancestor' not in request.form else None,
            'family': request.form.get('family') if 'skip_family' not in request.form else None
        }

        # Pass pepeha to the template, skipping empty fields
        return render_template('pepeha.html', pepeha=pepeha)

    return render_template('make.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
