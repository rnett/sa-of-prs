import re

ISSUE = "issue"
REVIEW = "review"
BOTH = "both"

class TextData:
    def __init__(self, id, type, text, merged, images, code_snippets):
        self.id = id
        self.type = type
        self.text = text
        self.merged = merged
        self.images = images
        self.code_snippets = code_snippets

    def __repr__(self):
        return ("TextData(" +
                "id: " + self.id + ", "
                "type: " + self.type + ", "
                " ... ) ")

def parse_text(text):
    combined_texts = " ".join(text)
    combined_texts = " ".join(combined_texts.split('\r\n'))  # remove \r\n between comments
    single_line_text = re.sub(r'\r|\n', ' ', combined_texts)  # remove remaining \r and \n
    return single_line_text

# takes in a list of PRs and creates a
# dict with keys of type of text and a list of TextData objects
# [data.PR] -> { str : [TextData] }
def convert(prs):
    results = {
        ISSUE: [],
        REVIEW: [],
        BOTH: []
    }

    for pr in prs:

        id = pr.id

        parsed_issue_comments = parse_text(pr.issue_comments)
        parsed_review_comments = parse_text(pr.review_comments)

        results[ISSUE].append(TextData(pr.id, ISSUE, parsed_issue_comments, pr.merged, False, False))
        results[REVIEW].append(TextData(pr.id, REVIEW, parsed_review_comments, pr.merged, False, False))
        results[BOTH].append(TextData(pr.id, BOTH, parsed_issue_comments + parsed_review_comments, pr.merged, False, False))

    return results


