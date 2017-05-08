# **JavaScript in Easy Steps - Create Functions for the Web (5th Edition)**
## Mike McGrath

<a href="THE BOOK ON JAVASCRIPT.md">Back to TOC</a>

# CHAPTER 7 REFERENCING THE WINDOW OBJECT
## Introducing the DOM
## Inspecting window properties
## Displaying dialog messages
## Scrolling and moving position
## Opening new windows
## Making a window timer
## Querying the browser
## Discovering what is enabled
## Controlling location
## Travelling through history
## Summary<br>
   * The Doument Object Model(DOM) is a hierarchial representation of all components of a web page
   * The __window__ object is the top level in the DOM hierarchy and has properties describing the
     browser window
   * The __screen__ object is a child of the __window__ object and has properties describing the 
     screen dimensions and color depth
   * Dialog messages can be displayed using the windos object's __alert()__, __confirm()__, and 
     __prompt()__ methods
   * A popup window can be created using the window object's __open()__ method but may be obstructed by
     a popup blocker
   * The window object's __setTimeout()__ method creates a timer, which can be cancelled later using the
     __clearTimeout()__ method
   * The __navigator__ object is a child of the __window__ object and has properties describing the browser
     and host platform versions
   * As the __window__ object exists in the global namespace all its child objects need not include that
     part of the address, so that __window.navigator__ can simply be referenced as __navigator__
   * The practice of browser detection by querying the __navigator__ properties is bad practice – feature
     detection should be used instead to ensure that DOM support exists
   * The __navigator.plugins__ and __navigator.mimeTypes__ properties are both arrays on Mozilla browsers,
     in which each element contains details of a supported feature
   * The __location__ object is a child of the __window__ object and has properties describing the address
     of the loaded document
   * The __history__ object is a child of the __window__ object that contains an array of visited locations
     in the current session and has methods to navigate along its elements

***Source Code for Chapter 7***
        <ul>
          <li><a href="src/7-Referencing the window object/dom.html">Introducing the DOM</a> -
            <a href="src/7-Referencing the window object/dom.js"> js</a></li>
          <li><a href="src/7-Referencing the window object/window.html">Inspecting window properties</a> -
            <a href="src/7-Referencing the window object/window.js"> js</a></li>
          <li><a href="src/7-Referencing the window object/dialog.html">Displaying dialog messages</a> -
            <a href="src/7-Referencing the window object/dialog.js"> js</a></li>
          <li><a href="src/7-Referencing the window object/scroll.html">Scrolling and moving position</a> -
            <a href="src/7-Referencing the window object/scroll.js"> js</a></li>
          <li><a href="src/7-Referencing the window object/popup.html">Opening new windows</a> -
            <a href="src/7-Referencing the window object/popup.js"> js</a></li>
          <li><a href="src/7-Referencing the window object/timer.html">Making a window timer</a> -
            <a href="src/7-Referencing the window object/timer.js"> js</a></li>
          <li><a href="src/7-Referencing the window object/browser.html">Querying the browser</a> -
            <a href="src/7-Referencing the window object/browser.js"> js</a></li>
          <li><a href="src/7-Referencing the window object/enabled.html">Discovering what is enabled</a> -
            <a href="src/7-Referencing the window object/enabled.js"> js</a></li>
          <li><a href="src/7-Referencing the window object/location.html">Controlling location</a> -
            <a href="src/7-Referencing the window object/location.js"> js</a></li>
          <li><a href="src/7-Referencing the window object/history-1.html">Travelling through history</a> -
            <a href="src/7-Referencing the window object/history.js"> js</a></li>
        </ul>