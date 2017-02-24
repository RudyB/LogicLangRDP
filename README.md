# LogicLangRDP
A Python based Reverse Descent Parser for basic logical languages that determines whether logical statements are valid or invalid.

## Valid Grammar
```
# --------------------------------------------
# SENTENCE : PROP | TRUTH | NEG | AND | OR | IMPL | EQ
# PROPOSITION : a | b | c | ... | z
# TRUTH : true | false
# NEGATION : not S
# AND : S and S
# OR : S or S
# IMPLICATION : S impl S
# EQUALITY : S = S
# --------------------------------------------
```

## Running the application
The application can be started with:  
`python main.py`

## License

This repository is released under the MIT license. See LICENSE for details.
