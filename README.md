# badsmoker
A python micro:bit v2 project to slow down bad habbits - press the button and get a bad noise if you are doing it too often. xmas project.

I am drinking beer as I write this, so do not take it seriously.  
I need to figure out if this can be unit tested or something and i can build a proper pipeline for micropython.  

# Concept for MVP
Take in buttons, count up and down, keep a timer, show something when interacting.  

# Concept for RC1:  

show me if ive had my last cigarette in under 15/30 minutes  

timers (beeps, waits, buttons, flashes) should be variables in case they are annoying.  

levels of bad - denoted by noise and flashing entire screen  
- \>45 minutes, good (center flash twice full bright) (two short hight beeps)  
- 30-45 mintues - bad, mild (outer pixels flash, half bright) (short low beep)  
- 15-30 minutes - very bad (all red flash, half bright) (low long beep)  
- less than 15 minutes very, very bad (all red flash twice (.5s on, .2s off, .6s on, full bright) (low long beep, two high/noisy short random bursts)  

if under 25 dots, counter displays number of dots, with randomly rotating disabled dots to match count  
if over 25 smokes today, scroll number, turn off for 3 seconds, scroll again  
after 1 minute, fade to min brightness  
after 3 minutes, disable display (deep sleep ? wakeup by gyro/brightness ?)  

button right - increase counter, beep with bad level  
if under 30 seconds since button right, if button left, twice in 3 seconds, silly beep (mid.2s-high.8s), hold down button for .5sec(?) to cancel last smoke, happy beep, update timer  

