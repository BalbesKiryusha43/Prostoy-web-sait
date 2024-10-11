from flask import Flask, request, render_template_string, redirect, url_for
app = Flask(__name__)
games = []
form_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Добавить видеоигру</title>
    <style>
        body {
            background-image: url('https://icegames.store/f1b6829d-d5f9-4fcb-a67b-d854ec6706ac.jpg');
            background-size: cover;
            font-family: Arial, sans-serif;
            color: white;
            text-align: center;
        }
        .container {
            background-color: rgba(0, 0, 0, 0.6);
            padding: 20px;
            margin: 100px auto;
            width: 50%;
            border-radius: 10px;
        }
        input[type="text"], input[type="number"] {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border-radius: 5px;
            border: none;
        }
        input[type="submit"] {
            padding: 10px 20px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        input[type="submit"]:hover {
            background-color: #45a049;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            background-color: rgba(255, 255, 255, 0.2);
            padding: 10px;
            margin: 5px;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Добавить видеоигру</h1>
        <form method="POST" action="/">
            <label for="name">Название игры:</label><br>
            <input type="text" id="name" name="name" required><br><br>
            <label for="genre">Жанр:</label><br>
            <input type="text" id="genre" name="genre" required><br><br>
            <label for="year">Год выпуска:</label><br>
            <input type="number" id="year" name="year" min="1950" max="2024" required><br><br>
            <label for="rating">Оценка (0-10):</label><br>
            <input type="number" id="rating" name="rating" min="0" max="10" required><br><br>
            <input type="submit" value="Добавить игру">
        </form>
        <h2>Список видеоигр:</h2>
        <ul>
            {% for game in games %}
            <li>{{ game['name'] }} - Жанр: {{ game['genre'] }} - Год выпуска: {{ game['year'] }} - Оценка: {{ game['rating'] }}</li>
            {% endfor %}
        </ul>
    </div>
</body>
</html>
"""
@app.route('/', methods=['GET', 'POST'])
def add_game():
    if request.method == 'POST':
        name = request.form.get('name')
        genre = request.form.get('genre')
        year = request.form.get('year')
        rating = request.form.get('rating')
        if not name or not genre or not year or not rating:
            return "Некорректный ввод данных", 400
        try:
            year = int(year)
            rating = float(rating)
            if year < 1950 or year > 2024:
                return "Год выпуска должен быть в пределах от 1950 до 2024", 400
            if rating < 0 or rating > 10:
                return "Оценка должна быть в пределах от 0 до 10", 400
        except ValueError:
            return "Оценка и год выпуска должны быть числом", 400
        games.append({'name': name, 'genre': genre, 'year': year, 'rating': rating})
        return redirect(url_for('add_game'))
    return render_template_string(form_template, games=games)
if __name__ == '__main__':
    app.run(debug=True)
