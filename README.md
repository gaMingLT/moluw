
# MoLuW (Metatwin on Linux using Wine)

![MoLuw Logo](logo.png)

This project is a result of integrating the Metatwin script into a R&D project concerning payload crafting, during my internship at [NVISO](https://www.nviso.eu/). Some of the logic was built into that project, but I have since "expanded" on this a little.

## Requirements

### Docker

If you build the docker container without adjusting the Docker file, no target executable will be present. The ``ADExplorer64.exe`` binary has been placed inside the repo and is copied over on building the container, this can be replaced by changing the Docker file.

Build the docker container:
```bash
docker build . -t moluw
```

Run and enter the container:
```bash
docker run -it moluw bash
```

This should have you enter the ``/usr/app/tools`` directory, where all of the required scripts and executables have been located.


### System

Required System Packages
- python3 
- python3-pip 
- wine 
- xvfb 
- openssl 
- wine32:i386

<!-- Python Packages
- pefile 
- distorm3 
- pycrypt  -->


Add the correct architecture:
```bash
sudo dpkg --add-architecture i386
```

The required packages:
```bash
sudo apt-get -y update && apt-get -y install python3 python3-pip wine xvfb openssl wine32:i386
```

<!-- Install the correct python packages:
```
python3 -m pip install pefile distorm3 pycrypt
``` -->

## Usage

The current script has the options as showcased in the image available,  you specify the source binary, target binary and if you would like to sign the executable.

```
usage: Metatwin Linux [-h] -s SOURCE -t TARGET [-si]

optional arguments:
  -h, --help            show this help message and exit
  -s SOURCE, --source SOURCE
                        Source (binary) of where to extract resources and signature from.
  -t TARGET, --target TARGET
                        Target of where to copy resources and signature to.
  -si, --sign           Sign the target binary.
```

Executing the script:
```bash
python3 metatwin.py -s source-bin.exe -t target-bin.exe -si
```

Depending on if you copied only resources and signature or only resources, the naming of the executables will be different:
- ``<executable-name>_signed`` (resources & signed)
- ``executable_written.ex`` (resources only)

Copy the resulting executable back to the system:
```bash
docker cp <image-name>:<path-to-executable> <name-executable-on-system>
```

## TODO
- Add proper extracting of signature information from copied over signature to target binary
- Turn down wine error's in console using ``export "WINEDEBUG=-all"'``
- Add bash script for installing dependencies on Linux system
- Add option for when running on GUI distribution
- Remove dependency on ``ResourceHacker.exe`` and ``wine``, find Linux compatible alternative
