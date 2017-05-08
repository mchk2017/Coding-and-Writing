# **JavaScript in Easy Steps - Create Functions for the Web (5th Edition)**
## Mike McGrath

<a href="THE BOOK ON JAVASCRIPT.md">Back to TOC</a>

# CHAPTER 12 PRODUCING WEB APPS
## Introducing AJAX
## Sending an HTTP request
## Using response text
## Using XML response data
## Creating a web application
## Providing application data
## Programming the application
## Running the web application
## Summary<br>
   * AJAX is an acronym for "Asynchronous JavaScript And XML" and incorporates HTML, CSS, the DOM,
     JavaScript and asynchronous data retrieval by the __XMLHttpRequest__ object
   * Requests are sent from the web browser to the web server via HyperText Transfer Protocol, or
     "HTTP" for short
   * Responses are also sent from the web server to the web browser via HTTP
   * An AJAX engine acts as an intermediary in the request/response cycle allowing the interface to
     be dynamically updated without a page reload
   * The DOM's __XMLHttpRequest__ object is at the core of AJAX
   * Each __XMLHttpRequest__ object has a __readystate__ property that gets assigned numeric values
     at each stage of a request
   * An __onreadystatechange__ property nominates an event handler to process a completed response
   * A successfully-completed response is signified when an __XMLHttpRequest__ object's __readystate__
     is 4 and its __status__ is 200
   * When an AJAX engine successfully requests text, the content is placed in the __XMLHttpRequest__
     object's __responseText__ property
   * When an AJAX engine successfully requests XML, the content is placed in the __XMLHttpRequest__
     object's __responseXML__ property
   * XML data stored in the __responseXML__ property represents the XML elements as nodes
   * Each node has a __firstChild__ property, which is the text node of the element, but the actual text
     within the XML element is contained in the __firstChild.data__ property
   * All XML elements of a particular name can be assigned to an array variable using the __getElementsByTagName()__
     method of the __XMLHttpRequest__ object's __responseXML__ property

***Source Code for Chapter 12***
<ul>
  <li>Introducing AJAX</li>
  <li><a href="src/12-Producing web apps/http-request.html">Sending a HTTP request</a> -
	<a href="src/12-Producing web apps/http-request.js"> js</a> -
	<a href="src/12-Producing web apps/data.txt"> txt</a></li>
  <li><a href="src/12-Producing web apps/request-text.html">Using response text</a> -
	<a href="src/12-Producing web apps/request-text.js"> js</a></li>
  <li><a href="src/12-Producing web apps/request-xml.html">Using XML response data</a> -
	<a href="src/12-Producing web apps/request-xml.js"> js</a> -
	<a href="src/12-Producing web apps/data.xml"> xml</a></li>
  <li>Creating a web application</li>
  <li>Programming the application</li>
  <li><a href="src/12-Producing web apps/ajax.html">Running the web application</a> -
	<a href="src/12-Producing web apps/ajax.js"> js</a> -
	<a href="src/12-Producing web apps/ajax.xml"> xml</a></li>
</ul>