# **Java Foundations (Second Edition)**
## John Lewis, Peter DePasquale & Joseph Chase

[Back to TOC](THE%20BOOK%20ON%20JAVA.md)

# CHAPTER 1 INTRODUCTION

### KEYWORDS ###

[hardware](#01) | [software](#02) | [program](#03) | [applications](#04) | [program statements](#05) |
[classes](#06) | [methods](#07) | [statements](#08) | [class header](#09) | [class body](#10) |
[method header](#11) | [method body](#12) | [comments](#13) | [identifiers](#14) | [case sensitive](#15) |
[title case](#16) | [upper case](#17) | [reserved words](#18) | [white space](#19) | [machine language](#20) |
[source code](#21) | [bytecode](#22) | [interpreter](#23) | [architecture-neutral](#24) | [development environment](#25) |
[integrated development environment](#26) | [debugger](#27) | [syntax](#28) | [semantics](#29) | [compile-time errors](#30) |
[run-time errors](#31) | [logical errors](#32) | [object-oriented approach](#33) | [development activities](#34) | [software requirements](#35) |
[functional specification](#36) | [software design](#37) | [implementation](#38) | [testing](#39) | [object-oriented](#40) |
[object](#41) | [state](#42) | [behaviours](#43) | [class](#44) | [inheritance](#45) |
[encapsulated](#46) 

    




Abraham Lincoln:

> Whatever you are, be a good one.

## <a id="Ch01_01">INTRODUCE THE JAVA PROGRAMMING LANGUAGE</a> ##

**What is a computer?**  
A computer is composed of _<a id="01">hardware</a>_ and _<a id="02">software</a>_. The hardware is some physical and 
tangible pieces that support computing power. The software consists of programs and the 
data those programs use. A _<a id="03">program</a>_ is a series of instructions that the hardware executes
one after the other. Programs are sometimes called _<a id="04">applications</a>_.

**What is a programming language?**  
A programming language specifies the words and symbols that we can use to write a program.
A programming language employs a set of rules that dictate how the words and symbols can be
put together to form valid _<a id="05">program statements</a>_. 

**The Java programming language**  
The Java programming language was created by Sun Microsystems, Inc. It was introduced in 1995 
and its popularity grew quickly.

A Java program is made up of one or more _<a id="06">classes</a>_. Each class contains one or more
 _<a id="07">methods</a>_. A method contains program _<a id="08">statements</a>_.

A Java application always contains a method called `main`.

Shown below is the basic structure a Java program:

```java
//********************************************************************
// Lincoln.java Java Foundations
//
// Demonstrates the basic structure of a Java application.
//********************************************************************
public class Lincoln {
	//-----------------------------------------------------------------
	// Prints a presidential quote.
	//-----------------------------------------------------------------
	public static void main(String[] args) {
		System.out.println("A quote by Abraham Lincoln:");
		System.out.println("Whatever you are, be a good one.");
	}
}
```
A typical Java program like `Lincoln.java` above has a class and a method(the `main` method). 
Each class has a _<a id="09">class header</a>_ and a _<a id="10">class body</a>_. By the same token, each method
consists of a _<a id="11">method header</a>_ and a _<a id="12">method body</a>_. 

You can add _<a id="13">comments</a>_ almost anywhere in the program. Comments should be added to explain 
the purpose of the program and describe processing detail. They do not affect how a program
works. Java comments come in three forms:

```java
// this comment runs to the end of the line
/* this comment runs to the terminating
   symbol, even across line breaks */
/** this is a javadoc comment */
```

**Identifiers**  

* The words a programmer uses in a program are called _<a id="14">identifiers</a>_
* An identifier can be made up of letters, digits, the underscore character (\_)
and the dollar sign
* An identifier cannot begin with a digit
* Java is _<a id="15">case sensitive</a>_. So `Total`, `total` and `TOTAL` are three different identifiers
* By convention, programmers take advantage of different case styles for different types of
identifiers, e.g. 
  * _<a id="16">title case</a>_ for class names - `Lincoln`
  * _<a id="17">upper case</a>_ for constants - `MAXIMUM`
* Sometimes we choose identifiers ourselves when writing a program (such as
`Lincoln`). Sometimes when we use another programmer's code, we need to use
the identifiers that he or she chose (such as `println`). Often we use special
identifiers called _<a id="18">reserved words</a>_ that already have a predefined meaning in
the programming language. A reserved word cannot be used in any other way.

**Java reserved words:**

 A - C       | D - F       | G - N       | P -  S      | T - W 
-------------|-------------|-------------|-------------|-------------
abstract     | default     | goto*       | package     | this
assert       | do          | if          | private     | throw 
boolean      | double      | implements  | protected   | throws
break        | else        | import      | public      | transient 
byte         | enum        | instanceof  | return      | true 
case         | extends     | int         | short       | try
catch        | false       | interface   | static      | void 
char         | final       | long        | strictfp    | volatile 
class        | finally     | native      | super       | while
const*       | float       | new         | switch      | 
continue     | for         | null        | synchronized|

**White space**  

* Spaces, blank lines, and tabs are called _<a id="19">white space</a>_
* White space is used to separate words and symbols in a program
* Extra white space is ignored

**Program formatting**  
A valid Java program can be formatted many ways. At any rate, programs should
be formatted to enhance readability (e.g. using consistent indentation).

## <a id="Ch01_02">PROGRAM COMPILATION AND EXECUTION</a> ##

**Basic programming steps**  
A program is written in an editor, compiled into an executable form, and then executed.
If errors occur during compilation, an executable form is not created.

**What is the mechanics of developing a program?**  
This involves several activities:

  * writing the program in a specific programming language (such as Java)
  * translating the program into a form executable by the computer
  * investigating and fixing various types of errors that can occur

Software tools can be used to help with all parts of this process.

**Language levels**  
There are four programming language levels:

* machine language (e.g. for x86 processors)
* assembly language (e.g. for x86 processors)
* high-level language (e.g. Java)
* fourth-generation language (e.g. SQL)

Each type of CPU has its own specific _<a id="20">machine language</a>_. The other levels were created 
to make it easier for a human being to read and write programs

A high-level expression and its lower level equivalents
![image1_1](images/LanguageLevels.JPG)

**Compilation and Java's approach**  
A compiler is a software tool which translates _<a id="21">source code</a>_ into a specific target
language. Often, that target language is the machine language for a particular CPU 
type. However, Java compiler is somewhat different.

The Java compiler translates Java source code into _<a id="22">bytecode</a>_. Java bytecode is not the
machine language for any traditional CPU. Another software tool, called _<a id="23">interpreter</a>_,
translates bytecode into machine language and executes it. Therefore the Java compiler is
not tied to any particular machine/CPU. Java is considered to be _<a id="24">architecture-neutral</a>_.

![image1_2](images/JavaTranslation.JPG)

**Environments for program development**  
A _<a id="25">development environment</a>_ is the set of tools used to create, test, and modify a 
program. And an _<a id="26">integrated development environment</a>_ (IDE) combine these tools into
one software program. All Java IDEs contain key tools such as a compiler and interpreter.
Some include additional tools such as a _<a id="27">debugger</a>_, which helps a programmer to find 
errors.

There are many IDEs that support the development of Java software, including:

* Eclipse
* NetBeans
* BlueJ
* jGRASP
  
Though the details of these IDEs differ, the basic compilation and execution process is
essentially the same.

**Syntax and semantics of a program**  
The _<a id="28">syntax</a>_ defines how identifiers, reserved words, and symbols can be 
put together to make a valid program. The _<a id="29">semantics</a>_ of a program statement defines 
what that statement means (i.e. its purpose or role in a program). A program that is
syntactically correct is not necessarily semantically/logically correct. A program will
always do what we tell it to do, not what we `meant` to tell it to do.

**Errors that can occur in a program**  
There are three types of errors:

* _<a id="30">compile-time errors</a>_ - The compiler will find syntax errors and other basic problems
* _<a id="31">run-time errors</a>_ - During program execution, a problem such as trying to divide by zero
will cause a program to terminate abnormally
* _<a id="32">logical errors</a>_ - A program may run, but produce incorrect results as a result of, 
perhaps, an incorrect formula.

## <a id="Ch01_03">PROBLEM SOLVING IN GENERAL</a> ##

**Problem solving process**  
The purpose of writing a program is to solve a problem.
 
Solving a problem consists of several activities:

- understand the problem
- design a solution
- consider alternatives and refine the solution
- implement the solution
- test the solution

These activities are not linear – they may overlap and interact.

**How to design a solution**  
The key to designing a solution is breaking it down into manageable pieces. Such separate
pieces are responsible for certain parts of the solution. An _<a id="33">object-oriented approach</a>_
is suitable for this kind of solution decomposition. Under this approach, our solutions are
dissected into pieces called objects and classes.

## <a id="Ch01_04">THE SOFTWARE DEVELOPMENT PROCESS</a> ##

**Basic development activities**  
Any proper software development effort consists of four basic _<a id="34">development activities</a>_:

- establishing the requirements (i.e. listing the requirements and then describing them in detail)
- creating a design (i.e. designing the requirements)
- implement the design (i.e. coding)
- testing the implementation (i.e. testing code)

These steps are not linear and may often overlap and interact

* _<a id="35">Software requirements</a>_ specify what a program must accomplish 要求規格
* _<a id="36">Functional specification</a>_ documents the expression of these requirements 具體說明
* A _<a id="37">software design</a>_ indicates how a program will accomplish its requirements 設計
* _<a id="38">Implementation</a>_ is the process of writing the source code that will solve the problem 付諸行動
* _<a id="39">Testing</a>_ is the act of ensuring that a program will work as intended given all the
constraints under which it must perform 測試

## <a id="Ch01_05">OVERVIEW OF OBJECT-ORIENTED PRINCIPLES</a> ##

**Object-oriented programming**  
Java is an _<a id="40">object-oriented</a>_ programming language. An object is a fundamental entity
in a Java program. Objects can be used effectively to represent real-world entities.
For instance, an object might represent a particular employee in a company. Each
employee object handles the processing and data management related to that employee.

**Objects**  
An _<a id="41">object</a>_ has _<a id="42">state</a>_ (descriptive characteristics) and _<a id="43">behaviours</a>_ (what it can do).
For instance, the state of a bank account includes its account number and its current
balance; the behaviours associated with a bank account include the ability to make
deposits and withdrawals. Note that the behaviour of an object might change its state.

**Classes**  
An object is defined by a _<a id="44">class</a>_, i.e. a class is the blueprint of an object. The class
uses methods to define the behaviours of the object. The class that contains the main
method of a Java program represents the entire program. 

**Classes and objects**  
A class represents a concept, and an object represents the embodiment of that concept.
Multiple objects can be created from the same class.

A class is like a blueprint of, say, a house from which you can create many of the "same"
house with different characteristics.

One class can be used to derive another class via/from _<a id="45">inheritance</a>_, such that classes
can be organized into hierachies.

An object is _<a id="46">encapsulated</a>_, protecting the data it manages.

![image1_3](./images/ClassesAndObjects.JPG)
