from utils.logger import Logger
import sqlite3

logger = Logger(name="account_manager").logger
# Initialize the database
conn = sqlite3.connect('db/credentials.db')
c = conn.cursor()


def add_account(platform, username, password, proxy=""):
    try:
        # Password should be hashed before inserting into the database in real applications!
        c.execute(
            "INSERT INTO credentials (platform, username, password, banned, start_date, ban_date, bot_logic, bot_type, proxy) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (platform, username, password, None, None, None, None, None, proxy))
        # Commit the transaction
        conn.commit()
    except Exception as e:
        logger.error("Problem with adding account " + str(e))


def delete_account(platform, username):
    try:
        c.execute("DELETE FROM credentials WHERE platform = ? AND username = ?", (platform, username))
        conn.commit()
    except Exception as e:
        logger.error("Problem with deleting account " + str(e))


def get_account(platform, username):
    c.execute("SELECT * FROM credentials WHERE platform = ? AND username = ?", (platform, username))
    return c.fetchall()


def get_random_phantom_profile():
    c.execute("SELECT * FROM phantom_profiles WHERE email_password = "" ORDER BY RANDOM() LIMIT 1")
    row = c.fetchone()
    return row[0], row[1], row[2], row[3], row[4], row[5]


def get_bot(platform, bot_type, bot_level):
    # Check for the existence of the required bot
    c.execute("""
        SELECT bots.*, phantom_profiles.* 
        FROM bots 
        JOIN phantom_profiles ON bots.phantom_profile_id = phantom_profiles.id
        WHERE bots.platform = ? 
        AND bots.bot_type = ? 
        AND bots.bot_level = ?
        AND bots.banned IS NULL
    """, (platform, bot_type, bot_level))
    bot = c.fetchone()

    # If the bot does not exist, create it
    if not bot:
        # Find a suitable phantom profile
        c.execute("""
            SELECT id FROM phantom_profiles 
            WHERE facebook = 1 
            AND id NOT IN (SELECT phantom_profile_id FROM bots)
        """)
        profile = c.fetchone()

        # If a suitable profile is found, insert a new bot
        if profile:
            profile_id = profile[0]
            # Insert the new bot into the bots table
            c.execute("""
                INSERT INTO bots (platform, phantom_profile_id, banned, bot_lifetime, bot_type, bot_logic, bot_info) 
                VALUES (?, ?, NULL, NULL, ?, ?, NULL)
            """, (platform, profile_id, bot_type, bot_level))
            conn.commit()
            logger.info("New bot created with phantom profile ID:", profile_id)

            # Return the new bot
            c.execute("""
                SELECT bots.*, phantom_profiles.* 
                FROM bots 
                JOIN phantom_profiles ON bots.phantom_profile_id = phantom_profiles.id
                WHERE bots.platform = ? 
                AND bots.bot_type = ? 
                AND bots.bot_level = ?
                AND bots.banned IS NULL
            """, (platform, bot_type, bot_level))
            new_bot = c.fetchone()
            return new_bot[13] + new_bot[15], new_bot[14]
        else:
            logger.info("No suitable phantom profile found.")

    else:
        return bot[13] + bot[15], bot[14]
