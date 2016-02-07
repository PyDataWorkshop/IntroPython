Control Structures

#### 2.4.1 if

The if statement enables us to execute code (or not) depending on a condition.

- `"if condition: ..."`
- `"if condition: ... else: ..."`
- `"if condition1: ... elif condition2: ... else: ..."`
Here is an example:

<pre><code>
>>> y = 25
>>>
>>> if y > 15:
...     print 'y is large'
... else:
...     print 'y is small'
...
y is large
</code></pre>
A few notes:

The condition can be any expression, i.e. something that returns a value. A detailed description of expressions can be found at http://www.python.org/doc/current/ref/expressions.html.
Parentheses are not needed around the condition. Use parentheses to group sub-expressions and control order of evaluation when the natural operator precedence is not what you want. Python's operator precedences are described at http://www.python.org/doc/current/ref/summary.html.
Python has no switch statement. Use if-elif. Or consider using a dictionary, for example:
<pre><code>
def function1():
    print "Hi. I'm function1."
def function2():
    print "Hi. I'm function2."
def function3():
    print "Hi. I'm function3."

mapper = {'one': function1, 'two': function2, 'three': function3}

while 1:
    code = raw_input('Enter "one", "two", "three", or "quit": ')
    if code == 'quit':
        break
    if code not in mapper:
        continue
    mapper[code]()
</code></pre>
Download as text (original file name: Examples/python_101_if_switch.py).
#### 2.4.2 for

The for statement enables us to iterate over collections. It enables us to repeat a set of lines of code once for each item in a collection. Collections are things like strings (arrays of characters), lists, tuples, and dictionaries.

Here is an example:
<pre><code>
>>> collection = [111,222,333]
>>> for item in collection:
...     print 'item:', item
...
item: 111
item: 222
item: 333
</code></pre>

##### Comments:

You can iterate over strings, lists, and tuples.
Iterate over the keys or values in a dictionary with "aDict.keys()" and "aDict.values()". Here is an example:
>>> aDict = {'cat': 'furry and cute', 'dog': 'friendly and smart'}
>>> aDict.keys()
['dog', 'cat']
>>> aDict.values()
['friendly and smart', 'furry and cute']
>>> for key in aDict.keys():
...     print 'A %s is %s.' % (key, aDict[key])
...
A dog is friendly and smart.
A cat is furry and cute.
In recent versions of Python, a dictionary itself is an iterator for its keys. Therefore, you can also do the following:
>>> for key in aDict:
...     print 'A %s is %s.' % (key, aDict[key])
...
A dog is friendly and smart.
A cat is furry and cute.
And, in recent versions of Python, a file is also an iterator over the lines in the file. Therefore, you can do the following:
>>> infile = file('tmp.txt', 'r')
>>> for line in infile:
...       print line,
... 
This is line #1
This is line #2
This is line #3
>>> infile.close()
There are other kinds of iterations. For example, the built-in iter will produce an iterator from a collection. Here is an example:
>>> anIter = iter([11,22,33])
>>> for item in anIter:
...     print 'item:', item
...
item: 11
item: 22
item: 33
You can also implement iterators of your own. To do so, define a function that returns values with yield (instead of with return). Here is an example:
>>> def t(collection):
...     icollection = iter(collection)
...     for item in icollection:
...         yield '||%s||' % item
...
>>> for x in t(collection): print x
...
||111||
||222||
||333||
2.4.3 while

while is another repeating statement. It executes a block of code until a condition is false.

Here is an example:

>>> reply = 'repeat'
>>> while reply == 'repeat':
...     print 'Hello'
...     reply = raw_input('Enter "repeat" to do it again: ')
...
Hello
Enter "repeat" to do it again: repeat
Hello
Enter "repeat" to do it again: bye
Comments:

Use the break statement to exit from a loop. This works for both for and while. Here is an example that uses break in a for statement:
# for_break.py
"""Count lines until a line that begins with a double #.
"""

import sys

def countLines(infilename):
    infile = file(infilename, 'r')
    count = 0
    for line in infile.readlines():
        line = line.strip()
        if line[:2] == '##':
            break
        count += 1
    return count

def usage():
    print 'Usage: python python_101_for_break.py <infilename>'
    sys.exit(-1)

def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    count = countLines(args[0])
    print 'count:', count

if __name__ == '__main__':
    main()
Download as text (original file name: Examples/python_101_for_break.py).
Use the continue statement to skip the remainder of the code block in a for or while. A continue is a short-circuit which, in effect, branches back to the top of the for or while (or if you prefer, to the end of the block).
The test "if __name__ == '__main__':" is used to enable the script to both be (1) imported and (2) run from the command line. That condition is true only when the script is run, but not imported. This is a common Python idiom, which you should consider including at the end of your scripts, whether (1) to give your users a demonstration of what your script does and how to use it or (2) to provide a test of the script.
