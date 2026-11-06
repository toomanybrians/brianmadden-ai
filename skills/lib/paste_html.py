"""Small fixes to rendered HTML so it survives being copied from the browser
and pasted into Substack's rich-text editor (the render.py files' whole
job: Brian copies the rendered page, or the emailed copy, into a draft).
"""

import re

# After a link, the space before the next word is the first character of the
# following text node. Rich-text editors are known to trim leading whitespace
# there on an HTML paste, which turns "[39 sources](...) today" into
# "39 sourcestoday" (Brian's examples, 2026-11-06). The generated markdown,
# the HTML and the email encoding were all checked and carry the space, so
# the loss happens at paste time. A non-breaking space is not collapsible
# whitespace, so it survives the paste and still reads as a space. Added only
# where a word, quote, bracket or inline tag follows, so a link followed by
# punctuation is left alone.
_SPACE_AFTER_LINK = re.compile(r"</a> (?=[^\s<]|<(?:strong|em|code|a|span)\b)")


def keep_space_after_links(html: str) -> str:
    return _SPACE_AFTER_LINK.sub("</a>&nbsp;", html)
