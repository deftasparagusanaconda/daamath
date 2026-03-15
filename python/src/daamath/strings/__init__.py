from . import utilities
from .utilities import *

from . import arrow, ascii, bracket, digit, greek, latin, square
from .arrow import *
from .ascii import *
from .bracket import *
from .digit import *
from .greek import *
from .latin import *
from .square import *

ROMAN_NUMERAL_UPPER                        = ' ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩⅪⅫ        ⅬⅭⅮⅯ'
ROMAN_NUMERAL_LOWER                        = ' ⅰⅱⅲⅳⅴⅵⅶⅷⅸⅹⅺⅻ        ⅼⅽⅾⅿ'
COUNTING_ROD_VERTICAL                      = '〇𝍩𝍪𝍫𝍬𝍭𝍮𝍯𝍰𝍱'
COUNTING_ROD_HORIZONTAL                    = '〇𝍠𝍡𝍢𝍣𝍤𝍥𝍦𝍧𝍨'
COUNTING_ROD_NEGATIVE                      = '\u20E5'
TALLY_MARK                                 = ' 𝍷   𝍸'
TALLY_MARK_IDEOGRAPHIC                     = ' 𝍲𝍳𝍴𝍵𝍶'
DECIMAL_EXPONENT                           = '⏨'
HEBREW                                     = 'ℵℶℷℸ'
RECIPROCAL                                 = '⅟'

CIRCLE_BIG_BIG                             = '𜰰𜰱𜰲𜰳𜰴𜰷𜰸𜰻𜰼𜰽𜰾𜰿'
CIRCLE_BIG                                 = '𜰵𜰶𜰹𜰺'

FRACTION_0_BY                              = '   ↉       '
FRACTION_1_BY                              = '  ½⅓¼⅕⅙⅐⅛⅑⅒'
FRACTION_2_BY                              = '   ⅔ ⅖     '
FRACTION_3_BY                              = '    ¾⅗  ⅜  '
FRACTION_4_BY                              = '     ⅘     '
FRACTION_5_BY                              = '      ⅚ ⅝  '
FRACTION_7_BY                              = '        ⅞  '
INCREMENT                                  = '∆'

NABLA                                      = '∇'
NABLA_BOLD                                 = '𝛁'
NABLA_ITALIC                               = '𝛻'
NABLA_BOLD_ITALIC                          = '𝜵'
NABLA_SANS_SERIF_BOLD                      = '𝝯'
NABLA_SANS_SERIF_BOLD_ITALIC               = '𝞩'

PARTIAL                                    = '∂'
PARTIAL_BOLD                               = '𝛛'
PARTIAL_ITALIC                             = '𝜕'
PARTIAL_BOLD_ITALIC                        = '𝝏'
PARTIAL_SANS_SERIF_BOLD                    = '𝞉'
PARTIAL_SANS_SERIF_BOLD_ITALIC             = '𝟃'

OPERATOR_RING                              = '∘ (not same as °)'
OPERATOR_ASTERISK                          = '∗ (not same as *)'
OPERATOR_BULLET                            = '∙ (not same as .)'
OPERATOR_TILDE                             = '∼ (not same as ~)'
OPERATOR_TILDE_REVERSED                    = '∽'
OPERATOR_DOT                               = '⋅ (not same as ·)'
OPERATOR_DOT_SQUARED                       = '⊡'
OPERATOR_DOT_CIRCLED                       = '⊙'
OPERATOR_DOT_CIRCLED_BIG                   = '⨀ (not same as ⊙)'
OPERATOR_REVERSE_SOLIDUS                   = '⧵'
OPERATOR_DIAMOND                           = '⋄'
OPERATOR_STAR                              = '⋆'
OPERATOR_TRIPLE_COLON                      = '⫶'

FOR_ALL                                    = '∀'
COMPLEMENT                                 = '∁'
EXISTS                                     = '∃'
EXISTS_STROKE                              = '∄'
PROPORTIONAL                               = '∝'
INFINITY                                   = '∞'
ROOT                                       = '√∛∜'
PRIME                                      = '′″‴⁗'
PRIME_REVERSED                             = '‵‶‷'

WREATH_PRODUCT                             = '≀'
THEREFORE                                  = '∴'
BECAUSE                                    = '∵'
RATIO                                      = '∶ (not same as :)'
PROPORTION                                 = '∷ (not same as ::)'
ANGLE                                      = '∠'

PLUS                                       = '+'
PLUS_DOUBLE                                = '⧺'
PLUS_TRIPLE                                = '⧻'
PLUS_DOT                                   = '∔'
PLUS_UNDERBAR                              = '±'
PLUS_OVERBAR                               = '∓'
PLUS_OVERBAR_DOUBLE                        = '⩱'
PLUS_UNDERBAR_DOUBLE                       = '⩲'
PLUS_SQUARED                               = '⊠'
PLUS_CIRCLED                               = '⊕'
PLUS_BIG_CIRCLED                           = '⨁ (not same as ⊕)'

BAR                                        = '− (minus)'
TILDE                                      = '~ '
TILDE_STROKE                               = '≁'
TILDE_REVERSE                              = '∽'
BAR_BAR                                    = '= (equals)'
BAR_BAR_DOUBLED                            = '⩵'
BAR_BAR_TRIPLED                            = '⩶'
BAR_BAR_STROKE                             = '≠'
BAR_TILDE                                  = '≂'
TILDE_BAR                                  = '≃'
TILDE_BAR_STROKE                           = '≄'
TILDE_REVERSE_BAR                          = '⋍'
TILDE_TILDE                                = '≈'
TILDE_TILDE_STROKE                         = '≉'
BAR_BAR_BAR                                = '≡'
BAR_BAR_BAR_STROKE                         = '≢'
BAR_BAR_TILDE                              = '⩳'
TILDE_BAR_BAR                              = '≅'
TILDE_BAR_BAR_STROKE                       = '≇≆'
TILDE_REVERSE_BAR_BAR                      = '≌'
TILDE_BAR_TILDE                            = '⩬'
TILDE_TILDE_BAR                            = '≊'
TILDE_TILDE_TILDE                          = '≋'
BAR_BAR_BAR_BAR                            = '≣'
TILDE_TILDE_BAR_BAR                        = '⩰'
BAR_OVERDOT                                = '∸'
BAR_SQUARED                                = '⊟'
BAR_CIRCLED                                = '⊖'

