from types import SimpleNamespace as _SimpleNamespace

bracket = _SimpleNamespace(
    round = _SimpleNamespace(
        left = '(',
        right = ')',
        top = '⏜',
        bottom = '⏝',
        double = _SimpleNamespace(
            left = '⸨',
            right = '⸩'
        ),
        white = _SimpleNamespace(
            left = '⦅',
            right = '⦆'
        ),
        small = _SimpleNamespace(
            left = '﹙',
            right = '﹚'
        ),
        superscript = _SimpleNamespace(
            left = '⁽',
            right = '⁾'
        ),
        subscript = _SimpleNamespace(
            left = '₍',
            right = '₎'
        ),
        half = _SimpleNamespace(
            top = _SimpleNamespace(
                left = '⹙',
                right = '⹚'
            ),
            bottom = _SimpleNamespace(
                left = '⹛',
                right = '⹜'
            )
        ),
        flattened = _SimpleNamespace(
            left = '⟮',
            right = '⟯'
        ),
        ornate = _SimpleNamespace(
            left = '﴾',
            right = '﴿'
        ),
        ornament = _SimpleNamespace(
            medium = _SimpleNamespace(
                left = '❨',
                right = '❩',
                flattened = _SimpleNamespace(
                    left = '❪',
                    right = '❫'
                )
            )
        ),
        fullwidth = _SimpleNamespace(
            left = '（',
            right = '）',
            white = _SimpleNamespace(
                left = '｟',
                right = '｠'
            )
        ),
        presentation = _SimpleNamespace(
            top = '︵',
            bottom = '︶'
        ),
        big = _SimpleNamespace(
            three = _SimpleNamespace(
                left = _SimpleNamespace(
                    top = '⎛',
                    middle = '⎜',
                    bottom = '⎝'
                ),
                right = _SimpleNamespace(
                    top = '⎞',
                    middle = '⎟',
                    bottom = '⎠'
                )
            )
        )
    ),
    floor = _SimpleNamespace(
        left = '⌊',
        right = '⌋'
    ),
    ceil = _SimpleNamespace(
        left = '⌈',
        right = '⌉'
    ),
    vertical = _SimpleNamespace(
        left = '⎸',
        right = '⎹'
    ),
    half = _SimpleNamespace(
        left = _SimpleNamespace(
            top = '⸢',
            bottom = '⸤'
        ),
        right = _SimpleNamespace(
            top = '⸣',
            bottom = '⸥'
        )
    ),
    square = _SimpleNamespace(
        left = '[',
        right = ']',
        top = '⎴',
        bottom = '⎵',
        white = _SimpleNamespace(
            left = '⟦',
            right = '⟧'
        ),
        quill = _SimpleNamespace(
            left = '⁅',
            right = '⁆'
        ),
        underbar = _SimpleNamespace(
            left = '⦋',
            right = '⦌'
        ),
        tick = _SimpleNamespace(
            top = _SimpleNamespace(
                left = '⦍',
                right = '⦐'
            ),
            bottom = _SimpleNamespace(
                left = '⦏',
                right = '⦎'
            )
        ),
        stroke = _SimpleNamespace(
            left = '⹕',
            right = '⹖',
            double = _SimpleNamespace(
                left = '⹗',
                right = '⹘'
            )
        ),
        fullwidth = _SimpleNamespace(
            left = '［',
            right = '］',
            white = _SimpleNamespace(
                left = '〚',
                right = '〛'
            )
        ),
        presentation = _SimpleNamespace(
            top = '﹇',
            bottom = '﹈'
        ),
        bottom_over_top = '⎶',
        big = _SimpleNamespace(
            three = _SimpleNamespace(
                left = _SimpleNamespace(
                    top = '⎡',
                    middle = '⎢',
                    bottom = '⎣'
                ),
                right = _SimpleNamespace(
                    top = '⎤',
                    middle = '⎥',
                    bottom = '⎦'
                )
            )
        )
    ),
    curly = _SimpleNamespace(
        left = '{',
        right = '}',
        top = '⏞',
        bottom = '⏟',
        white = _SimpleNamespace(
            left = '⦃',
            right = '⦄'
        ),
        ornament = _SimpleNamespace(
            medium = _SimpleNamespace(
                left = '❴',
                right = '❵'
            )
        ),
        fullwidth = _SimpleNamespace(
            left = '｛',
            right = '｝'
        ),
        small = _SimpleNamespace(
            left = '﹛',
            right = '﹜'
        ),
        presentation = _SimpleNamespace(
            top = '︷',
            bottom = '︸'
        ),
        big = _SimpleNamespace(
            two = _SimpleNamespace(
                left = _SimpleNamespace(
                    top = '⎰',
                    bottom = '⎱'
                )
            ),
            three = _SimpleNamespace(
                left = _SimpleNamespace(
                    top = '⎧',
                    middle = '⎨',
                    bottom = '⎩'
                ),
                right = _SimpleNamespace(
                    top = '⎫',
                    middle = '⎬',
                    bottom = '⎭'
                ),
                vertical = '⎪'
            )
        )
    ),
    angle = _SimpleNamespace(
        left = '⟨',
        right = '⟩',
        dotted = _SimpleNamespace(
            left = '⦑',
            right = '⦒'
        ),
        curved = _SimpleNamespace(
            left = '⧼',
            right = '⧽'
        ),
        fullwidth = _SimpleNamespace(
            narrow = _SimpleNamespace(
                left = '＜',
                right = '＞'
            ),
            wide = _SimpleNamespace(
                left = '〈',
                right = '〉'
            ),
            presentation = _SimpleNamespace(
                top = '︽',
                bottom = '︾'
            )
        ),
        presentation = _SimpleNamespace(
            top = '︿',
            bottom = '﹀'
        ),
        double = _SimpleNamespace(
            left = '⟪',
            right = '⟫',
            fullwidth = _SimpleNamespace(
                left = '《',
                right = '》'
            )
        ),
        ornament = _SimpleNamespace(
            medium = _SimpleNamespace(
                left = '❬',
                right = '❭'
            ),
            heavy = _SimpleNamespace(
                left = '❰',
                right = '❱'
            )
        )
    ),
    lenticular = _SimpleNamespace(
        fullwidth = _SimpleNamespace(
            black = _SimpleNamespace(
                left = '【',
                right = '】'
            ),
            white = _SimpleNamespace(
                left = '〖',
                right = '〗'
            )
        ),
        presentation = _SimpleNamespace(
            black = _SimpleNamespace(
                top = '︻',
                bottom = '︼'
            ),
            white = _SimpleNamespace(
                top = '︗',
                bottom = '︘'
            )
        )
    ),
    tortoise_shell = _SimpleNamespace(
        black = _SimpleNamespace(
            left = '⦗',
            right = '⦘',
            top = '⏠',
            bottom = '⏡'
        ),
        white = _SimpleNamespace(
            left = '⟬',
            right = '⟭'
        ),
        small = _SimpleNamespace(
            left = '﹝',
            right = '﹞'
        ),
        fullwidth = _SimpleNamespace(
            black = _SimpleNamespace(
                left = '〔',
                right = '〕'
            ),
            white = _SimpleNamespace(
                left = '〘',
                righ = '〙'
            )
        ),
        ornament = _SimpleNamespace(
            light = _SimpleNamespace(
                left = '❲',
                right = '❳'
            )
        ),
        presentation = _SimpleNamespace(
            top = '︹',
            bottom = '︺'
        )
    ),
    corner = _SimpleNamespace(
        left = _SimpleNamespace(
            top = '⌜',
            bottom = '⌞'
        ),
        right = _SimpleNamespace(
            top = '⌝',
            bottom = '⌟'
        ),
        dot = _SimpleNamespace(
            left = _SimpleNamespace(
                top = '⟔'
            ),
            right = _SimpleNamespace(
                bottom = '⟓'
            )
        ),
        halfwidth = _SimpleNamespace(
            left = _SimpleNamespace(
                top = '｢'
            ),
            right = _SimpleNamespace(
                bottom = '｣'
            )
        ),
        fullwidth = _SimpleNamespace(
            left = _SimpleNamespace(
                top = '「'
            ),
            right = _SimpleNamespace(
                bottom = '」'
            ),
            white = _SimpleNamespace(
                left = _SimpleNamespace(
                    top = '『'
                ),
                right = _SimpleNamespace(
                    bottom = '』'
                )
            )
        ),
        presentation = _SimpleNamespace(
            top = _SimpleNamespace(
                right = '﹁'
            ),
            bottom = _SimpleNamespace(
                left = '﹂'
            ),
            white = _SimpleNamespace(
                top = _SimpleNamespace(
                    right = '﹃'
                ),
                bottom = _SimpleNamespace(
                    left = '﹄'
                )
            )
        )
    ),
    image = _SimpleNamespace(
        left = '⦇',
        right = '⦈'
    ),
    binding = _SimpleNamespace(
        left = '⦉',
        right = '⦊'
    ),
    arc_inequality = _SimpleNamespace(
        left = '⦓',
        right = '⦔',
        double = _SimpleNamespace(
            left = '⦕',
            right = '⦖'
        )
    ),
    wiggly_fence = _SimpleNamespace(
        left = '⧘',
        right = '⧙',
        double = _SimpleNamespace(
            left = '⧚',
            right = '⧛'
        )
    ),
    paraphrase = _SimpleNamespace(
        low = _SimpleNamespace(
            left = '⸜',
            right = '⸝'
        )
    ),
    ogham_feather = _SimpleNamespace(
        left = '᚛',
        right = '᚜'
    ),
    gug_rtags = _SimpleNamespace(
        left = '༺',
        right = '༻'
    ),
    ang_khang = _SimpleNamespace(
        left = '༼',
        right = '༽'
    ),
    substitution = _SimpleNamespace(
        left = '⸂',
        right = '⸃',
        dotted = _SimpleNamespace(
            left = '⸄',
            right = '⸅'
        )
    ),
    transposition = _SimpleNamespace(
        left = '⸉',
        right = '⸊'
    ),
    omission_raised = _SimpleNamespace(
        left = '⸌',
        right = '⸍'
    ),
    sideways_u = _SimpleNamespace(
        left = '⸦',
        right = '⸧'
    ),
    prime_quotation_double = _SimpleNamespace(
        left = '〝',
        right = '〞'
    ),
    guillemet = _SimpleNamespace(
        left = '‹',
        right = '›',
        double = _SimpleNamespace(
            left = '«',
            right = '»'
        )
    )
)
