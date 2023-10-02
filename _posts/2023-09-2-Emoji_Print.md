---
toc: true
comments: false
layout: post
title: Emoji Print
type: hacks
courses: { "compsci": {"week": 3} }
permalink: /emoji-print
---



```python
pip install emoji

```

    Collecting emoji
      Downloading emoji-2.8.0-py2.py3-none-any.whl (358 kB)
    [2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m358.9/358.9 kB[0m [31m9.7 MB/s[0m eta [36m0:00:00[0m
    [?25hInstalling collected packages: emoji
    Successfully installed emoji-2.8.0
    
    [1m[[0m[34;49mnotice[0m[1;39;49m][0m[39;49m A new release of pip is available: [0m[31;49m23.1.2[0m[39;49m -> [0m[32;49m23.2.1[0m
    [1m[[0m[34;49mnotice[0m[1;39;49m][0m[39;49m To update, run: [0m[32;49mpip3 install --upgrade pip[0m
    Note: you may need to restart the kernel to use updated packages.



```python
from emoji import emojize 
print(emojize(":thumbs_up: Jayden and Will are awesome! :grinning_face:"))
```

    👍 Jayden and Will are Awesome! 😀


    The line of code you provided is written in Python and appears to be using a library called "emoji" to work with emojis. Here's an explanation of what this code does:

## Code Explanation

1. `from emoji import emojize`: This line imports a specific function called `emojize` from the "emoji" library. The `emojize` function is used to convert emoji shortcodes (like `:thumbs_up:` and `:grinning_face:`) into their corresponding emoji characters.

2. `print(emojize(":thumbs_up: Jayden and Will are awesome! :grinning_face:"))`: This line calls the `emojize` function with a string as its argument. The string contains emoji shortcodes surrounded by colons, and it also includes some text ("Jayden and Will are awesome!").

   - `:thumbs_up:` is a shortcode for the thumbs-up emoji.
   - `:grinning_face:` is a shortcode for the grinning face emoji.

   The `emojize` function replaces these shortcodes with the actual emoji characters and returns the modified string.

   Finally, the `print` function is used to display the modified string (with emojis) in the console or terminal.

So, when you run this code, it will output a message with emojis in place of the shortcodes, like this:

```
👍 Jayden and Will are awesome! 😁
```

It's a simple example of how to use the "emoji" library in Python to add emojis to your text.