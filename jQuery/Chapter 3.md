# **jQuery in Easy Steps - Create Dynamic Web Pages**
## Mike McGrath

[Back to TOC](THE%20BOOK%20ON%20JQUERY.md)

# CHAPTER 3 MANAGING FORMS
## Selecting text fields
## Selecting by ability
## Selecting radio buttons
## Selecting checkboxes
## Selecting options
## Selecting buttons
## Selecting file inputs
## Recognizing focus
## Submitting forms
## Summary<br>
   * Form elements can best be selected for a jQuery object by identifying their __type__ attribute
   * An input element in a collection can be referenced by stating its index number to the jQuery's object's
     __eq()__ method and its value retrieved by chaining the __val()__ method to the statement
   * Form __&lt;textarea&gt;__ elements can be selected for a jQuery object using their tag name and
     __name__ attribute
   * A jQuery's object's __prop()__ method can retrieve the value of a specified property or can set a
     property with a specified value
   * The __disabled__, __checked__, and __selected__ properties return a Boolean __true__ value when set,
     otherwise they return a __false__ value
   * A "change" event occurs when the user selects a dropdown list option and can be recognized by the
     jQuery __change()__ method
   * The currently selected option in a list can be determined by specifying a __":selected"__ argument to
     the jQuery __filter()__ method
   * Form input button elements and __&lt;button&gt;__ elments can both be selected for a jQuery object using
     a single multiple selector
   * Form input submit, reset, and file types buttons can also be selected for a jQuery's object by indentifying
     their __type__ attribute
   * A "change" event occurs when the user selects a file input and can be recognized by the jQuery __change()__ method
   * The "focus" and "blur" events occur as the user selects form elements and can be recognized by __focus()__ and
     __blur()__ methods
   * Bubbling is supported by the __focusin()__ and __focusout()__ methods
   * A "submit" event occurs when the user submits a form to the server and can be recognized by the jQuery
     __submit()__ method
   * Al jQuery methods that recognize events can specify an anonymous function to perform an appropriate response

***Source Code for Chapter 3***
<ul>
  <li>Selecting text fields: 
    <a href="src/textfield.html">textfield</a> - 
	<a href="src/textarea.html">textarea</a></li>
  <li>Selecting by ability: 
    <a href="src/disabled.html">disabled</a> - 
	<a href="src/enabled.html">enabled</a></li>
  <li>Selecting radio buttons: 
    <a href="src/radio.html">radio</a></li>
  <li>Selecting checkboxes: 
    <a href="src/checkbox.html">checkbox</a></li> 
  <li>Selecting options: 
    <a href="src/option.html">option</a> - 
	<a href="src/change.html">change</a></li>
  <li>Selecting buttons: 
    <a href="src/button.html">button</a> - 
	<a href="src/reset.html">reset</a></li>
  <li>Selecting file inputs: 
    <a href="src/file.html">file</a> - 
	<a href="src/image.html">image</a></li>
  <li>Recognizing focus: 
    <a href="src/focus.html">focus</a> - 
	<a href="src/focusin.html">focusin</a></li>
  <li>Submitting forms: 
	<a href="src/htdocs/submit.html">submit</a></li>
</ul>   