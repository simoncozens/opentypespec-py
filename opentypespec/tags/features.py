FEATURE_TAGS = {
    "aalt": {"name": "Access All Alternates"},
    "abvf": {"name": "Above-base Forms"},
    "abvm": {"name": "Above-base Mark Positioning"},
    "abvs": {"name": "Above-base Substitutions"},
    "afrc": {"name": "Alternative Fractions"},
    "akhn": {"name": "Akhand"},
    "blwf": {"name": "Below-base Forms"},
    "blwm": {"name": "Below-base Mark Positioning"},
    "blws": {"name": "Below-base Substitutions"},
    "c2pc": {"name": "Petite Capitals From Capitals"},
    "c2sc": {"name": "Small Capitals From Capitals"},
    "calt": {"name": "Contextual Alternates"},
    "case": {"name": "Case-Sensitive Forms"},
    "ccmp": {"name": "Glyph Composition/Decomposition"},
    "cfar": {"name": "Conjunct Form After Ro"},
    "chws": {"name": "Contextual Half-width Spacing"},
    "cjct": {"name": "Conjunct Forms"},
    "clig": {"name": "Contextual Ligatures"},
    "cpct": {"name": "Centered CJK Punctuation"},
    "cpsp": {"name": "Capital Spacing"},
    "cswh": {"name": "Contextual Swash"},
    "curs": {"name": "Cursive Positioning"},
    "dist": {"name": "Distances"},
    "dlig": {"name": "Discretionary Ligatures"},
    "dnom": {"name": "Denominators"},
    "dtls": {"name": "Dotless Forms"},
    "expt": {"name": "Expert Forms"},
    "falt": {"name": "Final Glyph on Line Alternates"},
    "fin2": {"name": "Terminal Form #2"},
    "fin3": {"name": "Terminal Form #3"},
    "fina": {"name": "Terminal Forms"},
    "flac": {"name": "Flattened accent forms"},
    "frac": {"name": "Fractions"},
    "fwid": {"name": "Quarter Widths"},
    "half": {"name": "Half Forms"},
    "haln": {"name": "Halant Forms"},
    "halt": {"name": "Alternate Half Widths"},
    "hist": {"name": "Historical Forms"},
    "hkna": {"name": "Horizontal Kana Alternates"},
    "hlig": {"name": "Historical Ligatures"},
    "hngl": {"name": "Hangul"},
    "hojo": {"name": "Hojo Kanji Forms (JIS X 0212-1990 Kanji Forms)"},
    "hwid": {"name": "Half Widths"},
    "init": {"name": "Initial Forms"},
    "isol": {"name": "Isolated Forms"},
    "ital": {"name": "Italics"},
    "jalt": {"name": "Justification Alternates"},
    "jp04": {"name": "JIS04 Forms"},
    "jp78": {"name": "JIS78 Forms"},
    "jp83": {"name": "JIS83 Forms"},
    "jp90": {"name": "JIS90 Forms"},
    "kern": {"name": "Kerning"},
    "lfbd": {"name": "Left Bounds"},
    "liga": {"name": "Standard Ligatures"},
    "ljmo": {"name": "Leading Jamo Forms"},
    "lnum": {"name": "Lining Figures"},
    "locl": {"name": "Localized Forms"},
    "ltra": {"name": "Left-to-right glyph alternates"},
    "ltrm": {"name": "Left-to-right mirrored forms"},
    "mark": {"name": "Mark Positioning"},
    "med2": {"name": "Medial Forms #2"},
    "medi": {"name": "Medial Forms"},
    "mgrk": {"name": "Mathematical Greek"},
    "mkmk": {"name": "Mark to Mark Positioning"},
    "mset": {"name": "Mark Positioning via substitution"},
    "nalt": {"name": "Alternate Annotation Forms"},
    "nlck": {"name": "NLC Kanji Forms"},
    "nukt": {"name": "Nukta Forms"},
    "numr": {"name": "Numerators"},
    "onum": {"name": "Oldstyle Figures"},
    "opbd": {"name": "Optical Bounds"},
    "ordn": {"name": "Ordinals"},
    "ornm": {"name": "Ornaments"},
    "palt": {"name": "Proportional Alternate Widths"},
    "pcap": {"name": "Petite Capitals"},
    "pkna": {"name": "Proportional Kana"},
    "pnum": {"name": "Proportional Figures"},
    "pref": {"name": "Pre-base Forms"},
    "pres": {"name": "Pre-base Substitutions"},
    "pstf": {"name": "Post-base Forms"},
    "psts": {"name": "Post-base Substitutions"},
    "pwid": {"name": "Proportional Widths"},
    "qwid": {"name": "Quarter Widths"},
    "rand": {"name": "Randomize"},
    "rclt": {"name": "Required Contextual Alternates"},
    "rkrf": {"name": "Rakar Forms"},
    "rlig": {"name": "Required Ligatures"},
    "rphf": {"name": "Reph Form"},
    "rtbd": {"name": "Right Bounds"},
    "rtla": {"name": "Right-to-left alternates"},
    "rtlm": {"name": "Right-to-left mirrored forms"},
    "ruby": {"name": "Ruby Notation Forms"},
    "rvrn": {"name": "Required Variation Alternates"},
    "salt": {"name": "Stylistic Alternates"},
    "sinf": {"name": "Scientific Inferiors"},
    "size": {"name": "Optical size"},
    "smcp": {"name": "Small Capitals"},
    "smpl": {"name": "Simplified Forms"},
    "ssty": {"name": "Math script style alternates"},
    "stch": {"name": "Stretching Glyph Decomposition"},
    "subs": {"name": "Subscript"},
    "sups": {"name": "Superscript"},
    "swsh": {"name": "Swash"},
    "titl": {"name": "Titling"},
    "tjmo": {"name": "Trailing Jamo Forms"},
    "tnam": {"name": "Traditional Name Forms"},
    "tnum": {"name": "Tabular Figures"},
    "trad": {"name": "Traditional Forms"},
    "twid": {"name": "Third Widths"},
    "unic": {"name": "Unicase"},
    "valt": {"name": "Alternate Vertical Metrics"},
    "vatu": {"name": "Vattu Variants"},
    "vchw": {"name": "Vertical Contextual Half-width Spacing"},
    "vert": {"name": "Vertical Alternates"},
    "vhal": {"name": "Alternate Vertical Half Metrics"},
    "vjmo": {"name": "Vowel Jamo Forms"},
    "vkna": {"name": "Vertical Kana Alternates"},
    "vkrn": {"name": "Vertical Kerning"},
    "vpal": {"name": "Proportional Alternate Vertical Metrics"},
    "vrt2": {"name": "Vertical Alternates and Rotation"},
    "vrtr": {"name": "Vertical Alternates for Rotation"},
    "zero": {"name": "Slashed Zero"},
}

for r in range(1, 100):
    FEATURE_TAGS["cv%02i" % r] = {"name": "Character variant %i" % r}
for r in range(1, 21):
    FEATURE_TAGS["ss%02i" % r] = {"name": "Stylistic Set %i" % r}