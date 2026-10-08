
```python
import softposit, itertools

for i in itertools.chain(range(2**7-1,-1,-1), range(2**8-1,2 ** 7-1, -1)):
    print(bin(i)[2:].zfill(8).replace('0', '□').replace('1', '■'), softposit.posit8(bits=i))
```

<pre>
<span style="color: var(--dm-red)">□</span><span style="color: yellow">■■■■■■■</span><span style="color: var(--dm-blue)"></span> = <span style="color: var(--dm-red)">+</span>64.0
<span style="color: var(--dm-red)">□</span><span style="color: yellow">■■■■■■□</span><span style="color: var(--dm-blue)"></span> = <span style="color: var(--dm-red)">+</span>32.0
<span style="color: var(--dm-red)">□</span><span style="color: yellow">■■■■■□</span><span style="color: var(--dm-blue)">■</span> = <span style="color: var(--dm-red)">+</span>24.0
<span style="color: var(--dm-red)">□</span><span style="color: yellow">■■■■■□</span><span style="color: var(--dm-blue)">□</span> = <span style="color: var(--dm-red)">+</span>16.0
<span style="color: var(--dm-red)">□</span><span style="color: yellow">■■■■□</span><span style="color: var(--dm-blue)">■■</span> = <span style="color: var(--dm-red)">+</span>14.0
<span style="color: var(--dm-red)">□</span><span style="color: yellow">■■■■□</span><span style="color: var(--dm-blue)">■□</span> = <span style="color: var(--dm-red)">+</span>12.0
<span style="color: var(--dm-red)">□</span><span style="color: yellow">■■■■□</span><span style="color: var(--dm-blue)">□■</span> = <span style="color: var(--dm-red)">+</span>10.0
<span style="color: var(--dm-red)">□</span><span style="color: yellow">■■■■□</span><span style="color: var(--dm-blue)">□□</span> = <span style="color: var(--dm-red)">+</span> 8.0
<span style="color: var(--dm-red)">□</span><span style="color: yellow">■■■□</span><span style="color: var(--dm-blue)">■■■</span> = <span style="color: var(--dm-red)">+</span> 7.5
<span style="color: var(--dm-red)">□</span><span style="color: yellow">■■■□</span><span style="color: var(--dm-blue)">■■□</span> = <span style="color: var(--dm-red)">+</span> 7.0
<span style="color: var(--dm-red)">□</span><span style="color: yellow">■■■□</span><span style="color: var(--dm-blue)">■□■</span> = <span style="color: var(--dm-red)">+</span> 6.5
<span style="color: var(--dm-red)">□</span><span style="color: yellow">■■■□</span><span style="color: var(--dm-blue)">■□□</span> = <span style="color: var(--dm-red)">+</span> 6.0
<span style="color: var(--dm-red)">□</span><span style="color: yellow">■■■□</span><span style="color: var(--dm-blue)">□■■</span> = <span style="color: var(--dm-red)">+</span> 5.5
<span style="color: var(--dm-red)">□</span><span style="color: yellow">■■■□</span><span style="color: var(--dm-blue)">□■□</span> = <span style="color: var(--dm-red)">+</span> 5.0
<span style="color: var(--dm-red)">□</span><span style="color: yellow">■■■□</span><span style="color: var(--dm-blue)">□□■</span> = <span style="color: var(--dm-red)">+</span> 4.5
<span style="color: var(--dm-red)">□</span><span style="color: yellow">■■■□</span><span style="color: var(--dm-blue)">□□□</span> = <span style="color: var(--dm-red)">+</span> 4.0
<span style="color: var(--dm-red)">□</span><span style="color: yellow">■■□</span><span style="color: var(--dm-blue)">■■■■</span> = <span style="color: var(--dm-red)">+</span> 3.875
<span style="color: var(--dm-red)">□</span><span style="color: yellow">■■□</span><span style="color: var(--dm-blue)">■■■□</span> = <span style="color: var(--dm-red)">+</span> 3.75
<span style="color: var(--dm-red)">□</span><span style="color: yellow">■■□</span><span style="color: var(--dm-blue)">■■□■</span> = <span style="color: var(--dm-red)">+</span> 3.625
<span style="color: var(--dm-red)">□</span><span style="color: yellow">■■□</span><span style="color: var(--dm-blue)">■■□□</span> = <span style="color: var(--dm-red)">+</span> 3.5
<span style="color: var(--dm-red)">□</span><span style="color: yellow">■■□</span><span style="color: var(--dm-blue)">■□■■</span> = <span style="color: var(--dm-red)">+</span> 3.375
<span style="color: var(--dm-red)">□</span><span style="color: yellow">■■□</span><span style="color: var(--dm-blue)">■□■□</span> = <span style="color: var(--dm-red)">+</span> 3.25
<span style="color: var(--dm-red)">□</span><span style="color: yellow">■■□</span><span style="color: var(--dm-blue)">■□□■</span> = <span style="color: var(--dm-red)">+</span> 3.125
<span style="color: var(--dm-red)">□</span><span style="color: yellow">■■□</span><span style="color: var(--dm-blue)">■□□□</span> = <span style="color: var(--dm-red)">+</span> 3.0
<span style="color: var(--dm-red)">□</span><span style="color: yellow">■■□</span><span style="color: var(--dm-blue)">□■■■</span> = <span style="color: var(--dm-red)">+</span> 2.875
<span style="color: var(--dm-red)">□</span><span style="color: yellow">■■□</span><span style="color: var(--dm-blue)">□■■□</span> = <span style="color: var(--dm-red)">+</span> 2.75
<span style="color: var(--dm-red)">□</span><span style="color: yellow">■■□</span><span style="color: var(--dm-blue)">□■□■</span> = <span style="color: var(--dm-red)">+</span> 2.625
<span style="color: var(--dm-red)">□</span><span style="color: yellow">■■□</span><span style="color: var(--dm-blue)">□■□□</span> = <span style="color: var(--dm-red)">+</span> 2.5
<span style="color: var(--dm-red)">□</span><span style="color: yellow">■■□</span><span style="color: var(--dm-blue)">□□■■</span> = <span style="color: var(--dm-red)">+</span> 2.375
<span style="color: var(--dm-red)">□</span><span style="color: yellow">■■□</span><span style="color: var(--dm-blue)">□□■□</span> = <span style="color: var(--dm-red)">+</span> 2.25
<span style="color: var(--dm-red)">□</span><span style="color: yellow">■■□</span><span style="color: var(--dm-blue)">□□□■</span> = <span style="color: var(--dm-red)">+</span> 2.125 
<span style="color: var(--dm-red)">□</span><span style="color: yellow">■■□</span><span style="color: var(--dm-blue)">□□□□</span> = <span style="color: var(--dm-red)">+</span> 2.0
<span style="color: var(--dm-red)">□</span><span style="color: yellow">■□</span><span style="color: var(--dm-blue)">■■■■■</span> = <span style="color: var(--dm-red)">+</span> 1.96875
<span style="color: var(--dm-red)">□</span><span style="color: yellow">■□</span><span style="color: var(--dm-blue)">■■■■□</span> = <span style="color: var(--dm-red)">+</span> 1.9375
<span style="color: var(--dm-red)">□</span><span style="color: yellow">■□</span><span style="color: var(--dm-blue)">■■■□■</span> = <span style="color: var(--dm-red)">+</span> 1.90625
<span style="color: var(--dm-red)">□</span><span style="color: yellow">■□</span><span style="color: var(--dm-blue)">■■■□□</span> = <span style="color: var(--dm-red)">+</span> 1.875
<span style="color: var(--dm-red)">□</span><span style="color: yellow">■□</span><span style="color: var(--dm-blue)">■■□■■</span> = <span style="color: var(--dm-red)">+</span> 1.84375
<span style="color: var(--dm-red)">□</span><span style="color: yellow">■□</span><span style="color: var(--dm-blue)">■■□■□</span> = <span style="color: var(--dm-red)">+</span> 1.8125
<span style="color: var(--dm-red)">□</span><span style="color: yellow">■□</span><span style="color: var(--dm-blue)">■■□□■</span> = <span style="color: var(--dm-red)">+</span> 1.78125
<span style="color: var(--dm-red)">□</span><span style="color: yellow">■□</span><span style="color: var(--dm-blue)">■■□□□</span> = <span style="color: var(--dm-red)">+</span> 1.75
<span style="color: var(--dm-red)">□</span><span style="color: yellow">■□</span><span style="color: var(--dm-blue)">■□■■■</span> = <span style="color: var(--dm-red)">+</span> 1.71875
<span style="color: var(--dm-red)">□</span><span style="color: yellow">■□</span><span style="color: var(--dm-blue)">■□■■□</span> = <span style="color: var(--dm-red)">+</span> 1.6875
<span style="color: var(--dm-red)">□</span><span style="color: yellow">■□</span><span style="color: var(--dm-blue)">■□■□■</span> = <span style="color: var(--dm-red)">+</span> 1.65625
<span style="color: var(--dm-red)">□</span><span style="color: yellow">■□</span><span style="color: var(--dm-blue)">■□■□□</span> = <span style="color: var(--dm-red)">+</span> 1.625
<span style="color: var(--dm-red)">□</span><span style="color: yellow">■□</span><span style="color: var(--dm-blue)">■□□■■</span> = <span style="color: var(--dm-red)">+</span> 1.59375
<span style="color: var(--dm-red)">□</span><span style="color: yellow">■□</span><span style="color: var(--dm-blue)">■□□■□</span> = <span style="color: var(--dm-red)">+</span> 1.5625
<span style="color: var(--dm-red)">□</span><span style="color: yellow">■□</span><span style="color: var(--dm-blue)">■□□□■</span> = <span style="color: var(--dm-red)">+</span> 1.53125
<span style="color: var(--dm-red)">□</span><span style="color: yellow">■□</span><span style="color: var(--dm-blue)">■□□□□</span> = <span style="color: var(--dm-red)">+</span> 1.5
<span style="color: var(--dm-red)">□</span><span style="color: yellow">■□</span><span style="color: var(--dm-blue)">□■■■■</span> = <span style="color: var(--dm-red)">+</span> 1.46875
<span style="color: var(--dm-red)">□</span><span style="color: yellow">■□</span><span style="color: var(--dm-blue)">□■■■□</span> = <span style="color: var(--dm-red)">+</span> 1.4375
<span style="color: var(--dm-red)">□</span><span style="color: yellow">■□</span><span style="color: var(--dm-blue)">□■■□■</span> = <span style="color: var(--dm-red)">+</span> 1.40625
<span style="color: var(--dm-red)">□</span><span style="color: yellow">■□</span><span style="color: var(--dm-blue)">□■■□□</span> = <span style="color: var(--dm-red)">+</span> 1.375
<span style="color: var(--dm-red)">□</span><span style="color: yellow">■□</span><span style="color: var(--dm-blue)">□■□■■</span> = <span style="color: var(--dm-red)">+</span> 1.34375
<span style="color: var(--dm-red)">□</span><span style="color: yellow">■□</span><span style="color: var(--dm-blue)">□■□■□</span> = <span style="color: var(--dm-red)">+</span> 1.3125
<span style="color: var(--dm-red)">□</span><span style="color: yellow">■□</span><span style="color: var(--dm-blue)">□■□□■</span> = <span style="color: var(--dm-red)">+</span> 1.28125
<span style="color: var(--dm-red)">□</span><span style="color: yellow">■□</span><span style="color: var(--dm-blue)">□■□□□</span> = <span style="color: var(--dm-red)">+</span> 1.25
<span style="color: var(--dm-red)">□</span><span style="color: yellow">■□</span><span style="color: var(--dm-blue)">□□■■■</span> = <span style="color: var(--dm-red)">+</span> 1.21875
<span style="color: var(--dm-red)">□</span><span style="color: yellow">■□</span><span style="color: var(--dm-blue)">□□■■□</span> = <span style="color: var(--dm-red)">+</span> 1.1875
<span style="color: var(--dm-red)">□</span><span style="color: yellow">■□</span><span style="color: var(--dm-blue)">□□■□■</span> = <span style="color: var(--dm-red)">+</span> 1.15625
<span style="color: var(--dm-red)">□</span><span style="color: yellow">■□</span><span style="color: var(--dm-blue)">□□■□□</span> = <span style="color: var(--dm-red)">+</span> 1.125
<span style="color: var(--dm-red)">□</span><span style="color: yellow">■□</span><span style="color: var(--dm-blue)">□□□■■</span> = <span style="color: var(--dm-red)">+</span> 1.09375
<span style="color: var(--dm-red)">□</span><span style="color: yellow">■□</span><span style="color: var(--dm-blue)">□□□■□</span> = <span style="color: var(--dm-red)">+</span> 1.0625
<span style="color: var(--dm-red)">□</span><span style="color: yellow">■□</span><span style="color: var(--dm-blue)">□□□□■</span> = <span style="color: var(--dm-red)">+</span> 1.03125
<span style="color: var(--dm-red)">□</span><span style="color: yellow">■□</span><span style="color: var(--dm-blue)">□□□□□</span> = <span style="color: var(--dm-red)">+</span> 1.0
<span style="color: var(--dm-red)">□</span><span style="color: yellow">□■</span><span style="color: var(--dm-blue)">■■■■■</span> = <span style="color: var(--dm-red)">+</span> 0.984375
<span style="color: var(--dm-red)">□</span><span style="color: yellow">□■</span><span style="color: var(--dm-blue)">■■■■□</span> = <span style="color: var(--dm-red)">+</span> 0.96875
<span style="color: var(--dm-red)">□</span><span style="color: yellow">□■</span><span style="color: var(--dm-blue)">■■■□■</span> = <span style="color: var(--dm-red)">+</span> 0.953125
<span style="color: var(--dm-red)">□</span><span style="color: yellow">□■</span><span style="color: var(--dm-blue)">■■■□□</span> = <span style="color: var(--dm-red)">+</span> 0.9375
<span style="color: var(--dm-red)">□</span><span style="color: yellow">□■</span><span style="color: var(--dm-blue)">■■□■■</span> = <span style="color: var(--dm-red)">+</span> 0.921875
<span style="color: var(--dm-red)">□</span><span style="color: yellow">□■</span><span style="color: var(--dm-blue)">■■□■□</span> = <span style="color: var(--dm-red)">+</span> 0.90625
<span style="color: var(--dm-red)">□</span><span style="color: yellow">□■</span><span style="color: var(--dm-blue)">■■□□■</span> = <span style="color: var(--dm-red)">+</span> 0.890625
<span style="color: var(--dm-red)">□</span><span style="color: yellow">□■</span><span style="color: var(--dm-blue)">■■□□□</span> = <span style="color: var(--dm-red)">+</span> 0.875
<span style="color: var(--dm-red)">□</span><span style="color: yellow">□■</span><span style="color: var(--dm-blue)">■□■■■</span> = <span style="color: var(--dm-red)">+</span> 0.859375
<span style="color: var(--dm-red)">□</span><span style="color: yellow">□■</span><span style="color: var(--dm-blue)">■□■■□</span> = <span style="color: var(--dm-red)">+</span> 0.84375
<span style="color: var(--dm-red)">□</span><span style="color: yellow">□■</span><span style="color: var(--dm-blue)">■□■□■</span> = <span style="color: var(--dm-red)">+</span> 0.828125
<span style="color: var(--dm-red)">□</span><span style="color: yellow">□■</span><span style="color: var(--dm-blue)">■□■□□</span> = <span style="color: var(--dm-red)">+</span> 0.8125
<span style="color: var(--dm-red)">□</span><span style="color: yellow">□■</span><span style="color: var(--dm-blue)">■□□■■</span> = <span style="color: var(--dm-red)">+</span> 0.796875
<span style="color: var(--dm-red)">□</span><span style="color: yellow">□■</span><span style="color: var(--dm-blue)">■□□■□</span> = <span style="color: var(--dm-red)">+</span> 0.78125
<span style="color: var(--dm-red)">□</span><span style="color: yellow">□■</span><span style="color: var(--dm-blue)">■□□□■</span> = <span style="color: var(--dm-red)">+</span> 0.765625
<span style="color: var(--dm-red)">□</span><span style="color: yellow">□■</span><span style="color: var(--dm-blue)">■□□□□</span> = <span style="color: var(--dm-red)">+</span> 0.75
<span style="color: var(--dm-red)">□</span><span style="color: yellow">□■</span><span style="color: var(--dm-blue)">□■■■■</span> = <span style="color: var(--dm-red)">+</span> 0.734375
<span style="color: var(--dm-red)">□</span><span style="color: yellow">□■</span><span style="color: var(--dm-blue)">□■■■□</span> = <span style="color: var(--dm-red)">+</span> 0.71875
<span style="color: var(--dm-red)">□</span><span style="color: yellow">□■</span><span style="color: var(--dm-blue)">□■■□■</span> = <span style="color: var(--dm-red)">+</span> 0.703125
<span style="color: var(--dm-red)">□</span><span style="color: yellow">□■</span><span style="color: var(--dm-blue)">□■■□□</span> = <span style="color: var(--dm-red)">+</span> 0.6875
<span style="color: var(--dm-red)">□</span><span style="color: yellow">□■</span><span style="color: var(--dm-blue)">□■□■■</span> = <span style="color: var(--dm-red)">+</span> 0.671875
<span style="color: var(--dm-red)">□</span><span style="color: yellow">□■</span><span style="color: var(--dm-blue)">□■□■□</span> = <span style="color: var(--dm-red)">+</span> 0.65625
<span style="color: var(--dm-red)">□</span><span style="color: yellow">□■</span><span style="color: var(--dm-blue)">□■□□■</span> = <span style="color: var(--dm-red)">+</span> 0.640625
<span style="color: var(--dm-red)">□</span><span style="color: yellow">□■</span><span style="color: var(--dm-blue)">□■□□□</span> = <span style="color: var(--dm-red)">+</span> 0.625
<span style="color: var(--dm-red)">□</span><span style="color: yellow">□■</span><span style="color: var(--dm-blue)">□□■■■</span> = <span style="color: var(--dm-red)">+</span> 0.609375
<span style="color: var(--dm-red)">□</span><span style="color: yellow">□■</span><span style="color: var(--dm-blue)">□□■■□</span> = <span style="color: var(--dm-red)">+</span> 0.59375
<span style="color: var(--dm-red)">□</span><span style="color: yellow">□■</span><span style="color: var(--dm-blue)">□□■□■</span> = <span style="color: var(--dm-red)">+</span> 0.578125
<span style="color: var(--dm-red)">□</span><span style="color: yellow">□■</span><span style="color: var(--dm-blue)">□□■□□</span> = <span style="color: var(--dm-red)">+</span> 0.5625
<span style="color: var(--dm-red)">□</span><span style="color: yellow">□■</span><span style="color: var(--dm-blue)">□□□■■</span> = <span style="color: var(--dm-red)">+</span> 0.546875
<span style="color: var(--dm-red)">□</span><span style="color: yellow">□■</span><span style="color: var(--dm-blue)">□□□■□</span> = <span style="color: var(--dm-red)">+</span> 0.53125
<span style="color: var(--dm-red)">□</span><span style="color: yellow">□■</span><span style="color: var(--dm-blue)">□□□□■</span> = <span style="color: var(--dm-red)">+</span> 0.515625
<span style="color: var(--dm-red)">□</span><span style="color: yellow">□■</span><span style="color: var(--dm-blue)">□□□□□</span> = <span style="color: var(--dm-red)">+</span> 0.5
<span style="color: var(--dm-red)">□</span><span style="color: yellow">□□■</span><span style="color: var(--dm-blue)">■■■■</span> = <span style="color: var(--dm-red)">+</span> 0.484375
<span style="color: var(--dm-red)">□</span><span style="color: yellow">□□■</span><span style="color: var(--dm-blue)">■■■□</span> = <span style="color: var(--dm-red)">+</span> 0.46875
<span style="color: var(--dm-red)">□</span><span style="color: yellow">□□■</span><span style="color: var(--dm-blue)">■■□■</span> = <span style="color: var(--dm-red)">+</span> 0.453125
<span style="color: var(--dm-red)">□</span><span style="color: yellow">□□■</span><span style="color: var(--dm-blue)">■■□□</span> = <span style="color: var(--dm-red)">+</span> 0.4375
<span style="color: var(--dm-red)">□</span><span style="color: yellow">□□■</span><span style="color: var(--dm-blue)">■□■■</span> = <span style="color: var(--dm-red)">+</span> 0.421875
<span style="color: var(--dm-red)">□</span><span style="color: yellow">□□■</span><span style="color: var(--dm-blue)">■□■□</span> = <span style="color: var(--dm-red)">+</span> 0.40625
<span style="color: var(--dm-red)">□</span><span style="color: yellow">□□■</span><span style="color: var(--dm-blue)">■□□■</span> = <span style="color: var(--dm-red)">+</span> 0.390625
<span style="color: var(--dm-red)">□</span><span style="color: yellow">□□■</span><span style="color: var(--dm-blue)">■□□□</span> = <span style="color: var(--dm-red)">+</span> 0.375
<span style="color: var(--dm-red)">□</span><span style="color: yellow">□□■</span><span style="color: var(--dm-blue)">□■■■</span> = <span style="color: var(--dm-red)">+</span> 0.359375
<span style="color: var(--dm-red)">□</span><span style="color: yellow">□□■</span><span style="color: var(--dm-blue)">□■■□</span> = <span style="color: var(--dm-red)">+</span> 0.34375
<span style="color: var(--dm-red)">□</span><span style="color: yellow">□□■</span><span style="color: var(--dm-blue)">□■□■</span> = <span style="color: var(--dm-red)">+</span> 0.328125
<span style="color: var(--dm-red)">□</span><span style="color: yellow">□□■</span><span style="color: var(--dm-blue)">□■□□</span> = <span style="color: var(--dm-red)">+</span> 0.3125
<span style="color: var(--dm-red)">□</span><span style="color: yellow">□□■</span><span style="color: var(--dm-blue)">□□■■</span> = <span style="color: var(--dm-red)">+</span> 0.296875
<span style="color: var(--dm-red)">□</span><span style="color: yellow">□□■</span><span style="color: var(--dm-blue)">□□■□</span> = <span style="color: var(--dm-red)">+</span> 0.28125
<span style="color: var(--dm-red)">□</span><span style="color: yellow">□□■</span><span style="color: var(--dm-blue)">□□□■</span> = <span style="color: var(--dm-red)">+</span> 0.265625
<span style="color: var(--dm-red)">□</span><span style="color: yellow">□□■</span><span style="color: var(--dm-blue)">□□□□</span> = <span style="color: var(--dm-red)">+</span> 0.25
<span style="color: var(--dm-red)">□</span><span style="color: yellow">□□□■</span><span style="color: var(--dm-blue)">■■■</span> = <span style="color: var(--dm-red)">+</span> 0.234375
<span style="color: var(--dm-red)">□</span><span style="color: yellow">□□□■</span><span style="color: var(--dm-blue)">■■□</span> = <span style="color: var(--dm-red)">+</span> 0.21875
<span style="color: var(--dm-red)">□</span><span style="color: yellow">□□□■</span><span style="color: var(--dm-blue)">■□■</span> = <span style="color: var(--dm-red)">+</span> 0.203125
<span style="color: var(--dm-red)">□</span><span style="color: yellow">□□□■</span><span style="color: var(--dm-blue)">■□□</span> = <span style="color: var(--dm-red)">+</span> 0.1875
<span style="color: var(--dm-red)">□</span><span style="color: yellow">□□□■</span><span style="color: var(--dm-blue)">□■■</span> = <span style="color: var(--dm-red)">+</span> 0.171875
<span style="color: var(--dm-red)">□</span><span style="color: yellow">□□□■</span><span style="color: var(--dm-blue)">□■□</span> = <span style="color: var(--dm-red)">+</span> 0.15625
<span style="color: var(--dm-red)">□</span><span style="color: yellow">□□□■</span><span style="color: var(--dm-blue)">□□■</span> = <span style="color: var(--dm-red)">+</span> 0.140625
<span style="color: var(--dm-red)">□</span><span style="color: yellow">□□□■</span><span style="color: var(--dm-blue)">□□□</span> = <span style="color: var(--dm-red)">+</span> 0.125
<span style="color: var(--dm-red)">□</span><span style="color: yellow">□□□□■</span><span style="color: var(--dm-blue)">■■</span> = <span style="color: var(--dm-red)">+</span> 0.109375
<span style="color: var(--dm-red)">□</span><span style="color: yellow">□□□□■</span><span style="color: var(--dm-blue)">■□</span> = <span style="color: var(--dm-red)">+</span> 0.09375
<span style="color: var(--dm-red)">□</span><span style="color: yellow">□□□□■</span><span style="color: var(--dm-blue)">□■</span> = <span style="color: var(--dm-red)">+</span> 0.078125
<span style="color: var(--dm-red)">□</span><span style="color: yellow">□□□□■</span><span style="color: var(--dm-blue)">□□</span> = <span style="color: var(--dm-red)">+</span> 0.0625
<span style="color: var(--dm-red)">□</span><span style="color: yellow">□□□□□■</span><span style="color: var(--dm-blue)">■</span> = <span style="color: var(--dm-red)">+</span> 0.046875
<span style="color: var(--dm-red)">□</span><span style="color: yellow">□□□□□■</span><span style="color: var(--dm-blue)">□</span> = <span style="color: var(--dm-red)">+</span> 0.03125
<span style="color: var(--dm-red)">□</span><span style="color: yellow">□□□□□□■</span><span style="color: var(--dm-blue)"></span> = <span style="color: var(--dm-red)">+</span> 0.015625
<span style="color: var(--dm-red)">□</span><span style="color: yellow">□□□□□□□</span><span style="color: var(--dm-blue)"></span> =   0.0
<span style="color: var(--dm-red)">■</span><span style="color: yellow">■■■■■■■</span><span style="color: var(--dm-blue)"></span> = <span style="color: var(--dm-red)">-</span> 0.015625
<span style="color: var(--dm-red)">■</span><span style="color: yellow">■■■■■■□</span><span style="color: var(--dm-blue)"></span> = <span style="color: var(--dm-red)">-</span> 0.03125
<span style="color: var(--dm-red)">■</span><span style="color: yellow">■■■■■□</span><span style="color: var(--dm-blue)">■</span> = <span style="color: var(--dm-red)">-</span> 0.046875
<span style="color: var(--dm-red)">■</span><span style="color: yellow">■■■■■□</span><span style="color: var(--dm-blue)">□</span> = <span style="color: var(--dm-red)">-</span> 0.0625
<span style="color: var(--dm-red)">■</span><span style="color: yellow">■■■■□</span><span style="color: var(--dm-blue)">■■</span> = <span style="color: var(--dm-red)">-</span> 0.078125
<span style="color: var(--dm-red)">■</span><span style="color: yellow">■■■■□</span><span style="color: var(--dm-blue)">■□</span> = <span style="color: var(--dm-red)">-</span> 0.09375
<span style="color: var(--dm-red)">■</span><span style="color: yellow">■■■■□</span><span style="color: var(--dm-blue)">□■</span> = <span style="color: var(--dm-red)">-</span> 0.109375
<span style="color: var(--dm-red)">■</span><span style="color: yellow">■■■■□</span><span style="color: var(--dm-blue)">□□</span> = <span style="color: var(--dm-red)">-</span> 0.125
<span style="color: var(--dm-red)">■</span><span style="color: yellow">■■■□</span><span style="color: var(--dm-blue)">■■■</span> = <span style="color: var(--dm-red)">-</span> 0.140625
<span style="color: var(--dm-red)">■</span><span style="color: yellow">■■■□</span><span style="color: var(--dm-blue)">■■□</span> = <span style="color: var(--dm-red)">-</span> 0.15625
<span style="color: var(--dm-red)">■</span><span style="color: yellow">■■■□</span><span style="color: var(--dm-blue)">■□■</span> = <span style="color: var(--dm-red)">-</span> 0.171875
<span style="color: var(--dm-red)">■</span><span style="color: yellow">■■■□</span><span style="color: var(--dm-blue)">■□□</span> = <span style="color: var(--dm-red)">-</span> 0.1875
<span style="color: var(--dm-red)">■</span><span style="color: yellow">■■■□</span><span style="color: var(--dm-blue)">□■■</span> = <span style="color: var(--dm-red)">-</span> 0.203125
<span style="color: var(--dm-red)">■</span><span style="color: yellow">■■■□</span><span style="color: var(--dm-blue)">□■□</span> = <span style="color: var(--dm-red)">-</span> 0.21875
<span style="color: var(--dm-red)">■</span><span style="color: yellow">■■■□</span><span style="color: var(--dm-blue)">□□■</span> = <span style="color: var(--dm-red)">-</span> 0.234375
<span style="color: var(--dm-red)">■</span><span style="color: yellow">■■■□</span><span style="color: var(--dm-blue)">□□□</span> = <span style="color: var(--dm-red)">-</span> 0.25
<span style="color: var(--dm-red)">■</span><span style="color: yellow">■■□</span><span style="color: var(--dm-blue)">■■■■</span> = <span style="color: var(--dm-red)">-</span> 0.265625
<span style="color: var(--dm-red)">■</span><span style="color: yellow">■■□</span><span style="color: var(--dm-blue)">■■■□</span> = <span style="color: var(--dm-red)">-</span> 0.28125
<span style="color: var(--dm-red)">■</span><span style="color: yellow">■■□</span><span style="color: var(--dm-blue)">■■□■</span> = <span style="color: var(--dm-red)">-</span> 0.296875
<span style="color: var(--dm-red)">■</span><span style="color: yellow">■■□</span><span style="color: var(--dm-blue)">■■□□</span> = <span style="color: var(--dm-red)">-</span> 0.3125
<span style="color: var(--dm-red)">■</span><span style="color: yellow">■■□</span><span style="color: var(--dm-blue)">■□■■</span> = <span style="color: var(--dm-red)">-</span> 0.328125
<span style="color: var(--dm-red)">■</span><span style="color: yellow">■■□</span><span style="color: var(--dm-blue)">■□■□</span> = <span style="color: var(--dm-red)">-</span> 0.34375
<span style="color: var(--dm-red)">■</span><span style="color: yellow">■■□</span><span style="color: var(--dm-blue)">■□□■</span> = <span style="color: var(--dm-red)">-</span> 0.359375
<span style="color: var(--dm-red)">■</span><span style="color: yellow">■■□</span><span style="color: var(--dm-blue)">■□□□</span> = <span style="color: var(--dm-red)">-</span> 0.375
<span style="color: var(--dm-red)">■</span><span style="color: yellow">■■□</span><span style="color: var(--dm-blue)">□■■■</span> = <span style="color: var(--dm-red)">-</span> 0.390625
<span style="color: var(--dm-red)">■</span><span style="color: yellow">■■□</span><span style="color: var(--dm-blue)">□■■□</span> = <span style="color: var(--dm-red)">-</span> 0.40625
<span style="color: var(--dm-red)">■</span><span style="color: yellow">■■□</span><span style="color: var(--dm-blue)">□■□■</span> = <span style="color: var(--dm-red)">-</span> 0.421875
<span style="color: var(--dm-red)">■</span><span style="color: yellow">■■□</span><span style="color: var(--dm-blue)">□■□□</span> = <span style="color: var(--dm-red)">-</span> 0.4375
<span style="color: var(--dm-red)">■</span><span style="color: yellow">■■□</span><span style="color: var(--dm-blue)">□□■■</span> = <span style="color: var(--dm-red)">-</span> 0.453125
<span style="color: var(--dm-red)">■</span><span style="color: yellow">■■□</span><span style="color: var(--dm-blue)">□□■□</span> = <span style="color: var(--dm-red)">-</span> 0.46875
<span style="color: var(--dm-red)">■</span><span style="color: yellow">■■□</span><span style="color: var(--dm-blue)">□□□■</span> = <span style="color: var(--dm-red)">-</span> 0.484375
<span style="color: var(--dm-red)">■</span><span style="color: yellow">■■□</span><span style="color: var(--dm-blue)">□□□□</span> = <span style="color: var(--dm-red)">-</span> 0.5
<span style="color: var(--dm-red)">■</span><span style="color: yellow">■□</span><span style="color: var(--dm-blue)">■■■■■</span> = <span style="color: var(--dm-red)">-</span> 0.515625
<span style="color: var(--dm-red)">■</span><span style="color: yellow">■□</span><span style="color: var(--dm-blue)">■■■■□</span> = <span style="color: var(--dm-red)">-</span> 0.53125
<span style="color: var(--dm-red)">■</span><span style="color: yellow">■□</span><span style="color: var(--dm-blue)">■■■□■</span> = <span style="color: var(--dm-red)">-</span> 0.546875
<span style="color: var(--dm-red)">■</span><span style="color: yellow">■□</span><span style="color: var(--dm-blue)">■■■□□</span> = <span style="color: var(--dm-red)">-</span> 0.5625
<span style="color: var(--dm-red)">■</span><span style="color: yellow">■□</span><span style="color: var(--dm-blue)">■■□■■</span> = <span style="color: var(--dm-red)">-</span> 0.578125
<span style="color: var(--dm-red)">■</span><span style="color: yellow">■□</span><span style="color: var(--dm-blue)">■■□■□</span> = <span style="color: var(--dm-red)">-</span> 0.59375
<span style="color: var(--dm-red)">■</span><span style="color: yellow">■□</span><span style="color: var(--dm-blue)">■■□□■</span> = <span style="color: var(--dm-red)">-</span> 0.609375
<span style="color: var(--dm-red)">■</span><span style="color: yellow">■□</span><span style="color: var(--dm-blue)">■■□□□</span> = <span style="color: var(--dm-red)">-</span> 0.625
<span style="color: var(--dm-red)">■</span><span style="color: yellow">■□</span><span style="color: var(--dm-blue)">■□■■■</span> = <span style="color: var(--dm-red)">-</span> 0.640625
<span style="color: var(--dm-red)">■</span><span style="color: yellow">■□</span><span style="color: var(--dm-blue)">■□■■□</span> = <span style="color: var(--dm-red)">-</span> 0.65625
<span style="color: var(--dm-red)">■</span><span style="color: yellow">■□</span><span style="color: var(--dm-blue)">■□■□■</span> = <span style="color: var(--dm-red)">-</span> 0.671875
<span style="color: var(--dm-red)">■</span><span style="color: yellow">■□</span><span style="color: var(--dm-blue)">■□■□□</span> = <span style="color: var(--dm-red)">-</span> 0.6875
<span style="color: var(--dm-red)">■</span><span style="color: yellow">■□</span><span style="color: var(--dm-blue)">■□□■■</span> = <span style="color: var(--dm-red)">-</span> 0.703125
<span style="color: var(--dm-red)">■</span><span style="color: yellow">■□</span><span style="color: var(--dm-blue)">■□□■□</span> = <span style="color: var(--dm-red)">-</span> 0.71875
<span style="color: var(--dm-red)">■</span><span style="color: yellow">■□</span><span style="color: var(--dm-blue)">■□□□■</span> = <span style="color: var(--dm-red)">-</span> 0.734375
<span style="color: var(--dm-red)">■</span><span style="color: yellow">■□</span><span style="color: var(--dm-blue)">■□□□□</span> = <span style="color: var(--dm-red)">-</span> 0.75
<span style="color: var(--dm-red)">■</span><span style="color: yellow">■□</span><span style="color: var(--dm-blue)">□■■■■</span> = <span style="color: var(--dm-red)">-</span> 0.765625
<span style="color: var(--dm-red)">■</span><span style="color: yellow">■□</span><span style="color: var(--dm-blue)">□■■■□</span> = <span style="color: var(--dm-red)">-</span> 0.78125
<span style="color: var(--dm-red)">■</span><span style="color: yellow">■□</span><span style="color: var(--dm-blue)">□■■□■</span> = <span style="color: var(--dm-red)">-</span> 0.796875
<span style="color: var(--dm-red)">■</span><span style="color: yellow">■□</span><span style="color: var(--dm-blue)">□■■□□</span> = <span style="color: var(--dm-red)">-</span> 0.8125
<span style="color: var(--dm-red)">■</span><span style="color: yellow">■□</span><span style="color: var(--dm-blue)">□■□■■</span> = <span style="color: var(--dm-red)">-</span> 0.828125
<span style="color: var(--dm-red)">■</span><span style="color: yellow">■□</span><span style="color: var(--dm-blue)">□■□■□</span> = <span style="color: var(--dm-red)">-</span> 0.84375
<span style="color: var(--dm-red)">■</span><span style="color: yellow">■□</span><span style="color: var(--dm-blue)">□■□□■</span> = <span style="color: var(--dm-red)">-</span> 0.859375
<span style="color: var(--dm-red)">■</span><span style="color: yellow">■□</span><span style="color: var(--dm-blue)">□■□□□</span> = <span style="color: var(--dm-red)">-</span> 0.875
<span style="color: var(--dm-red)">■</span><span style="color: yellow">■□</span><span style="color: var(--dm-blue)">□□■■■</span> = <span style="color: var(--dm-red)">-</span> 0.890625
<span style="color: var(--dm-red)">■</span><span style="color: yellow">■□</span><span style="color: var(--dm-blue)">□□■■□</span> = <span style="color: var(--dm-red)">-</span> 0.90625
<span style="color: var(--dm-red)">■</span><span style="color: yellow">■□</span><span style="color: var(--dm-blue)">□□■□■</span> = <span style="color: var(--dm-red)">-</span> 0.921875
<span style="color: var(--dm-red)">■</span><span style="color: yellow">■□</span><span style="color: var(--dm-blue)">□□■□□</span> = <span style="color: var(--dm-red)">-</span> 0.9375
<span style="color: var(--dm-red)">■</span><span style="color: yellow">■□</span><span style="color: var(--dm-blue)">□□□■■</span> = <span style="color: var(--dm-red)">-</span> 0.953125
<span style="color: var(--dm-red)">■</span><span style="color: yellow">■□</span><span style="color: var(--dm-blue)">□□□■□</span> = <span style="color: var(--dm-red)">-</span> 0.96875
<span style="color: var(--dm-red)">■</span><span style="color: yellow">■□</span><span style="color: var(--dm-blue)">□□□□■</span> = <span style="color: var(--dm-red)">-</span> 0.984375
<span style="color: var(--dm-red)">■</span><span style="color: yellow">■□</span><span style="color: var(--dm-blue)">□□□□□</span> = <span style="color: var(--dm-red)">-</span> 1.0
<span style="color: var(--dm-red)">■</span><span style="color: yellow">□■</span><span style="color: var(--dm-blue)">■■■■■</span> = <span style="color: var(--dm-red)">-</span> 1.03125
<span style="color: var(--dm-red)">■</span><span style="color: yellow">□■</span><span style="color: var(--dm-blue)">■■■■□</span> = <span style="color: var(--dm-red)">-</span> 1.0625
<span style="color: var(--dm-red)">■</span><span style="color: yellow">□■</span><span style="color: var(--dm-blue)">■■■□■</span> = <span style="color: var(--dm-red)">-</span> 1.09375
<span style="color: var(--dm-red)">■</span><span style="color: yellow">□■</span><span style="color: var(--dm-blue)">■■■□□</span> = <span style="color: var(--dm-red)">-</span> 1.125
<span style="color: var(--dm-red)">■</span><span style="color: yellow">□■</span><span style="color: var(--dm-blue)">■■□■■</span> = <span style="color: var(--dm-red)">-</span> 1.15625
<span style="color: var(--dm-red)">■</span><span style="color: yellow">□■</span><span style="color: var(--dm-blue)">■■□■□</span> = <span style="color: var(--dm-red)">-</span> 1.1875
<span style="color: var(--dm-red)">■</span><span style="color: yellow">□■</span><span style="color: var(--dm-blue)">■■□□■</span> = <span style="color: var(--dm-red)">-</span> 1.21875
<span style="color: var(--dm-red)">■</span><span style="color: yellow">□■</span><span style="color: var(--dm-blue)">■■□□□</span> = <span style="color: var(--dm-red)">-</span> 1.25
<span style="color: var(--dm-red)">■</span><span style="color: yellow">□■</span><span style="color: var(--dm-blue)">■□■■■</span> = <span style="color: var(--dm-red)">-</span> 1.28125
<span style="color: var(--dm-red)">■</span><span style="color: yellow">□■</span><span style="color: var(--dm-blue)">■□■■□</span> = <span style="color: var(--dm-red)">-</span> 1.3125
<span style="color: var(--dm-red)">■</span><span style="color: yellow">□■</span><span style="color: var(--dm-blue)">■□■□■</span> = <span style="color: var(--dm-red)">-</span> 1.34375
<span style="color: var(--dm-red)">■</span><span style="color: yellow">□■</span><span style="color: var(--dm-blue)">■□■□□</span> = <span style="color: var(--dm-red)">-</span> 1.375
<span style="color: var(--dm-red)">■</span><span style="color: yellow">□■</span><span style="color: var(--dm-blue)">■□□■■</span> = <span style="color: var(--dm-red)">-</span> 1.40625
<span style="color: var(--dm-red)">■</span><span style="color: yellow">□■</span><span style="color: var(--dm-blue)">■□□■□</span> = <span style="color: var(--dm-red)">-</span> 1.4375
<span style="color: var(--dm-red)">■</span><span style="color: yellow">□■</span><span style="color: var(--dm-blue)">■□□□■</span> = <span style="color: var(--dm-red)">-</span> 1.46875
<span style="color: var(--dm-red)">■</span><span style="color: yellow">□■</span><span style="color: var(--dm-blue)">■□□□□</span> = <span style="color: var(--dm-red)">-</span> 1.5
<span style="color: var(--dm-red)">■</span><span style="color: yellow">□■</span><span style="color: var(--dm-blue)">□■■■■</span> = <span style="color: var(--dm-red)">-</span> 1.53125
<span style="color: var(--dm-red)">■</span><span style="color: yellow">□■</span><span style="color: var(--dm-blue)">□■■■□</span> = <span style="color: var(--dm-red)">-</span> 1.5625
<span style="color: var(--dm-red)">■</span><span style="color: yellow">□■</span><span style="color: var(--dm-blue)">□■■□■</span> = <span style="color: var(--dm-red)">-</span> 1.59375
<span style="color: var(--dm-red)">■</span><span style="color: yellow">□■</span><span style="color: var(--dm-blue)">□■■□□</span> = <span style="color: var(--dm-red)">-</span> 1.625
<span style="color: var(--dm-red)">■</span><span style="color: yellow">□■</span><span style="color: var(--dm-blue)">□■□■■</span> = <span style="color: var(--dm-red)">-</span> 1.65625
<span style="color: var(--dm-red)">■</span><span style="color: yellow">□■</span><span style="color: var(--dm-blue)">□■□■□</span> = <span style="color: var(--dm-red)">-</span> 1.6875
<span style="color: var(--dm-red)">■</span><span style="color: yellow">□■</span><span style="color: var(--dm-blue)">□■□□■</span> = <span style="color: var(--dm-red)">-</span> 1.71875
<span style="color: var(--dm-red)">■</span><span style="color: yellow">□■</span><span style="color: var(--dm-blue)">□■□□□</span> = <span style="color: var(--dm-red)">-</span> 1.75
<span style="color: var(--dm-red)">■</span><span style="color: yellow">□■</span><span style="color: var(--dm-blue)">□□■■■</span> = <span style="color: var(--dm-red)">-</span> 1.78125
<span style="color: var(--dm-red)">■</span><span style="color: yellow">□■</span><span style="color: var(--dm-blue)">□□■■□</span> = <span style="color: var(--dm-red)">-</span> 1.8125
<span style="color: var(--dm-red)">■</span><span style="color: yellow">□■</span><span style="color: var(--dm-blue)">□□■□■</span> = <span style="color: var(--dm-red)">-</span> 1.84375
<span style="color: var(--dm-red)">■</span><span style="color: yellow">□■</span><span style="color: var(--dm-blue)">□□■□□</span> = <span style="color: var(--dm-red)">-</span> 1.875
<span style="color: var(--dm-red)">■</span><span style="color: yellow">□■</span><span style="color: var(--dm-blue)">□□□■■</span> = <span style="color: var(--dm-red)">-</span> 1.90625
<span style="color: var(--dm-red)">■</span><span style="color: yellow">□■</span><span style="color: var(--dm-blue)">□□□■□</span> = <span style="color: var(--dm-red)">-</span> 1.9375
<span style="color: var(--dm-red)">■</span><span style="color: yellow">□■</span><span style="color: var(--dm-blue)">□□□□■</span> = <span style="color: var(--dm-red)">-</span> 1.96875
<span style="color: var(--dm-red)">■</span><span style="color: yellow">□■</span><span style="color: var(--dm-blue)">□□□□□</span> = <span style="color: var(--dm-red)">-</span> 2.0
<span style="color: var(--dm-red)">■</span><span style="color: yellow">□□■</span><span style="color: var(--dm-blue)">■■■■</span> = <span style="color: var(--dm-red)">-</span> 2.125
<span style="color: var(--dm-red)">■</span><span style="color: yellow">□□■</span><span style="color: var(--dm-blue)">■■■□</span> = <span style="color: var(--dm-red)">-</span> 2.25
<span style="color: var(--dm-red)">■</span><span style="color: yellow">□□■</span><span style="color: var(--dm-blue)">■■□■</span> = <span style="color: var(--dm-red)">-</span> 2.375
<span style="color: var(--dm-red)">■</span><span style="color: yellow">□□■</span><span style="color: var(--dm-blue)">■■□□</span> = <span style="color: var(--dm-red)">-</span> 2.5
<span style="color: var(--dm-red)">■</span><span style="color: yellow">□□■</span><span style="color: var(--dm-blue)">■□■■</span> = <span style="color: var(--dm-red)">-</span> 2.625
<span style="color: var(--dm-red)">■</span><span style="color: yellow">□□■</span><span style="color: var(--dm-blue)">■□■□</span> = <span style="color: var(--dm-red)">-</span> 2.75
<span style="color: var(--dm-red)">■</span><span style="color: yellow">□□■</span><span style="color: var(--dm-blue)">■□□■</span> = <span style="color: var(--dm-red)">-</span> 2.875
<span style="color: var(--dm-red)">■</span><span style="color: yellow">□□■</span><span style="color: var(--dm-blue)">■□□□</span> = <span style="color: var(--dm-red)">-</span> 3.0
<span style="color: var(--dm-red)">■</span><span style="color: yellow">□□■</span><span style="color: var(--dm-blue)">□■■■</span> = <span style="color: var(--dm-red)">-</span> 3.125
<span style="color: var(--dm-red)">■</span><span style="color: yellow">□□■</span><span style="color: var(--dm-blue)">□■■□</span> = <span style="color: var(--dm-red)">-</span> 3.25
<span style="color: var(--dm-red)">■</span><span style="color: yellow">□□■</span><span style="color: var(--dm-blue)">□■□■</span> = <span style="color: var(--dm-red)">-</span> 3.375
<span style="color: var(--dm-red)">■</span><span style="color: yellow">□□■</span><span style="color: var(--dm-blue)">□■□□</span> = <span style="color: var(--dm-red)">-</span> 3.5
<span style="color: var(--dm-red)">■</span><span style="color: yellow">□□■</span><span style="color: var(--dm-blue)">□□■■</span> = <span style="color: var(--dm-red)">-</span> 3.625
<span style="color: var(--dm-red)">■</span><span style="color: yellow">□□■</span><span style="color: var(--dm-blue)">□□■□</span> = <span style="color: var(--dm-red)">-</span> 3.75
<span style="color: var(--dm-red)">■</span><span style="color: yellow">□□■</span><span style="color: var(--dm-blue)">□□□■</span> = <span style="color: var(--dm-red)">-</span> 3.875
<span style="color: var(--dm-red)">■</span><span style="color: yellow">□□■</span><span style="color: var(--dm-blue)">□□□□</span> = <span style="color: var(--dm-red)">-</span> 4.0
<span style="color: var(--dm-red)">■</span><span style="color: yellow">□□□■</span><span style="color: var(--dm-blue)">■■■</span> = <span style="color: var(--dm-red)">-</span> 4.5
<span style="color: var(--dm-red)">■</span><span style="color: yellow">□□□■</span><span style="color: var(--dm-blue)">■■□</span> = <span style="color: var(--dm-red)">-</span> 5.0
<span style="color: var(--dm-red)">■</span><span style="color: yellow">□□□■</span><span style="color: var(--dm-blue)">■□■</span> = <span style="color: var(--dm-red)">-</span> 5.5
<span style="color: var(--dm-red)">■</span><span style="color: yellow">□□□■</span><span style="color: var(--dm-blue)">■□□</span> = <span style="color: var(--dm-red)">-</span> 6.0
<span style="color: var(--dm-red)">■</span><span style="color: yellow">□□□■</span><span style="color: var(--dm-blue)">□■■</span> = <span style="color: var(--dm-red)">-</span> 6.5
<span style="color: var(--dm-red)">■</span><span style="color: yellow">□□□■</span><span style="color: var(--dm-blue)">□■□</span> = <span style="color: var(--dm-red)">-</span> 7.0
<span style="color: var(--dm-red)">■</span><span style="color: yellow">□□□■</span><span style="color: var(--dm-blue)">□□■</span> = <span style="color: var(--dm-red)">-</span> 7.5
<span style="color: var(--dm-red)">■</span><span style="color: yellow">□□□■</span><span style="color: var(--dm-blue)">□□□</span> = <span style="color: var(--dm-red)">-</span> 8.0
<span style="color: var(--dm-red)">■</span><span style="color: yellow">□□□□■</span><span style="color: var(--dm-blue)">■■</span> = <span style="color: var(--dm-red)">-</span>10.0
<span style="color: var(--dm-red)">■</span><span style="color: yellow">□□□□■</span><span style="color: var(--dm-blue)">■□</span> = <span style="color: var(--dm-red)">-</span>12.0
<span style="color: var(--dm-red)">■</span><span style="color: yellow">□□□□■</span><span style="color: var(--dm-blue)">□■</span> = <span style="color: var(--dm-red)">-</span>14.0
<span style="color: var(--dm-red)">■</span><span style="color: yellow">□□□□■</span><span style="color: var(--dm-blue)">□□</span> = <span style="color: var(--dm-red)">-</span>16.0
<span style="color: var(--dm-red)">■</span><span style="color: yellow">□□□□□■</span><span style="color: var(--dm-blue)">■</span> = <span style="color: var(--dm-red)">-</span>24.0
<span style="color: var(--dm-red)">■</span><span style="color: yellow">□□□□□■</span><span style="color: var(--dm-blue)">□</span> = <span style="color: var(--dm-red)">-</span>32.0
<span style="color: var(--dm-red)">■</span><span style="color: yellow">□□□□□□■</span><span style="color: var(--dm-blue)"></span> = <span style="color: var(--dm-red)">-</span>64.0
<span style="color: var(--dm-red)">■</span><span style="color: yellow">□□□□□□□</span><span style="color: var(--dm-blue)"></span> =   NaR
</pre>
