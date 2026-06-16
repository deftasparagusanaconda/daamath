from ..python_utils import Namespace

arrow = Namespace(**{
    'west': '←',
    'east': '→',
    'north': '↑',
    'south': '↓',
    'horizontal': '↔',
    'vertical': '↕',
    'north_west': '↖',
    'north_east': '↗',
    'south_west': '↙',
    'south_east': '↘',
    'stroke': Namespace(**{
        'vertical': Namespace(**{
            'west': '⇷',
            'east': '⇸',
            'horizontal': '⇹'
        }),
        'double': Namespace(**{
            'west': '⇺',
            'east': '⇻',
            'horizontal': '⇼'
        })
    }),
    'wave': Namespace(**{
        'west': '↜',
        'east': '↝',
        'horizontal': '↭'
    }),
    'squiggle': Namespace(**{
        'west': '⇜',
        'east': '⇝'
    }),
    'two_headed': Namespace(**{
        'west': '↞',
        'east': '↠',
        'north': '↟',
        'south': '↡'
    }),
    'tailed': Namespace(**{
        'west': '↢',
        'east': '↣'
    }),
    'from_bar': Namespace(**{
        'west': '↤',
        'east': '↦',
        'north': '↥',
        'south': '↧'
    }),
    'to_bar': Namespace(**{
        'west': '⇤',
        'east': '⇥',
        'north': '⤒',
        'south': '⤓'
    }),
    'underbar': Namespace(**{
        'vertical': '↨'
    }),
    'hook': Namespace(**{
        'west': '↩',
        'east': '↪'
    }),
    'loop': Namespace(**{
        'west': '↫',
        'east': '↬'
    }),
    'zigzag': Namespace(**{
        'south': '↯'
    }),
    'long': Namespace(**{
        'west': '⟵',
        'east': '⟶',
        'horizontal': '⟷',
        'from_bar': Namespace(**{
            'west': '⟻',
            'east': '⟼'
        }),
        'squiggle': Namespace(**{
            'east': '⟿'
        }),
        'double': Namespace(**{
            'west': '⟸',
            'east': '⟹',
            'horizontal': '⟺'
        })
    }),
    'double': Namespace(**{
        'west': '⇐',
        'east': '⇒',
        'north': '⇑',
        'south': '⇓',
        'horizontal': '⇔',
        'vertical': '⇕',
        'north_west': '⇖',
        'north_east': '⇗',
        'south_west': '⇙',
        'south_east': '⇘',
        'from_bar': Namespace(**{
            'west': '⟽',
            'east': '⟾'
        }),
        'stroke': Namespace(**{
            'west': '⇍',
            'east': '⇏',
            'horizontal': '⇎'
        })
    }),
    'triple': Namespace(**{
        'west': '⇚',
        'east': '⇛',
        'north': '⤊',
        'south': '⤋'
    }),
    'quadruple': Namespace(**{
        'west': '⭅',
        'east': '⭆'
    }),
    'doubled': Namespace(**{
        'west': '⇇',
        'east': '⇉',
        'north': '⇈',
        'south': '⇊'
    }),
    'opposite': Namespace(**{
        'horizontal': Namespace(**{
            'clockwise': '⇆',
            'anticlockwise': '⇄'
        }),
        'vertical': Namespace(**{
            'clockwise': '⇅',
            'anticlockwise': '⇵'
        })
    }),
    'tripled': Namespace(**{
        'west': '⬱',
        'east': '⇶'
    }),
    'dash': Namespace(**{
        'west': '⇠',
        'east': '⇢',
        'north': '⇡',
        'south': '⇣'
    }),
    'white': Namespace(**{
        'west': '⇦',
        'east': '⇨',
        'north': '⇧',
        'south': '⇩',
        'horizontal': '⬄',
        'vertical': '⇳',
        'north_west': '⬁',
        'north_east': '⬀',
        'south_west': '⬃',
        'south_east': '⬂'
    }),
    'black': Namespace(**{
        'west': '⬅',
        'east': '⮕',
        'north': '⬆',
        'south': '⬇',
        'horizontal': '⬌',
        'vertical': '⬍',
        'north_west': '⬉',
        'north_east': '⬈',
        'south_west': '⬋',
        'south_east': '⬊'
    }),
    'open_headed': Namespace(**{
        'west': '⇽',
        'east': '⇾',
        'horizontal': '⇿'
    }),
    'clockwise': '↻',
    'anticlockwise': '↺'
})
