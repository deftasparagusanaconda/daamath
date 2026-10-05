# approximate

we have quite a few constants in mathematics:

| name | eponyms | formula | decimal |
| ---- | ------- | ------- | ------- |
{{ math_constants() }}

# exceptions

* the [🇳🇴 Viggo Brun](https://no.wikipedia.org/wiki/Viggo_Brun) constant $\href{https://en.wikipedia.org/wiki/Brun%27s_theorem}{\mathrm B_2} := \left.\displaystyle\sum \left(\dfrac 1p + \dfrac 1q\right)\;\right\vert\;\href{https://no.wikipedia.org/wiki/Tvillingprimtall}{\begin{aligned} &p, q \in \mathbb P \\ &p + 2 = q \end{aligned}}$ ≈ [1.902160583104…](https://oeis.org/A065421) is excluded because we do not know enough digits to saturate the precision of the datatypes
<!--* constants like 0, 1, -1, 2, ½ are not stored since their construction is trivial--><!-- i excluded this because its stating the obvious -->

# sources

* [wikipedia](https://en.wikipedia.org/wiki/List_of_mathematical_constants)

<!--
```python
--8<-- "py files/generate math constants.py"
```
-->

{{ yaml_source(page) }}
