# unicode

daamath maintains a namespace tree of unicode characters — each with has exactly one name and stored exactly once as the implementation's native string/character format (instead of the codepoint uint). 

a tree is not the most natural way — parameterized functions are more natural — but using the namespace as the wayfinder is both terser and faster, so daamath does it this way.
