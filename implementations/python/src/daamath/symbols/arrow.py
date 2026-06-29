from types import SimpleNamespace as _SimpleNamespace

arrow = _SimpleNamespace(
    west = '←',
    east = '→',
    north = '↑',
    south = '↓',
    horizontal = '↔',
    vertical = '↕',
    north_west = '↖',
    north_east = '↗',
    south_west = '↙',
    south_east = '↘',
    stroke = _SimpleNamespace(
        vertical = _SimpleNamespace(
            west = '⇷',
            east = '⇸',
            horizontal = '⇹'
        ),
        double = _SimpleNamespace(
            west = '⇺',
            east = '⇻',
            horizontal = '⇼'
        )
    ),
    wave = _SimpleNamespace(
        west = '↜',
        east = '↝',
        horizontal = '↭'
    ),
    squiggle = _SimpleNamespace(
        west = '⇜',
        east = '⇝'
    ),
    two_headed = _SimpleNamespace(
        west = '↞',
        east = '↠',
        north = '↟',
        south = '↡'
    ),
    tailed = _SimpleNamespace(
        west = '↢',
        east = '↣'
    ),
    from_bar = _SimpleNamespace(
        west = '↤',
        east = '↦',
        north = '↥',
        south = '↧'
    ),
    to_bar = _SimpleNamespace(
        west = '⇤',
        east = '⇥',
        north = '⤒',
        south = '⤓'
    ),
    underbar = _SimpleNamespace(
        vertical = '↨'
    ),
    hook = _SimpleNamespace(
        west = '↩',
        east = '↪'
    ),
    loop = _SimpleNamespace(
        west = '↫',
        east = '↬'
    ),
    zigzag = _SimpleNamespace(
        south = '↯'
    ),
    long = _SimpleNamespace(
        west = '⟵',
        east = '⟶',
        horizontal = '⟷',
        from_bar = _SimpleNamespace(
            west = '⟻',
            east = '⟼'
        ),
        squiggle = _SimpleNamespace(
            east = '⟿'
        ),
        double = _SimpleNamespace(
            west = '⟸',
            east = '⟹',
            horizontal = '⟺'
        )
    ),
    double = _SimpleNamespace(
        west = '⇐',
        east = '⇒',
        north = '⇑',
        south = '⇓',
        horizontal = '⇔',
        vertical = '⇕',
        north_west = '⇖',
        north_east = '⇗',
        south_west = '⇙',
        south_east = '⇘',
        from_bar = _SimpleNamespace(
            west = '⟽',
            east = '⟾'
        ),
        stroke = _SimpleNamespace(
            west = '⇍',
            east = '⇏',
            horizontal = '⇎'
        )
    ),
    triple = _SimpleNamespace(
        west = '⇚',
        east = '⇛',
        north = '⤊',
        south = '⤋'
    ),
    quadruple = _SimpleNamespace(
        west = '⭅',
        east = '⭆'
    ),
    doubled = _SimpleNamespace(
        west = '⇇',
        east = '⇉',
        north = '⇈',
        south = '⇊'
    ),
    opposite = _SimpleNamespace(
        horizontal = _SimpleNamespace(
            clockwise = '⇆',
            anticlockwise = '⇄'
        ),
        vertical = _SimpleNamespace(
            clockwise = '⇅',
            anticlockwise = '⇵'
        )
    ),
    tripled = _SimpleNamespace(
        west = '⬱',
        east = '⇶'
    ),
    dash = _SimpleNamespace(
        west = '⇠',
        east = '⇢',
        north = '⇡',
        south = '⇣'
    ),
    white = _SimpleNamespace(
        west = '⇦',
        east = '⇨',
        north = '⇧',
        south = '⇩',
        horizontal = '⬄',
        vertical = '⇳',
        north_west = '⬁',
        north_east = '⬀',
        south_west = '⬃',
        south_east = '⬂'
    ),
    black = _SimpleNamespace(
        west = '⬅',
        east = '⮕',
        north = '⬆',
        south = '⬇',
        horizontal = '⬌',
        vertical = '⬍',
        north_west = '⬉',
        north_east = '⬈',
        south_west = '⬋',
        south_east = '⬊'
    ),
    open_headed = _SimpleNamespace(
        west = '⇽',
        east = '⇾',
        horizontal = '⇿'
    ),
    clockwise = '↻',
    anticlockwise = '↺'
)
