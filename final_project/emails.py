import string
import pickle
from pathlib import Path
from nltk.stem import SnowballStemmer
from progress.bar import Bar


# Copied from text learning mini-project
def parse_out_text(path):
    """Get the content of an email"""

    words = ""
    stemmer = SnowballStemmer("english")

    with path.open() as f:
        all_text = f.read()
        content = all_text.split("X-FileName:")

        if len(content) > 1:
            # Remove punctuations and numbers
            text_string = content[1].translate({
                ord(char): None for char in (string.punctuation + string.digits)
            })

            # Stem each word, then combine into single string
            words = " ".join([stemmer.stem(x) for x in text_string.split()])

    return words


def get_all_words_by_author(email):
    """Get all the email content sent from a specific email address"""

    list_path = Path("emails_by_address/from_%s.txt" % email)
    contents = []

    # The corpus doesn't contain some of the email data
    if list_path.exists():

        with list_path.open() as f:
            # Every line of the reference file refers to an actual email
            for line in f:

                # The reference path is actually wrong in our case,
                # they all have a prefix of "enron_mail_20110402/maildir/",
                # but the maildir/ is actually located in our parent folder
                incorrect_path = Path(line.strip())
                real_path = Path("..", *incorrect_path.parts[1:]).resolve()

                contents.append(parse_out_text(real_path))

    # Return a single string which contains all of the content
    return " ".join(contents)


if __name__ == "__main__":
    with open("final_project_dataset.pkl", "rb") as f:
        dataset = pickle.load(f)

    word_data = {}

    # Output format: {"NAME": "CONTENT", ...}

    for name, row in Bar("Processing").iter(sorted(dataset.items())):
        # These two are outliers
        if name not in ("TOTAL", "THE TRAVEL AGENCY IN THE PARK"):
            if row["email_address"] != "NaN":
                word_data[name] = get_all_words_by_author(row["email_address"])
            else:
                word_data[name] = ""

    with open("word_data.pkl", "wb") as f:
        pickle.dump(word_data, f)