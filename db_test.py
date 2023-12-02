import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('db/credentials.db')
c = conn.cursor()

c.execute("""
    SELECT id FROM phantom_profiles 
    WHERE facebook = 1 
    AND id NOT IN (SELECT phantom_profile_id FROM bots)
""")



# Fetch all results from the cursor
bot = c.fetchone()
print(bot[0])


# Close the connection
conn.close()