TIMES                                      = '×' # (not same as x)
TIMES_BIG                                  = '⨉' # (not same as ×)
TIMES_SQUARED                              = '⊞'
TIMES_CIRCLED                              = '⊗'
TIMES_BIG_CIRCLED                          = '⨂' # (not same as ⊗)

DIVISION_SLASH                             = '∕' # (not same as /)
DIVISION_SIGN                              = '÷' # (unconventional. use ∕)
FRACTION                                   = '⁄' # (not same as ∕)
CROSS_PRODUCT                              = '⨯' # (not same as ×)
COPRODUCT                                  = '⨿'
INTERIOR_PRODUCT                           = '⨼'
INTERIOR_RIGHT                             = '⨽'
N_ARY_PRODUCT                              = '∏'
N_ARY_COPRODUCT                            = '∐'
N_ARY_SUMMATION                            = '∑ (not same as Σ)'
SET_MINUS                                  = '∖'

WEDGE                                      = '<>∧∨'
WEDGE_STROKE                               = '≮≯'
WEDGE_DASH                                 = '  ⩜⩝'
WEDGE_STEM                                 = '  ⩚⩛'
WEDGE_DOT                                  = '⋖⋗⟑⟇'
WEDGE_CIRCLE                               = '⩹⩺'
WEDGE_QUESTION_MARK                        = '⩻⩼'
WEDGE_OVERBAR                              = '⋜⋝⊼⊽'
WEDGE_OVERBAR_SLANT                        = '⪕⪖'
WEDGE_OVERBAR_SLANT_AND_DOT                = '⪗⪘'
WEDGE_OVERBAR_DOUBLE                       = '⪙⪚⩞⩢'
WEDGE_UNDERBAR                             = '≤≥⩟⊻'
WEDGE_UNDERBAR_SLANT                       = '⩽⩾'
WEDGE_UNDERBAR_DOUBLE                      = '≦≧⩠⩣'
WEDGE_STROKE_UNDERBAR                      = '≰≱'
WEDGE_DOUBLE                               = '≪≫'
WEDGE_DOUBLE_NEST                          = '⪡⪢⩓⩔'
WEDGE_DOUBLE_UNDERBAR                      = '⪣'
WEDGE_CLOSED                               = '⪦⪧'
WEDGE_CLOSED_UNDERBAR_SLANT                = '⪨⪩'
WEDGE_DOUBLE_INTERSECT                     = '  ⩕⩖'
WEDGE_TRIPLE                               = '⋘⋙'
WEDGE_TRIPLE_NEST                          = '⫷⫸ '
WEDGE_BIG                                  = '  ⋀⋁'
WEDGE_FULLWIDTH                            = '＜＞'
WEDGE_CIRCLED                              = '⧀⧁'
WEDGE_SQUARED                              = '  ⟎⟏'

CURVE                                      = '≺≻⋏⋎'
CURVE_DOUBLE                               = '⪻⪼'
CURVE_STROKE                               = '⊀⊁'
CURVE_UNDERBAR_SLANT                       = '≼≽'
CURVE_UNDERBAR                             = '⪯⪰'
CURVE_OVERBAR_SLANT                        = '⋞⋟'
CURVE_STROKE_UNDERBAR_SLANT                = '⋠⋡'
CURVE_OVERBAR_CURVED                       = '⋞⋟'

SET                                        = '⊂⊃∩∪'
SET_OPEN                                   = '⟃⟄'   # (perhaps should be SET_CIRCLE?)
SET_DOT                                    = '⪽⪾'
SET_STROKE                                 = '⊄⊅'
SET_DOUBLE                                 = '⋐⋑⋒⋓'
SET_UNDERBAR                               = '⊆⊇'
SET_UNDERTILDE                             = '⫇⫈'
SET_UNDERTILDE_DOUBLE                      = '⫉⫊'
SET_UNDERPLUS                              = '⪿⫀'
SET_UNDERTIMES                             = '⫁⫂'
SET_UNDERBAR_DOUBLE                        = '⫅⫆'
SET_UNDERBAR_DOUBLE_STROKE                 = '⫋⫌'
SET_OVERBAR                                = '  ⩂⩃'
SET_STROKE_UNDERBAR                        = '⊈⊉'
SET_UNDERBAR_STROKE                        = '⊊⊋'
SET_CLOSED                                 = '⫏⫐'
SET_BIG                                    = '  ⋂⋃'

SOLIDUS                                    = '/\\'
SOLIDUS_DOUBLE                             = '⫽'
SOLIDUS_BIG                                = '⧸⧹'
SOLIDUS_OVERBAR                            = '⧶'
SOLIDUS_DASH                               = '⧷'
SOLIDUS_CIRCLED                            = '⦸'

IN                                         = '∈∋⫙⟒'
IN_STROKE                                  = '∉∌'
IN_OVERBAR                                 = '⋶⋽'
IN_UNDERBAR                                = '⋸'
IN_SMALL                                   = '∊∍'
IN_SMALL_OVERBAR                           = '⋷⋾'

TACK                                       = '⊢⊣⊤⊥⟛'
TACK_DOUBLE                                = '  ⫪⫫⟚'
TACK_SHORT                                 = ' ⫞⫟⫠'
TACK_LONG                                  = '⟝⟞   '
TACK_BIG                                   = '  ⟙⟘ '

