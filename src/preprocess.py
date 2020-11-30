import re, sys
import inflect 

def remove_punctuation(text):
        # punctuation characters to remove
        punc = '''!()[]{};:"\,<>./?@#$%^&*_~'''

        for char in text:
                if char in punc:
                        text = text.replace(char, '')
                if char == '-':
                        text = text.replace(char, ' ')
        return text

def main(args):
        # parse arguments
        in_file = open(args[0], 'r')
        out_file = open(args[1], 'w')

        text = in_file.readlines()

        # regex to remove all content before the utterance for each line 
        regex_rem_speaker_time = r'(^[^:\r\n]+:[ \t]*)+(.*[0-9]:[0-9][0-9])+([ \t]*)'
        subst_speaker_time = ""

        # regex to remove repeating characters more than four times 
        regex_repeat_char = r'(.)\1+'
        subst_repear_char = "\\1\\1"

        # list to store the utterances 
        txt = []

        for line in text:
                # remove speakers and timestamps
                line = re.sub(regex_rem_speaker_time, subst_speaker_time, line)

                # lowercase
                line = line.lower()

                # replace new line with empty space
                line = ' '.join(line.split())

                # avoid repeating characters more than 4 times

                # avoid repeating words more than 4 times 

                # removing the [inaudible] comments

                # remove punctuation
                line = remove_punctuation(line)

                # spell out the numbers using inflect package
                p = inflect.engine()
                tokens = line.split()
                for token in tokens: 
                        if token.isnumeric():
                                number = remove_punctuation(p.number_to_words(token))
                                line = line.replace(token, number)

                # append non-empty lines to list of all lines
                if line:
                        txt.append(line)

        # join list of text into single string
        txt = ' '.join(txt)

        # save output
        out_file.write(txt)

        # close files
        in_file.close()
        out_file.close()

if __name__ == "__main__":
        main(sys.argv[1:])