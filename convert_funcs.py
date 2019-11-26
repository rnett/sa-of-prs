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

def has_code_snippet(text):
    match = re.search(r"```(.+)```", str(text))
    if match:
        return True
    return False

def has_image(text):
    match = re.search(r"!\[[A-Za-z]*\]\((.+)\)", str(text))

    if match:
        return True
    return False


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
        issue_has_code_snippet = has_code_snippet(parsed_issue_comments)
        review_has_code_snippet = has_code_snippet(parsed_review_comments)

        if issue_has_code_snippet or review_has_code_snippet:
            both_has_code_snippet = True
        else:
            both_has_code_snippet = False

        issue_has_image = has_image(parsed_issue_comments)
        review_has_image = has_image(parsed_review_comments)

        if issue_has_image or review_has_image:
            both_has_image = True
        else:
            both_has_image = False

        results[ISSUE].append(TextData(pr.id, ISSUE, parsed_issue_comments, pr.merged, issue_has_code_snippet, issue_has_image))
        results[REVIEW].append(TextData(pr.id, REVIEW, parsed_review_comments, pr.merged, review_has_code_snippet, review_has_image))
        results[BOTH].append(TextData(pr.id, BOTH, parsed_issue_comments + parsed_review_comments, pr.merged, both_has_code_snippet, both_has_image))

    return results


