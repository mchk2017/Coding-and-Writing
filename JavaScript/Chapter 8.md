# **JavaScript in Easy Steps - Create Functions for the Web (5th Edition)**
## Mike McGrath

[Back to TOC](./THE BOOK ON JAVASCRIPT.md)

# CHAPTER 8 INTERACTING WITH THE DOCUMENT
## Extracting document info
## Addressing component arrays
## Addressing components direct
## Setting and retrieving cookies
## Writing with JavaScript
## Summary<br>
   * The __document__ object is a child of the top-level __window__ object and has properties describing
     the HTML document
   * When the HTML document has been reached by the user following a hyperlink, the URL of the page
     containing the link is available in the __document.referrer__ property
   * The value specified by the HTML __&lt;title&gt;__ element is also available from the __document.title__ property
   * The current location can be found in the __document.URL__ property and the domain in the __document.domain__
     property
   * In the DOM the __document__ object has __forms__, __anchors__, __images__, and __links__ component arrays
   * A __document.forms__ array has its own child __elements__ array that can be used to reference a form's
     components
   * The __document.getElementById()__ method accepts an __id__ of an HTML element attribute to reference that
     element without regard to the DOM hierarchy
   * An array of all HTML elements of a specified tagname is returned by the __document.getElementsByTagName()__ method
   * Cookies store up to 4KB of data on the user's computer and may optionally specify an expiry date
   * Cookie data is stored as name=value pairs and the __escape()__ method should be used to convert whitespace,
     commas, and semi-colons to Unicode format
   * Retrieved cookie data can be converted from Unicode by the __unescape()__ method and separated by the
     string __split()__ method
   * Changes to the __innerHTML__ property of a document object are processed by the HTML parser and the DOM tree is updated
   * Calling __document.write()__ after the HTML document has loaded opens a new document in which to write content

***Source Code for Chapter 8***
        <ul>
          <li><a href="src/8-Interacting with the document/info-1.html">Extracting document info</a> -
            <a href="src/8-Interacting with the document/info.js"> js</a></li>
          <li><a href="src/8-Interacting with the document/components.html">Addressing component arrays</a> -
            <a href="src/8-Interacting with the document/components.js"> js</a></li>
          <li><a href="src/8-Interacting with the document/direct.html">Addressing components direct</a> -
            <a href="src/8-Interacting with the document/direct.js"> js</a></li>
          <li><a href="src/8-Interacting with the document/cookie.html">Setting and retrieving cookies</a> -
            <a href="src/8-Interacting with the document/cookie.js"> js</a></li>
          <li><a href="src/8-Interacting with the document/write.html">Writing with JavaScript</a> -
            <a href="src/8-Interacting with the document/write.js"> js</a></li>
        </ul>
