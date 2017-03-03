# **JavaScript in Easy Steps - Create Functions for the Web (5th Edition)**
## Mike McGrath

[Back to TOC](./THE BOOK ON JAVASCRIPT.md)

# CHAPTER 11 CREATING DYNAMIC EFFECTS
## Swapping backgrounds
## Toggling visibility
## Rotating image source
## Enlarging thumbnails
## Animating elements
## Summary<br>
   * The appearance of an object in an HTML document can be dynamically manipulated from JavaScript by
     assigning new values to its presentational DOM properties
   * All presentational DOM properties are contained within the __style__ property, which is a child of
     the object
   * A rollover effect can be created by assigning new values to an object's __style.background__ property
     in response to __mouseover__, __mousedown__, __mouseup__, and __mouseout__ events
   * A popup layer effect can be created by toggling an object's __style.visibility__ property between
     __hidden__ and __visible__ values
   * Images that are to appear in a slideshow can be preloaded into the browser's cache so they are 
     available when required
   * A slideshow effect can be created by sequentially assigning the path to an image file to an image
     object's __src__ property within a timer function
   * The original full-size version of a thumbnail image can be downloaded in response to a user action
   * The position of an object in an HTML document can be dynamically manipulated by assigning new values
     to its __style.left__ and __style.top__ DOM properties
   * An animation effect can be created by assigning new position values within a timer function to 
     continuously reposition an object on the page
   * The __style.left__ and __style.top__ values have a "px" suffix that must be removed before manipulating
     the numerical value
   * Current browser window size in pixels can be found in the __document.body.clientWidth__ property

***Souce Code for Chapter 11***
        <ul>
          <li><a href="src/11-Creating dynamic effects/rollover.html">Swapping backgrounds</a> -
            <a href="src/11-Creating dynamic effects/rollover.js"> js</a></li>
          <li><a href="src/11-Creating dynamic effects/toggle.html">Toggling visibility</a> -
            <a href="src/11-Creating dynamic effects/toggle.js"> js</a></li>
          <li><a href="src/11-Creating dynamic effects/slideshow.html">Rotating image source</a> -
            <a href="src/11-Creating dynamic effects/slideshow.js"> js</a></li>
          <li><a href="src/11-Creating dynamic effects/zoom.html">Enlarging thumbnails</a> -
            <a href="src/11-Creating dynamic effects/zoom.js"> js</a></li>
          <li><a href="src/11-Creating dynamic effects/animate.html">Animating elements</a> -
            <a href="src/11-Creating dynamic effects/animate.js"> js</a></li>
        </ul>