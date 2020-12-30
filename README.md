# Description

Discord bot for helping conversation by generating questions.

# Setup

## Local deployment

1. Install the dependencies using requirements.txt [`pip install -e .`] or poetry [`poetry intall -v`]. If using poetry, remember to activate the shell using `poetry shell`.
2. Create a `.env` file in the repo root by copying the `.env.template`. The `.env` file *should not be commited* and is already ignored in `.gitignore`.
3. Edit the `DB_HOST` variable in `.env`. It's possible to use other SQL backends (e.g. MySQL, PostgreSQL).
2. Create the database by running `python owa_discordbot/scripts/db/migrate.py`.
3. Import the questions from a csv file by running `python owa_discordbot/scripts/db/import_csv.py [csv directory]`. A csv file is already included in `data/raw/questions.csv`, but you can create your own by following its headers.
4. Set your bot token and command-prefix in `.env` as well as other available settings.
5. Run the bot by running `python owa_discordbot/main.py`.

# Notes

- The question table does not have unique constraint on its content, so duplicate questions may exist.
- The database module uses sqlalchemy framework which not async. Since the bot client has some async functions, concurrent calls may experience blocking or inconsistency. But since currently the bot only performs read operations, the inconsistency concern can be deferred for now.
