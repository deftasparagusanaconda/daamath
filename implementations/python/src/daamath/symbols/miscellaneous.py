from types import SimpleNamespace as _SimpleNamespace

roman_numeral_upper = 'ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩⅪⅫ        ⅬⅭⅮⅯ'
roman_numeral_lower = 'ⅰⅱⅲⅳⅴⅵⅶⅷⅸⅹⅺⅻ        ⅼⅽⅾⅿ'
counting_rod_vertical = '〇𝍩𝍪𝍫𝍬𝍭𝍮𝍯𝍰𝍱'
counting_rod_horizontal = '〇𝍠𝍡𝍢𝍣𝍤𝍥𝍦𝍧𝍨'
counting_rod_negative = 'U+20E5'
tally_mark = '𝍷   𝍸'
tally_mark_ideographic = '𝍲𝍳𝍴𝍵𝍶'
decimal_exponent = '⏨'
hebrew = 'ℵℶℷℸ'
reciprocal = '⅟'
increment = '∆'
nabla = '∇'
nabla_italic = '𝛻'
nabla_bold = '𝛁'
nabla_bold_sans_serif = '𝝯'
nabla_bold_italic = '𝜵'
nabla_bold_italic_sans_serif = '𝞩'
partial = '∂'
partial_bold = '𝛛'
partial_italic = '𝜕'
partial_bold_italic = '𝝏'
partial_sans_serif_bold = '𝞉'
partial_sans_serif_bold_italic = '𝟃'
operator = _SimpleNamespace(
    ring = '∘',
    asterisk = '∗',
    bullet = '∙',
    tilde = '∼',
    tilde_reversed = '∽',
    dot = '⋅',
    dot_squared = '⊡',
    dot_circled = '⊙',
    dot_circled_big = '⨀',
    reverse_solidus = '⧵',
    diamond = '⋄',
    star = '⋆',
    triple_colon = '⫶'
)
for_all = '∀'
complement = '∁'
exists = '∃'
exists_stroke = '∄'
proportional = '∝'
infinity = '∞'
root = '√∛∜'
prime = '′″‴⁗'
prime_reversed = '‵‶‷'
wreath_product = '≀'
therefore = '∴'
because = '∵'
ratio = '∶'
proportion = '∷'
angle = '∠'
plus = '+'
plus_double = '⧺'
plus_triple = '⧻'
plus_dot = '∔'
plus_underbar = '±'
plus_overbar = '∓'
plus_overbar_double = '⩱'
plus_underbar_double = '⩲'
plus_squared = '⊠'
plus_circled = '⊕'
plus_big_circled = '⨁'
bar = '−'
tilde = '~'
tilde_stroke = '≁'
tilde_reverse = '∽'
bar_bar = '='
bar_bar_doubled = '⩵'
bar_bar_tripled = '⩶'
bar_bar_stroke = '≠'
bar_tilde = '≂'
tilde_bar = '≃'
tilde_bar_stroke = '≄'
tilde_reverse_bar = '⋍'
tilde_tilde = '≈'
tilde_tilde_stroke = '≉'
bar_bar_bar = '≡'
bar_bar_bar_stroke = '≢'
bar_bar_tilde = '⩳'
tilde_bar_bar = '≅'
tilde_bar_bar_stroke = '≇≆'
tilde_reverse_bar_bar = '≌'
tilde_bar_tilde = '⩬'
tilde_tilde_bar = '≊'
tilde_tilde_tilde = '≋'
bar_bar_bar_bar = '≣'
tilde_tilde_bar_bar = '⩰'
bar_overdot = '∸'
bar_squared = '⊟'
bar_circled = '⊖'
times = '×'
times_big = '⨉'
times_squared = '⊞'
times_circled = '⊗'
times_big_circled = '⨂'
division_slash = '∕'
division_sign = '÷'
fraction = '⁄'
cross_product = '⨯'
coproduct = '⨿'
interior_product = '⨼'
interior_right = '⨽'
n_ary_product = '∏'
n_ary_coproduct = '∐'
n_ary_summation = '∑'
set_minus = '∖'
wedge = _SimpleNamespace(
    left = '<',
    right = '',
    up = '∧',
    down = '∨',
    stroke = _SimpleNamespace(
        left = '≮',
        right = '≯',
        underbar = _SimpleNamespace(
            left = '≰',
            right = '≱'
        )
    ),
    dash = _SimpleNamespace(
        up = '⩜',
        down = '⩝'
    ),
    stem = _SimpleNamespace(
        up = '⩚',
        down = '⩛'
    ),
    dot = _SimpleNamespace(
        left = '⋖',
        right = '⋗',
        up = '⟑',
        down = '⟇'
    ),
    circle = _SimpleNamespace(
        left = '⩹',
        right = '⩺'
    ),
    question_mark = _SimpleNamespace(
        left = '⩻',
        right = '⩼'
    ),
    over = _SimpleNamespace(
        bar = _SimpleNamespace(
            left = '⋜',
            right = '⋝',
            up = '⊼',
            down = '⊽',
            slant = _SimpleNamespace(
                left = '⪕',
                right = '⪖',
                dot = _SimpleNamespace(
                    left = '⪗',
                    right = '⪘'
                )
            ),
            double = _SimpleNamespace(
                left = '⪙',
                right = '⪚',
                up = '⩞',
                down = '⩢'
            )
        )
    ),
    under = _SimpleNamespace(
        bar = _SimpleNamespace(
            left = '≤',
            right = '≥',
            up = '⩟',
            down = '⊻',
            slant = _SimpleNamespace(
                left = '⩽',
                right = '⩾'
            ),
            double = _SimpleNamespace(
                left = '≦',
                right = '≧',
                up = '⩠',
                down = '⩣'
            )
        )
    ),
    double = _SimpleNamespace(
        left = '≪',
        right = '≫',
        underbar = _SimpleNamespace(
            left = '⪣'
        ),
        intersect = _SimpleNamespace(
            up = '⩕',
            down = '⩖'
        ),
        nest = _SimpleNamespace(
            double = _SimpleNamespace(
                left = '⪡',
                right = '⪢',
                up = '⩓',
                down = '⩔'
            )
        )
    ),
    closed = _SimpleNamespace(
        left = '⪦',
        right = '⪧',
        under = _SimpleNamespace(
            bar = _SimpleNamespace(
                slant = _SimpleNamespace(
                    left = '⪨',
                    right = '⪩'
                )
            )
        )
    ),
    triple = _SimpleNamespace(
        left = '⋘',
        right = '⋙',
        nest = _SimpleNamespace(
            left = '⫷',
            right = '⫸'
        )
    ),
    big = _SimpleNamespace(
        left = '⋀',
        right = '⋁'
    ),
    fullwidth = _SimpleNamespace(
        left = '＜',
        right = '＞'
    ),
    circled = _SimpleNamespace(
        left = '⧀',
        right = '⧁'
    ),
    squared = _SimpleNamespace(
        up = '⟎',
        down = '⟏'
    )
)
curve = _SimpleNamespace(
    left = '≺',
    right = '≻',
    up = '⋏',
    down = '⋎',
    double = _SimpleNamespace(
        left = '⪻',
        right = '⪼'
    ),
    stroke = _SimpleNamespace(
        left = '⊀',
        right = '⊁',
        under = _SimpleNamespace(
            bar = _SimpleNamespace(
                slant = _SimpleNamespace(
                    left = '⋠',
                    right = '⋡'
                )
            )
        )
    ),
    under = _SimpleNamespace(
        bar = _SimpleNamespace(
            left = '⪯',
            right = '⪰',
            slant = _SimpleNamespace(
                left = '≼',
                right = '≽'
            )
        )
    ),
    over = _SimpleNamespace(
        bar = _SimpleNamespace(
            slant = _SimpleNamespace(
                left = '⋞',
                right = '⋟'
            ),
            curved = _SimpleNamespace(
                left = '⋞',
                right = '⋟'
            )
        )
    )
)
cup = _SimpleNamespace(
    left = '⊂',
    right = '⊃',
    up = '∩',
    down = '∪',
    circle = _SimpleNamespace(
        left = '⟃',
        right = '⟄'
    ),
    dot = _SimpleNamespace(
        left = '⪽',
        right = '⪾'
    ),
    stroke = _SimpleNamespace(
        left = '⊄',
        right = '⊅',
        under = _SimpleNamespace(
            bar = _SimpleNamespace(
                left = '⊈',
                right = '⊉'
            )
        )
    ),
    double = _SimpleNamespace(
        left = '⋐',
        right = '⋑',
        up = '⋒',
        down = '⋓'
    ),
    under = _SimpleNamespace(
        bar = _SimpleNamespace(
            left = '⊆',
            right = '⊇',
            stroke = _SimpleNamespace(
                left = '⊊',
                right = '⊋'
            ),
            double = _SimpleNamespace(
                left = '⫅',
                right = '⫆',
                stroke = _SimpleNamespace(
                    left = '⫋',
                    right = '⫌'
                )
            )
        ),
        tilde = _SimpleNamespace(
            left = '⫇',
            right = '⫈',
            double = _SimpleNamespace(
                left = '⫉',
                right = '⫊'
            )
        ),
        plus = _SimpleNamespace(
            left = '⪿',
            right = '⫀'
        ),
        times = _SimpleNamespace(
            left = '⫁',
            right = '⫂'
        )
    ),
    over = _SimpleNamespace(
        bar = _SimpleNamespace(
            up = '⩃',
            down = '⩂'
        )
    ),
    closed = _SimpleNamespace(
        left = '⫏',
        right = '⫐'
    ),
    big = _SimpleNamespace(
        up = '⋂',
        down = '⋃'
    )
)
solidus = '/\\'
solidus_double = '⫽'
solidus_big = '⧸⧹'
solidus_overbar = '⧶'
solidus_dash = '⧷'
solidus_circled = '⦸'
in_ = _SimpleNamespace(
    left = '∈',
    right = '∋',
    up = '⫙',
    down = '⟒',
    stroke = _SimpleNamespace(
        left = '∉',
        right = '∌'
    ),
    overbar = _SimpleNamespace(
        left = '⋶',
        right = '⋽'
    ),
    underbar = _SimpleNamespace(
        left = '⋸'
    ),
    small = _SimpleNamespace(
        left = '∊',
        right = '∍',
        overbar = _SimpleNamespace(
            left = '⋷',
            right = '⋾'
        )
    )
)
tack = _SimpleNamespace(
    left = '⊢',
    right = '⊣',
    up = '⊤',
    down = '⊥',
    right_left = '⟛',
    double = _SimpleNamespace(
        up = '⫪',
        down = '⫫',
        right_left = '⟚'
    ),
    short = _SimpleNamespace(
        right = '⫞',
        up = '⫟',
        down = '⫠'
    ),
    long = _SimpleNamespace(
        left = '⟝',
        right = '⟞'
    ),
    big = _SimpleNamespace(
        up = '⟙',
        down = '⟘'
    )
)
triangle = '⊲⊳'
triangle_underbar = '⊴⊵'
triangle_stroke = '⋪⋫'
triangle_stroke_underbar = '⋬⋭'
triangle_big = '⨞'
box = _SimpleNamespace(
    left = '⊏',
    right = '⊐',
    up = '⊓',
    down = '⊔',
    double = _SimpleNamespace(
        up = '⩎',
        down = '⩏'
    ),
    under = _SimpleNamespace(
        bar = _SimpleNamespace(
            left = '⊑',
            right = '⊒'
        ),
        stroke = _SimpleNamespace(
            left = '⋤',
            right = '⋥'
        )
    ),
    stroke = _SimpleNamespace(
        under = _SimpleNamespace(
            bar = _SimpleNamespace(
                left = '⋢',
                right = '⋣'
            )
        )
    ),
    big = _SimpleNamespace(
        up = '⨅',
        down = '⨆'
    )
)
integral = _SimpleNamespace(
    single = '∫',
    double = '∬',
    triple = '∭',
    quadruple = '⨌',
    closed = _SimpleNamespace(
        single = '∮',
        double = '∯',
        triple = '∰'
    ),
    overbar = _SimpleNamespace(
        single = '⨛'
    ),
    underbar = _SimpleNamespace(
        single = '⨜'
    ),
    big = _SimpleNamespace(
        top = '⌠',
        middle = '⎮',
        bottom = '⌡'
    )
)
divides = _SimpleNamespace(
    yes = '∣',
    no = '∤'
)
parallel = _SimpleNamespace(
    yes = '∥',
    no = '∦'
)
vertical_line = ''
vertical_line_white = '⫾'
vertical_line_big_white = '⫿'
vertical_line_double = '‖'
vertical_bar_circled = '⦶'
intercalate = '⊺'
perpendicular = '⟂'
empty_set = '∅'
diameter = '⌀'
numero = '№'
euler_constant = 'ℇ'
dotless_italic_i = '𝚤'
dotless_italic_j = '𝚥'
shuffle_product = '⧢'
tiny = '⧾'
miny = '⧿'
degree = '°'
not_ = '¬'
not_reversed = '⌐'
not_turned = '⌙'
big_sigma = _SimpleNamespace(
    top = '⎲',
    bottom = '⎳'
)
circled_division_slash = '⊘'
circled_division_sign = '⨸'
circled_equal = '⊜'
circled_parallel = '⦷'
circled_perpendicular = '⦹'
circled_less_than = None
circled_greater_than = None
circled_triangle = '⎊'
asterisk_squared = '⧆'
circle_squared = '⧇'
square_squared = '⧈'
ellipsis = _SimpleNamespace(
    bottomed = _SimpleNamespace(
        horizontal = '…'
    ),
    centred = _SimpleNamespace(
        vertical = '⋮',
        horizontal = '⋯',
        forward = '⋰',
        backward = '⋱'
    )
)
braille = '⠀⠁⠂⠃⠄⠅⠆⠇⠈⠉⠊⠋⠌⠍⠎⠏⠐⠑⠒⠓⠔⠕⠖⠗⠘⠙⠚⠛⠜⠝⠞⠟⠠⠡⠢⠣⠤⠥⠦⠧⠨⠩⠪⠫⠬⠭⠮⠯⠰⠱⠲⠳⠴⠵⠶⠷⠸⠹⠺⠻⠼⠽⠾⠿⡀⡁⡂⡃⡄⡅⡆⡇⡈⡉⡊⡋⡌⡍⡎⡏⡐⡑⡒⡓⡔⡕⡖⡗⡘⡙⡚⡛⡜⡝⡞⡟⡠⡡⡢⡣⡤⡥⡦⡧⡨⡩⡪⡫⡬⡭⡮⡯⡰⡱⡲⡳⡴⡵⡶⡷⡸⡹⡺⡻⡼⡽⡾⡿⢀⢁⢂⢃⢄⢅⢆⢇⢈⢉⢊⢋⢌⢍⢎⢏⢐⢑⢒⢓⢔⢕⢖⢗⢘⢙⢚⢛⢜⢝⢞⢟⢠⢡⢢⢣⢤⢥⢦⢧⢨⢩⢪⢫⢬⢭⢮⢯⢰⢱⢲⢳⢴⢵⢶⢷⢸⢹⢺⢻⢼⢽⢾⢿⣀⣁⣂⣃⣄⣅⣆⣇⣈⣉⣊⣋⣌⣍⣎⣏⣐⣑⣒⣓⣔⣕⣖⣗⣘⣙⣚⣛⣜⣝⣞⣟⣠⣡⣢⣣⣤⣥⣦⣧⣨⣩⣪⣫⣬⣭⣮⣯⣰⣱⣲⣳⣴⣵⣶⣷⣸⣹⣺⣻⣼⣽⣾⣿'
braille_alternate = '⠀⠁⠈⠉⠂⠃⠊⠋⠐⠑⠘⠙⠒⠓⠚⠛⠄⠅⠌⠍⠆⠇⠎⠏⠔⠕⠜⠝⠖⠗⠞⠟⠠⠡⠨⠩⠢⠣⠪⠫⠰⠱⠸⠹⠲⠳⠺⠻⠤⠥⠬⠭⠦⠧⠮⠯⠴⠵⠼⠽⠶⠷⠾⠿⡀⡁⡈⡉⡂⡃⡊⡋⡐⡑⡘⡙⡒⡓⡚⡛⡄⡅⡌⡍⡆⡇⡎⡏⡔⡕⡜⡝⡖⡗⡞⡟⡠⡡⡨⡩⡢⡣⡪⡫⡰⡱⡸⡹⡲⡳⡺⡻⡤⡥⡬⡭⡦⡧⡮⡯⡴⡵⡼⡽⡶⡷⡾⡿⢀⢁⢈⢉⢂⢃⢊⢋⢐⢑⢘⢙⢒⢓⢚⢛⢄⢅⢌⢍⢆⢇⢎⢏⢔⢕⢜⢝⢖⢗⢞⢟⢠⢡⢨⢩⢢⢣⢪⢫⢰⢱⢸⢹⢲⢳⢺⢻⢤⢥⢬⢭⢦⢧⢮⢯⢴⢵⢼⢽⢶⢷⢾⢿⣀⣁⣈⣉⣂⣃⣊⣋⣐⣑⣘⣙⣒⣓⣚⣛⣄⣅⣌⣍⣆⣇⣎⣏⣔⣕⣜⣝⣖⣗⣞⣟⣠⣡⣨⣩⣢⣣⣪⣫⣰⣱⣸⣹⣲⣳⣺⣻⣤⣥⣬⣭⣦⣧⣮⣯⣴⣵⣼⣽⣶⣷⣾⣿'
line_extension = _SimpleNamespace(
    horizontal = '⎯',
    vertical = '⏐'
)
line = _SimpleNamespace(
    horizontal = '─',
    vertical = '│',
    north = _SimpleNamespace(
        west = '┌',
        east = '┐'
    ),
    south = _SimpleNamespace(
        west = '└',
        east = '┘'
    ),
    left = '├',
    right = '┤',
    up = '┬',
    down = '┴',
    plus = '┼',
    half = _SimpleNamespace(
        left = '╴',
        top = '╵',
        right = '╶',
        bottom = '╷'
    ),
    forward = '╱',
    backward = '╲',
    cross = '╳',
    arc = _SimpleNamespace(
        north = _SimpleNamespace(
            west = '╭',
            east = '╮'
        ),
        south = _SimpleNamespace(
            west = '╰',
            east = '╯'
        )
    ),
    heavy = '━┃┏┓┗┛┣┫┳┻╋╸╹╺╻   ╼╾╽╿┍┎┑┒┕┖┙┚┝┞┟┠┡┢┥┦┧┨┩┪┭┮┯┰┱┲┵┶┷┸┹┺┽┾┿╀╁╂╃╄╅╆╇╈╉╊',
    doubled = '═║╔╗╚╝╠╣╦╩╬           ╒╓╕╖╘╙╛╜╞  ╟  ╡  ╢    ╤╥    ╧╨    ╪  ╫',
    light_double = '╌╎',
    light_triple = '┄┆',
    light_quadruple = '┈┊',
    heavy_double = '╍╏',
    heavy_triple = '┅┇',
    heavy_quadruple = '┉┋'
)
third_left = '🯏🯎█'
eighth_lower = '▁▂▃▄▅▆▇█'
eighth_upper = '▔🮂🮃▀🮄🮅🮆█'
eighth_left = '▏▎▍▌▋▊▉█'
eighth_right = '▕🮇🮈▐🮉🮊🮋█'
shade = _SimpleNamespace(
    fourth = _SimpleNamespace(
        one = '░',
        two = '▒',
        three = '▓'
    )
)
one_sixteenth = '𜺐𜺑𜺒𜺓𜺔𜺕𜺖𜺗𜺘𜺙𜺚𜺛𜺜𜺝𜺞𜺟'
one_eighth_vertical = '▏🭰🭱🭲🭳🭴🭵▕'
one_eighth_horizontal = '▔🭶🭷🭸🭹🭺🭻▁'
quadrant = '▘▝▀▖▌▞▛▗▚▐▜▄▙▟█'
quadrant_separated = '𜰡𜰢𜰣𜰤𜰥𜰦𜰧𜰨𜰩𜰪𜰫𜰬𜰭𜰮𜰯'
sextant = '🬀🬁🬂🬃🬄🬅🬆🬇🬈🬉🬊🬋🬌🬍🬎🬏🬐🬑🬒🬓▌🬔🬕🬖🬗🬘🬙🬚🬛🬜🬝🬞🬟🬠🬡🬢🬣🬤🬥🬦🬧▐🬨🬩🬪🬫🬬🬭🬮🬯🬰🬱🬲🬳🬴🬵🬶🬷🬸🬹🬺🬻█'
sextant_separated = '𜹑𜹒𜹓𜹔𜹕𜹖𜹗𜹘𜹙𜹚𜹛𜹜𜹝𜹞𜹟𜹠𜹡𜹢𜹣𜹤𜹥𜹦𜹧𜹨𜹩𜹪𜹫𜹬𜹭𜹮𜹯𜹰𜹱𜹲𜹳𜹴𜹵𜹶𜹷𜹸𜹹𜹺𜹻𜹼𜹽𜹾𜹿𜺀𜺁𜺂𜺃𜺄𜺅𜺆𜺇𜺈𜺉𜺊𜺋𜺌𜺍𜺎𜺏'
octant = '𜺨𜺫🮂𜴀▘𜴁𜴂𜴃𜴄▝𜴅𜴆𜴇𜴈▀𜴉𜴊𜴋𜴌🯦𜴍𜴎𜴏𜴐𜴑𜴒𜴓𜴔𜴕𜴖𜴗𜴘𜴙𜴚𜴛𜴜𜴝𜴞𜴟🯧𜴠𜴡𜴢𜴣𜴤𜴥𜴦𜴧𜴨𜴩𜴪𜴫𜴬𜴭𜴮𜴯𜴰𜴱𜴲𜴳𜴴𜴵🮅𜺣𜴶𜴷𜴸𜴹𜴺𜴻𜴼𜴽𜴾𜴿𜵀𜵁𜵂𜵃𜵄▖𜵅𜵆𜵇𜵈▌𜵉𜵊𜵋𜵌▞𜵍𜵎𜵏𜵐▛𜵑𜵒𜵓𜵔𜵕𜵖𜵗𜵘𜵙𜵚𜵛𜵜𜵝𜵞𜵟𜵠𜵡𜵢𜵣𜵤𜵥𜵦𜵧𜵨𜵩𜵪𜵫𜵬𜵭𜵮𜵯𜵰𜺠𜵱𜵲𜵳𜵴𜵵𜵶𜵷𜵸𜵹𜵺𜵻𜵼𜵽𜵾𜵿𜶀𜶁𜶂𜶃𜶄𜶅𜶆𜶇𜶈𜶉𜶊𜶋𜶌𜶍𜶎𜶏▗𜶐𜶑𜶒𜶓▚𜶔𜶕𜶖𜶗▐𜶘𜶙𜶚𜶛▜𜶜𜶝𜶞𜶟𜶠𜶡𜶢𜶣𜶤𜶥𜶦𜶧𜶨𜶩𜶪𜶫▂𜶬𜶭𜶮𜶯𜶰𜶱𜶲𜶳𜶴𜶵𜶶𜶷𜶸𜶹𜶺𜶻𜶼𜶽𜶾𜶿𜷀𜷁𜷂𜷃𜷄𜷅𜷆𜷇𜷈𜷉𜷊𜷋𜷌𜷍𜷎𜷏𜷐𜷑𜷒𜷓𜷔𜷕𜷖𜷗𜷘𜷙𜷚▄𜷛𜷜𜷝𜷞▙𜷟𜷠𜷡𜷢▟𜷣▆𜷤𜷥█'
