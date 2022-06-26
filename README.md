<p align = 'center'>
<img src = './assets/spyke.png' alt = 'logo' width = '500px'>
</p>

# SPYKE PROGRAMMING LANGUAGE

Spyke is a high-level, interpreted, general-purpose programming language. It's syntax is similar to Python / Ruby. Spyke is dynamically-typed and garbage-collected and supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. This language is currently open-source and you can contribute to this project if you want. This programming language with it's structure is *free to use* and *free to contribute*, **currently** and Spyke's build is still in progress, follow this channel for instant notifications on updates.

Spyke is created using SLY (Sly Lex Yacc) and Python.

### SLY is a lexing and parsing tool that helped this projects creation
```python
pip install sly
```

## Lexical Analysis

Lexical Analysis is the first phase of the compiler also known as a scanner. It converts the High level input program into a sequence of Tokens.
* Lexical Analysis can be implemented with the Deterministic finite Automata.
* The output is a sequence of tokens that is sent to the parser for syntax analysis

<p align='center'>
<img src='https://media.geeksforgeeks.org/wp-content/uploads/20190301115936/lexical.png'>

### What is lexical token?
A lexical token is a sequence of characters that can be treated as a unit in the grammar of the programming languages.

Example of tokens:
* Type token (id, number, real, . . . )
* Punctuation tokens (IF, void, return, . . . )
* Alphabetic tokens (keywords)

```
Keywords; Examples-for, while, if etc.
Identifier; Examples-Variable name, function name, etc.
Operators; Examples '+', '++', '-' etc.
Separators; Examples ',' ';' etc
```

Example of Non-Tokens:

* Comments, preprocessor directive, macros, blanks, tabs, newline, etc.

**Lexeme**: The sequence of characters matched by a pattern to form
the corresponding token or a sequence of input characters that comprises a single token is called a lexeme. eg- `float`, `abs_zero_Kelvin`, `=`, `-`, `273`, `;` .

**How Lexical Analyzer functions**

1. Tokenization i.e. Dividing the program into valid tokens.
1. Remove white space characters.
1. Remove comments.
1. It also provides help in generating error messages by providing row numbers and column numbers.

<p align='center'>
<img src='https://media.geeksforgeeks.org/wp-content/cdn-uploads/Compiler_design_lexical_analysis.jpg'>
</p>

The lexical analyzer identifies the error with the help of the automation machine and the grammar of the given language on which it is based like C, C++, and gives row number and column number of the error.
Suppose we pass a statement through lexical analyzer

- `a = b + c;`  It will generate token sequence like this:
- `id = id + id;` Where each id refers to it’s variable in the symbol table referencing all details

For example, consider the program:
```c
int main()
{
  // 2 variables
  int a, b;
  a = 10;
  return 0;
}
```

All the valid tokens are:

```
'int'  'main'  '('  ')'  '{'  'int'  'a' ','  'b' 
';' 'a'  '='  '10'  ';' 'return'  '0'  ';'  '}'
 ```

Above are the valid tokens.
You can observe that we have omitted comments.

As another example, consider below printf statement.

```c
printf("Spyke");
```

As you can see printf function is gonna be 1; Left bracket will be 2. string in brackets is 3. right bracket is 4. and semicolon is gonna be 5.There are 5 valid token in this printf statement.

Number of tokens :

`int max(int i);`

