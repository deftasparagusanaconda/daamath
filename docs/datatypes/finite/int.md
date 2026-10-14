# int


integers: …, −2, −1, 0, +1, +2, …

| name | description |
| - | - |
| int8 | −2^7^, −2^7^ + 1, −2^7^ + 2, …, +2^7 − 3, +2^7 − 2, +2^7 − 1 |
| int16 | −2^15^, −2^15^ + 1, −2^15^ + 2, …, +2^15 − 3, +2^15 − 2, +2^15 − 1 |
| int32 | −2^31^, −2^31^ + 1, −2^31^ + 2, …, +2^31 − 3, +2^31 − 2, +2^31 − 1 |
| int64 | −2^64^, −2^64^ + 1, −2^64^ + 2, …, +2^64 − 3, +2^64 − 2, +2^64 − 1 |
| int128 | −2^128^, −2^128^ + 1, −2^128^ + 2, …, +2^128 − 3, +2^128 − 2, +2^128 − 1 |

# int8

<pre>
<span style="color: var(--dm-blue)">□</span><span style="color: var(--dm-red)">■■■■■■■</span> = <span style="color: var(--dm-blue)">+</span><span style="color: var(--dm-red)">127</span>
<span style="color: var(--dm-blue)">□</span><span style="color: var(--dm-red)">■■■■■■□</span> = <span style="color: var(--dm-blue)">+</span><span style="color: var(--dm-red)">126</span>
<span style="color: var(--dm-blue)">□</span><span style="color: var(--dm-red)">■■■■■□■</span> = <span style="color: var(--dm-blue)">+</span><span style="color: var(--dm-red)">125</span>
<span style="color: var(--dm-blue)">□</span><span style="color: var(--dm-red)">·······</span> = <span style="color: var(--dm-blue)">+</span><span style="color: var(--dm-red)">···</span>
<span style="color: var(--dm-blue)">□</span><span style="color: var(--dm-red)">□□□□□■■</span> = <span style="color: var(--dm-blue)">+</span><span style="color: var(--dm-red)">  3</span>
<span style="color: var(--dm-blue)">□</span><span style="color: var(--dm-red)">□□□□□■□</span> = <span style="color: var(--dm-blue)">+</span><span style="color: var(--dm-red)">  2</span>
<span style="color: var(--dm-blue)">□</span><span style="color: var(--dm-red)">□□□□□□■</span> = <span style="color: var(--dm-blue)">+</span><span style="color: var(--dm-red)">  1</span>
<span style="color: var(--dm-blue)">□</span><span style="color: var(--dm-red)">□□□□□□□</span> = <span style="color: var(--dm-blue)"> </span><span style="color: var(--dm-red)">  0</span>
<span style="color: var(--dm-blue)">■</span><span style="color: var(--dm-red)">■■■■■■■</span> = <span style="color: var(--dm-blue)">-</span><span style="color: var(--dm-red)">  1</span>
<span style="color: var(--dm-blue)">■</span><span style="color: var(--dm-red)">■■■■■■□</span> = <span style="color: var(--dm-blue)">-</span><span style="color: var(--dm-red)">  2</span>
<span style="color: var(--dm-blue)">■</span><span style="color: var(--dm-red)">■■■■■□■</span> = <span style="color: var(--dm-blue)">-</span><span style="color: var(--dm-red)">  3</span>
<span style="color: var(--dm-blue)">■</span><span style="color: var(--dm-red)">·······</span> = <span style="color: var(--dm-blue)">-</span><span style="color: var(--dm-red)">···</span>
<span style="color: var(--dm-blue)">■</span><span style="color: var(--dm-red)">□□□□□■□</span> = <span style="color: var(--dm-blue)">-</span><span style="color: var(--dm-red)">126</span>
<span style="color: var(--dm-blue)">■</span><span style="color: var(--dm-red)">□□□□□□■</span> = <span style="color: var(--dm-blue)">-</span><span style="color: var(--dm-red)">127</span>
<span style="color: var(--dm-blue)">■</span><span style="color: var(--dm-red)">□□□□□□□</span> = <span style="color: var(--dm-blue)">-</span><span style="color: var(--dm-red)">128</span>
</pre>
