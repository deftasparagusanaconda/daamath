# approximates

daamath stores important constants approximately in some common IEEE754 floating point formats. the [nearest_even]-rounded value and the error of this rounded value are both stored, so that a bounded interval or a ball interval may be created (see [examples](#examples) below), or simply to store the constant in doubled precision.

constants are maintained in the following formats:

| name | radix | binary precision | decimal precision | 
| - | - | - | - |
| [f16](https://en.wikipedia.org/wiki/Half-precision_floating-point_format)  | 2 (binary) | 11 | ≈3.3113299523… | 
| [f32](https://en.wikipedia.org/wiki/Single-precision_floating-point_format)  | 2 (binary) | 24 | ≈7.22471989594… | 
| [f64](https://en.wikipedia.org/wiki/Double-precision_floating-point_format)  | 2 (binary) | 53 | ≈15.9545897702… | 
| [f128](https://en.wikipedia.org/wiki/Quadruple-precision_floating-point_format) | 2 (binary) | 113 | ≈34.01638951… | 
| [f256](https://en.wikipedia.org/wiki/Octuple-precision_floating-point_format) | 2 (binary) | 237 | ≈71.3441089724… | 
| [d32](https://en.wikipedia.org/wiki/Decimal32_floating-point_format)  | 10 (decimal) | ≈23.2534966642… | 7 | 
| [d64](https://en.wikipedia.org/wiki/Decimal64_floating-point_format)  | 10 (decimal) | ≈53.1508495182… | 16 | 
| [d128](https://en.wikipedia.org/wiki/Decimal128_floating-point_format) | 10 (decimal) | ≈112.945555226… | 34 | 

the following constants are maintained:

<!--| SUPERGOLDEN | 1.465571231876768… |-->
| name | common names | common symbols | decimal expansion |
| - | - | - | - |
| metallic_1 | [golden ratio](https://en.wikipedia.org/wiki/Golden_ratio) | φ | 1.61803398874989484820458683436563811772030917980576286213544862270526046281890244970720720418939113… |
| metallic_2 | [silver ratio](https://en.wikipedia.org/wiki/Silver_ratio) | σ | 2.41421356237309504880168872420969807856967187537694807317667973799073247846210703885038753432764157… |
| metallic_3 | bronze ratio |  | 3.30277563773199464655961063373524797312564828692262310635522652811358347414650522260230954100924535… |
| zeta_3 | [Apéry's constant](https://en.wikipedia.org/wiki/Ap%C3%A9ry%27s_constant) | [ζ](https://en.wikipedia.org/wiki/Riemann_zeta_function)(3) | 1.20205690315959428539973816151144999076498629234049888179227155534183820578631309018645587360933525… |
| zeta_5 |  | [ζ](https://en.wikipedia.org/wiki/Riemann_zeta_function)(5) | 1.03692775514336992633136548645703416805708091950191281197419267790380358978628148456004310655713333… |
| champernowne_10 | 1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950515253545… |
| liouville_10 | 0.11000100000000000000000100000000000000000000000000000000000000000000000000000000000000000000000000… |
| archimedes |  | [π](https://en.wikipedia.org/wiki/Pi) | 3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706… |
| eulers_number | Napier's constant | [e](https://en.wikipedia.org/wiki/E_(mathematical_constant)) | 2.71828182845904523536028747135266249775724709369995957496696762772407663035354759457138217852516642… |
| euler_mascheroni |  |  | 0.57721566490153286060651209008240243104215933593992359880576723488486772677766467093694706329174674… |
| catalan | 0.91596559417721901505460351493238411077414937428167213426649811962176301977625476947935651292611510… |
| khinchin | 2.68545200106530644530971483548179569382038229399446295305115234555721885953715200280114117493184769… |
| glaisher | 1.28242712910062263687534256886979172776768892732500119206374002174040630885882646112973649195820237… |
| mertens | 0.26149721284764278375542683860869585905156664826119920619206421392492451089736820971414263143424665… |
| twin_prime | 0.66016181584686957392781211001455577843262336028473341331944842333540564230449527714376003141383986… |
| plastic | 1.32471795724474602596090885447809734073440405690173336453401505030282785124554759405469934798178728… |
| gompertz | 0.59634736232319407434107849936927937607417786015254878157348491048232721911487441747043049709361276… |
| [feigenbaum_alpha](https://en.wikipedia.org/wiki/Feigenbaum_constants#The_second_constant) |  | α | -2.5029078750958928222839028732182157863812713767271499773361920567792354631795902067032996497464338… |
| [feigenbaum_delta](https://en.wikipedia.org/wiki/Feigenbaum_constants#The_first_constant) |  | δ | 4.66920160910299067185320382046620161725818557747576863274565134300413433021131473713868974402394801… |

daamath defines angle units w.r.t. radians since they are the most natural unit of angles (as evident in circular trigonometry):

| name | common names | exact value | decimal expansion |
| - | - |
| turn    | [tau](https://en.wikipedia.org/wiki/Tau) | τ / 1 | 6.28318530717958647692528676655900576839433879875021164194988918461563281257241799725606965068423413… |
| degree  |  | τ / 360 | 0.01745329251994329576923690768488612713442871888541725456097191440171009114603449443682241569634509… |
| gradian |  | τ / 400 | 0.01570796326794896619231321691639751442098584699687552910487472296153908203143104499314017412671058… |
| minute  |  | τ / (360 * 60) | 0.00029088820866572159615394846141476878557381198142362090934953190669516818576724157394704026160575… |
| second  |  | τ / (360 * 60 * 60) | 0.00004848136811095359935899141023579479759563533023727015155825531778252803096120692899117337693429… |

# examples

```
# get τ as an f16 approximation

TAU = dm.TAU.f16.nearest
```

```
# create e as a bound interval of f64

E = dm.E.f32.nearest          
E = (dm.pred(E), E) if dm.E.f32.error < 0 else (E, dm.succ(E))           
```

```
# create e as a ball interval of f32

E = dm.ball(centre=dm.E.f32.nearest, radius=abs(dm.E.f32.error))
```


# what is a constant?

a constant is something whose value doesnt depend on anything and doesnt change. daamath stores common constants but is honest about their precision. thus if a machines tries to use PI_f128 in a language with only f64, daamath correctly prevents dishonesty.

daamath maintains the following constants:

| name | value |
| - | - |
| [I](https://en.wikipedia.org/wiki/Imaginary_unit) | i |
| TRUE    | boolean top element |
| FALSE   | boolean bottom element |
| PLASTIC     | 1.324717957244746… |
| SUPERGOLDEN | 1.465571231876768… |
| GOLDEN      | 1.618033988749… |
| SILVER      | 2.41421356237309504880… |

# what can become a constant?

if a set of constants has no clear bound to it, that set should not exist. `DIV_X_TAU` can create an infinite amount of constants, but its not clear where to end it. so its not done. same with `DIV_TAU_X` for example.

# unicode support

daamath will NOT deal with unicode in the namespace. it is very very non-portable. i also would love to type `from daamath import τ` but unicode support is inconsistent, and that harms our cross-language consistency a lot. 

# where is π??

daamath has a strong stance on π & τ. π is inelegant. τ is elegant. daamath is elegant. daamath uses ONLY τ. 

# rant

`DIV_X_Y` seemed like a good idea until i realized the space blows up and i have to start making arbitrary decisions on where to stop. this is bad. daamath shouldnt make assumptions unless they are mathematically sound and clear. if you want `DIV_1_PI`, make it yourself: `div(1, pi)` or `minv(pi)`


