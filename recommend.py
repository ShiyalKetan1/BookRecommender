import pandas as pd

# Load book data
books = pd.read_csv('books.csv', encoding='latin1')

# Ask the user for input
user_input = input("Enter a book name or genre: ").strip().lower()

# Try to match book name
matched = books[books['Book Name'].str.lower().str.contains(user_input)]

if not matched.empty:
    genre = matched.iloc[0]['Genre']
    # print(f"\nRecommended books based on genre '{genre}':")
    print(f"\n📚 Recommended books in '{genre}' genre:")

    similar_books = books[books['Genre'] == genre]
    for book in similar_books['Book Name']:
        if book.lower() != matched.iloc[0]['Book Name'].lower():
            print(f"- {book}")
else:
    # If not a book name, try matching genre
    genre_match = books[books['Genre'].str.lower() == user_input]
    if not genre_match.empty:
        print(f"\nBooks in '{user_input}' genre:")
        for book in genre_match['Book Name']:
            print(f"- {book}")
    else:
        print("Sorry, no matching books or genre found.")
