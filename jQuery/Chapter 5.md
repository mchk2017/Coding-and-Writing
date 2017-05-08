# **jQuery in Easy Steps - Create Dynamic Web Pages**
## Mike McGrath

[Back to TOC](THE%20BOOK%20ON%20JQUERY.md)

# CHAPTER 5 RECOGNIZING EVENTS
## Detecting clicks
## Feeling pressure
## Detecting presence
## Guarding borders
## Spotting movement
## Detecting keys
## Adjusting size
## Scrolling around
## Summary<br>
   * Click events on an element in a jQuery object can be recognized by that object's __click()__ and
     __dbclick()__ methods
   * An event-handler can be specified as an argument to those methods that recognize events to provide
     dynamic responses
   * An event can be fired by specifying its name within quote marks as an argument to a jQuery object's
     __trigger()__ method
   * Mouse button events that occur while over an element can be recognized by the __mousedown()__ and
     __mouseup()__ methods
   * Mouse movement events that occur over an element can be recognized by the __mouseover()__, 
   * __mouseout()__, __mouseenter()__, __mouseleave()__, and __mousemove()__ methods
   * An event can be passed to an event-handler as an argument and multiple values can be specified in
     a JavaScript object
   * A value in a JavaScript object passed to an event-handler can be referenced by their associated key
     with the __data__ property
   * The mousemove object has __pageX__ and __pageY__ properties that contain cursor position relative to
     the top left of the document
   * Key events of an element in a jQuery object can be recognized by that object's __keypress()__, 
     __keydown()__, and __keyup()__ methods
   * Key events passed to the __keypress()__ method have a __which__ property that contains a Character Code
     numeric value
   * Key events passed to the __keydown()__ and __keyup()__ methods have a __which__ property that contains
     a Key Code numeric value
   * Resize events are sent to the DOM __window__ object and can be recognized by that object's __resize()__ 
     method
   * Scroll events of an element in a jQuery object can be recognized by that object's __scroll()__ method
   * The offset position of a scrolled element in a jQuery object can be revealed by calling its __scrollLeft()__
     and __scrollTop()__ methods

***Source Code for Chapter 5***
<ul>
  <li>Detecting clicks: 
  <a href="src/click.html">click</a> - 
  <a href="src/triggerclick.html">triggerclick</a></li>
  <li>Feeling pressure: 
  <a href="src/mousebutton.html">mousebutton</a> - 
  <a href="src/triggermousedown.html">triggermousedown</a></li>
  <li>Detecting presence: 
  <a href="src/mouseover.html">mouseover</a> - 
  <a href="src/eventdata.html">eventdata</a></li>
  <li>Guarding borders: 
  <a href="src/mouseenter.html">mouseenter</a> - 
  <a href="src/eventbubble.html">eventbubble</a></li>
  <li>Spotting movement: 
  <a href="src/mousemove.html">mousemove</a> - 
  <a href="src/mousetrack.html">mousetrack</a></li>
  <li>Detecting keys: 
  <a href="src/keypress.html">keypress</a> - 
  <a href="src/keydown.html">keydown</a></li>
  <li>Adjusting size: 
  <a href="src/resize.html">resize</a></li>
  <li>Scrolling around: 
  <a href="src/scroll.html">scroll</a> - 
  <a href="src/scrollaxis.html">scrollaxis</a></li>
</ul>   