TRIANGLE                                   = '⊲⊳'
TRIANGLE_UNDERBAR                          = '⊴⊵'
TRIANGLE_STROKE                            = '⋪⋫'
TRIANGLE_STROKE_UNDERBAR                   = '⋬⋭'
TRIANGLE_BIG                               = '⨞ '

BOX                                        = '⊏⊐⊓⊔'
BOX_DOUBLE                                 = '  ⩎⩏'
BOX_UNDERBAR                               = '⊑⊒'
BOX_STROKE_UNDERBAR                        = '⋢⋣'
BOX_UNDERBAR_STROKE                        = '⋤⋥'
BOX_BIG                                    = '  ⨅⨆'

INTEGRAL                                   = '∫∬∭⨌'
INTEGRAL_CLOSED                            = '∮∯∰'
INTEGRAL_OVERBAR                           = '⨛'
INTEGRAL_UNDERBAR                          = '⨜'
INTEGRAL_BIG                               = '⌠⎮⌡'

DIVIDES                                    = '∣'
NOT_DIVIDES                                = '∤'
PARALLEL                                   = '∥'
NOT_PARALLEL                               = '∦'

VERTICAL_LINE                              = '|'
VERTICAL_LINE_WHITE                        = '⫾'
VERTICAL_LINE_BIG_WHITE                    = '⫿'
VERTICAL_LINE_DOUBLE                       = '‖' # (not same as ||)

INTERCALATE                                = '⊺' # (not same as T)
PERPENDICULAR                              = '⟂' # (not same as ⊥)
EMPTY_SET                                  = '∅' # (not same as θ)
DIAMETER                                   = '⌀' # (not same as ∅)
NUMERO                                     = '№'
EULER_CONSTANT                             = 'ℇ' # (unconventional. use γ or 𝛾)
DOTLESS_ITALIC_I                           = '𝚤'
DOTLESS_ITALIC_J                           = '𝚥'
SHUFFLE_PRODUCT                            = '⧢'
TINY                                       = '⧾'
MINY                                       = '⧿'
DEGREE                                     = '°'

NOT                                        = '¬'
NOT_REVERSED                               = '⌐'
NOT_TURNED                                 = '⌙'

BIG_BIG_SIGMA                              = '⎲⎳'

CIRCLED_DIVISION_SLASH                     = '⊘'
CIRCLED_DIVISION_SIGN                      = '⨸' # (unconventional. use ⊘)
CIRCLED_EQUAL                              = '⊜'
CIRCLED_VERTICAL_BAR                       = '⦶'
CIRCLED_PARALLEL                           = '⦷'
CIRCLED_PERPENDICULAR                      = '⦹'
CIRCLED_LESS_THAN                          = ''
CIRCLED_GREATER_THAN                       = ''
CIRCLED_TRIANGLE                           = '⎊'

ASTERISK_SQUARED                           = '⧆'
CIRCLE_SQUARED                             = '⧇'
SQUARE_SQUARED                             = '⧈'

ELLIPSIS_VERTICAL                          = '⋮'
ELLIPSIS_HORIZONTAL                        = '⋯'
ELLIPSIS_DIAGONAL_UP                       = '⋰'
ELLIPSIS_DIAGONAL_DOWN                     = '⋱'

CIRCLE_BLACK                               = '●'
CIRCLE_WHITE                               = '○'
CIRCLE_HEAVY                               = '⭘'
CIRCLE_LARGE_BLACK                         = '⬤'
CIRCLE_LARGE_WHITE                         = '◯'
CIRCLE_LARGE_HEAVY                         = '⭕'

ELLIPSE_HORIZONTAL_BLACK                   = '⬬'
ELLIPSE_HORIZONTAL_WHITE                   = '⬭'
ELLIPSE_VERTICAL_BLACK                     = '⬮'
ELLIPSE_VERTICAL_WHITE                     = '⬯'

TRIANGLE_BLACK                             = '◀▶▲▼◤◥◣◢'
TRIANGLE_WHITE                             = '◁▷△▽◸◹◺◿'
TRIANGLE_SMALL_BLACK                       = '◂▸▴▾'
TRIANGLE_SMALL_WHITE                       = '◃▹▵▿'
TRIANGLE_CENTRED_MEDIUM_BLACK              = '⯇⯈⯅⯆'
TRIANGLE_UNDERBAR                          = '  ⧋'

POINTER_BLACK                              = '◄►'
POINTER_WHITE                              = '◅▻'

SQUARE_BLACK                               = '■'
SQUARE_WHITE                               = '□'
SQUARE_MEDIUM_BLACK                        = '◼'
SQUARE_MEDIUM_WHITE                        = '◻'
SQUARE_SMALL_BLACK                         = '▪'
SQUARE_SMALL_WHITE                         = '▫'
SQUARE_VERY_SMALL_BLACK                    = '⬝'
SQUARE_VERY_SMALL_WHITE                    = '⬞'
SQUARE_CENTRED_BLACK                       = '⯀'

RECTANGLE_HORIZONTAL_BLACK                 = '▬'
RECTANGLE_HORIZONTAL_WHITE                 = '▭'
RECTANGLE_VERTICAL_BLACK                   = '▮'
RECTANGLE_VERTICAL_WHITE                   = '▯'

PARALLELOGRAM_BLACK                        = '▰'
PARALLELOGRAM_WHITE                        = '▱'

DIAMOND_BLACK                              = '◆'
DIAMOND_WHITE                              = '◇'
DIAMOND_MEDIUM_BLACK                       = '⬥'
DIAMOND_MEDIUM_WHITE                       = '⬦'
DIAMOND_SMALL_BLACK                        = '⬩'
DIAMOND_CENTRED_BLACK                      = '⯁'
DIAMOND_WHITE_DOTTED                       = '⟐'

