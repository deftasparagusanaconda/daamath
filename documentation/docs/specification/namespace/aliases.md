# arithmetic  
succ  = dm.h0c # hyperoperation of 0th order, solving for c in the equation a ? b = c  
pred  = dm.h0b  
add   = dm.h1c  
sub   = dm.h1b  
mul   = dm.h2c  
div   = dm.h2b  
pow   = dm.h3c  
log   = dm.h3b  
root  = dm.h3a  
spow  = dm.h4c  
slog  = dm.h4b  
sroot = dm.h4a  
  
# arithmetic extra  
ainv    = dm.h1b_0  # sub with first argument fixed to 0  
minv    = dm.h2b_1  
exp     = dm.h3c_e  
exp2    = dm.h3c_2  
exp10   = dm.h3c_10  
ln      = dm.h3b__e # log with second argument fixed to e  
log2    = dm.h3b__2  
log10   = dm.h3b__10  
square  = dm.h3c__2  
cube    = dm.h3c__3  
sqrt    = dm.h3a__2  
cbrt    = dm.h3a__3  
rsquare = dm.h2b_1_h3c__2 # minv of square of x  
rcube   = dm.h2b_1_h3c__3  
rsqrt   = dm.h2b_1_h3a__2  
rcbrt   = dm.h2b_1_h3a__3  
fma     = dm.h1c_h2c      # dm.add_mul  
expm1   = dm.h1b_h3c_e__1 # dm.sub_pow_e__1  
ln1p    = dm.h3b_h1c_1__e # dm.log_add_1__e  
  
# trigonometry  
sin   = dm.croh # circular ratio from opposite and hypotenuse  
cos   = dm.crah  
tan   = dm.croa  
cot   = dm.crao  
sec   = dm.crha  
csc   = dm.crho  
asin  = dm.csoh  
acos  = dm.csah  
atan  = dm.csoa  
acot  = dm.csao  
asec  = dm.csha  
acsc  = dm.csho  
sinh  = dm.hroh  
cosh  = dm.hrah  
tanh  = dm.hroa  
coth  = dm.hrao  
sech  = dm.hrha  
csch  = dm.hrho  
asinh = dm.hsoh  
acosh = dm.hsah # hyperbolic semiarea from adjacent and hypotenuse  
atanh = dm.hsoa  
acoth = dm.hsao  
asech = dm.hsha  
acsch = dm.hsho  
  
# trigonometry extra  
asin2  = dm.csoh2 # 2-argument version of dm.csoh  
acos2  = dm.csah2  
atan2  = dm.csoa2  
acot2  = dm.csao2  
asec2  = dm.csha2  
acsc2  = dm.csho2  
sinc   = dm.h2b_croh_S_S  # dm.div_sin_S_S  
  
# boolean  
not_ = dm.tf   # F, T → T, F  
and_ = dm.ffft # FF, FT, TF, TT → F, F, F, T  
or_  = dm.fttt  
xor  = dm.fttf  
imp  = dm.ttft  
con  = dm.tftt  
nand = dm.tttf  
nor  = dm.tfff  
nxor = dm.tfft # NOTE: nxor, not xnor  
nimp = dm.fftf  
ncon = dm.ftff  
  
# interval  
lt = dm.iee   # A |B| C → include exclude exclude  
le = dm.iie  
eq = dm.eie  
ne = dm.iei  
ge = dm.eii  
gt = dm.eei  
oo = dm.eeiee # A |B| C |D| E → exclude exclude include exclude exclude  
oc = dm.eeiie  
co = dm.eiiee  
cc = dm.eiiie  
  
# variadic  
sum   = dm.vh1c  
prod  = dm.vh2c  
all   = dm.vffft  
any   = dm.vfttt  
min   = dm.mean__h1b_0_inf  
hmean = dm.mean__h1b_0_1  
gmean = dm.mean__0  
amean = dm.mean__1  
rms   = dm.mean__2  
cmean = dm.mean__3  
max   = dm.mean__inf  
  
# idk bro  
abs = dm.norm__2  
sgn = dm.normalize__2  
  
# quantization  
floor      = dm.round__true_floor  
ceil       = dm.round__true_ceil  
trunc      = dm.round__true_trunc  
away       = dm.round__true_away  
roundfloor = dm.round__false_floor  
roundceil  = dm.round__false_ceil  
roundtrunc = dm.round__false_trunc  
roundaway  = dm.round__false_away  
roundeven  = dm.round__false_even  
roundodd   = dm.round__false_odd  

