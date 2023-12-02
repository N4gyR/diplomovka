import sqlite3
import random
from datetime import datetime, timedelta
from itertools import product

# Create or connect to a SQLite database
conn = sqlite3.connect('db/MyDB.db')
cursor = conn.cursor()

# Create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS phantom_profiles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    surname TEXT,
    lastname TEXT,
    date_of_birth TEXT,
    sex TEXT,
    username TEXT UNIQUE,
    mail_password TEXT
);
''')

uncommon_surnames = [
    'Zephyr', 'Quill', 'Vortex', 'Gryffon', 'Kaelthas',
    'Obsidian', 'Pyre', 'Stratos', 'Thaladred', 'Vigil',
    'Wraith', 'Xanadu', 'Ysera', 'Zephyra', 'Altair',
    'Baelnorn', 'Celestia', 'Duskrunner', 'Eirwen', 'Frostveil'
]

uncommon_firstnames = [
    'Lyra', 'Tyrion', 'Elara', 'Arya', 'Maelis',
    'Zaela', 'Orion', 'Yennefer', 'Quorra', 'Thranduil',
    'Galen', 'Lysandra', 'Morgana', 'Oberyn', 'Valkyrie',
    'Xerxes', 'Yara', 'Zenobia', 'Astrid', 'Branwen'
]

sexes = ['M', 'F']

# Generate unique combinations
combinations = list(product(uncommon_surnames, uncommon_firstnames, sexes))

# Shuffle the combinations to randomize
random.shuffle(combinations)

# Generate and insert rows
for i, (surname, lastname, sex) in enumerate(combinations):
    birth_date = datetime(1980, 1, 1) + timedelta(days=i)  # Unique date of birth
    birth_date_str = birth_date.strftime('%Y-%m-%d')
    username = f"{surname.lower()}.{lastname.lower()}.{i}"  # Unique username
    cursor.execute("INSERT INTO phantom_profiles (surname, lastname, date_of_birth, sex, username, mail_password) VALUES (?, ?, ?, ?, ?, ?)",
                   (surname, lastname, birth_date_str, sex, username, ""))

# Commit the changes and close the connection
conn.commit()
conn.close()
