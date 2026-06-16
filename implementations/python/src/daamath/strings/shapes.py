from ..python_utils import Namespace

circle = Namespace(**{
    'black': '●',
    'white': '○',
    'heavy': '⭘',
    'large': Namespace(**{
        'black': '⬤',
        'white': '◯',
        'heavy': '⭕'
    })
})
ellipse = Namespace(**{
    'horizontal': Namespace(**{
        'black': '⬬',
        'white': '⬭'
    }),
    'vertical': Namespace(**{
        'black': '⬮',
        'white': '⬯'
    })
})
triangle = Namespace(**{
    'black': Namespace(**{
        'west': '◀',
        'east': '▶',
        'north': '▲',
        'south': '▼',
        'north_west': '◤',
        'north_east': '◥',
        'south_west': '◣',
        'south_east': '◢'
    }),
    'white': Namespace(**{
        'west': '◁',
        'east': '▷',
        'north': '△',
        'south': '▽',
        'north_west': '◸',
        'north_east': '◹',
        'south_west': '◺',
        'south_east': '◿'
    }),
    'underbar': Namespace(**{
        'north': '⧋'
    }),
    'small': Namespace(**{
        'black': Namespace(**{
            'west': '◂',
            'east': '▸',
            'north': '▴',
            'south': '▾'
        }),
        'white': Namespace(**{
            'west': '◃',
            'east': '▹',
            'north': '▵',
            'south': '▿'
        })
    }),
    'centred': Namespace(**{
        'medium': Namespace(**{
            'black': Namespace(**{
                'west': '⯇',
                'east': '⯈',
                'north': '⯅',
                'south': '⯆'
            })
        })
    })
})
pointer = Namespace(**{
    'black': Namespace(**{
        'east': '◄',
        'west': '►'
    }),
    'white': Namespace(**{
        'east': '◅',
        'west': '▻'
    })
})
square = Namespace(**{
    'black': '■',
    'white': '□',
    'medium': Namespace(**{
        'black': '◼',
        'white': '◻'
    }),
    'small': Namespace(**{
        'black': '▪',
        'white': '▫'
    }),
    'very_small': Namespace(**{
        'black': '⬝',
        'white': '⬞'
    }),
    'centred': Namespace(**{
        'black': '⯀'
    })
})
rectangle = Namespace(**{
    'horizontal': Namespace(**{
        'black': '▬',
        'white': '▭'
    }),
    'vertical': Namespace(**{
        'black': '▮',
        'white': '▯'
    })
})
parallelogram = Namespace(**{
    'black': '▰',
    'white': '▱'
})
diamond = Namespace(**{
    'black': '◆',
    'white': '◇',
    'medium': Namespace(**{
        'black': '⬥',
        'white': '⬦'
    }),
    'small': Namespace(**{
        'black': '⬩'
    }),
    'centred': Namespace(**{
        'black': '⯁'
    }),
    'dotted': Namespace(**{
        'white': '⟐'
    })
})
lozenge = Namespace(**{
    'black': '⧫',
    'white': '◊',
    'medium': Namespace(**{
        'black': '⬧',
        'white': '⬨'
    }),
    'small': Namespace(**{
        'black': '⬪',
        'white': '⬫'
    })
})
cusp = Namespace(**{
    'black': '⯌',
    'white': '⯎',
    'rotated': Namespace(**{
        'black': '⯍',
        'white': '⯏'
    })
})
pentagon = Namespace(**{
    'north': Namespace(**{
        'black': '⬟',
        'white': '⬠'
    }),
    'east': Namespace(**{
        'black': '⭓',
        'white': '⭔'
    }),
    'south': Namespace(**{
        'black': '⯂'
    })
})
star = Namespace(**{
    'small': Namespace(**{
        'black': '⭑',
        'white': '⭒'
    })
})
hexagon = Namespace(**{
    'vertical': Namespace(**{
        'black': '⬢',
        'white': '⬡'
    }),
    'horizontal': Namespace(**{
        'black': '⬣'
    })
})
octagon = Namespace(**{
    'vertical': Namespace(**{
        'black': '⯄'
    }),
    'horizontal': Namespace(**{
        'black': '⯃'
    })
})
