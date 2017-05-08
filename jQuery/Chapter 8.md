# **jQuery in Easy Steps - Create Dynamic Web Pages**
## Mike McGrath

[Back to TOC](THE%20BOOK%20ON%20JQUERY.md)

# CHAPTER 8 EMPLOYING AJAX
## Loading content
## Loading spans
## Testing loads
## Getting response
## Performing requests
## Serializing form data
## Handling failure
## Setting global handlers
## Summary<br>
   * Content of an element in a jQuery object can be replaced via AJAX by specifying a URL to that
     object's __load()__ method
   * A jQuery selector can be added after a space and the URL argument to the __load()__ method to specify a
     document portion
   * Optionally, a callback function can be specified as an additional argument to the __load()__ method, to be
     executed on completion
   * A callback function for the __load()__ method can receive the returned content, status, and XMLHttpRequest object
   * The __load()__ method uses the HTTP __GET__ and __POST__ methods to retrieve data from the server and to send
     data to the server
   * The jQuery __$.get()__ method uses the HTTP __GET__ method and can accept URL, data, callback, and data type arguments
   * The jQuery __$.post()__ method uses the HTTP __POST__ method and can accept URL, data, callback, and data type arguments
   * JavaScript objects can be retrieved by the jQuery __$.getJSON()__ method and scripts by the jQuery __$.getScript()__ method
   * Maximum control when performing AJAX requests is provided by the options of the jQuery __$.ajax()__ method
   * Form data can be prepared for submission as a string with the __serialize()__ method or as an array with 
     __serializeArray()__ method
   * Unlike __$.post()__ or __$.get()__ the jQuery __$.ajax()__ method provides the ability to execute a function when an
     AJAX call fails
   * Callback functions can be specified as __$.ajax()__ options to the AJAX "Local Events" __beforeSend__, __success__,
     __error__, and __complete__
   * Event-handlers can be specified to the AJAX "Global Events" __ajaxStart__, __ajaxSend__, __ajaxSuccess__, __ajaxComplete__, 
     and __ajaxStop__
   * Global event-handler functions must be specified as arguments to like-named methods attached to the __$(document)__ object

***Source Code for Chapter 8***
<ul>
  <li>Loading content: 
    <a href="src/htdocs/load.html">load</a> - 
    <a href="src/htdocs/load.txt"> txt</a></li>
  <li>Loading spans: 
    <a href="src/htdocs/loadspan.html">loadspan</a></li>
  <li>Testing loads: 
    <a href="src/htdocs/loadtest.html">loadtest</a></li>
  <li>Getting response: 
    <a href="src/htdocs/getpost.html">getpost</a> - 
    <a href="src/htdocs/getpost.txt"> txt</a> - 
    <a href="src/htdocs/getpost.js"> js</a> -
    <a href="src/htdocs/getpost.php"> php</a></li>
  <li>Performing requests: 
    <a href="src/htdocs/ajax.html">AJAX</a> - 
    <a href="src/htdocs/ajax.txt"> txt</a></li>
  <li>Serializing form data: 
    <a href="src/htdocs/serialform.html">serialform</a> - 
	<a href="src/htdocs/serialize.html"> serialize</a> -
    <a href="src/htdocs/serialize.php"> php</a></li>
  <li>Handling failure: 
    <a href="src/htdocs/successful.html">successful</a> - 
    <a href="src/htdocs/successful.php"> php</a></li>
  <li>Setting global handlers: 
    <a href="src/htdocs/global.html">global</a></li>
</ul>   