"""
Define a function that transforms a given string into a new string where the original
string was split into strings of a specified size.

For example:
If the input string was this:

"supercalifragilisticexpialidocious"

and the specified size was 3, then the return string would be:

"sup erc ali fra gil ist ice xpi ali doc iou s"

The assumptions we are making about our input are the following:

- The input string's length is always greater than 0.
- The string has no spaces.
- The specified size is always a positive integer.
"""

def split_in_parts(s, part_length):

    # we need to split the input string into smaller chucks of whatever
    # the specified size is

    # initialize an output array to hold the split letters
    # initialize a an empty substring to hold counted letters
    output = []
    s_substring = ""

    # iterate over characters in the input string
    for letter in s:
        # add letter to the substring until it's equal to the part_length
        if len(s_substring) < part_length:
            s_substring += letter
        # when substring is equal to part_length, append to output and reset
        # substring to empty string to start over
        if len(s_substring) == part_length:
            output.append(s_substring)
            s_substring = ""
    # if any letters are left over, add them at the end.
    if s_substring != "":
        output.append(s_substring)

    # make the array into a string
    result = " ".join(output)
    # return output array
    return result



print(split_in_parts("supercalifragilisticexpialidocious", 3))
print(split_in_parts("supercalifragilisticexpialidocious", 5))
print(split_in_parts("oscargribble", 5))