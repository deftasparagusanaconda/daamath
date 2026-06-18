from types import SimpleNamespace as _SimpleNamespace

circle = _SimpleNamespace(
    black = '●',
    white = '○',
    heavy = '⭘',
    large = _SimpleNamespace(
        black = '⬤',
        white = '◯',
        heavy = '⭕'
    )
)
ellipse = _SimpleNamespace(
    horizontal = _SimpleNamespace(
        black = '⬬',
        white = '⬭'
    ),
    vertical = _SimpleNamespace(
        black = '⬮',
        white = '⬯'
    )
)
triangle = _SimpleNamespace(
    black = _SimpleNamespace(
        west = '◀',
        east = '▶',
        north = '▲',
        south = '▼',
        north_west = '◤',
        north_east = '◥',
        south_west = '◣',
        south_east = '◢'
    ),
    white = _SimpleNamespace(
        west = '◁',
        east = '▷',
        north = '△',
        south = '▽',
        north_west = '◸',
        north_east = '◹',
        south_west = '◺',
        south_east = '◿'
    ),
    underbar = _SimpleNamespace(
        north = '⧋'
    ),
    small = _SimpleNamespace(
        black = _SimpleNamespace(
            west = '◂',
            east = '▸',
            north = '▴',
            south = '▾'
        ),
        white = _SimpleNamespace(
            west = '◃',
            east = '▹',
            north = '▵',
            south = '▿'
        )
    ),
    centred = _SimpleNamespace(
        medium = _SimpleNamespace(
            black = _SimpleNamespace(
                west = '⯇',
                east = '⯈',
                north = '⯅',
                south = '⯆'
            )
        )
    )
)
pointer = _SimpleNamespace(
    black = _SimpleNamespace(
        east = '◄',
        west = '►'
    ),
    white = _SimpleNamespace(
        east = '◅',
        west = '▻'
    )
)
square = _SimpleNamespace(
    black = '■',
    white = '□',
    medium = _SimpleNamespace(
        black = '◼',
        white = '◻'
    ),
    small = _SimpleNamespace(
        black = '▪',
        white = '▫'
    ),
    very_small = _SimpleNamespace(
        black = '⬝',
        white = '⬞'
    ),
    centred = _SimpleNamespace(
        black = '⯀'
    )
)
rectangle = _SimpleNamespace(
    horizontal = _SimpleNamespace(
        black = '▬',
        white = '▭'
    ),
    vertical = _SimpleNamespace(
        black = '▮',
        white = '▯'
    )
)
parallelogram = _SimpleNamespace(
    black = '▰',
    white = '▱'
)
diamond = _SimpleNamespace(
    black = '◆',
    white = '◇',
    medium = _SimpleNamespace(
        black = '⬥',
        white = '⬦'
    ),
    small = _SimpleNamespace(
        black = '⬩'
    ),
    centred = _SimpleNamespace(
        black = '⯁'
    ),
    dotted = _SimpleNamespace(
        white = '⟐'
    )
)
lozenge = _SimpleNamespace(
    black = '⧫',
    white = '◊',
    medium = _SimpleNamespace(
        black = '⬧',
        white = '⬨'
    ),
    small = _SimpleNamespace(
        black = '⬪',
        white = '⬫'
    )
)
cusp = _SimpleNamespace(
    black = '⯌',
    white = '⯎',
    rotated = _SimpleNamespace(
        black = '⯍',
        white = '⯏'
    )
)
pentagon = _SimpleNamespace(
    north = _SimpleNamespace(
        black = '⬟',
        white = '⬠'
    ),
    east = _SimpleNamespace(
        black = '⭓',
        white = '⭔'
    ),
    south = _SimpleNamespace(
        black = '⯂'
    )
)
star = _SimpleNamespace(
    small = _SimpleNamespace(
        black = '⭑',
        white = '⭒'
    )
)
hexagon = _SimpleNamespace(
    vertical = _SimpleNamespace(
        black = '⬢',
        white = '⬡'
    ),
    horizontal = _SimpleNamespace(
        black = '⬣'
    )
)
octagon = _SimpleNamespace(
    vertical = _SimpleNamespace(
        black = '⯄'
    ),
    horizontal = _SimpleNamespace(
        black = '⯃'
    )
)
