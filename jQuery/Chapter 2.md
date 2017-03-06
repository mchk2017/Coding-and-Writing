# **jQuery in Easy Steps - Create Dynamic Web Pages**
## Mike McGrath

[Back to TOC](./THE BOOK ON JQUERY.md)

# CHAPTER 2 PERFORMING ACTIONS
## Traversing elements
## Moving along
## Visiting relatives
## Interrogating selections
## Applying styles
## Adding values
## Toggling classes
## Calculating sizes
## Summary<br>
   * Elements in a jQuery object can be iterated over using the object's __each()__ method and the element
     on the current iteration can be referenced using the __this__ keyword
   * The first element in a collection can be referenced by the __first()__ method and the last element by
     the __last()__ method
   * Following elements in the DOM tree can be referenced by the __next()__, __nextUntil()__, or __nextAll()__
     methods and previous elements by the __prev()__, __prevUntil()__, or __preAll()__ methods
   * Relative elements in the DOM tree can be referenced using __children()__, __siblings()__, __parent()__, or
     __parents()__ methods
   * A specified element can be sought in a jQuery collection by the __has()__ method, by the __is()__ method, or
     by the __not()__ method
   * A style property value of an element in a jQuery object can be retrieved or set using that object's __css()__ 
     method
   * Multiple styles of an element can be set when specified as a JavaScript (JSON) object argument to the
     __css()__ method
   * One or more classes can be added to an element in a jQuery object using that object's __addClass()__ method
     and may be removed using that object's __removeClass()__ method
   * A style class applied to an element can be switched (toggled) using its jQuery object's __toggleClass()__ method
   * A specified class can be sought in the element within a jQuery object by using that object's __hasClass()__ method
   * The dimensions of a box element, without padding or margin, can be retrieved in numeric format using its jQuery's
     object's __width()__ and __height()__ method
   * Overall dimensions of a box element, including padding and margin, can be retrieved in numeric format using its
     jQuery's object's __outerWidth()__ and __outerHeight()__ methods

***Source Code for Chapter 2***
<ul>
  <li>Traversing elements: 
    <a href="src/each.html">each</a> - 
    <a href="src/first.html">first</a></li>
  <li>Moving along: 
    <a href="src/next.html">next</a> - 
    <a href="src/until.html">until</a></li>
  <li>Visiting relatives: 
    <a href="src/children.html">children</a> - 
    <a href="src/parents.html">parents</a></li>
  <li>Interrogating selections: 
    <a href="src/interrogate.html">interrogate</a> - 
    <a href="src/not.html">not</a></li>
  <li>Applying styles: 
    <a href="src/getproperty.html">getproperty</a> - 
    <a href="src/setproperty.html">setproperty</a></li>
  <li>Adding values: 
    <a href="src/object.html">object</a> - 
    <a href="src/addclass.html">addclass</a></li>
  <li>Toggling classes: 
    <a href="src/toggleclass.html">toggleclass</a> - 
    <a href="src/removeclass.html">removeclass</a></li>
  <li>Calculating sizes: 
    <a href="src/size.html">size</a> - 
    <a href="src/overall.html">overall</a></li>
</ul>   


