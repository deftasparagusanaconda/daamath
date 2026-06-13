greeks = {
    'greek_upper'                               : 'ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩϜϺͶϷͰϘͲͿϚ',
    'greek_upper_variant'                       : '       ϴ                     ϞϠ  ',
    'greek_lower'                               : 'αβγδεζηθικλμνξοπρστυφχψωϝϻͷϸͱϙͳϳϛ',
    'greek_lower_variant'                       : ' ϐ  ϵ  ϑ ϰ     ϖϱς  ϕ        ϟϡ  ',
    'greek_lower_superscript'                   : ' ᵝᵞᵟᵋ  ᶿᶥ           ᵠᵡ           ',
    'greek_lower_subscript'                     : ' ᵦᵧ             ᵨ   ᵩᵪ           ',
    'greek_bold_upper'                          : '𝚨𝚩𝚪𝚫𝚬𝚭𝚮𝚯𝚰𝚱𝚲𝚳𝚴𝚵𝚶𝚷𝚸𝚺𝚻𝚼𝚽𝚾𝚿𝛀𝟊        ',
    'greek_bold_upper_variant'                  : '       𝚹                         ',
    'greek_bold_lower'                          : '𝛂𝛃𝛄𝛅𝛆𝛇𝛈𝛉𝛊𝛋𝛌𝛍𝛎𝛏𝛐𝛑𝛒𝛔𝛕𝛖𝛗𝛘𝛙𝛚𝟋        ',
    'greek_bold_lower_variant'                  : '    𝛜  𝛝 𝛞     𝛡𝛠𝛓  𝛟            ',
    'greek_italic_upper'                        : '𝛢𝛣𝛤𝛥𝛦𝛧𝛨𝛩𝛪𝛫𝛬𝛭𝛮𝛯𝛰𝛱𝛲𝛴𝛵𝛶𝛷𝛸𝛹𝛺         ',
    'greek_italic_upper_variant'                : '       𝛳                         ',
    'greek_italic_lower'                        : '𝛼𝛽𝛾𝛿𝜀𝜁𝜂𝜃𝜄𝜅𝜆𝜇𝜈𝜉𝜊𝜋𝜌𝜎𝜏𝜐𝜑𝜒𝜓𝜔         ',
    'greek_italic_lower_variant'                : '    𝜖  𝜗 𝜘     𝜛𝜚𝜍  𝜙            ',
    'greek_bold_italic_upper'                   : '𝜜𝜝𝜞𝜟𝜠𝜡𝜢𝜣𝜤𝜥𝜦𝜧𝜨𝜩𝜪𝜫𝜬𝜮𝜯𝜰𝜱𝜲𝜳𝜴         ',
    'greek_bold_italic_upper_variant'           : '       𝜭                         ',
    'greek_bold_italic_lower'                   : '𝜶𝜷𝜸𝜹𝜺𝜻𝜼𝜽𝜾𝜿𝝀𝝁𝝂𝝃𝝄𝝅𝝆𝝈𝝉𝝊𝝋𝝌𝝍𝝎         ',
    'greek_bold_italic_lower_variant'           : '    𝝐  𝝑 𝝒     𝝕𝝔𝝇  𝝓            ',
    'greek_sans_serif_bold_upper'               : '𝝖𝝗𝝘𝝙𝝚𝝛𝝜𝝝𝝞𝝟𝝠𝝡𝝢𝝣𝝤𝝥𝝦𝝨𝝩𝝪𝝫𝝬𝝭𝝮         ',
    'greek_sans_serif_bold_upper_variant'       : '       𝝧                         ',
    'greek_sans_serif_bold_lower'               : '𝝰𝝱𝝲𝝳𝝴𝝵𝝶𝝷𝝸𝝹𝝺𝝻𝝼𝝽𝝾𝝿𝞀𝞂𝞃𝞄𝞅𝞆𝞇𝞈         ',
    'greek_sans_serif_bold_lower_variant'       : '    𝞊  𝞋 𝞌     𝞏𝞎𝞁  𝞍            ',
    'greek_sans_serif_bold_italic_upper'        : '𝞐𝞑𝞒𝞓𝞔𝞕𝞖𝞗𝞘𝞙𝞚𝞛𝞜𝞝𝞞𝞟𝞠𝞢𝞣𝞤𝞥𝞦𝞧𝞨         ',
    'greek_sans_serif_bold_italic_upper_variant': '       𝞡                         ',
    'greek_sans_serif_bold_italic_lower'        : '𝞪𝞫𝞬𝞭𝞮𝞯𝞰𝞱𝞲𝞳𝞴𝞵𝞶𝞷𝞸𝞹𝞺𝞼𝞽𝞾𝞿𝟀𝟁𝟂         ',
    'greek_sans_serif_bold_italic_lower_variant': '    𝟄  𝟅 𝟆     𝟉𝟈𝞻  𝟇            ',
    'greek_double_struck_upper'                 : '  ℾ            ℿ ⅀               ',
    'greek_double_struck_lower'                 : '  ℽ            ℼ                 ',
}

char_names: list[str] = ['alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu', 'nu', 'xi', 'omicron', 'pi', 'rho', 'sigma', 'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega', 'digamma', 'san', 'tsan', 'sho', 'heta', 'koppa', 'sampi', 'yot', 'stigma']

lines: list[str] = []

for name, string in greeks.items():
    lines.append(f'{name}:\n')
    for char_name, char in zip(char_names[:-9], string[:-9]):
        if char == ' ':
            continue
        lines.append(f'  {char_name}: {char}\n')

[print(line) for line in lines]

with open('greek.yaml', 'w') as file:
    file.writelines(lines)

