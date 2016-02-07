Functions
==========================
#### A basic function

Use `def` to define a function. Here is a simple example:

<pre><code>
def test(msg, count):
    for idx in range(count):
        print '%s %d' % (msg, idx)

test('Test #', 4)
</code></pre>

#### Comments:

- After evaluation def creates a function object.
- Call the function using the parentheses function call notation, in this case `test('Test #', 4)`.
- As with other Python objects, you can stuff a function object into other structures such as tuples, lists, and dictionaries. 

Here is an example:

<pre><code>
# Create a tuple:
val = (test, 'A label:', 5)

# Call the function:
val[0](val[1], val[2])
</code></pre>

#### A function with default arguments

Providing default arguments allows the caller to omit some arguments. Here is an example:

<pre><code>
def testDefaultArgs(arg1='default1', arg2='default2'):
    print 'arg1:', arg1
    print 'arg2:', arg2

testDefaultArgs('Explicit value')
</code></pre>
The above example prints:

<pre><code>
arg1: Explicit value
arg2: default2
</code></pre>

#### Argument lists and keyword argument lists

Here is an example:
<pre><code>
def testArgLists_1(*args, **kwargs):
    print 'args:', args
    print 'kwargs:', kwargs
            
testArgLists_1('aaa', 'bbb', arg1='ccc', arg2='ddd')

def testArgLists_2(arg0, *args, **kwargs):
    print 'arg0: "%s"' % arg0
    print 'args:', args
    print 'kwargs:', kwargs
            
print '=' * 40
testArgLists_2('a first argument', 'aaa', 'bbb', arg1='ccc', arg2='ddd')
</code></pre>
