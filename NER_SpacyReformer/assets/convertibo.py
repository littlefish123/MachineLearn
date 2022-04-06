import pandas as pd
import json
import sys, getopt


# convertibo -i <input_file> -o <output_file>

def clean(text):
    filters = ["!", "#", "$", "%", "&", "(", ")", "/", "*", ". ", ":", ";", "<", "=", ">", "?", "@", "[",
               "\\", "]", "_", "`", "{", "}", "~", "'"]
    for i in text:
        if i in filters:
            text = text.replace(i, " " + i)

    return text


def mark_sentence(parsetext, s, match_list):

    # initialize each word to be 'O'
    word_dict = {}
    for word in parsetext.split():
        if word[-1] == '.':
            word = word[:-1]
        word_dict[word] = 'O'

    for start,end, e_type in match_list['entities']:
        temp_str = s[start:end]
        tmp_list = temp_str.split()
        if len(tmp_list) > 1:
            word_dict[tmp_list[0]] = 'B-' + e_type
            for w in tmp_list[1:]:
                word_dict[w] = 'I-' + e_type
        else:
            word_dict[temp_str] = 'B-' + e_type

    return word_dict


def create_data(df, filepath):

    with open(filepath, 'w') as f:
        for id, row in df.iterrows():
            text = clean(row.text)
            d = mark_sentence(text, row.text, row.annotation)

            for i in d.keys():
                f.writelines(i + ' ' + d[i] + '\n')
            f.writelines('\n')

    f.close()

def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ['ifile=', 'ofile='])
        for opt, arg in opts:
            if opt == '-h':
                print('convertibo -i <inputfile> -o <outputfile?')
                sys.exit()
            elif opt in ("-i", "--ifile"):
                inputfile = arg
            elif opt in ("-o", "--ofile"):
                    outputfile = arg
    except getopt.GetoptError:
        print('convertibo -i <inputfile> -o <outputfile?')
        sys.exit(2)

    with open(inputfile) as f:
        data = json.load(f)
        df = pd.DataFrame(data, columns=['text', 'annotation'])
        create_data(df, outputfile)


if __name__ == '__main__':
    main(sys.argv[1:])

