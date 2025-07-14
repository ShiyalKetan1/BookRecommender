from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load the book data
books = pd.read_csv('books.csv')

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

# @app.route('/recommend', methods=['POST'])
# def recommend():
#     user_input = request.form['user_input'].strip().lower()
#     recommendations = []

#     # Match book name
#     matched = books[books['Book Name'].str.lower().str.contains(user_input)]

#     if not matched.empty:
#         genre = matched.iloc[0]['Genre']
#         similar_books = books[books['Genre'] == genre]
#         for book in similar_books['Book Name']:
#             if book.lower() != matched.iloc[0]['Book Name'].lower():
#                 recommendations.append(book)
#     else:
#         # Try matching genre
#         genre_match = books[books['Genre'].str.lower() == user_input]
#         if not genre_match.empty:
#             for book in genre_match['Book Name']:
#                 recommendations.append(book)
#         else:
#             recommendations = ["No recommendations found."]

#     return render_template('index.html', recommendations=recommendations)


@app.route('/recommend', methods=['POST'])
def recommend():
    user_input = request.form['user_input'].strip().lower()
    recommendations = []

    # Match by Book Name
    matched = books[books['Book Name'].str.lower().str.contains(user_input)]

    if not matched.empty:
        genre = matched.iloc[0]['Genre']
        similar_books = books[books['Genre'] == genre]
        # for book in similar_books['Book Name']:
        for book in similar_books['Book Name'].head(5):

            if book.lower() != matched.iloc[0]['Book Name'].lower():
                recommendations.append(book)

    else:
        # Match by Author
        author_match = books[books['Author'].str.lower().str.contains(user_input)]
        if not author_match.empty:
            # for book in author_match['Book Name']:
            for book in author_match['Book Name'].head(5):

                recommendations.append(book)

        else:
            # Match by Genre
            genre_match = books[books['Genre'].str.lower().str.contains(user_input)]
            if not genre_match.empty:
                # for book in genre_match['Book Name']:
                for book in genre_match['Book Name'].head(5):

                    recommendations.append(book)
            else:
                recommendations = ["No recommendations found."]

    return render_template('index.html', recommendations=recommendations)


if __name__ == '__main__':
    #app.run(debug=True)
    app.run(debug=True, host='0.0.0.0')

