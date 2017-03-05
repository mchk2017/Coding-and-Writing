# **JavaScript in Easy Steps - Create Functions for the Web (5th Edition)**
## Mike McGrath

[Back to TOC](./THE BOOK ON JAVASCRIPT.md)

# CHAPTER 9 RESPONDING TO ACTIONS
## Reacting to window events
## Responding to button clicks
## Acknowledging key strokes
## Recognizing mouse moves
## Identifying focus
## Summary<br>
   * An event-handler function for a window event is nominated by assigning the function name to a 
     __window__ object property
   * When the browser fires an event it seeks an event-handler for that event and, if one exists, will
     execute its statements.
   * The load event is fired when the window has loaded a document and its event-handler is sought via
     the __window__ object's __onload__ property
   * The unload event is fired when the user navigates to a new location, or closes the browser, and its
     event-handler is sought via the __window__ object's __onunload__ property
   * A runtime error event passes three arguments to the event-handler nominated by the __window__ object's
     __onerror__ property describing the nature and script location of the error
   * Mouse button clock events seek event-handlers via the clicked object's __onclick__ and __ondblclick__
     properties, and also its __onmousedown__ and __onmouseup__ properties
   * Internet Explorer provides a __window.event__ object that has __event.keyCode__, __event.x__ and 
     __event.y__ properties storing key values and coordinates
   * Mozilla browsers pass __KeyboardEvent__ and __MouseEvent__ objects as arguments to the event-handler
     that have __which__, __pageX__ and __pageY__ properties storing key values and coordinates
   * Key stroke events can seek event-handlers via the __document__ object's __onkeydown__, __onkeypress__,
     and __onkeyup__ properties
   * Mouse movement events can seek event-handlers via the __onmousemove__, __onmouseover__, and __onmouseout__
     properties of the object which the pointer is moving
   * Focus events can seek event-handlers via an object's __onfocus__ and __onblur__ properties, and a statement
     can ensure an object receives the focus by calling that object's __focus()__ method.

***Source Code for Chapter 9***
        <ul>
          <li><a href="src/9-Responding to actions/onerror.html">Reacting to window events</a> -
            <a href="src/9-Responding to actions/onerror.js"> js</a></li>
          <li><a href="src/9-Responding to actions/onclick.html">Responding to button clicks</a> -
            <a href="src/9-Responding to actions/onclick.js"> js</a></li>
          <li><a href="src/9-Responding to actions/onkey.html">Acknowledging key strokes</a> -
            <a href="src/9-Responding to actions/onkey.js"> js</a></li>
          <li><a href="src/9-Responding to actions/onmouse.html">Recognizing mouse moves</a> -
            <a href="src/9-Responding to actions/onmouse.js"> js</a></li>
          <li><a href="src/9-Responding to actions/onfocus.html">Identifying focus</a> -
            <a href="src/9-Responding to actions/onfocus.js"> js</a></li>
        </ul>