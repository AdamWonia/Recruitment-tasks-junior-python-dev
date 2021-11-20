"""
Task 3.

So, a third task. It might be a bit tricky. All you need to do is *just* justify a given text.
The algorithm you'll design has to be somewhat elastic - the width of formatted text should be
parameterized with maximum_width arg. The result should be returned as a list with every
line as a separate element.

Few notes:
    ● The justification should be greedy - it means that you should fit as many words as
      possible in a single line.
    ● Add spaces ' ' to make sure that each line has the exact length of maximum_width.
    ● Spaces between words should be distributed evenly.
    ● The last line should be aligned left with no additional spaces (between words or
      trailing).

Example 1:

Input: words = "Hey there mate, it’s nice to finally meet you!",
maximum_width = 16
Output:
[
"Hey  there mate,"
"it’s   nice   to",
"finally     meet",
"you."
]
Note: Please keep in mind that the last line is aligned left.


The module 'task3_test.py' contains tests for the functions in this programme.
"""

import pdb, math


# Function to justify the given text:
def justify(words, max_width):
    """
    Function returns list with justified rows of given phrase
    :param words: phrase to be justified
    :param max_width: number of characters per line
    :return: list with justified rows
    """
    # Variables used in code:
    row = []
    check = []
    sub_results = []
    final_results = []

    # Splitting words:
    split_words = words.split()

    # Adding words to row if max_width is not exceeded:
    for word in split_words:
        check.append(word)
        min_spaces = len(check) - 1
        if len("".join(check)) + min_spaces < max_width:
            row.append(word)
        else:
            sub_results.append(row)
            row = []
            row.append(word)
            check = []
            check.append(word)

    sub_results.append(row)

    for result in sub_results:
        # Merge all words in result
        row_merged = "".join(result)

        # Number of spaces to fill between words:
        numb_space_fill = max_width - len("".join(row_merged))

        # Min Number of spaces between words in row:
        min_spaces = len(result) - 1

        # Calculate the number of spaces between each word:
        tab = []

        # If there is one space needed -> add one long space between words:
        if min_spaces == 1:
            tab.append(numb_space_fill)
        # If there is more than one space needed -> add few spaces between words:
        if min_spaces > 1:
            x = math.ceil(numb_space_fill / min_spaces)
            for i in range(min_spaces):
                tab.append(x)
                x = numb_space_fill - tab[i]
                x = math.ceil(x / min_spaces)

            # If characters are missing in a row -> add as many spaces:
            chech_sum = sum(tab)
            if chech_sum < numb_space_fill:
                diff = numb_space_fill - sum(tab)
                tab[-1] += diff

        tab.append(0)

        # Getting justified text:
        row_justified = []

        # Concatenate words and spaces and place it into final_results:
        for (word, space) in zip(result, tab):
            row_justified.append(word + space * ' ')

        final_results.append("".join(row_justified))

    return final_results


# Function to show results:
def print_results(results):
    """
    Function used to print all elements in given list
    :param results: list
    :return: prints all elements in given list
    """
    for element in results:
        print(element)


if __name__ == "__main__":
    # Program does not work correctly
    # The last line should not be justified
    # It works in some cases, but not in all

    words = "Hey there mate, it’s nice to finally meet you!"
    max_width = 16
    print_results(justify(words, max_width))
