# ecal_sep

Trying to classifiy photon or merge-photon response of electronic calorimeter. Calorimeter - set of pixels, responce - square 5*5.
We take it and create features.

Every event describe by ROOT-file.
Every element in ROOT - tuple describing a hit of one (or merged) particle: center cell in calorimeter(elem 6,7), area(elem 5), 
squares 5*5 around center cell (two, for main and PS-calorimeter: 8,9), event ID(0), energy of square(1), photon hypothesis(10).

**models/** - An attempt to wrap XGB to custom class

**utils/** Preprocessing
We have a Electronic and Pre-shower Calorimeter:
https://docs.google.com/document/d/1ZD6YeYcOv8fUM4BvnXNWvFzxNuRRHUUvOUirDCFHZ5Y/edit?usp=sharing

There are 3 areas with different granularity. Every area has its own size in pixels, own bound in pixels.
For example, area1 https://docs.google.com/document/d/1c-8ayyhAFun8rmGjIX-tZiBh-nncIQ-pNCMOpQWwo5k/edit?usp=sharing
has outer bound (12, 51) - on x; (0, 63) - on y.

The granularity relations is 3:2:1 as area2:area1:area0

If square lay in any area totaly - means square not extends beyond the inner and outer bound of area - we only check energy and hyposesis.
If extends, use 
**reconstruct_new**(cell_x, cell_y, distance_, axis, area_bound, n_area_bound, ecal_square, ps_square, n_ecal_data, n_ps_data, type_='norm')
  
  distance_ - distance between center cells and bound (for 5*5 square it may be 1 or 2)
  
  axis - top, bottom, left or right side. 
  
  area_bound - host area, 
  
  n_area_bound - neighbour area
  
  n_ecal_data, n_ps_data - tuples as (x,y, energy) for neighbour area.
  
  type_='norm' or "inv" - must we recount to larger or smaller cells (in or out)
  
 We recover missing row or column of square 5_5 by def **make_vector_*()**
 and rewrite inital not-full square by def **assigment_*()**
  multiplayer, devider - coefficient to recount cells.
  
  
  Middle, Inner, Outer - classes of different areas.
