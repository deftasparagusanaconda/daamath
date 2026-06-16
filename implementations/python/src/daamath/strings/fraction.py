from ..python_utils import Namespace

fraction = Namespace(**{
    'zero': Namespace(**{
        'three': '↉'
    }),
    'one': Namespace(**{
        'two': '½',
        'three': '⅓',
        'four': '¼',
        'five': '⅕',
        'six': '⅙',
        'seven': '⅐',
        'eight': '⅛',
        'nine': '⅑',
        'ten': '⅒'
    }),
    'two': Namespace(**{
        'three': '⅔',
        'five': '⅖'
    }),
    'three': Namespace(**{
        'four': '¾',
        'five': '⅗',
        'eight': '⅜'
    }),
    'four': Namespace(**{
        'five': '⅘'
    }),
    'five': Namespace(**{
        'six': '⅚',
        'eight': '⅝'
    }),
    'seven': Namespace(**{
        'eight': '⅞'
    })
})