LOZENGE_BLACK                              = '⧫'
LOZENGE_WHITE                              = '◊'
LOZENGE_MEDIUM_BLACK                       = '⬧'
LOZENGE_MEDIUM_WHITE                       = '⬨'
LOZENGE_SMALL_BLACK                        = '⬪'
LOZENGE_SMALL_WHITE                        = '⬫'

CUSP_BLACK                                 = '⯌'
CUSP_WHITE                                 = '⯎'
CUSP_ROTATED_BLACK                         = '⯍'
CUSP_ROTATED_WHITE                         = '⯏'

PENTAGON_BLACK                             = '⬟'
PENTAGON_WHITE                             = '⬠'
PENTAGON_RIGHT_BLACK                       = '⭓'
PENTAGON_RIGHT_WHITE                       = '⭔'
PENTAGON_DOWN_BLACK                        = '⯂'

STAR_SMALL_BLACK                           = '⭑'
STAR_SMALL_WHITE                           = '⭒'

HEXAGON_VERTICAL_WHITE                     = '⬡'
HEXAGON_VERTICAL_BLACK                     = '⬢'
HEXAGON_HORIZONTAL_BLACK                   = '⬣'

OCTAGON_VERTICAL_BLACK                     = '⯄'
OCTAGON_HORIZONTAL_BLACK                   = '⯃'

BRAILLE                                    = '⠀⠁⠂⠃⠄⠅⠆⠇⠈⠉⠊⠋⠌⠍⠎⠏⠐⠑⠒⠓⠔⠕⠖⠗⠘⠙⠚⠛⠜⠝⠞⠟⠠⠡⠢⠣⠤⠥⠦⠧⠨⠩⠪⠫⠬⠭⠮⠯⠰⠱⠲⠳⠴⠵⠶⠷⠸⠹⠺⠻⠼⠽⠾⠿⡀⡁⡂⡃⡄⡅⡆⡇⡈⡉⡊⡋⡌⡍⡎⡏⡐⡑⡒⡓⡔⡕⡖⡗⡘⡙⡚⡛⡜⡝⡞⡟⡠⡡⡢⡣⡤⡥⡦⡧⡨⡩⡪⡫⡬⡭⡮⡯⡰⡱⡲⡳⡴⡵⡶⡷⡸⡹⡺⡻⡼⡽⡾⡿⢀⢁⢂⢃⢄⢅⢆⢇⢈⢉⢊⢋⢌⢍⢎⢏⢐⢑⢒⢓⢔⢕⢖⢗⢘⢙⢚⢛⢜⢝⢞⢟⢠⢡⢢⢣⢤⢥⢦⢧⢨⢩⢪⢫⢬⢭⢮⢯⢰⢱⢲⢳⢴⢵⢶⢷⢸⢹⢺⢻⢼⢽⢾⢿⣀⣁⣂⣃⣄⣅⣆⣇⣈⣉⣊⣋⣌⣍⣎⣏⣐⣑⣒⣓⣔⣕⣖⣗⣘⣙⣚⣛⣜⣝⣞⣟⣠⣡⣢⣣⣤⣥⣦⣧⣨⣩⣪⣫⣬⣭⣮⣯⣰⣱⣲⣳⣴⣵⣶⣷⣸⣹⣺⣻⣼⣽⣾⣿'
BRAILLE_ALTERNATE                          = '⠀⠁⠈⠉⠂⠃⠊⠋⠐⠑⠘⠙⠒⠓⠚⠛⠄⠅⠌⠍⠆⠇⠎⠏⠔⠕⠜⠝⠖⠗⠞⠟⠠⠡⠨⠩⠢⠣⠪⠫⠰⠱⠸⠹⠲⠳⠺⠻⠤⠥⠬⠭⠦⠧⠮⠯⠴⠵⠼⠽⠶⠷⠾⠿⡀⡁⡈⡉⡂⡃⡊⡋⡐⡑⡘⡙⡒⡓⡚⡛⡄⡅⡌⡍⡆⡇⡎⡏⡔⡕⡜⡝⡖⡗⡞⡟⡠⡡⡨⡩⡢⡣⡪⡫⡰⡱⡸⡹⡲⡳⡺⡻⡤⡥⡬⡭⡦⡧⡮⡯⡴⡵⡼⡽⡶⡷⡾⡿⢀⢁⢈⢉⢂⢃⢊⢋⢐⢑⢘⢙⢒⢓⢚⢛⢄⢅⢌⢍⢆⢇⢎⢏⢔⢕⢜⢝⢖⢗⢞⢟⢠⢡⢨⢩⢢⢣⢪⢫⢰⢱⢸⢹⢲⢳⢺⢻⢤⢥⢬⢭⢦⢧⢮⢯⢴⢵⢼⢽⢶⢷⢾⢿⣀⣁⣈⣉⣂⣃⣊⣋⣐⣑⣘⣙⣒⣓⣚⣛⣄⣅⣌⣍⣆⣇⣎⣏⣔⣕⣜⣝⣖⣗⣞⣟⣠⣡⣨⣩⣢⣣⣪⣫⣰⣱⣸⣹⣲⣳⣺⣻⣤⣥⣬⣭⣦⣧⣮⣯⣴⣵⣼⣽⣶⣷⣾⣿'

LINE_EXTENSION                             = '⎯⏐'
BOX_LIGHT                                  = '─│┌┐└┘├┤┬┴┼╴╵╶╷╱╲╳'
BOX_ARC                                    = '─│╭╮╰╯├┤┬┴┼╴╵╶╷╱╲╳'
BOX_HEAVY                                  = '━┃┏┓┗┛┣┫┳┻╋╸╹╺╻   ╼╾╽╿┍┎┑┒┕┖┙┚┝┞┟┠┡┢┥┦┧┨┩┪┭┮┯┰┱┲┵┶┷┸┹┺┽┾┿╀╁╂╃╄╅╆╇╈╉╊'
BOX_DOUBLE                                 = '═║╔╗╚╝╠╣╦╩╬           ╒╓╕╖╘╙╛╜╞  ╟  ╡  ╢    ╤╥    ╧╨    ╪  ╫'
BOX_LIGHT_DOUBLE                           = '╌╎'
BOX_LIGHT_TRIPLE                           = '┄┆'
BOX_LIGHT_QUADRUPLE                        = '┈┊'
BOX_HEAVY_DOUBLE                           = '╍╏'
BOX_HEAVY_TRIPLE                           = '┅┇'
BOX_HEAVY_QUADRUPLE                        = '┉┋'

