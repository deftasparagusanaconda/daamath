---
hide:
  - toc
---

# angle

we have 5 useful angle constants: [`turn`](#turn) [`gradian`](#gradian) [`degree`](#)

since [radians](https://en.wikipedia.org/wiki/Radian) are the most natural unit for 2D angles, [daa] *is* aware of 3D angles like steradians and squared degrees but for these conversions, you should compose the conversion yourself.

<table>
	<tr>
		<th>name</th>
		<th>common symbols</th>
		<th>radians</th>
		<th>approximations</th>
	</tr>
	<tr>
		<td><a href="https://en.wikipedia.org/wiki/Turn_(angle)"><code>turn</code></a></td>
		<td></td>
		<td><a href="https://en.wikipedia.org/wiki/Tau">τ</a></td>
		<td>
			<details>
				<summary>6.2831853…</summary>
				6.28318530717958647692528676655900576839433879875021164194988918461563281257241799725606965068423413… 
			</details>
		</td>
	</tr>
	<tr>
		<td><a href="https://en.wikipedia.org/wiki/Gradian"><code>gradian</code></a></td>
		<td></td>
		<td></td>
		<td> <a href="https://en.wikipedia.org/wiki/Tau">τ</a> / 400</td>
		<td>
			<details>
				<summary>0.0157079…</summary>
				0.01570796326794896619231321691639751442098584699687552910487472296153908203143104499314017412671058… 
			</details>
		</td>
	</tr>
	<tr>
		<td><code><a href="https://en.wikipedia.org/wiki/Degree_(angle)">degree</a></code></td>
		<td></td>
		<td><a href="https://en.wikipedia.org/wiki/Degree_symbol">°</a></td>
		<td><a href="https://en.wikipedia.org/wiki/Tau">τ</a> / 360</td>
		<td>
			<details>
				<summary>0.0174532…</summary>
				0.01745329251994329576923690768488612713442871888541725456097191440171009114603449443682241569634509… 
			</details>
		</td>
	</tr>
	<tr>
		<td><a href="https://en.wikipedia.org/wiki/Minute_and_second_of_arc"><code>arcminute</code></a></td>
		<td><a href="https://en.wikipedia.org/wiki/Second#Etymology">′</a></td>
		<td><a href="https://en.wikipedia.org/wiki/Tau">τ</a> / 360 / 60¹</td> 
		<td>
			<details>
				<summary>0.0002908…</summary>
				0.00029088820866572159615394846141476878557381198142362090934953190669516818576724157394704026160575… 
			</details>
		</td>
	</tr>
	<tr>
		<td><code>arcsecond</code></td>
		<td><a href="https://en.wikipedia.org/wiki/Minute_and_second_of_arc">second</a>, <a href="https://en.wikipedia.org/wiki/Second#Etymology">pars minuta secunda</a></td>
		<td>″</td>
		<td><a href="https://en.wikipedia.org/wiki/Tau">τ</a> / 360 / 60²</td>
		<td>
			<details>
				<summary>0.0000048…</summary>
				0.000004848136811095359935899141023579479759563533023727015155825531778252803096120692899117337693429… 
			</details>
		</td>
	</tr>
</table>

{{ yaml_source(page) }}

[daa]: hi!
