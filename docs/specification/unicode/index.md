# unicode

daamath maintains a namespace tree of unicode characters — each with has exactly one name and stored exactly once as the implementation's native string/character format (instead of the codepoint uint). 

a tree is not the most natural way — parameterized functions are more natural — but using the namespace as the wayfinder is both terser and faster, so daamath does it this way.

# miscellaneous

characters that could not be categorized are listed here:

```yaml
roman_numeral_upper                        :  ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩⅪⅫ        ⅬⅭⅮⅯ
roman_numeral_lower                        :  ⅰⅱⅲⅳⅴⅵⅶⅷⅸⅹⅺⅻ        ⅼⅽⅾⅿ
counting_rod_vertical                      : 〇𝍩𝍪𝍫𝍬𝍭𝍮𝍯𝍰𝍱
counting_rod_horizontal                    : 〇𝍠𝍡𝍢𝍣𝍤𝍥𝍦𝍧𝍨
counting_rod_negative                      : U+20E5
tally_mark                                 :  𝍷   𝍸
tally_mark_ideographic                     :  𝍲𝍳𝍴𝍵𝍶
decimal_exponent                           : ⏨
hebrew                                     : ℵℶℷℸ
reciprocal                                 : ⅟
                                          
increment                                  : ∆

nabla: ∇
nabla_italic: 𝛻
nabla_bold: 𝛁
nabla_bold_sans_serif: 𝝯
nabla_bold_italic: 𝜵
nabla_bold_italic_sans_serif: 𝞩
                                           
partial                                    : ∂
partial_bold                               : 𝛛
partial_italic                             : 𝜕
partial_bold_italic                        : 𝝏
partial_sans_serif_bold                    : 𝞉
partial_sans_serif_bold_italic             : 𝟃
                                        
operator:
  ring: ∘ # not same as °
  asterisk: ∗ # not same as *
  bullet: ∙ # not same as .
  tilde: ∼ # not same as ~
  tilde_reversed: ∽
  dot: ⋅ # not same as ·
  dot_squared: ⊡
  dot_circled: ⊙
  dot_circled_big: ⨀ # not same as ⊙
  reverse_solidus: ⧵
  diamond: ⋄
  star: ⋆
  triple_colon: ⫶
                                           
for_all                                    : ∀
complement                                 : ∁
exists                                     : ∃
exists_stroke                              : ∄
proportional                               : ∝
infinity                                   : ∞
root                                       : √∛∜
prime                                      : ′″‴⁗
prime_reversed                             : ‵‶‷
                                          
wreath_product                             : ≀
therefore                                  : ∴
because                                    : ∵
ratio                                      : ∶ # not same as :
proportion                                 : ∷ # not same as ::
angle                                      : ∠
                                           
plus                                       : +
plus_double                                : ⧺
plus_triple                                : ⧻
plus_dot                                   : ∔
plus_underbar                              : ±
plus_overbar                               : ∓
plus_overbar_double                        : ⩱
plus_underbar_double                       : ⩲
plus_squared                               : ⊠
plus_circled                               : ⊕
plus_big_circled                           : ⨁  # not same as ⊕
                                           
bar                                        : − # minus
tilde                                      : '~'
tilde_stroke                               : ≁
tilde_reverse                              : ∽
bar_bar                                    : '=' # equals
bar_bar_doubled                            : ⩵
bar_bar_tripled                            : ⩶
bar_bar_stroke                             : ≠
bar_tilde                                  : ≂
tilde_bar                                  : ≃
tilde_bar_stroke                           : ≄
tilde_reverse_bar                          : ⋍
tilde_tilde                                : ≈
tilde_tilde_stroke                         : ≉
bar_bar_bar                                : ≡
bar_bar_bar_stroke                         : ≢
bar_bar_tilde                              : ⩳
tilde_bar_bar                              : ≅
tilde_bar_bar_stroke                       : ≇≆
tilde_reverse_bar_bar                      : ≌
tilde_bar_tilde                            : ⩬
tilde_tilde_bar                            : ≊
tilde_tilde_tilde                          : ≋
bar_bar_bar_bar                            : ≣
tilde_tilde_bar_bar                        : ⩰
bar_overdot                                : ∸
bar_squared                                : ⊟
bar_circled                                : ⊖
                                          
times                                      : × # not same as x
times_big                                  : ⨉ # not same as ×
times_squared                              : ⊞
times_circled                              : ⊗
times_big_circled                          : ⨂ # not same as ⊗
                                          
division_slash                             : ∕ # not same as /
division_sign                              : ÷ # unconventional. use ∕
fraction                                   : ⁄ # not same as ∕
cross_product                              : ⨯ # not same as ×
coproduct                                  : ⨿
interior_product                           : ⨼
interior_right                             : ⨽
n_ary_product                              : ∏
n_ary_coproduct                            : ∐
n_ary_summation                            : ∑ # not same as Σ
set_minus                                  : ∖
                                           
wedge: 
  left: <
  right: >
  up: ∧
  down: ∨
  stroke: 
    left: ≮
    right: ≯
    underbar: 
      left: ≰
      right: ≱
  dash: 
    up: ⩜
    down: ⩝
  stem: 
    up: ⩚
    down: ⩛
  dot: 
    left: ⋖
    right: ⋗
    up: ⟑
    down: ⟇
  circle: 
    left: ⩹
    right: ⩺
  question_mark: 
    left: ⩻
    right: ⩼
  over: 
    bar:
      left: ⋜
      right: ⋝
      up: ⊼
      down: ⊽
      slant: 
        left: ⪕
        right: ⪖
        dot: 
          left: ⪗
          right: ⪘
      double: 
        left: ⪙
        right: ⪚
        up: ⩞
        down: ⩢
  under:
    bar: 
      left: ≤
      right: ≥
      up: ⩟
      down: ⊻
      slant: 
        left: ⩽
        right: ⩾
      double: 
        left: ≦
        right: ≧
        up: ⩠
        down: ⩣
  double: 
    left: ≪
    right: ≫
    underbar: 
      left: ⪣
    intersect:
      up: ⩕
      down: ⩖
    nest:
      double:
        left: ⪡
        right: ⪢
        up: ⩓
        down: ⩔
  closed: 
    left: ⪦
    right: ⪧
    under:
      bar:
        slant: 
          left: ⪨
          right: ⪩
  triple: 
    left: ⋘
    right: ⋙
    nest: 
      left: ⫷
      right: ⫸ 
  big: 
    left: ⋀
    right: ⋁
  fullwidth: 
    left: ＜
    right: ＞
  circled: 
    left: ⧀
    right: ⧁
  squared: 
    up: ⟎
    down: ⟏
                                          
curve: 
  left: ≺
  right: ≻
  up: ⋏
  down: ⋎
  double: 
    left: ⪻
    right: ⪼
  stroke: 
    left: ⊀
    right: ⊁
    under:
      bar:
        slant: 
          left: ⋠
          right: ⋡
  under:
    bar: 
      left: ⪯
      right: ⪰
      slant: 
        left: ≼ 
        right: ≽
  over:
    bar:
      slant: 
        left: ⋞
        right: ⋟
      curved: 
        left: ⋞
        right: ⋟

cup: 
  left: ⊂
  right: ⊃
  up: ∩
  down: ∪
  circle: 
    left: ⟃
    right: ⟄
  dot: 
    left: ⪽
    right: ⪾
  stroke: 
    left: ⊄
    right: ⊅
    under:
      bar: 
        left: ⊈
        right: ⊉
  double: 
    left: ⋐
    right: ⋑
    up: ⋒
    down: ⋓
  under:
    bar: 
      left: ⊆
      right: ⊇
      stroke: 
        left: ⊊
        right: ⊋
      double: 
        left: ⫅
        right: ⫆
        stroke: 
          left: ⫋
          right: ⫌
    tilde: 
      left: ⫇
      right: ⫈
      double: 
        left: ⫉
        right: ⫊
    plus: 
      left: ⪿
      right: ⫀
    times: 
      left: ⫁
      right: ⫂
  over:
    bar:
      up: ⩃
      down: ⩂
  closed: 
    left: ⫏
    right: ⫐
  big:
    up: ⋂
    down: ⋃
                                          
solidus                                    : /\
solidus_double                             : ⫽
solidus_big                                : ⧸⧹
solidus_overbar                            : ⧶
solidus_dash                               : ⧷
solidus_circled                            : ⦸
                                           
in: 
  left: ∈
  right: ∋
  up: ⫙
  down: ⟒
  stroke: 
    left: ∉
    right: ∌
  overbar: 
    left: ⋶
    right: ⋽
  underbar: 
    left: ⋸
  small: 
    left: ∊
    right: ∍
    overbar:
      left: ⋷
      right: ⋾
                                          
tack:
  left: ⊢
  right: ⊣
  up: ⊤
  down: ⊥
  right_left: ⟛
  double: 
    up: ⫪
    down: ⫫
    right_left: ⟚
  short:  
    right: ⫞
    up: ⫟
    down: ⫠
  long: 
    left: ⟝
    right: ⟞   
  big:
    up: ⟙
    down: ⟘ 
                                           
triangle                                   : ⊲⊳
triangle_underbar                          : ⊴⊵
triangle_stroke                            : ⋪⋫
triangle_stroke_underbar                   : ⋬⋭
triangle_big                               : ⨞ 
                                      
box: 
  left: ⊏
  right: ⊐
  up: ⊓
  down: ⊔
  double: 
    up: ⩎
    down: ⩏
  under: 
    bar: 
      left: ⊑
      right: ⊒
    stroke: 
      left: ⋤
      right: ⋥
  stroke:
    under:
      bar:
        left: ⋢
        right: ⋣
  big:   
    up: ⨅
    down: ⨆

integral: 
  single: ∫
  double: ∬
  triple: ∭
  quadruple: ⨌
  closed: 
    single: ∮
    double: ∯
    triple: ∰
  overbar: 
    single: ⨛
  underbar:
    single: ⨜
  big: 
    top: ⌠
    middle: ⎮
    bottom: ⌡

divides: 
  'yes': ∣
  'no': ∤
parallel:
  'yes': ∥
  'no': ∦

vertical_line                              : |
vertical_line_white                        : ⫾
vertical_line_big_white                    : ⫿
vertical_line_double                       : ‖ # not same as ||
vertical_bar_circled                       : ⦶

intercalate                                : ⊺ # not same as T
perpendicular                              : ⟂ # not same as ⊥
empty_set                                  : ∅ # not same as θ
diameter                                   : ⌀ # not same as ∅
numero                                     : №
euler_constant                             : ℇ # unconventional. use γ or 𝛾
dotless_italic_i                           : 𝚤
dotless_italic_j                           : 𝚥
shuffle_product                            : ⧢
tiny                                       : ⧾
miny                                       : ⧿
degree                                     : °
                                          
not                                        : ¬
not_reversed                               : ⌐
not_turned                                 : ⌙
                                          
big_sigma:
  top: ⎲
  bottom: ⎳
                                           
circled_division_slash                     : ⊘
circled_division_sign                      : ⨸ # unconventional. use ⊘
circled_equal                              : ⊜
circled_parallel                           : ⦷
circled_perpendicular                      : ⦹
circled_less_than                          : 
circled_greater_than                       : 
circled_triangle                           : ⎊
                                           
asterisk_squared                           : ⧆
circle_squared                             : ⧇
square_squared                             : ⧈
                                           
ellipsis:
  bottomed: 
    horizontal: …
  centred:
    vertical: ⋮
    horizontal: ⋯
    forward: ⋰ # like how / is forward slash
    backward: ⋱ # like how \ is backward slash


braille                                    : ⠀⠁⠂⠃⠄⠅⠆⠇⠈⠉⠊⠋⠌⠍⠎⠏⠐⠑⠒⠓⠔⠕⠖⠗⠘⠙⠚⠛⠜⠝⠞⠟⠠⠡⠢⠣⠤⠥⠦⠧⠨⠩⠪⠫⠬⠭⠮⠯⠰⠱⠲⠳⠴⠵⠶⠷⠸⠹⠺⠻⠼⠽⠾⠿⡀⡁⡂⡃⡄⡅⡆⡇⡈⡉⡊⡋⡌⡍⡎⡏⡐⡑⡒⡓⡔⡕⡖⡗⡘⡙⡚⡛⡜⡝⡞⡟⡠⡡⡢⡣⡤⡥⡦⡧⡨⡩⡪⡫⡬⡭⡮⡯⡰⡱⡲⡳⡴⡵⡶⡷⡸⡹⡺⡻⡼⡽⡾⡿⢀⢁⢂⢃⢄⢅⢆⢇⢈⢉⢊⢋⢌⢍⢎⢏⢐⢑⢒⢓⢔⢕⢖⢗⢘⢙⢚⢛⢜⢝⢞⢟⢠⢡⢢⢣⢤⢥⢦⢧⢨⢩⢪⢫⢬⢭⢮⢯⢰⢱⢲⢳⢴⢵⢶⢷⢸⢹⢺⢻⢼⢽⢾⢿⣀⣁⣂⣃⣄⣅⣆⣇⣈⣉⣊⣋⣌⣍⣎⣏⣐⣑⣒⣓⣔⣕⣖⣗⣘⣙⣚⣛⣜⣝⣞⣟⣠⣡⣢⣣⣤⣥⣦⣧⣨⣩⣪⣫⣬⣭⣮⣯⣰⣱⣲⣳⣴⣵⣶⣷⣸⣹⣺⣻⣼⣽⣾⣿
braille_alternate                          : ⠀⠁⠈⠉⠂⠃⠊⠋⠐⠑⠘⠙⠒⠓⠚⠛⠄⠅⠌⠍⠆⠇⠎⠏⠔⠕⠜⠝⠖⠗⠞⠟⠠⠡⠨⠩⠢⠣⠪⠫⠰⠱⠸⠹⠲⠳⠺⠻⠤⠥⠬⠭⠦⠧⠮⠯⠴⠵⠼⠽⠶⠷⠾⠿⡀⡁⡈⡉⡂⡃⡊⡋⡐⡑⡘⡙⡒⡓⡚⡛⡄⡅⡌⡍⡆⡇⡎⡏⡔⡕⡜⡝⡖⡗⡞⡟⡠⡡⡨⡩⡢⡣⡪⡫⡰⡱⡸⡹⡲⡳⡺⡻⡤⡥⡬⡭⡦⡧⡮⡯⡴⡵⡼⡽⡶⡷⡾⡿⢀⢁⢈⢉⢂⢃⢊⢋⢐⢑⢘⢙⢒⢓⢚⢛⢄⢅⢌⢍⢆⢇⢎⢏⢔⢕⢜⢝⢖⢗⢞⢟⢠⢡⢨⢩⢢⢣⢪⢫⢰⢱⢸⢹⢲⢳⢺⢻⢤⢥⢬⢭⢦⢧⢮⢯⢴⢵⢼⢽⢶⢷⢾⢿⣀⣁⣈⣉⣂⣃⣊⣋⣐⣑⣘⣙⣒⣓⣚⣛⣄⣅⣌⣍⣆⣇⣎⣏⣔⣕⣜⣝⣖⣗⣞⣟⣠⣡⣨⣩⣢⣣⣪⣫⣰⣱⣸⣹⣲⣳⣺⣻⣤⣥⣬⣭⣦⣧⣮⣯⣴⣵⣼⣽⣶⣷⣾⣿
                                          
line_extension: 
  horizontal: ⎯
  vertical: ⏐
line: 
  horizontal: ─
  vertical: │
  north:
    west: ┌
    east: ┐
  south:
    west: └
    east: ┘
  left: ├
  right: ┤
  up: ┬
  down: ┴
  plus: ┼
  half:
    left: ╴
    top: ╵
    right: ╶
    bottom: ╷
  forward: ╱
  backward: ╲
  cross: ╳
  arc:
    north:
      west: ╭
      east: ╮
    south:
      west: ╰
      east: ╯
  heavy                                  : ━┃┏┓┗┛┣┫┳┻╋╸╹╺╻   ╼╾╽╿┍┎┑┒┕┖┙┚┝┞┟┠┡┢┥┦┧┨┩┪┭┮┯┰┱┲┵┶┷┸┹┺┽┾┿╀╁╂╃╄╅╆╇╈╉╊
  doubled                                : ═║╔╗╚╝╠╣╦╩╬           ╒╓╕╖╘╙╛╜╞  ╟  ╡  ╢    ╤╥    ╧╨    ╪  ╫
  light_double                           : ╌╎
  light_triple                           : ┄┆
  light_quadruple                        : ┈┊
  heavy_double                           : ╍╏
  heavy_triple                           : ┅┇
  heavy_quadruple                        : ┉┋
                                           
third_left                                 :  🯏🯎█
eighth_lower                               :  ▁▂▃▄▅▆▇█
eighth_upper                               :  ▔🮂🮃▀🮄🮅🮆█
eighth_left                                :  ▏▎▍▌▋▊▉█
eighth_right                               :  ▕🮇🮈▐🮉🮊🮋█
shade:
  fourth: 
    one: ░
    two: ▒
    three: ▓
one_sixteenth                              : 𜺐𜺑𜺒𜺓𜺔𜺕𜺖𜺗𜺘𜺙𜺚𜺛𜺜𜺝𜺞𜺟
one_eighth_vertical                        : ▏🭰🭱🭲🭳🭴🭵▕
one_eighth_horizontal                      : ▔🭶🭷🭸🭹🭺🭻▁
                                           
quadrant                                   :  ▘▝▀▖▌▞▛▗▚▐▜▄▙▟█
quadrant_separated                         :  𜰡𜰢𜰣𜰤𜰥𜰦𜰧𜰨𜰩𜰪𜰫𜰬𜰭𜰮𜰯
sextant                                    :  🬀🬁🬂🬃🬄🬅🬆🬇🬈🬉🬊🬋🬌🬍🬎🬏🬐🬑🬒🬓▌🬔🬕🬖🬗🬘🬙🬚🬛🬜🬝🬞🬟🬠🬡🬢🬣🬤🬥🬦🬧▐🬨🬩🬪🬫🬬🬭🬮🬯🬰🬱🬲🬳🬴🬵🬶🬷🬸🬹🬺🬻█
sextant_separated                          :  𜹑𜹒𜹓𜹔𜹕𜹖𜹗𜹘𜹙𜹚𜹛𜹜𜹝𜹞𜹟𜹠𜹡𜹢𜹣𜹤𜹥𜹦𜹧𜹨𜹩𜹪𜹫𜹬𜹭𜹮𜹯𜹰𜹱𜹲𜹳𜹴𜹵𜹶𜹷𜹸𜹹𜹺𜹻𜹼𜹽𜹾𜹿𜺀𜺁𜺂𜺃𜺄𜺅𜺆𜺇𜺈𜺉𜺊𜺋𜺌𜺍𜺎𜺏
octant                                     :  𜺨𜺫🮂𜴀▘𜴁𜴂𜴃𜴄▝𜴅𜴆𜴇𜴈▀𜴉𜴊𜴋𜴌🯦𜴍𜴎𜴏𜴐𜴑𜴒𜴓𜴔𜴕𜴖𜴗𜴘𜴙𜴚𜴛𜴜𜴝𜴞𜴟🯧𜴠𜴡𜴢𜴣𜴤𜴥𜴦𜴧𜴨𜴩𜴪𜴫𜴬𜴭𜴮𜴯𜴰𜴱𜴲𜴳𜴴𜴵🮅𜺣𜴶𜴷𜴸𜴹𜴺𜴻𜴼𜴽𜴾𜴿𜵀𜵁𜵂𜵃𜵄▖𜵅𜵆𜵇𜵈▌𜵉𜵊𜵋𜵌▞𜵍𜵎𜵏𜵐▛𜵑𜵒𜵓𜵔𜵕𜵖𜵗𜵘𜵙𜵚𜵛𜵜𜵝𜵞𜵟𜵠𜵡𜵢𜵣𜵤𜵥𜵦𜵧𜵨𜵩𜵪𜵫𜵬𜵭𜵮𜵯𜵰𜺠𜵱𜵲𜵳𜵴𜵵𜵶𜵷𜵸𜵹𜵺𜵻𜵼𜵽𜵾𜵿𜶀𜶁𜶂𜶃𜶄𜶅𜶆𜶇𜶈𜶉𜶊𜶋𜶌𜶍𜶎𜶏▗𜶐𜶑𜶒𜶓▚𜶔𜶕𜶖𜶗▐𜶘𜶙𜶚𜶛▜𜶜𜶝𜶞𜶟𜶠𜶡𜶢𜶣𜶤𜶥𜶦𜶧𜶨𜶩𜶪𜶫▂𜶬𜶭𜶮𜶯𜶰𜶱𜶲𜶳𜶴𜶵𜶶𜶷𜶸𜶹𜶺𜶻𜶼𜶽𜶾𜶿𜷀𜷁𜷂𜷃𜷄𜷅𜷆𜷇𜷈𜷉𜷊𜷋𜷌𜷍𜷎𜷏𜷐𜷑𜷒𜷓𜷔𜷕𜷖𜷗𜷘𜷙𜷚▄𜷛𜷜𜷝𜷞▙𜷟𜷠𜷡𜷢▟𜷣▆𜷤𜷥█
#celsius: ℃ # not same as °C
#fahrenheit: ℉ # not same as °F
#kelvin: K # not same as K; do NOT use degree symbol °
#angstrom                   : Å # not same as Å; unconventional. use Å
#ohm                        : Ω 
#mho                        : ℧ 


# use these special characters only if you will display them without typesetting. generally try to rely on typesetting software if it is available'
```
