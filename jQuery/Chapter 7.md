# **jQuery in Easy Steps - Create Dynamic Web Pages**
## Mike McGrath

[Back to TOC](./THE BOOK ON JQUERY.md)

# CHAPTER 7 PRODUCING EFFECTS
## Hiding elements
## Toggling elements
## Sliding elements
## Fading content
## Fading to levels
## Animating elements
## Stopping animations
## Handling queues
## Summary<br>
   * Visibility of an element in a jQuery object can be changed using that object's __hide()__ and __show()__
     methods
   * Animation effects must specify a duration argument, expressed in milliseconds or using the keywords "fast" 
     or "slow"
   * Optionally, a final callback function argument can be specified to be called on completion of an animation
     effect
   * The __toggle()__ method reverses the current CSS __display__ property or can accept a Boolean value to 
     explicitly determine visibility
   * The __slideUp()__, __slideDown()__, and __slideToggle()__ animation effect methods change the visible CSS
     __height__ property
   * The __fadeIn()__, __fadeOut()__, and fadeToggle()__ animation effect methods change the visible CSS __opacity__
     property
   * The level of opacity at which to stop fading is specified as an argument in the range 0.0 to 1.0 with the __fadeTo()__
     method
   * Any numeric CSS property of an element in a jQuery object can be dynamically changed by that object's __animate()__
     method
   * CSS properties and values are specified as key:value pairs in a JavaScript object as the first argument to the
     __animate()__ method
   * An animation currently running on an element object can be immediately stopped by calling that object's __stop()__
     method
   * The __stop()__ method can accept a pair of Boolean values to explicitly determine "clearQueue" and "jumpToEnd" properties
   * Multiple animations assigned to an element in a jQuery object get placed in a default queue named "fx"
   * The __length__property of the __queue()__ method contains an integer denoting the number of animations remaining
     in the queue
   * Queued animiations can be paused by the __delay()__ method and the entire queue can be terminated by the __finished()__ 
     method

***Source Code for Chapter 7***
<ul>
  <li>
  <a href="src/visibility.html">Hiding elements</a></li>
  <li>
  <a href="src/toggle.html">Toggling elements</a></li>
  <li>
  <a href="src/slide.html">Sliding elements</a></li>
  <li>
  <a href="src/fade.html">Fading content</a></li>
  <li>
  <a href="src/fadeto.html">Fading to levels</a></li>
  <li>
  <a href="src/animate.html">Animating elements</a></li>
  <li>
  <a href="src/stop.html">Stopping animations</a></li>
  <li>
  <a href="src/queue.html">Handling queues</a></li>
</ul>   