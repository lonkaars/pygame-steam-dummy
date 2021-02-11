# PyGame Steam dummy

This is a simple proof-of-concept steam message dummy for PyGame. This is also my first PyGame project so beware of spaghetti code!

![](screenshot.png)

## How to use in your own project

Rename main.py to steam_message.py and copy it and gradients.py into your own project folder.

```py
from steam_message import steam_message

...

# initialize the message
msg = steam_message(
		author = string,
		message = string,
		avatar = pygame.Surface,
		fonts = pygame.Font[3],
		frame = int,
		framerate = int,
		window = Surface
		)

# show message after 5 seconds
msg.starting_frame = 5 * framerate

...

while True: # drawloop
	# pygame boilerplate code left out

	msg.render(int(current_frame)) # call at the end of your drawloop to draw on top of everything else
```

Example usage is provided in `main.py > main()`