* Lexical analyzer first read int and finds it to be valid and accepts as token
* **max** is read by it and found to be a valid function name after reading (
* **int**  is also a token , then again i as another token and finally ;

```
int, max, ( ,int, i, ), ;
```
Total number of tokens 7:     

## The Parser

The **parser** is that phase of the compiler which takes a token string as input and with the help of existing grammar, converts it into the corresponding Intermediate Representation(IR). The parser is also known as *Syntax Analyzer*.

<p align='center'>
<img src='https://media.geeksforgeeks.org/wp-content/uploads/20190726164056/Capture55555.jpg'>
</p>

Types of Parser: 

The parser is mainly classified into two categories, i.e. Top-down Parser, and Bottom-up Parser. These are explained below:</br>
Top-Down Parser:

The top-down parser is the parser that generates parse for the given input string with the help of grammar productions by expanding the non-terminals i.e. it starts from the start symbol and ends on the terminals. It uses left most derivation. 
Further Top-down parser is classified into 2 types: A recursive descent parser, and Non-recursive descent parser. 

1. **Recursive descent parser** is also known as the Brute force parser or the backtracking parser. It basically generates the parse tree by using brute force and backtracking. 
1. **Non-recursive descent parser** is also known as LL(1) parser or predictive parser or without backtracking parser or dynamic parser. It uses a parsing table to generate the parse tree instead of backtracking.

Bottom-up Parser: 

Bottom-up Parser is the parser that generates the parse tree for the given input string with the help of grammar productions by compressing the non-terminals i.e. it starts from non-terminals and ends on the start symbol. It uses the reverse of the rightmost derivation. 
Further Bottom-up parser is classified into two types: LR parser, and Operator precedence parser. 

* LR parser is the bottom-up parser that generates the parse tree for the given string by using unambiguous grammar. It follows the reverse of the rightmost derivation. 
LR parser is of four types: 

```
(a)LR(0)
(b)SLR(1)
(c)LALR(1)
(d)CLR(1) 
```

* **Operator precedence parser** generates the parse tree from given grammar and string but the only condition is two consecutive non-terminals and epsilon never appears on the right-hand side of any production. 
The operator precedence parsing techniques can be applied to Operator grammars.
* **Operator grammar**: A grammar is said to be operator grammar if there does not exist any production rule on the right-hand side.

1. as ε(Epsilon)
1. Two non-terminals appear consecutively, that is, without any terminal between them operator precedence parsing is not a simple technique to apply to most the language constructs, but it evolves into an easy technique to implement where a suitable grammar may be produced.


## Building a Lexer

```Python
from sly import Lexer
```

```Python
class BasicLexer(Lexer):
    tokens = { NAME, NUMBER, STRING }
    ignore = '\t '
    literals = { '=', '+', '-', '/', 
                '*', '(', ')', ',', ';'}

    # Define tokens as regular expressions
    # (stored as raw strings)
    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    STRING = r'\".*?\"'
  
    # Number token
    @_(r'\d+')
    def NUMBER(self, t):
        
        # convert it into a python integer
        t.value = int(t.value) 
        return t
  
    # Comment token
    @_(r'//.*')
    def COMMENT(self, t):
        pass
  
    # Newline token(used only for showing
    # errors in new line)
    @_(r'\n+')
    def newline(self, t):
        self.lineno = t.value.count('\n')
```

## Building a Parser

```Python
class BasicParser(Parser):
	#tokens are passed from lexer to parser
	tokens = BasicLexer.tokens

	precedence = (
		('left', '+', '-'),
		('left', '*', '/'),
		('right', 'UMINUS'),
	)

	def __init__(self):
		self.env = { }

	@_('')
	def statement(self, p):
		pass

	@_('var_assign')
	def statement(self, p):
		return p.var_assign

	@_('NAME "=" expr')
	def var_assign(self, p):
		return ('var_assign', p.NAME, p.expr)

	@_('NAME "=" STRING')
	def var_assign(self, p):
		return ('var_assign', p.NAME, p.STRING)

	@_('expr')
	def statement(self, p):
		return (p.expr)

	@_('expr "+" expr')
	def expr(self, p):
		return ('add', p.expr0, p.expr1)

	@_('expr "-" expr')
	def expr(self, p):
		return ('sub', p.expr0, p.expr1)

	@_('expr "*" expr')
	def expr(self, p):
		return ('mul', p.expr0, p.expr1)

	@_('expr "/" expr')
	def expr(self, p):
		return ('div', p.expr0, p.expr1)

	@_('"-" expr %prec UMINUS')
	def expr(self, p):
		return p.expr

	@_('NAME')
	def expr(self, p):
		return ('var', p.NAME)

	@_('NUMBER')
	def expr(self, p):
		return ('num', p.NUMBER)
```

## Execution

<img src='https://media.geeksforgeeks.org/wp-content/uploads/20200530132954/ParseTree.png'>

## Syntax and semantics 
Python is meant to be an easily readable language. Its formatting is visually uncluttered and often uses English keywords where other languages use punctuation. It has fewer syntactic exceptions and special cases than C, Pascal or Java.

## Statements and control flow

Spyke's statements include:

* The **assignment** statement, using a single equals sign `=`.
* The **sif** statement, which conditionally executes a block of code, along with **selse** and **seif** (a contraction of else-if).
* The **sfor** statement, which iterates over an iterable object, capturing each element to a local variable for use by the attached block.
* The **swhile** statement, which executes a block of code as long as its condition is `true`.
* The **stry** statement, which allows exceptions raised in its attached code block to be caught and handled by except clauses (or new syntax **sexcept**, it also ensures that clean-up code in a finally block is always run regardless of how the block exits.
* The **sraise** statement, used to raise a specified exception or re-raise a caught `exception`.
* The **class** statement, which executes a block of code and attaches its *local namespace* to a class, for use in object-oriented programming.
* The **func** statement, which defines a function or method.
* The **swith** statement, which encloses a code block within a context manager (for example, acquiring a lock before it is run, then releasing the lock; or opening and closing a file), allowing resource-acquisition-is-initialization (RAII)-like behavior and replacing a common try/finally idiom.
* The **sbreak** statement, which exits a loop.
* The **scontinue** statement, which skips the current iteration and continues with the next.
* The **srem** statement, which removes a variable—deleting the reference from the name to the value, and producing an error if the variable is referred to before it is redefined.
* The **spass** statement, serving as a NOP, syntactically needed to create an empty code block.
* The **sassert** statement, used in debugging to check for conditions that should apply.
* The **syield** statement, which returns a value from a generator function (and also an operator); used to implement coroutines.
* The **sreturn** statement, used to return a value from a function.
* The **simport** statement, used to import modules whose functions or variables can be used in the current program.
* The **sexport** statement, used to export modules whose functions or variables can be used in the differend program.

Unlike other languages Spyke's statements are differend because of adding it's name, for example `if`, `else if`, are replaced with `sif` and `seif` - Spyke if, Spyke else if.

## Typing 

Spyke uses duck typing and has typed objects but untyped variable names. Type constraints are not checked at compile time; rather, operations on an object may fail, signifying that it is not of a suitable type. Despite being dynamically-typed, Python is strongly-typed, forbidding operations that are not well-defined (for example, adding a number to a string) rather than silently attempting to make sense of them.

### Summary of Spyke's built-in types

| **Type** | **Mutability** | **Description** | **Syntax examples** |
| :------- | :------- | :------- | :------- | 
| `bool` | immutable | Boolean value | `True False` |
| `bytearray `| mutable | Sequence of bytes | `bytearray(b'Some ASCII') bytearray(b"Some ASCII") bytearray([119, 105, 107, 105])` |
| `bytes` | immutable | Sequence of bytes | `b'Some ASCII' b"Some ASCII" bytes([119, 105, 107, 105])` |
| `complex` | immutable | Complex number with real and imaginary parts | `3+2.7j 3 + 2.7j` |
| `dict` | mutable | Associative array (or dictionary) of key and value pairs; can contain mixed types (keys and values), keys must be a hashable type | `{'key1': 1.0, 3: False} {}` |
| `types.EllipsisType` | immutable | An ellipsis placeholder to be used as an index in NumPy arrays | `...Ellipsis` |
| `float` | immutable | Double-precision floating-point number. The precision is machine-dependent but in practice is generally implemented as a 64-bit IEEE 754 number with 53 bits of precision. | `1.33333` |
| `frozenset` | immutable | Unordered set, contains no duplicates; can contain mixed types, if hashable | `frozenset([4.0,'string', True])` |
| `int` | immutable | Integer of unlimited magnitude | `42` |
| `list` | mutable | List, can contain mixed types | `[4.0, 'string', True] []` |
| `types.NoneType` | immutable | An object representing the absence of a value, often called null in other languages | `None` | 
| `types.NotImplementedType` | immutable | A placeholder that can be returned from overloaded operators to indicate unsupported operand types. | `NotImplemented` |
| `range` | immutable | A Sequence of numbers commonly used for looping specific number of times in `for` loops | `range(-1, 10) range(10, -5, -2)` |
| `set` | mutable | Unordered set, contains no duplicates; can contain mixed types, if hashable | `{4.0, 'string', True} set()` |
| `str` | immutable | A character string: sequence of Unicode codepoints | `'Spyke' "Spyke" """Spanning multiple lines"""` |
| `tuple` | immutable | Can contain mixed types | `(4.0, 'string', True) ('single element',) ()` |

**Expressions**, **Methods**, **Arithmetic operations**, **Libraries** and other `references` will be posted here in the nex post-update.