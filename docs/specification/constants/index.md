# constants

a constant is something whose value doesnt depend on anything and doesnt change unless the universe changes. under this definition, daamath has a few kinds of constants:

# rational approximations

an irrational constant may be stored as a rational approximation:

- each constant has 5 [IEEE 754] basic formats: [f32], [f64], [f128], [d64], [d128]
- each format has 2 residuals: the [nearest_even]-rounded value and the error of that rounded value
- each residual has 3 integers: significand, radix, exponent

the advantages of this are:

- the approximation is explicit, and not implicit in machine/language datatype
- a box (lower, upper) or a ball (centre, radius) interval can be constructed
- the constant can be easily hydrated into a float/fraction/string/int/interval/…

for convenience, an implementation may also store hydrated versions of the integer triple

the following irrational constants are approximated:

<!--| SUPERGOLDEN | 1.465571231876768… |-->
| name | common names | common symbols | decimal |
| - | - | - | - |
| archimedes |  | [π](https://en.wikipedia.org/wiki/Pi) | 3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706… |
| catalan | | | 0.91596559417721901505460351493238411077414937428167213426649811962176301977625476947935651292611510… |
| champernowne_10 | | |  1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950515253545… |
| euler_mascheroni |  |  | 0.57721566490153286060651209008240243104215933593992359880576723488486772677766467093694706329174674… |
| eulers_number | Napier's constant | [e](https://en.wikipedia.org/wiki/E_(mathematical_constant)) | 2.71828182845904523536028747135266249775724709369995957496696762772407663035354759457138217852516642… |
| [feigenbaum_alpha](https://en.wikipedia.org/wiki/Feigenbaum_constants#The_second_constant) |  | α | -2.5029078750958928222839028732182157863812713767271499773361920567792354631795902067032996497464338… |
| [feigenbaum_delta](https://en.wikipedia.org/wiki/Feigenbaum_constants#The_first_constant) |  | δ | 4.66920160910299067185320382046620161725818557747576863274565134300413433021131473713868974402394801… |
| glaisher | | | 1.28242712910062263687534256886979172776768892732500119206374002174040630885882646112973649195820237… |
| gompertz | | | 0.59634736232319407434107849936927937607417786015254878157348491048232721911487441747043049709361276… |
| khinchin | | | 2.68545200106530644530971483548179569382038229399446295305115234555721885953715200280114117493184769… |
| liouville_10 | | | 0.11000100000000000000000100000000000000000000000000000000000000000000000000000000000000000000000000… |
| mertens | | | 0.26149721284764278375542683860869585905156664826119920619206421392492451089736820971414263143424665… |
| metallic_1_plus_root | [golden ratio](https://en.wikipedia.org/wiki/Golden_ratio) | φ | 1.61803398874989484820458683436563811772030917980576286213544862270526046281890244970720720418939113… |
| metallic_2_plus_root | [silver ratio](https://en.wikipedia.org/wiki/Silver_ratio) | σ | 2.41421356237309504880168872420969807856967187537694807317667973799073247846210703885038753432764157… |
| metallic_3_plus_root | bronze ratio |  | 3.30277563773199464655961063373524797312564828692262310635522652811358347414650522260230954100924535… |
| metallic_1_minus_root | | | -0.6180339887498948482045868343656381177203091798057628621354486227052604628189024497072072041893911… |
| metallic_2_minus_root | | | -0.4142135623730950488016887242096980785696718753769480731766797379907324784621070388503875343276415… |
| metallic_3_minus_root | | | -0.3027756377319946465596106337352479731256482869226231063552265281135834741465052226023095410092453… |
| plastic | | | 1.32471795724474602596090885447809734073440405690173336453401505030282785124554759405469934798178728… |
| twin_prime | | | 0.66016181584686957392781211001455577843262336028473341331944842333540564230449527714376003141383986… |
| zeta_3 | [Apéry's constant](https://en.wikipedia.org/wiki/Ap%C3%A9ry%27s_constant) | [ζ](https://en.wikipedia.org/wiki/Riemann_zeta_function)(3) | 1.20205690315959428539973816151144999076498629234049888179227155534183820578631309018645587360933525… |
| zeta_5 |  | [ζ](https://en.wikipedia.org/wiki/Riemann_zeta_function)(5) | 1.03692775514336992633136548645703416805708091950191281197419267790380358978628148456004310655713333… |

daamath defines angle units w.r.t. radians since they are the most natural unit of angles (as evident in circular trigonometry):

| name | common names | exact value | decimal expansion |
| - | - | - | - |
| degree  |  | τ / 360 | 0.01745329251994329576923690768488612713442871888541725456097191440171009114603449443682241569634509… |
| gradian |  | τ / 400 | 0.01570796326794896619231321691639751442098584699687552910487472296153908203143104499314017412671058… |
| minute  |  | τ / (360 * 60) | 0.00029088820866572159615394846141476878557381198142362090934953190669516818576724157394704026160575… |
| second  |  | τ / (360 * 60 * 60) | 0.00004848136811095359935899141023579479759563533023727015155825531778252803096120692899117337693429… |
| turn    | [tau](https://en.wikipedia.org/wiki/Tau) | τ / 1 | 6.28318530717958647692528676655900576839433879875021164194988918461563281257241799725606965068423413… |

# specials

| name | common names | common symbols |
| - | - | - |
| i | complex imaginary unit | 
| j | split-complex imaginary unit |
| e | dual imaginary unit |
| true | boolean top element |
| false | boolean bottom element |

# examples

```
# get τ as an f16 approximation

TAU = dm.TAU.f16.nearest
```

```
# create e as a box interval of f64

E = dm.E.f32.nearest          
E = (dm.pred(E), E) if dm.E.f32.error < 0 else (E, dm.succ(E))           
```

```
# create e as a ball interval of f32

E = dm.ball(centre=dm.E.f32.nearest, radius=abs(dm.E.f32.error))
```


# notes

the rational approximations are stored as three integers. this is actually slightly redundant because rationals only need two integers (or three natural numbers!). but storing two ginormous integers is less efficient than the three handle-able integers because they match the structure of the float datatypes better.

# rant

`DIV_X_Y` seemed like a good idea until i realized the space blows up and i have to start making arbitrary decisions on where to stop. this is bad. daamath shouldnt make assumptions unless they are mathematically sound and clear. if you want `DIV_1_PI`, make it yourself: `div(1, pi)` or `minv(pi)`

[f16]: https://en.wikipedia.org/wiki/Half-precision_floating-point_format
[f32]: https://en.wikipedia.org/wiki/Single-precision_floating-point_format
[f64]: https://en.wikipedia.org/wiki/Double-precision_floating-point_format
[f128]: https://en.wikipedia.org/wiki/Quadruple-precision_floating-point_format
[f256]: https://en.wikipedia.org/wiki/Octuple-precision_floating-point_format
[d32]: https://en.wikipedia.org/wiki/Decimal32_floating-point_format
[d64]: https://en.wikipedia.org/wiki/Decimal64_floating-point_format
[d128]: https://en.wikipedia.org/wiki/Decimal128_floating-point_format
[IEEE 754]: https://en.wikipedia.org/wiki/IEEE_754
