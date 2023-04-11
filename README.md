# raspi-powerbuttond

Power button control for Raspberry pi.

Configurable GPIO pin, reboot time and halt time.

See `raspi-powerbuttond --help` for the options and their defaults.


## Development

There's `gpiozero.py` stub to shut up LSP server in Neovim.  Should be replaced with an emulator or something, but for now, it's Good Enough™

This file should _not_ be copied over to the Raspberry Pi you'll be running on.


## Install

Copy the `raspi-powerbuttond` script somewhere on the file system of the Raspberry Pi and make sure it's executable.  In `/etc/rc.local` add the line `sudo /path/to/raspi-powerbuttond &` and the power button control will be available next time you boot.  Alternatively, this can be set up via systemd.  I still need to look into this myself.
