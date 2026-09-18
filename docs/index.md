# daamath

daamath is a cross-language math library specification. it consists of four parts: [characters](characters), [constants](constants), [datatypes](datatypes), [functions](functions)

# implementations

<table>
	<tr>
      	<td><a href="https://github.com/deftasparagusanaconda/daamath-python">python</a></td>
		<td><code>python -m pip install daamath</code></td>
	</tr>
</table>

an implementation is a realization of the [specification] in a programming language. 

an implementation shall NOT have interfaces that other implementations dont. this causes portability issues. for example, the python implementation should not have methods for the Context class, because non-OOP languages will lack those features. thus those methods should live as separate functions.

