# Image intensity analyzer
Matplotlib based script for fast &amp; easy image intensity plotting

## Motivation
The program was created during Polish Children Fund (http://fundusz.org/x/en/) workshop at Institute of Physics Polish Academy of Sciences (http://www.ifpan.edu.pl/index_en.php). During the workshop my team was analyzing reflection high-energy electron diffraction (rheed, https://en.wikipedia.org/wiki/Reflection_high-energy_electron_diffraction) pictures of thin films samples created in molecular beam epitaxy process (https://en.wikipedia.org/wiki/Molecular_beam_epitaxy).

## What it actually do
The program shows animation of intensity distribution in subsequent ,,slices'' of image i.e. horizontal lines each with bigger and bigger y coordinate.
![Alt text](/rheed.bmp)
![Alt text](/screenshot.png)

## Usage
``` python
python analize.py -i <path/to/image>
```
Take a screenshot at given y 
``` python
python analize.py -i <path/to/image> -p <y>
```

Help
``` python
python analize.py -h
```