THIRD_LEFT                                 = ' 🯏🯎█'
EIGHTH_LOWER                               = ' ▁▂▃▄▅▆▇█'
EIGHTH_UPPER                               = ' ▔🮂🮃▀🮄🮅🮆█'
EIGHTH_LEFT                                = ' ▏▎▍▌▋▊▉█'
EIGHTH_RIGHT                               = ' ▕🮇🮈▐🮉🮊🮋█'
SHADE_FOURTH                               = ' ░▒▓█'
ONE_SIXTEENTH                              = '𜺐𜺑𜺒𜺓𜺔𜺕𜺖𜺗𜺘𜺙𜺚𜺛𜺜𜺝𜺞𜺟'
ONE_EIGHTH_VERTICAL                        = '▏🭰🭱🭲🭳🭴🭵▕'
ONE_EIGHTH_HORIZONTAL                      = '▔🭶🭷🭸🭹🭺🭻▁'

TWO_BY_TWO                                 = ' ▘▝▀▖▌▞▛▗▚▐▜▄▙▟█'
TWO_BY_TWO_SEPARATED                       = ' 𜰡𜰢𜰣𜰤𜰥𜰦𜰧𜰨𜰩𜰪𜰫𜰬𜰭𜰮𜰯'
TWO_BY_THREE                               = ' 🬀🬁🬂🬃🬄🬅🬆🬇🬈🬉🬊🬋🬌🬍🬎🬏🬐🬑🬒🬓▌🬔🬕🬖🬗🬘🬙🬚🬛🬜🬝🬞🬟🬠🬡🬢🬣🬤🬥🬦🬧▐🬨🬩🬪🬫🬬🬭🬮🬯🬰🬱🬲🬳🬴🬵🬶🬷🬸🬹🬺🬻█'
TWO_BY_THREE_SEPARATED                     = ' 𜹑𜹒𜹓𜹔𜹕𜹖𜹗𜹘𜹙𜹚𜹛𜹜𜹝𜹞𜹟𜹠𜹡𜹢𜹣𜹤𜹥𜹦𜹧𜹨𜹩𜹪𜹫𜹬𜹭𜹮𜹯𜹰𜹱𜹲𜹳𜹴𜹵𜹶𜹷𜹸𜹹𜹺𜹻𜹼𜹽𜹾𜹿𜺀𜺁𜺂𜺃𜺄𜺅𜺆𜺇𜺈𜺉𜺊𜺋𜺌𜺍𜺎𜺏'
TWO_BY_FOUR                                = ' 𜺨𜺫🮂𜴀▘𜴁𜴂𜴃𜴄▝𜴅𜴆𜴇𜴈▀𜴉𜴊𜴋𜴌🯦𜴍𜴎𜴏𜴐𜴑𜴒𜴓𜴔𜴕𜴖𜴗𜴘𜴙𜴚𜴛𜴜𜴝𜴞𜴟🯧𜴠𜴡𜴢𜴣𜴤𜴥𜴦𜴧𜴨𜴩𜴪𜴫𜴬𜴭𜴮𜴯𜴰𜴱𜴲𜴳𜴴𜴵🮅𜺣𜴶𜴷𜴸𜴹𜴺𜴻𜴼𜴽𜴾𜴿𜵀𜵁𜵂𜵃𜵄▖𜵅𜵆𜵇𜵈▌𜵉𜵊𜵋𜵌▞𜵍𜵎𜵏𜵐▛𜵑𜵒𜵓𜵔𜵕𜵖𜵗𜵘𜵙𜵚𜵛𜵜𜵝𜵞𜵟𜵠𜵡𜵢𜵣𜵤𜵥𜵦𜵧𜵨𜵩𜵪𜵫𜵬𜵭𜵮𜵯𜵰𜺠𜵱𜵲𜵳𜵴𜵵𜵶𜵷𜵸𜵹𜵺𜵻𜵼𜵽𜵾𜵿𜶀𜶁𜶂𜶃𜶄𜶅𜶆𜶇𜶈𜶉𜶊𜶋𜶌𜶍𜶎𜶏▗𜶐𜶑𜶒𜶓▚𜶔𜶕𜶖𜶗▐𜶘𜶙𜶚𜶛▜𜶜𜶝𜶞𜶟𜶠𜶡𜶢𜶣𜶤𜶥𜶦𜶧𜶨𜶩𜶪𜶫▂𜶬𜶭𜶮𜶯𜶰𜶱𜶲𜶳𜶴𜶵𜶶𜶷𜶸𜶹𜶺𜶻𜶼𜶽𜶾𜶿𜷀𜷁𜷂𜷃𜷄𜷅𜷆𜷇𜷈𜷉𜷊𜷋𜷌𜷍𜷎𜷏𜷐𜷑𜷒𜷓𜷔𜷕𜷖𜷗𜷘𜷙𜷚▄𜷛𜷜𜷝𜷞▙𜷟𜷠𜷡𜷢▟𜷣▆𜷤𜷥█'
TWO_BY_TWO_SINGLE                          = '▘▝▖▗'
TWO_BY_TWO_SINGLE_SEPARATED                = '𜰡𜰢𜰤𜰨'
TWO_BY_THREE_SINGLE                        = '🬀🬁🬃🬇🬏🬞'
TWO_BY_THREE_SINGLE_SEPARATED              = '𜹑𜹒𜹔𜹘𜹠𜹰'
TWO_BY_FOUR_SINGLE                         = '𜺨𜺫𜴀𜴃𜴉𜴘𜺣𜺠'
FOUR_BY_FOUR_SINGLE                        = '𜺐𜺑𜺒𜺓𜺔𜺕𜺖𜺗𜺘𜺙𜺚𜺛𜺜𜺝𜺞𜺟'
# 𜺠𜺡𜺢𜺣𜺤𜺥𜺦𜺧𜺨𜺩𜺪𜺫𜺬𜺭𜺮𜺯 

