# enums

daamath requires a few enums for the context tree.

# ErrorPolicy

the [context] tree sets policies for how to handle [errors]

| value | explanation|
| - | - |
| SENTINEL | return sentinel |
| FLAG_SENTINEL | set flags, return sentinel |
| RAISE_HALT | raise exception, halt execution |
| FLAG_RAISE_HALT | set flags, raise exception, halt execution |

`RAISE_HALT` and `FLAG_RAISE_HALT` are only available if the language has exceptions.  
these policies apply to all errors in daamath

# SentinelPolicy:

the [context] tree sets policies for how to handle sentinel values

| value | explanation|
| - | - |
| PROPAGATE | return sentinel as-is |
| IGNORE | treat sentinel as normal value |

[context:] context.md
[errors]: errors.md
