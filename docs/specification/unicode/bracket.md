---
hide:
  - toc
---

<!-- # () {} [] ⌊⌋ ⌈⌉ ⟨⟩ ⦗⦘ -->

```yaml
bracket:
  # ------------------
  # 2-partite brackets
  # ------------------
  round:           {left: ( , right: ) , top: ⏜ , bottom: ⏝ , 
    double:        {left: ⸨ , right: ⸩ ,                    },
    white:         {left: ⦅ , right: ⦆ ,                    },
    small:         {left: ﹙, right: ﹚,                    },
    superscript:   {left: ⁽ , right: ⁾ ,                    },
    subscript:     {left: ₍ , right: ₎ ,                    },
    half: 
    { top:         {left: ⹙ , right: ⹚ ,                    },
      bottom:      {left: ⹛ , right: ⹜ ,                    }},
    flattened:     {left: ⟮ , right: ⟯ ,                    },
    ornate:        {left: ﴾ , right: ﴿ ,                    },
    ornament: 
    { medium:      {left: ❨ , right: ❩ ,
        flattened: {left: ❪ , right: ❫ ,                    }}},
    fullwidth:     {left: （, right: ）,
      white:       {left: ｟, right: ｠,                    }},
    presentation:  {                     top: ︵, bottom: ︶},
    big: 
    { three:
      { left:
        { top:    ⎛,
          middle: ⎜,
          bottom: ⎝},
        right:
        { top:    ⎞,
          middle: ⎟,
          bottom: ⎠}
      } 
    }
  }
  
  square:      {left: '[', right: ']', top: ⎴ , bottom: ⎵ ,
    white:     {left:  ⟦ , right:  ⟧ ,                    },
    quill:     {left:  ⁅ , right:  ⁆ ,                    },
    underbar:  {left:  ⦋ , right:  ⦌ ,                    }, 
    tick:
    { top:     {left:  ⦍ , right:  ⦐ ,                    },
      bottom:  {left:  ⦏ , right:  ⦎ ,                    }},
    stroke:    {left:  ⹕ , right:  ⹖ ,                  
      double:  {left:  ⹗ , right:  ⹘ ,                    }},
    fullwidth: {left:  ［, right:  ］,
      white:   {left:  〚, right:  〛,                    }},
    presentation: {                    top: ﹇, bottom: ﹈},
    bottom_over_top: ⎶, # shouldnt... the top be over the bottom? xd ahem ahem
    big: 
    { three:
      { left:
        { top:    ⎡,
          middle: ⎢,
          bottom: ⎣
        },
        right:
        { top:    ⎤,
          middle: ⎥,
          bottom: ⎦
        }
      }
    }
  }

  curly:          {left: '{', right: '}', top: ⏞ , bottom: ⏟ ,
    white:        {left:  ⦃ , right:  ⦄                      },
    ornament:  
    { 
      medium:     {left:  ❴ , right:  ❵                      }
    },
    fullwidth:    {left:  ｛, right:  ｝,                    },
    small:        {left:  ﹛, right:  ﹜                     },
    presentation: {                       top: ︷, bottom: ︸},
    big: 
    { two: 
      { 
        rising:  ⎰,
        falling: ⎱
      },
      three: 
      {
        vertical: ⎪,
        left: 
        {
          top:    ⎧,
          middle: ⎨,
          bottom: ⎩},
        right: 
        {
          top:    ⎫,
          middle: ⎬,
          bottom: ⎭
        }
      }
    }
  }

  angle:         {left: ⟨ , right: ⟩ ,
    deprecated:  {left: 〈, right: 〉},
    dotted:      {left: ⦑ , right: ⦒ },
    curved:      {left: ⧼ , right: ⧽ },
    fullwidth: {
      narrow:    {left: ＜, right: ＞},
      wide:      {left: 〈, right: 〉},
      presentation: {                 top: ︽, bottom: ︾}},
    presentation: {                   top: ︿, bottom: ﹀},
    double:      {left: ⟪ , right: ⟫ , 
      fullwidth: {left: 《, right: 》}},
    ornament: {
      medium:    {left: ❬ , right: ❭ },
      heavy:     {left: ❰ , right: ❱ }}}
  #quotation_mark_ornament_heavy: "❮❯"
               
  lenticular:
    fullwidth:
      black:       {left: 【, right: 】,                    }
      white:       {left: 〖, right: 〗,                    }
    presentation:
      black:       {                     top: ︻, bottom: ︼}
      white:       {                     top: ︗, bottom: ︘}

  tortoise_shell:
    black:         {left: ⦗ , right: ⦘ , top: ⏠ , bottom: ⏡ }
    white:         {left: ⟬ , right: ⟭ ,                    }
    small:         {left: ﹝, right: ﹞,                    }
    fullwidth:
      black:       {left: 〔, right: 〕,                    }
      white:       {left: 〘, right: 〙,                    }
    ornament:
      light:       {left: ❲ , right: ❳ ,                    }
    presentation:  {                     top: ︹, bottom: ︺}

  arc_inequality:  {left: ⦓ , right: ⦔ ,
    double:        {left: ⦕ , right: ⦖ }}

  wiggly_fence:    {left: ⧘ , right: ⧙ ,
    double:        {left: ⧚ , right: ⧛ }}

  substitution:    {left: ⸂ , right: ⸃ ,
    dotted:        {left: ⸄ , right: ⸅ }}

  guillemet:       {left: ‹ , right: › ,
    double:        {left: « , right: » }}
  
  paraphrase:
    low:           {left: ⸜ , right: ⸝ }

  prime_quotation:
    double:        {left: 〝, right: 〞}

  floor:           {left: ⌊ , right: ⌋ }
  ceil:            {left: ⌈ , right: ⌉ }
  vertical:        {left: ⎸ , right: ⎹ }
  image:           {left: ⦇ , right: ⦈ }
  binding:         {left: ⦉ , right: ⦊ }
  ogham_feather:   {left: ᚛ , right: ᚜ }
  gug_rtags:       {left: ༺ , right: ༻ }
  ang_khang:       {left: ༼ , right: ༽ }
  transposition:   {left: ⸉ , right: ⸊ }
  omission_raised: {left: ⸌ , right: ⸍ }
  sideways_u:      {left: ⸦ , right: ⸧ }

  # ------------------
  # 4-partite brackets
  # ------------------

  corner:         {top_left: ⌜ , top_right: ⌝ , bottom_left: ⌞ , bottom_right: ⌟ ,
    dot:          {top_left: ⟔ ,                                 bottom_right: ⟓ },
    halfwidth:    {top_left: ｢ ,                                 bottom_right: ｣ },
    fullwidth:    {top_left: 「,                                 bottom_right: 」,
      white:      {top_left: 『,                                 bottom_right: 』}},
    presentation: {              top_right: ﹁, bottom_left: ﹂,                 
      white:      {              top_right: ﹃, bottom_left: ﹄,                 }}}

  half:           {top_left: ⸢ , top_right: ⸣ , bottom_left: ⸤ , bottom_right: ⸥ }
  # crop:           {top_left: ⌌ , top_right: ⌍ , bottom_left: ⌎ , bottom_right: ⌏ }
                                            
```
