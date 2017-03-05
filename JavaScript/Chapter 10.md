# **JavaScript in Easy Steps - Create Functions for the Web (5th Edition)**
## Mike McGrath

[Back to TOC](./THE BOOK ON JAVASCRIPT.md)

# CHAPTER 10 PROCESSING HTML FORMS
## Assigning values
## Polling radios & checkboxes
## Choosing options
## Reacting to form changes
## Submitting valid forms
## Summary<br>
   * Each element of a form can be dynamically assigned a value from JavaScript.
   * If a form element contains an id attribute, that element can be referenced using the
     __document.getElementById()__ method
   * A form element that does not contain an id attribute can be referenced using the 
     __document.forms[].elements[]__ arrays
   * The value assigned to the __name__ attribute of a radio button group or checkbox group is also the
     name of an array in which each button can be referenced by their index value
   * When a form radio button or checkbox button has been selected its __checked__ property becomes
     a __true__ value
   * A loop can be used to examine the __checked__ property of each button in a button group to determine
     which are selected
   * The options of a selection list object are represented in the DOM by its __options[]__ array
   * A selection list object has a __selectedindex__ property containing the array element index value of
     the currently-selected option
   * The value of the current selected option can be retrieved by specifying the __selectedindex__ value 
     in the __options[]__ array
   * An event-handler function can be nominated by the __onchange__ property to respond to changes in 
     text field content
   * An event-handler function can be nominated by the __onreset__ property to respond when the user pushes
     a form's reset button
   * An event-handler function can be nominated by the __onsubmit__ property to respond when the user pushes
     a form's submit button
   * When the __onsubmit__ event-handler returns a __false__ value the form will not be submitted
   * A form can be submitted from script by calling the __submit()__ method of the form object

***Source Code for Chapter 10***
        <ul>
          <li><a href="src/10-Processing HTML forms/assign.html">Assigning values</a> -
            <a href="src/10-Processing HTML forms/assign.js"> js</a></li>
          <li><a href="src/10-Processing HTML forms/poll.html">Polling radios & checkboxes</a> -
            <a href="src/10-Processing HTML forms/poll.js"> js</a></li>
          <li><a href="src/10-Processing HTML forms/select.html">Choosing options</a> -
            <a href="src/10-Processing HTML forms/select.js"> js</a></li>
          <li><a href="src/10-Processing HTML forms/change.html">Reacting to form changes</a> -
            <a href="src/10-Processing HTML forms/change.js"> js</a></li>
          <li><a href="src/10-Processing HTML forms/validate.html">Submitting valid forms</a> -
            <a href="src/10-Processing HTML forms/validate.js"> js</a></li>
        </ul>