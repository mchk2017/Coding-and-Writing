# **jQuery in Easy Steps - Create Dynamic Web Pages**
## Mike McGrath

[Back to TOC](THE%20BOOK%20ON%20JQUERY.md)

# CHAPTER 6 ATTACHING HANDLERS
## Binding to an event
## Binding multiple handlers
## Passing event data
## Triggering handlers
## Removing handlers
## Registering callbacks
## Deferring callbacks
## Keeping promises
## Summary<br>
   * Event-handlers can be bound to browser events by specifying event and handler name arguments to the
     __on()__ method
   * A handler function bound to an event with the __one()__ method will only execute the first time that
     event fires in the browser
   * Multiple event-handlers can be specified to the __one()__ method as a JavaScript object defining events
     and asssociated handlers
   * A data argument can be specified to the __on()__ method as a JavaScript object defining key:value pairs
     for the event object
   * Passing an event object to a handler enables stored values to be referenced using the event object's
     __data__ property and keys
   * An event-handler bound to an element in a jQuery object can be excuted remotely by calling the element's
     __trigger()__ method and can be removed by calling that elment's __off()__ method
   * A callback is a function passed as an argument to another function that can call back the received function
     later
   * The jQuery __$.Callbacks()__ constructor creates a Callbacks object list in which functions can be registered
     using its __add()__ method and subsequently executed using its __fire()__ method
   * The jQuery __$.Deferred()__ constructor creates a Deferred object in which callbacks can be specified indicating
     success or failure
   * A Deferred object's __resolve()__ method fires __done()__ upon success, its __reject()__ method fires __fail()__
     upon failure, and its __always()__ method always fires upon completion regardless of success
   * Calling a Deferred object's __state()__ method returns a string describing current state as "pending", "resolved",
     or "rejected"
   * A Deferred object's __promised()__ method returns a Promise object to which callbacks can be attached indicating
     success or failure
   * The jQuery __$.when()__ method accepts a Promise object argument so callback functions can be attached on completion

***Source Code for Chapter 6***
<ul>
  <li>
  <a href="src/bindhandler.html">Binding to an event</a></li>
  <li>
  <a href="src/multihandler.html">Binding multiple handlers</a></li>
  <li>
  <a href="src/datahandler.html">Passing event data</a></li>
  <li>
  <a href="src/triggerhandler.html">Triggering handlers</a></li>
  <li>
  <a href="src/removehandler.html">Removing handlers</a></li>
  <li>Registering callbacks: 
  <a href="src/simple.html">simple</a> - 
  <a href="src/callbacks.html">callbacks</a></li>
  <li>
  <a href="src/deferred.html">Deferring callbacks</a></li>
  <li>
  <a href="src/promise.html">Keeping promises</a></li>
</ul>   