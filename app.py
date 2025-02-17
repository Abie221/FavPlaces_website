from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

# Placeholder route for city pages; you'll expand this later.
@app.route('/<city_name>')
def city(city_name):
    return f"City page for {city_name.capitalize()}"

@app.route('/suggest', methods=['GET', 'POST'])
def suggest():
    if request.method == 'POST':
        # Here you would handle the submitted form data,
        # e.g., extract values and save them to the database.
        # For now, we'll just print them or redirect.
        country = request.form.get('country')
        city = request.form.get('city')
        place = request.form.get('place')
        description = request.form.get('description')
        rating = request.form.get('rating')
        story = request.form.get('story')
        # Process the data as needed (e.g., insert into your database)
        print(country, city, place, description, rating, story)
        return redirect(url_for('home'))
    return render_template('suggest.html')

@app.route('/warsaw')
def warsaw():
    return render_template('warsaw.html')


if __name__ == '__main__':
    app.run(debug=True)
