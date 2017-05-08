# **jQuery in Easy Steps - Create Dynamic Web Pages**
## Mike McGrath

[Back to TOC](THE%20BOOK%20ON%20JQUERY.md)

# CHAPTER 1 GETTING STARTED
## Introducing jQuery
## Enabling jQuery
## Recognizing readiness
## Avoiding conflict
## Selecting by tag name
## Selecting by ID and class
## Selecting attributes and order
## Selecting family relatives
## Selecting multiple elements
## Filtering visibility
## Optimizing selections
## Summary<br>
   * jQuery is a lightweight multi-browser JavaScript library that makes it easier to incorporate
     JavaScript features on websites
   * jQuery can be enabled by hosting the minimized jQuery library file on your website or alternatively
     by indicating the library file's location online at the Google or Microsoft CDN
   * A jQuery statement typically contains a selector to return a collection of elements and an action
     to be performed on them
   * The __$( document ).ready()__ function gets called when the DOM has loaded and so can usefully contain
     an anonymous JavaScript function enclosing all jQuery statements
   * The __$()__ function syntax is a shortcut for the __jQuery()__ function that can be used instead, and if
     using __jQuery.noConflict()__
   * jQuery's most basic selectors specify elements by tag name __$( "p" )__, by ID __$( "#theId" )__, and
     by class __$( ".theClass" )__
   * jQuery __Attribute__ selectors select all elements containing a set attribute __$( "[lang]" )__ or those of
     set value __$( "[lang='fr']" )__
   * jQuery __Order__ selectors select elements according to their zero-based index position in a selected
     collection __$( "li:eq( 1 )" )__
   * jQuery __Child__ selectors select only all immediate children of a specified parent element, but not
     grandchildren __$( "ol > li" )__
   * jQuery __Descendant__ selectors select all hierarchy levels below a specific parent element, including
     grandchildren __$( "p span" )__
   * Multiple selection expressions can appear in a single jQuery selector as a comma-separated list
   * The * universal selector can be used with the __find()__ method to select all descendants of an 
     element __$( "body" ).find( "*" )__
   * Elements can be selected according to visibility with the 
     __filter()__ method __$( "body" ).find( "*" ).filter( ":hidden" )__

***Source Code for Chapter 1***
<ul>
  <li>Introducing jQuery</li>
  <li>Enabling jQuery</li>
  <li><a href="src/ready.html">Recognizing readiness</a></li>
  <li><a href="src/noconflict.html">Avoiding conflict</a></li>
  <li><a href="src/tagname.html">Selecting by tag name</a></li>
  <li><a href="src/identity.html">Selecting by ID</a> and 
     <a href="src/class.html">Selecting by class</a></li>
  <li><a href="src/attribute.html">Selecting attributes</a> and
     <a href="src/order.html">Selecting order</a></li>
  <li>Selecting family relatives: 
     <a href="src/descendant.html">descendant</a> - 
	 <a href="src/child.html">child</a></li>
  <li>Selecting multiple elements:
     <a href="src/multiple.html">multiple</a> - 
	 <a href="src/universal.html">universal</a></li>
  <li><a href="src/hidden.html">Filtering visibility</a></li>
  <li>Optimizing selections</li>
</ul>