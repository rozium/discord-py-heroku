import argparse
import csv
from owa_discordbot import settings
from owa_discordbot.logging import owa_logger as logger
from owa_discordbot.database import get_session
from owa_discordbot.database.models import Question, LangEnum


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Import csv data into the database.")
    parser.add_argument("csv_dir", help="The location of the csv file.")
    args = parser.parse_args()

    logger.info(f"Importing data from {args.csv_dir}")
    with open(args.csv_dir, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        count = 0
        session = get_session()
        for row in reader:
            question = Question(
                text=row["question"],
                lang=LangEnum[row["lang"]],
                question_type=row["question_type"],
            )
            session.add(question)
            logger.debug(row)
            count += 1
        session.commit()
        session.close()
        logger.info(f"Imported {count} rows")
