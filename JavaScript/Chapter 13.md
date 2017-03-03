# **JavaScript in Easy Steps - Create Functions for the Web (5th Edition)**
## Mike McGrath

[Back to TOC](./THE BOOK ON JAVASCRIPT.md)

# CHAPTER 13 SCRIPTING MAGIC
## Dragging objects
## Storing information
## Passing messages
## Interacting with vectors
## Locating users
## Painting on canvas
## Swapping pixels
## Summary<br>
   * The __Drag-and-Drop API__ allows the user to drag page objects and drop them onto a target within the
     page – by scripting __ondragstart__, __ondragover__, and __ondrop__ event-handler functions
   * The __Web Storage API__ provides the ability to store user data – either permanently with its
     __localStorage__ object, or temporarily until the browser gets closed with its __sessionStorage__
	 object
   * The __Messageing API__ allows plain text messages to be sent securely between documents with its
     __postMessage()__ method – and the documents need not be on the same domain
   * Embedded __SVG__ graphics maintain a node tree of elements so can easily be made interactive or
     animated by scripting – after creating a reference with the __getSVGDocument()__ method
   * The __Geolocation API__ provides the ability to pin-point the user's location by estimating latitude
     and longitude coordinates – but only if the user consents to send information
   * The __Canvas 2D API__ provides properties and methods that allow JavaScript to paint shape and text
     onto a bitmap canvas area created by the HTML5 **<canvas\>** element
   * The Canvas 2D API can be used to manipulate pixel color via the **<data\>** property of its
     __CanvasPixelArray__ object

***Source Code for Chapter 13***
<ul>
  <li><a href="src/13-Scripting magic/dragndrop.html">Dragging objects</a> -
	<a href="src/13-Scripting magic/dragndrop.js"> js</a></li>
  <li><a href="src/13-Scripting magic/webstorage.html">Storing information</a> -
	<a href="src/13-Scripting magic/webstorage.js"> js</a></li>
  <li><a href="src/13-Scripting magic/msg-send.html">Passing messages</a> -
	<a href="src/13-Scripting magic/msg-receive.html">Passing messages (web server)</a>-
	<a href="src/13-Scripting magic/msg.js"> js</a></li>
  <li><a href="src/13-Scripting magic/interact.html">Interacting with vectors</a> -
	<a href="src/13-Scripting magic/interact.svg">Interacting with vectors (SVG)</a> -
	<a href="src/13-Scripting magic/interact.js"> js</a></li>
  <li><a href="src/13-Scripting magic/geolocation.html">Locating users</a> -
	<a href="src/13-Scripting magic/geolocation.js"> js</a></li>
  <li><a href="src/13-Scripting magic/canvas.html">Painting on canvas</a> -
	<a href="src/13-Scripting magic/canvas.js"> js</a></li>
  <li><a href="src/13-Scripting magic/pixel.html">Swapping pixels</a> -
	<a href="src/13-Scripting magic/pixel.js"> js</a></li>
</ul>