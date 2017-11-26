"""
Given a C++ program, remove comments from it. The program source is an array where source[i] is the
i-th line of the source code. This represents the result of splitting the original source code string by
the newline character \n.
In C++, there are two types of comments, line comments, and block comments.

The string // denotes a line comment, which represents that it and rest of the characters to the right
of it in the same line should be ignored.

The string /* denotes a block comment, which represents that all characters until the next (non-overlapping)
occurrence of */ should be ignored. (Here, occurrences happen in reading order: line by line from left to right.)
To be clear, the string /*/ does not yet end the block comment, as the ending would be overlapping the beginning.

The first effective comment takes precedence over others: if the string // occurs in a block comment,
it is ignored. Similarly, if the string /* occurs in a line or block comment, it is also ignored.

If a certain line of code is empty after removing comments, you must not output that line: each string
in the answer list will be non-empty.

There will be no control characters, single quote, or double quote characters. For example,
source = "string s = "/* Not a comment. */";" will not be a test case. (Also, nothing else such as
defines or macros will interfere with the comments.)

It is guaranteed that every open block comment will eventually be closed, so /* outside of a line or
block comment always starts a new comment.

Finally, implicit newline characters can be deleted by block comments. Please see the examples below for details.

After removing the comments from the source code, return the source code in the same format





Input:
source = ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]

The line by line code is visualized as below:
/*Test program */
int main()
{
  // variable declaration
int a, b, c;
/* This is a test
   multiline
   comment for
   testing */
a = b + c;
}

Output: ["int main()","{ ","  ","int a, b, c;","a = b + c;","}"]

The line by line code is visualized as below:
int main()
{

int a, b, c;
a = b + c;
}

Explanation:
The string
/*
 denotes a block comment, including line 1 and lines 6-9. The string
//
 denotes line 4 as comments.
"""

class Stack():
    def __init__(self, initial=None):
        if initial is None:
            self.holder = []
        else:
            self.holder = initial
    def push(self, item):
            self.holder.append(item)
    def pop(self):
        self.holder.pop()

    def is_empty(self):
        if len(self.holder) == 0:
            return True
        else:
            return False
    def clear_stack(self):
        self.holder = []




def remove_comments(source):
    output = []
    stack = Stack()
    for index, item in enumerate(source):
        print item
        if item.lstrip().startswith("//"):
            break
        if item.startswith("/*"):
            stack.push(item)
            if item.endswith("*/"):
                stack.clear_stack()
        else:
            output.append(item)
    return output






source = ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test",
          "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]
print remove_comments(source)


