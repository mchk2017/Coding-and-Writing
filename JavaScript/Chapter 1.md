# **JavaScript in Easy Steps - Create Functions for the Web (5th Edition)**
## Mike McGrath

<a href="THE BOOK ON JAVASCRIPT.md">Back to TOC</a>

# CHAPTER 1 GETTING STARTED
## Introduction
## JavaScript keywords
## Including inline script
## Caling head section script
## Embedding external script
## Accelerating initialization
## Storing data in variables
## Passing function arguments
## Recognizing variable scope
## Summary<br>
   * JavaScript is a client-side, object-based, case-sensitive interpreted scripting language whose
     interpreter is embedded in web browser software
   * Variable names and function names must avoid the JavaScript keywords, reserved words, and 
     built-in or DOM object names
   * For JavaScript code each opening HTML **&lt;script&gt;** tag must specify the MIME type of "text/javascript"
     to its __type__ attribute
   * Script blocks may include single-line and multi-line comments
   * Each JavaScript statement must be terminated by a semi-colon
   * Inline JavaScript code can be assigned to any HTML event attribute, such as __onload__, or enclosed 
     within a  **&lt;script&gt;** element in the document body section – but is best avoided
   * All JavaScript code is best located in an external file whose path is specified to an __src__ attribute
     of the  **&lt;script&gt;** tag
   * Unobtrusive JavaScript places all script code in an external file and can specify a function to the
     __DOMContentLoaded__ event to set behaviours when the entire page content has loaded
   * The __window.onload__ event can be used to set behaviours for older browsers when the entire page
     content has loaded
   * JavaScript variables are declared using the __var__ keyword and can store any data type – boolean,
     number, string, function, or object
   * JavaScript functions are declared using the __function__ keyword and the function name must have
     trailing parentheses (), followed by a pair of {} braces enclosing statements to execute
   * A function declaration may specify arguments within its trailing parentheses () that must be passed
     from its caller
   * A value can be returned to the caller using the __return__ keyword
   * Unlike global variables declared in the main script body, local variables declared inside a function
     are only accessible from within that function

***Source Code for Chapter 1***
<ul>
  <li>Introduction</li>
  <li>JavaScript keywords</li>
  <li><a href="src/1-Getting started/inline.html">Including inline script</a></li>
  <li><a href="src/1-Getting started/head.html">Calling head section script</a></li>
  <li><a href="src/1-Getting started/external.html">Embedding external script</a> -
	<a href="src/1-Getting started/external.js"> js</a></li>
  <li><a href="src/1-Getting started/variable.html">Storing data in variables</a> -
	<a href="src/1-Getting started/variable.js"> js</a></li>
  <li><a href="src/1-Getting started/argument.html">Passing function arguments</a> -
	<a href="src/1-Getting started/argument.js"> js</a></li>
  <li><a href="src/1-Getting started/scope.html">Recognizing variable scope</a> -
	<a href="src/1-Getting started/scope.js"> js</a></li>
  <li><a href="src/1-Getting started/domload.html">Domload</a> - 
	<a href="src/1-Getting started/domload.js"> js</a></li>
</ul>      	 
     
	 
	 
	 
	 

