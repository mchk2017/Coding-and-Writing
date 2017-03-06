# **jQuery in Easy Steps - Create Dynamic Web Pages**
## Mike McGrath

[Back to TOC](./THE BOOK ON JQUERY.md)

# CHAPTER 9 USING PLUGINS
## Grabbing plugins
## Writing plugins
## Enabling chains
## Protecting the alias
## Passing parameters
## Visiting each element
## Providing options
## Plugging-in dialogs
## Summary<br>
   * Plugin scripts are JavaScript files that can be used to extend the functionality of the jQuery library
   * The jQuery Plugins Registry offers freely available plugins that can be downloaded for addition to your
     own web pages
   * All methods of a jQuery object are contained in the __$.fn__ object
   * Additional methods can be appended to the __$.fn__ object and can reference other methods in that
     object by the __this__ keyword
   * Plugin files should adhere to the jQuery naming convention
   * It is good practice to have each plugin method return the jQuery object to the caller so it becomes
     chain-able
   * All plugin code should be enclosed in an Immediately Invoked Function Expression (IIFE) to protect the __$__ alias from conflict
   * Enclosing code within an IIFE to protect
     variables from possible conflict
   * Plugin scripts should not duplicate functionality
   * Methods that allow parameter to be passed to them as arguments are efficient and flexible
   * It is worthwhile specifying parameter default values in a method definition so it may be called
     without arguments
   * A plugin method can manipulate the entire collection of elements in a jQuery object or use the __each()__
     method to manipulate individual elements in turn
   * As the __each()__ method is itself chain-able it automatically returns the jQuery object so the caller
     becomes chain-able
   * Plugin methods can be made customizable by accepting an options list within a JavaScript object
   * The jQuery __$.extend()__ method can merge two argument objects into a single object specifying a list
     of options to appy

***Source Code for Chapter 9***
<ul>
  <li><a href="src/htdocs/getouter.html">Grabbing plugins</a> - 
      <a href="src/htdocs/jquery.get-outer-html.js"> js</a></li>
  <li><a href="src/htdocs/basic-plugin.html">Writing plugins</a> - 
      <a href="src/htdocs/jquery.basic-plugin.js"> js</a></li>
  <li><a href="src/htdocs/chain-plugin.html">Enabling chains</a> - 
      <a href="src/htdocs/jquery.chain-plugin.js"> js</a></li>
  <li><a href="src/htdocs/standard-plugin.html">Protecting the alias</a> - 
      <a href="src/htdocs/jquery.standard-plugin.js"> js</a></li>
  <li><a href="src/htdocs/param-plugin.html">Passing parameters</a> - 
      <a href="src/htdocs/jquery.param-plugin.js"> js</a></li>
  <li><a href="src/htdocs/each-plugin.html">Visiting each element</a> - 
      <a href="src/htdocs/jquery.each-plugin.js"> js</a></li>
  <li><a href="src/htdocs/option-plugin.html">Providing options</a> - 
      <a href="src/htdocs/jquery.option-plugin.js"> js</a></li>
  <li><a href="src/htdocs/modal-plugin.html">Plugging-in dialogs</a> - 
      <a href="src/htdocs/jquery.modal-plugin.js"> js</a></li>
</ul>      