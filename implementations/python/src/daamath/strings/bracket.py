from ..utils import Namespace

bracket = Namespace(**{
    'round': Namespace(**{
        'left': '(',
        'right': ')',
        'top': '⏜',
        'bottom': '⏝',
        'double': Namespace(**{
            'left': '⸨',
            'right': '⸩'
        }),
        'white': Namespace(**{
            'left': '⦅',
            'right': '⦆'
        }),
        'small': Namespace(**{
            'left': '﹙',
            'right': '﹚'
        }),
        'superscript': Namespace(**{
            'left': '⁽',
            'right': '⁾'
        }),
        'subscript': Namespace(**{
            'left': '₍',
            'right': '₎'
        }),
        'half': Namespace(**{
            'top': Namespace(**{
                'left': '⹙',
                'right': '⹚'
            }),
            'bottom': Namespace(**{
                'left': '⹛',
                'right': '⹜'
            })
        }),
        'flattened': Namespace(**{
            'left': '⟮',
            'right': '⟯'
        }),
        'ornate': Namespace(**{
            'left': '﴾',
            'right': '﴿'
        }),
        'ornament': Namespace(**{
            'medium': Namespace(**{
                'left': '❨',
                'right': '❩',
                'flattened': Namespace(**{
                    'left': '❪',
                    'right': '❫'
                })
            })
        }),
        'fullwidth': Namespace(**{
            'left': '（',
            'right': '）',
            'white': Namespace(**{
                'left': '｟',
                'right': '｠'
            })
        }),
        'presentation': Namespace(**{
            'top': '︵',
            'bottom': '︶'
        }),
        'big': Namespace(**{
            'three': Namespace(**{
                'left': Namespace(**{
                    'top': '⎛',
                    'middle': '⎜',
                    'bottom': '⎝'
                }),
                'right': Namespace(**{
                    'top': '⎞',
                    'middle': '⎟',
                    'bottom': '⎠'
                })
            })
        })
    }),
    'floor': Namespace(**{
        'left': '⌊',
        'right': '⌋'
    }),
    'ceil': Namespace(**{
        'left': '⌈',
        'right': '⌉'
    }),
    'vertical': Namespace(**{
        'left': '⎸',
        'right': '⎹'
    }),
    'half': Namespace(**{
        'left': Namespace(**{
            'top': '⸢',
            'bottom': '⸤'
        }),
        'right': Namespace(**{
            'top': '⸣',
            'bottom': '⸥'
        })
    }),
    'square': Namespace(**{
        'left': '[',
        'right': ']',
        'top': '⎴',
        'bottom': '⎵',
        'white': Namespace(**{
            'left': '⟦',
            'right': '⟧'
        }),
        'quill': Namespace(**{
            'left': '⁅',
            'right': '⁆'
        }),
        'underbar': Namespace(**{
            'left': '⦋',
            'right': '⦌'
        }),
        'tick': Namespace(**{
            'top': Namespace(**{
                'left': '⦍',
                'right': '⦐'
            }),
            'bottom': Namespace(**{
                'left': '⦏',
                'right': '⦎'
            })
        }),
        'stroke': Namespace(**{
            'left': '⹕',
            'right': '⹖',
            'double': Namespace(**{
                'left': '⹗',
                'right': '⹘'
            })
        }),
        'fullwidth': Namespace(**{
            'left': '［',
            'right': '］',
            'white': Namespace(**{
                'left': '〚',
                'right': '〛'
            })
        }),
        'presentation': Namespace(**{
            'top': '﹇',
            'bottom': '﹈'
        }),
        'bottom_over_top': '⎶',
        'big': Namespace(**{
            'three': Namespace(**{
                'left': Namespace(**{
                    'top': '⎡',
                    'middle': '⎢',
                    'bottom': '⎣'
                }),
                'right': Namespace(**{
                    'top': '⎤',
                    'middle': '⎥',
                    'bottom': '⎦'
                })
            })
        })
    }),
    'curly': Namespace(**{
        'left': '{',
        'right': '}',
        'top': '⏞',
        'bottom': '⏟',
        'white': Namespace(**{
            'left': '⦃',
            'right': '⦄'
        }),
        'ornament': Namespace(**{
            'medium': Namespace(**{
                'left': '❴',
                'right': '❵'
            })
        }),
        'fullwidth': Namespace(**{
            'left': '｛',
            'right': '｝'
        }),
        'small': Namespace(**{
            'left': '﹛',
            'right': '﹜'
        }),
        'presentation': Namespace(**{
            'top': '︷',
            'bottom': '︸'
        }),
        'big': Namespace(**{
            'two': Namespace(**{
                'left': Namespace(**{
                    'top': '⎰',
                    'bottom': '⎱'
                })
            }),
            'three': Namespace(**{
                'left': Namespace(**{
                    'top': '⎧',
                    'middle': '⎨',
                    'bottom': '⎩'
                }),
                'right': Namespace(**{
                    'top': '⎫',
                    'middle': '⎬',
                    'bottom': '⎭'
                }),
                'vertical': '⎪'
            })
        })
    }),
    'angle': Namespace(**{
        'left': '⟨',
        'right': '⟩',
        'dotted': Namespace(**{
            'left': '⦑',
            'right': '⦒'
        }),
        'curved': Namespace(**{
            'left': '⧼',
            'right': '⧽'
        }),
        'fullwidth': Namespace(**{
            'narrow': Namespace(**{
                'left': '＜',
                'right': '＞'
            }),
            'wide': Namespace(**{
                'left': '〈',
                'right': '〉'
            }),
            'presentation': Namespace(**{
                'top': '︽',
                'bottom': '︾'
            })
        }),
        'presentation': Namespace(**{
            'top': '︿',
            'bottom': '﹀'
        }),
        'double': Namespace(**{
            'left': '⟪',
            'right': '⟫',
            'fullwidth': Namespace(**{
                'left': '《',
                'right': '》'
            })
        }),
        'ornament': Namespace(**{
            'medium': Namespace(**{
                'left': '❬',
                'right': '❭'
            }),
            'heavy': Namespace(**{
                'left': '❰',
                'right': '❱'
            })
        })
    }),
    'lenticular': Namespace(**{
        'fullwidth': Namespace(**{
            'black': Namespace(**{
                'left': '【',
                'right': '】'
            }),
            'white': Namespace(**{
                'left': '〖',
                'right': '〗'
            })
        }),
        'presentation': Namespace(**{
            'black': Namespace(**{
                'top': '︻',
                'bottom': '︼'
            }),
            'white': Namespace(**{
                'top': '︗',
                'bottom': '︘'
            })
        })
    }),
    'tortoise_shell': Namespace(**{
        'black': Namespace(**{
            'left': '⦗',
            'right': '⦘',
            'top': '⏠',
            'bottom': '⏡'
        }),
        'white': Namespace(**{
            'left': '⟬',
            'right': '⟭'
        }),
        'small': Namespace(**{
            'left': '﹝',
            'right': '﹞'
        }),
        'fullwidth': Namespace(**{
            'black': Namespace(**{
                'left': '〔',
                'right': '〕'
            }),
            'white': Namespace(**{
                'left': '〘',
                'righ': '〙'
            })
        }),
        'ornament': Namespace(**{
            'light': Namespace(**{
                'left': '❲',
                'right': '❳'
            })
        }),
        'presentation': Namespace(**{
            'top': '︹',
            'bottom': '︺'
        })
    }),
    'corner': Namespace(**{
        'left': Namespace(**{
            'top': '⌜',
            'bottom': '⌞'
        }),
        'right': Namespace(**{
            'top': '⌝',
            'bottom': '⌟'
        }),
        'dot': Namespace(**{
            'left': Namespace(**{
                'top': '⟔'
            }),
            'right': Namespace(**{
                'bottom': '⟓'
            })
        }),
        'halfwidth': Namespace(**{
            'left': Namespace(**{
                'top': '｢'
            }),
            'right': Namespace(**{
                'bottom': '｣'
            })
        }),
        'fullwidth': Namespace(**{
            'left': Namespace(**{
                'top': '「'
            }),
            'right': Namespace(**{
                'bottom': '」'
            }),
            'white': Namespace(**{
                'left': Namespace(**{
                    'top': '『'
                }),
                'right': Namespace(**{
                    'bottom': '』'
                })
            })
        }),
        'presentation': Namespace(**{
            'top': Namespace(**{
                'right': '﹁'
            }),
            'bottom': Namespace(**{
                'left': '﹂'
            }),
            'white': Namespace(**{
                'top': Namespace(**{
                    'right': '﹃'
                }),
                'bottom': Namespace(**{
                    'left': '﹄'
                })
            })
        })
    }),
    'image': Namespace(**{
        'left': '⦇',
        'right': '⦈'
    }),
    'binding': Namespace(**{
        'left': '⦉',
        'right': '⦊'
    }),
    'arc_inequality': Namespace(**{
        'left': '⦓',
        'right': '⦔',
        'double': Namespace(**{
            'left': '⦕',
            'right': '⦖'
        })
    }),
    'wiggly_fence': Namespace(**{
        'left': '⧘',
        'right': '⧙',
        'double': Namespace(**{
            'left': '⧚',
            'right': '⧛'
        })
    }),
    'paraphrase': Namespace(**{
        'low': Namespace(**{
            'left': '⸜',
            'right': '⸝'
        })
    }),
    'ogham_feather': Namespace(**{
        'left': '᚛',
        'right': '᚜'
    }),
    'gug_rtags': Namespace(**{
        'left': '༺',
        'right': '༻'
    }),
    'ang_khang': Namespace(**{
        'left': '༼',
        'right': '༽'
    }),
    'substitution': Namespace(**{
        'left': '⸂',
        'right': '⸃',
        'dotted': Namespace(**{
            'left': '⸄',
            'right': '⸅'
        })
    }),
    'transposition': Namespace(**{
        'left': '⸉',
        'right': '⸊'
    }),
    'omission_raised': Namespace(**{
        'left': '⸌',
        'right': '⸍'
    }),
    'sideways_u': Namespace(**{
        'left': '⸦',
        'right': '⸧'
    }),
    'prime_quotation_double': Namespace(**{
        'left': '〝',
        'right': '〞'
    }),
    'guillemet': Namespace(**{
        'left': '‹',
        'right': '›',
        'double': Namespace(**{
            'left': '«',
            'right': '»'
        })
    })
})
