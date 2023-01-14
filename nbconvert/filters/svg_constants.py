"""SVG constants for sanitization."""
# These are lifted from html5lib's sanitizer module, which is deprecated.
#
# Quoth the migration guide (https://github.com/mozilla/bleach/blob/main/docs/migrating.rst#different-allow-lists):
#
# > If you want to stick to the html5lib sanitizer's allow lists, get them from the sanitizer code.
# > It's probably best to copy them as static lists.

# TODO: Bleach currently drops attribute namespaces; cleaning SVGs will probably require more elbow grease.
#       See https://github.com/mozilla/bleach/issues/362

ALLOWED_SVG_TAGS = {
    "a",
    "animate",
    "animateColor",
    "animateMotion",
    "animateTransform",
    "circle",
    "clipPath",
    "defs",
    "desc",
    "ellipse",
    "font-face",
    "font-face-name",
    "font-face-src",
    "g",
    "glyph",
    "hkern",
    "line",
    "linearGradient",
    "marker",
    "metadata",
    "missing-glyph",
    "mpath",
    "path",
    "polygon",
    "polyline",
    "radialGradient",
    "rect",
    "set",
    "stop",
    "svg",
    "switch",
    "text",
    "title",
    "tspan",
    "use",
}
ALLOWED_SVG_ATTRIBUTES = {
    "accent-height",
    "accumulate",
    "additive",
    "alphabetic",
    "arabic-form",
    "ascent",
    "attributeName",
    "attributeType",
    "baseProfile",
    "bbox",
    "begin",
    "by",
    "calcMode",
    "cap-height",
    "class",
    "clip-path",
    "color",
    "color-rendering",
    "content",
    "cx",
    "cy",
    "d",
    "descent",
    "display",
    "dur",
    "dx",
    "dy",
    "end",
    "fill",
    "fill-opacity",
    "fill-rule",
    "font-family",
    "font-size",
    "font-stretch",
    "font-style",
    "font-variant",
    "font-weight",
    "from",
    "fx",
    "fy",
    "g1",
    "g2",
    "glyph-name",
    "gradientUnits",
    "hanging",
    "height",
    "horiz-adv-x",
    "horiz-origin-x",
    "id",
    "ideographic",
    "k",
    "keyPoints",
    "keySplines",
    "keyTimes",
    "lang",
    "marker-end",
    "marker-mid",
    "marker-start",
    "markerHeight",
    "markerUnits",
    "markerWidth",
    "mathematical",
    "max",
    "min",
    "name",
    "offset",
    "opacity",
    "orient",
    "origin",
    "overline-position",
    "overline-thickness",
    "panose-1",
    "path",
    "pathLength",
    "points",
    "preserveAspectRatio",
    "r",
    "refX",
    "refY",
    "repeatCount",
    "repeatDur",
    "requiredExtensions",
    "requiredFeatures",
    "restart",
    "rotate",
    "rx",
    "ry",
    "slope",
    "stemh",
    "stemv",
    "stop-color",
    "stop-opacity",
    "strikethrough-position",
    "strikethrough-thickness",
    "stroke",
    "stroke-dasharray",
    "stroke-dashoffset",
    "stroke-linecap",
    "stroke-linejoin",
    "stroke-miterlimit",
    "stroke-opacity",
    "stroke-width",
    "style",
    "systemLanguage",
    "target",
    "text-anchor",
    "to",
    "transform",
    "type",
    "u1",
    "u2",
    "underline-position",
    "underline-thickness",
    "unicode",
    "unicode-range",
    "units-per-em",
    "values",
    "version",
    "viewBox",
    "visibility",
    "width",
    "widths",
    "x",
    "x-height",
    "x1",
    "x2",
    "xlink:actuate",
    "xlink:arcrole",
    "xlink:href",
    "xlink:role",
    "xlink:show",
    "xlink:title",
    "xlink:type",
    "xml:base",
    "xml:lang",
    "xml:space",
    "y",
    "y1",
    "y2",
    "zoomAndPan",
}