CELSIUS                                    = '℃'
FAHRENHEIT                                 = '℉'
KELVIN                                     = 'K'
"""
𜸚𜸛𜸜𜸝𜸞𜸟𜸠𜸡𜸢𜸣𜸤𜸥𜸦𜸧𜸨𜸩𜸪𜸫𜸬𜸭𜸮𜸯𜸰𜸱𜸲𜸳𜸴𜸵𜸶𜸷𜸸𜸹𜸺𜸻𜸼𜸽𜸾𜸿𜹀𜹁𜹂𜹃𜹄𜹅𜹆𜹇𜹈𜹉𜹊𜹋𜹌𜹍𜹎𜹏𜹐

ARC        = '𜸤𜸚𜸾𜹃'
ARC_RAISED = '𜸵'
CORNER     = '𜸧𜸛𜸽𜹄'
CROTCH     = '𜸦𜸝𜸿𜹆'
DIAGONAL   = '𜸫𜸻𜸢𜸬'
TERMINAL   = '𜸞𜸼𜸥𜸜'
idfk       = '𜸩𜸟'
𜸨 𜹀 𜸶 𜸠 𜸺
"""
"""
----------------- 3x3 -----------------
𜸚𜸟𜸤𜸬𜸦 𜸚𜸟𜸤𜸞𜸟𜸤𜸜 𜸜𜸛𜸟𜸥𜸚𜸟𜸥𜸞𜸟𜸤𜸚𜸟𜸤𜸚𜸟𜸤𜸞𜸟𜸧𜸚𜸟𜸟
𜸩𜸟𜸩 𜸩 𜸬𜸴𜸻𜸞𜸟𜸷𜸽𜸟𜸶𜸽𜸟𜸤𜸨𜸟𜸤  𜸩𜸮𜸟𜸷𜸾𜸟𜸶𜸬𜸴𜸻𜸮𜸟𜸟
𜸾𜸟𜹃𜸞𜹀𜸥𜸽𜸟𜸥𜸞𜸟𜹃  𜸼𜸞𜸟𜹃𜸾𜸟𜹃  𜸼𜸾𜸟𜹃  𜸼𜸾𜸟𜹃𜸾𜸟𜸟
   𜸜       𜸜𜸛𜸟𜸥𜸚𜸟𜸥𜸚𜸟𜸤𜸜   𜸣  𜸣 𜸜   𜸜 
𜸚𜸟𜸧𜸨𜸟𜸤𜸚𜸟𜸥𜸚𜸟𜸶𜸨𜸟𜸥𜸨𜸟𜸥𜸾𜸟𜸶𜸨𜸟𜸤 𜸜  𜸜 𜸨𜸟𜸷 𜸩 𜸚𜸠𜸤
𜸾𜸟𜹄𜸽𜸟𜹃𜸾𜸟𜸥𜸾𜸟𜹄𜸽𜸟𜸥𜸼  𜸾𜸟𜹃𜸼 𜸼 𜸼 𜸾𜹃 𜸼 𜸼 𜸾𜸥𜸼𜸼𜸼
       𜸚𜸤𜸚𜸤        𜸺          𜸜 𜸜𜸜 𜸜𜸞𜸟𜸧
𜸛𜸟𜸤𜸚𜸟𜸤 𜸨𜹃𜸾𜸶  𜸚𜸥 𜸚𜸥 𜸩 𜸜 𜸜𜸜 𜸜𜸜𜸜𜸜𜸪𜸲𜸸𜸫𜸳𜸻𜸬𜸴𜸻
𜸼 𜸼𜸾𜸟𜹃 𜸼  𜸿𜸻 𜸼 𜸞𜹃  𜸾𜹃𜸾𜸟𜹃𜸫𜹁𜸻𜸾𜹀𜹃𜸼 𜸼 𜸼 𜸽𜸟𜸥
𜸚𜸟𜸤𜸛𜸟𜸤𜸚𜸟𜸥𜸛𜸟𜸤𜸛𜸟𜸥𜸛𜸟𜸥𜸚𜸟𜸥𜸜 𜸜𜸞𜸠𜸥𜸞𜸟𜸧𜸜 𜸜𜸜  𜸝𜸡𜸦
𜸨𜸟𜸶𜸨𜸟𜸷𜸩  𜸩 𜸩𜸨𜸟𜸥𜸨𜸟𜸥𜸩𜸞𜸧𜸨𜸟𜸶 𜸩   𜸩𜸨𜸯𜸸𜸩  𜸩𜸰𜸩
𜸼 𜸼𜸽𜸟𜹃𜸾𜸟𜸥𜸽𜸟𜹃𜸽𜸟𜸥𜸼  𜸾𜸟𜹃𜸼 𜸼𜸞𜹀𜸥𜸾𜸟𜹃𜸼 𜸼𜸽𜸟𜸥𜸼 𜸼
𜸝𜸢𜸜𜸚𜸟𜸤𜸛𜸟𜸤𜸚𜸟𜸤𜸛𜸟𜸤𜸚𜸟𜸥𜸞𜸠𜸥𜸜 𜸜𜸜 𜸜𜸜 𜸜𜸜 𜸜𜸜 𜸜𜸞𜸟𜸧
𜸩𜸩𜸩𜸩 𜸩𜸨𜸟𜹃𜸩 𜸩𜸨𜸟𜸷𜸾𜸟𜸤 𜸩 𜸩 𜸩𜸩 𜸩𜸩𜸱𜸩𜸪𜸲𜸸𜸫𜸳𜸻𜸬𜸴𜸻
𜸼𜸫𜹆𜸾𜸟𜹃𜸼  𜸾𜸟𜹅𜸼 𜸼𜸞𜸟𜹃 𜸼 𜸾𜸟𜹃𜸫𜹁𜸻𜸿𜹂𜹆𜸼 𜸼 𜸼 𜸽𜸟𜸥
------------------- 3x3ascii -------------------
    𜸜 𜹐 𜹐𜸺𜸟𜸺𜸚𜸺𜸥𜸣 𜸬𜸚𜸤  𜹐  𜸚𜸥𜸞𜸤 𜸢𜸜𜸬 𜸣           𜸬𜹃
    𜸩    𜸩 𜸩𜸾𜸺𜸤𜸬𜸴𜸻𜸮𜹀𜸠    𜸩  𜸩 𜸪𜸺𜸸𜸞𜸺𜸥   𜸞𜸟𜸥    𜸩  
    𜹍    𜸺𜸟𜸺𜸞𜸺𜹃𜸻 𜸭𜸾𜸟𜹅    𜸾𜸥𜸞𜹃 𜸻𜸼𜸫 𜸭  𜹃     𜸭 𜸚𜸻  
𜸚𜸟𜸤𜸬𜸦 𜸚𜸟𜸤𜸞𜸟𜸤𜸜 𜸜𜸛𜸟𜸥𜸚𜸟𜸥𜸞𜸟𜸤𜸚𜸟𜸤𜸚𜸟𜸤 𜸣  𜸣  𜸬𜹃𜸞𜸟𜸥𜸾𜸢 𜸚𜸟𜸤
𜸩𜸟𜸩 𜸩 𜸬𜸴𜸻𜸞𜸟𜸷𜸽𜸟𜸶𜸽𜸟𜸤𜸨𜸟𜸤  𜸩𜸮𜸟𜸷𜸾𜸟𜸶      𜹍𜸸     𜸪𜹍 𜸚𜹃
𜸾𜸟𜹃𜸞𜹀𜸥𜸽𜸟𜸥𜸞𜸟𜹃  𜸼𜸞𜸟𜹃𜸾𜸟𜹃  𜸼𜸾𜸟𜹃  𜸼 𜸭  𜹃  𜸫𜸤𜸞𜸟𜸥𜸚𜸻  𜹏 
𜸚𜸟𜸤𜸚𜸟𜸤𜸛𜸟𜸤𜸚𜸟𜸥𜸛𜸟𜸤𜸛𜸟𜸥𜸛𜸟𜸥𜸚𜸟𜸥𜸜 𜸜𜸞𜸠𜸥𜸞𜸟𜸧𜸜 𜸜𜸜  𜸝𜸡𜸦𜸝𜸢𜸜𜸚𜸟𜸤
𜸩𜸝𜸩𜸨𜸟𜸶𜸨𜸟𜸷𜸩  𜸩 𜸩𜸨𜸟𜸥𜸨𜸟𜸥𜸩𜸞𜸧𜸨𜸟𜸶 𜸩   𜸩𜸨𜸯𜸸𜸩  𜸩𜸰𜸩𜸩𜸩𜸩𜸩 𜸩
𜸾𜸾𜹃𜸼 𜸼𜸽𜸟𜹃𜸾𜸟𜸥𜸽𜸟𜹃𜸽𜸟𜸥𜸼  𜸾𜸟𜹃𜸼 𜸼𜸞𜹀𜸥𜸾𜸟𜹃𜸼 𜸼𜸽𜸟𜸥𜸼 𜸼𜸼𜸫𜹆𜸾𜸟𜹃
𜸛𜸟𜸤𜸚𜸟𜸤𜸛𜸟𜸤𜸚𜸟𜸥𜸞𜸠𜸥𜸜 𜸜𜸜 𜸜𜸜 𜸜𜸜 𜸜𜸜 𜸜𜸞𜸟𜸧 𜸛𜸥𜸾𜸢 𜸞𜸧 𜸚𜹂𜸤   
𜸨𜸟𜹃𜸩 𜸩𜸨𜸟𜸷𜸾𜸟𜸤 𜸩 𜸩 𜸩𜸩 𜸩𜸩𜸱𜸩𜸪𜸲𜸸𜸫𜸳𜸻𜸬𜸴𜸻 𜸩  𜸩  𜸩 𜸻 𜸫   
𜸼  𜸾𜸟𜹅𜸼 𜸼𜸞𜸟𜹃 𜸼 𜸾𜸟𜹃𜸫𜹁𜸻𜸿𜹂𜹆𜸼 𜸼 𜸼 𜸽𜸟𜸥 𜸽𜸥 𜸫𜸤𜸞𜹄    𜸞𜸟𜸥
 𜸢    𜸜       𜸜𜸚𜸟𜸤 𜸚𜸥𜸚𜸟𜸤𜸜   𜸣  𜸣 𜸜   𜸜          
 𜸫 𜸚𜸟𜸧𜸨𜸟𜸤𜸚𜸟𜸥𜸚𜸟𜸶𜸨𜸟𜹄𜸞𜸺𜸥𜸾𜸟𜸶𜸨𜸟𜸤 𜸜  𜸜 𜸨𜸟𜸷 𜸩 𜸚𜸠𜸤𜸚𜸟𜸤𜸚𜸟𜸤
   𜸾𜸟𜹄𜸽𜸟𜹃𜸾𜸟𜸥𜸾𜸟𜹄𜸾𜸟𜸥 𜸼 𜸾𜸟𜹃𜸼 𜸼 𜸼 𜸾𜹃 𜸼 𜸼 𜸾𜸥𜸼𜸼𜸼𜸼 𜸼𜸾𜸟𜹃
 𜸚𜸤𜸚𜸤        𜸣                    𜸚𜸥 𜸩 𜸞𜸤 𜸬𜸢𜸬
 𜸨𜹃𜸾𜸶  𜸚𜸥 𜸚𜸥𜸞𜸺𜸥𜸜 𜸜𜸜 𜸜𜸜𜸜𜸜𜸪𜸲𜸸𜸫𜸳𜸻𜸞𜸧 𜸞𜸷     𜸮𜸥𜸻𜸫𜸻𜸾𜸠𜹃
 𜸼  𜸿𜸻 𜸼 𜸞𜹃  𜸾𜸥𜸾𜸟𜹃𜸫𜹁𜸻𜸾𜹀𜹃𜸼 𜸼 𜸼  𜸽𜸥 𜸾𜸥 𜸩 𜸞𜹃     𜸼 𜸫𜸹
𜸣𜹇𜹈𜹉𜹊𜹋𜹌𜹍𜹎𜹏𜹐𜸭	
𜸾𜸡𜹃
𜸚𜹂𜸤
𜸚𜸤𜸵   𜸢 𜸬𜸴  
𜸮𜸷 𜸯  𜸪𜸲𜸸 𜸫𜹁𜸻𜸫𜸳𜸻
𜸾𜹃 𜹅 𜸴𜸻 𜸫
𜸛𜸟𜸠𜸟𜸧
𜸩 𜸜 𜸩
𜸨𜸞𜸺𜸥𜸶
𜸩 𜸼 𜸩
𜸽𜸟𜹀𜸟𜹄
𜸝𜸡𜸦 𜸱
𜸿𜹂𜹆𜸹𜸰

------------------------ 4x3 -----------------------
𜸚𜸟𜸟𜸤𜸛𜸟𜸟𜸤𜸚𜸟𜸟𜸥𜸛𜸟𜸟𜸤𜸛𜸟𜸟𜸥𜸛𜸟𜸟𜸥𜸚𜸟𜸟𜸥𜸜  𜸜 𜸟𜸠𜸟 𜸟𜸠𜸟𜸜  𜸜𜸜   𜸝𜸢𜸬𜸦
𜸨𜸟𜸟𜸶𜸨𜸟𜸟𜸷𜸩   𜸩  𜸩𜸨𜸟𜸟𜸥𜸨𜸟𜸟𜸥𜸩 𜸞𜸧𜸨𜸟𜸟𜸶  𜸩   𜸩 𜸨𜸟𜸯𜸸𜸩   𜸩𜸫𜸻𜸩    
𜸼  𜸼𜸽𜸟𜸟𜹃𜸾𜸟𜸟𜸥𜸽𜸟𜸟𜹃𜸽𜸟𜸟𜸥𜸼   𜸾𜸟𜸟𜹃𜸼  𜸼 𜸟𜹀𜸟𜸾𜸟𜹃 𜸼  𜸼𜸽𜸟𜸟𜸥𜸼  𜸼
𜸝𜸢 𜸜𜸚𜸟𜸟𜸤𜸛𜸟𜸟𜸤𜸚𜸟𜸟𜸤𜸛𜸟𜸟𜸤𜸚𜸟𜸟𜸥 𜸟𜸠𜸟𜸜  𜸜𜸜  𜸜𜸜  𜸜𜸞𜸢𜸬𜸥 𜸜 𜸜 𜸞𜸟𜸧
𜸩𜸾𜸤𜸩𜸩  𜸩𜸨𜸟𜸟𜹃𜸩  𜸩𜸨𜸟𜸟𜸷𜸾𜸟𜸟𜸤  𜸩 𜸩  𜸩𜸾𜸢𜸬𜹃𜸩𜸬𜸢𜸩 𜸮𜸷  𜸫𜸳𜸻 𜸬𜸴𜸻  
𜸼 𜸫𜹆𜸾𜸟𜸟𜹃𜸼   𜸾𜸟𜸟𜹅𜸼  𜸼𜸞𜸟𜸟𜹃  𜸼 𜸾𜸟𜸟𜹃 𜸫𜸻 𜸿𜸻𜸫𜹆𜸞𜸻𜸫𜸥  𜸼  𜸽𜸟𜸥    

𜸝𜸢 𜸬𜸦
𜸩𜸫𜹁𜸻𜸩
𜸼   𜸼


"""

