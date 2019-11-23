import convert_funcs
import data

def output_data(filename, data):
    f = open(filename, 'w')
    for issue_data in data:
        f.write(issue_data.id + '\t' +
                issue_data.text + '\t' +
                ("True" if issue_data.merged else "False") + '\n')

if __name__ == '__main__':
    pickled_data = data.PR.load_all() # load all

    if len(pickled_data) > 0:
        prs = pickled_data[0]

        parsed_data = convert_funcs.convert(prs)

        output_data("input-se-issues", parsed_data[convert_funcs.ISSUE])
        output_data("input-se-review", parsed_data[convert_funcs.REVIEW])
        output_data("input-se-both", parsed_data[convert_funcs.BOTH])

