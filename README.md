# codrone-drone-show
make crappy educational drones do drone show 

Browser-only build for CoDrone EDU using Python for Robolink (Browser IDE).
One drone per device, 15 devices running at once for the show.
3 groups of 5, each with its own recipe, all merging into one shared
finale partway through.
 
## Folder layout
 
```
shared/
  main.py          the file you click Run on, same on all 15 machines
  show_lib.py      LED effects and the safety abort, same everywhere
  shared_cues.py   the merge finale, same everywhere
 
group_a/
  template.py      warm ripple recipe, same on all 5 of group A's machines
  a1/cues.py       position 1, front row
  a2/cues.py
  a3/cues.py
  a4/cues.py
  a5/cues.py       position 5, back row
 
group_b/
  template.py      cool spin recipe
  b1/cues.py ... b5/cues.py
 
group_c/
  template.py      gradient riser recipe
  c1/cues.py ... c5/cues.py
```
 
Position 1 is the front row, closest to the audience. Position 5 is the
back row, against the back wall. Back rows fly a bit higher so they stay
visible over the front rows.
 
## Setting up one device
 
Example: this device is drone A3.
 
1. Create `main.py`, `show_lib.py`, and `shared_cues.py`, and paste in the
   contents from `shared/`.
2. Create `template.py` and paste in `group_a/template.py`.
3. Create `cues.py` and paste in `group_a/a3/cues.py`. It's one line:
   `cues = build_cues(position=3)`.
4. Connect the controller and click Run on `main.py`.
Every machine in the same group runs the same `template.py`. Only the
position number in `cues.py` changes.
 
## Why it's not 15 separate scripts
 
Each group's look is written once as a function of position in that
group's `template.py`. Change the ripple timing or the colors there once,
copy the file back to that group's 5 machines, and all 5 update together.
 
## Devices needed
 
One Chromebook per drone, running at the same time, for a live show with
everything in the air at once. The browser tool connects to one controller
per session, so there's no way to fly more than one drone from a single
Chromebook here. With fewer devices, fall back to a wave structure:
groups perform and land in sequence instead of flying together.
 
## Starting the show
 
Every operator hits Run at roughly the same moment. `main.py` prints its
own 3-2-1-GO countdown, then each drone runs off its own clock from there.
 
## Safety
 
Each drone checks its own front sensor between cues and lands itself if
something gets too close. The IDE's Stop and Land buttons are still the
final backup for any operator at any time.