"""
# 0 1
# 2 3
LINE_QUADRANTS = [
		['𜺐' , '▔' , '▏' , '╲' ],
		['▔' , '𜺓' , '╱' , '▕' ],
		['▏' , '╱' , '𜺜' , '▁' ],
		['╲' , '▕' , '▁' , '𜺟' ],
		]

# 0 1
# 2 3
LINE_QUADRANTS_TWO = ''

# 012
# 345
# 678
LINE_NONANTS = [
		['\0', None, '▔' , None, None, '🯒' , '▏' , '🯔' , '╲' ],
		[None, '\0', None, '🮠' , '╵' , '🮡' , '🯗' , '│' , '🯕' ],
		['▔' , None, '\0', '🯑' , None, None, '╱' , '🯖' , '▕' ],
		[None, '🮠' , '🯑' , '\0', '╴' , '─' , None, '🮢' , '🯓' ],
		[None, '╵' , None, '╴' , '\0', '╶' , None, '╷' , None],
		['🯒' , '🮡' , None, '─' , '╶' , '\0', '🯐' , '🮣' , None],
		['▏' , '🯗' , '╱' , None, None, '🯐' , '\0', None, '▁' ],
		['🯔' , '│' , '🯖' , '🮢' , '╷' , '🮣' , None, '\0', None],
		['╲' , '🯕' , '▕' , '🯓' , None, None, '▁' , None, '\0'],
		]
"""
