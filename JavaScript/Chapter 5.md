# **JavaScript in Easy Steps - Create Functions for the Web (5th Edition)**
## Mike McGrath

<a href="THE BOOK ON JAVASCRIPT.md">Back to TOC</a>

# CHAPTER 5 TELLING THE TIME
## Getting the date
## Extracting date components
## Extracting time components
## Setting the date and time
## Summary<br>
   * JavaScript has a built-in Date object to represent date, time, and timezone components of a
     particular point in time
   * A Date object is created using the __new__ keyword and the __Date()__ constructor
   * Where no arguments are specified to the __Date()__ constructor a Date object is created based upon
     the system time clock
   * JavaScript Date objects record the elapsed number of milliseconds since the epoch at January 1, 1970
     00:00:00 and its value can be found using the object's __getTime()__ method
   * The components of a Date object can be converted to a string value with its __toString()__ or
     __toUTCString()__ method
   * A Date object's __getTimezoneOffset()__ method returns the number of minutes that local time differs
     from UTC time
   * Individual Date components can be retrieved using __getFullYear()__, __getMonth()__, __getDate()__,
     and __getDay()__ methods
   * Individual time components can be retrieved from a Date object using its __getHours()__, __getMinutes()__,
     __getSeconds()__, and __getMilliseconds()__ methods
   * The __Date()__ constructor can optionally accept up to seven arguments to set each of the date and
     time components
   * Individual date and time components can be set for a Date object using its __setFullYear()__, __setMonth()__, 
     __setDate()__, __setHours()__, __setMinutes()__, __setSeconds()__, and __setMilliseconds()__ methods
   * The __toLocaleString()__ method returns a string using the computer's locale conventions while __toDateString()__
     and __toTimeString()__ methods display the date and time components

***Source Code for Chapter 5***
        <ul>
          <li><a href="src/5-Telling the time/date.html">Getting the date</a> -
            <a href="src/5-Telling the time/date.js"> js</a></li>
          <li><a href="src/5-Telling the time/months.html">Extracting date components</a> -
            <a href="src/5-Telling the time/months.js"> js</a></li>
          <li><a href="src/5-Telling the time/minutes.html">Extracting time components</a> -
            <a href="src/5-Telling the time/minutes.js"> js</a></li>
          <li><a href="src/5-Telling the time/setdate.html">Setting the date and time</a> -
            <a href="src/5-Telling the time/setdate.js"> js</a></li>
        </ul>
