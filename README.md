# SENG265 Grade Received: A+
Programs I wrote in SENG 265. Written in C and Python.



 

# Welcome to my SENG 265 Term Portfolio Project


![hello](https://wallpapercave.com/wp/MvrOQq0.jpg)
<img src="https://wallpapercave.com/wp/MvrOQq0.jpg" align ="center" alt="Tux" style="height: 90;"/>


#### Paul MacKay 
#### 3rd Year, Computer Science Major
#### University of Victoria

This Jupyter Notebook documents my SENG 265 experience.
I will summarize here what I am learning in this course about:
programming languages (i.e., C, Python 3, Bash, Jupyter Markdown, LaTex, SVG),
- software development methods (i.e, version control, configuration management, object-oriented programming, debugging, testing, seperate compilation), and</li>
- software development techniques and tools (i.e., Jupyter Notebooks, Unix, Bash, Git, Gitlab, make, makefiles, GNU C, C libraries, Python C interpreter, Python 3 libraries).</li>


## Part 1



Part 1 of this project, deals with the following aspects of my software development journey as follows:

#### 1. What is my background in Jupyter Notebooks? What is the core functionality of Jupyter notebooks?

- I have used Jupyter Notebooks in order to ducument small to medium python programs in order to solve a number of math problems on *Project Euler*.
- In my understanding and experience - Jupyter Notebooks are an all-in-one interpreter, formatting and documentation platform. Used extensively, though commonly used to present or document acedemic research, software development, science or engineering logbooks, and professoinal portfolios. 




#### 2.  Summarize simple Jupyter notebook markdown including how to insert links and images?

- Markdown is similar to HTML in function. Markdown is used to add and modify text in the following ways:
    - **Headings** can be made by inserting "# ", ..., "###### " before text, the user can create different sizes of headers in decending order (# is the largest sized heading)
    - **Paragraphs** can be formatted by leaving one cariage return between two lines of text.
    - **line Breaks** are made by simply pressing return at the end of the line which you desire to have a line break.
    - **Emphasis** can be made on text in the following ways:
        - Text can be made **bold** by adding double asterisk's on both sides of some given text. (ex. ** text ** )
        - *Italicized* text can be made my adding single asterisk's on both side of the text. (ex. * text * ) 
        - ***Bold and Italic*** text can be made by adding tripple asterisk's on both sides of the text. (ex. *** text *** )
    - **Blockquotes** allows having a part of the content from another source link. These are similar to reply email text. Add the symbol greater than ‘>’ to the line that contains the text.
    - **Lists** allow the user to organize information in a readable way.
        - *Ordered Lists* is a numbered list from (1-n). Can be nested where every level up is indented.
        - *Unordered Lists* is a non-numbered list. Can be nested where every level up is indented.
            - Unordered list nested in an ordered list, or vice versa.
    - **Links** can be inserted by [link] (https://www.example.com)
    - **Images** can be inserted by ![description] (filepath/image.png)
    
    


#### 3. How can I typeset mathematical formulas including Greek letters using LaTeX Markdown in Jupyter Notebooks?

- Mathematical formulas and symbols are rendered using LaTeX inside Markdown using MathJax.

- To use LaTeX in markdown surround the desired math inside dollar signs.
- For example Euler's identity: $ e^{i \pi} + 1 = 0 $ can be rendered like so.




#### 4. What is my background in Unix or Linux? How prevalent is Unix or Linux in software development?

- Linux has been my daily driver for the past two years. During that time I've had to learn lots about bash commands, editing config files in vim, using vim for any file editing and creation, using Linux as a software development platform, using almost exclusively free and open source software, debugging if I run into any issues on Linux, been exposed to many Linux distributions, downloading software from repositories git, Arch User/Official Repository, and apt (Debian based)
- The internet runs on Linux, it is the backbone to the structure of the internet. Basically all internet servers are built on Linux, most software development companies use linux for every component of their work, front-end and back-end. 




#### 5. What is my background in the programming language C? How prevalent is C in software development?

- I have written small to medium sized programs in C. Written in vim and compiled with gcc in a terminal. Made use and continuing to master the following attributes of C:

    - Functions
    - Variable Declaration, Definition and Scope
    - Pointers
    - Data Types
    - Struct
    - Input/Output
    - Memory Management
    - File Handling 
    - Operators
    - Arrays & Strings
    
- C is very prevalent in software development. Like all other programming languages C has a specific use. C being a low-level programming language it is superior for large, complex, and long term supported software. The other reason C is used for long living programs is because no new features are being added to it, so a program from 20 years ago will still run today. The low level nature of C gives the programmer more control over the hardware and memory, therefore programs can be written more efficiently, and in a manner that is executed faster therefore is light on resources.




#### 6. What is my background in the programming language Python 3? How prevalent is Python 3 in software development?

- Written small programs interpereted in Jupyter Notebooks, in order to solve math problems on Project Euler. Used the following attributes of Python3:

    - Data Structures
        - Tuple
        - Dictionary
        - Operators 
        - Arrays
    - Conditional loops
        - if...else, elif, switch
        - For and While loops
    - Strings
        - Replace, Join, Split, Reverse, Uppercase, Lowercase
        - strip() Function
        - count() Function
        - format() Function
        - len() Function
        - find() Function
    - Functions
    - File handling 
    - List
    - DateTime
    
- Python one of the most used languages on the planet. Its a very versitile language, but usually used for prototyping. You wouldn't want to use Python to write a long lasting software, for one because it is always being updated and it would be a nightmare to change millions of lines of code to update it. Second it is much heavier of a language due to the fact that it is interpereted instead of compiled, therefore using more resourses making it much slower than a compiled language like C.




#### 7. What is the core functionality of the Bash command and scripting language?

- Bash commands provide the user with a robust set of commands that are administered in the terminal (stdin). The purpose of these commands is to do operations on files and directories.
- Scrips are used for automation. A script would be comprised of a series of bash commands in order to achieve a desired outcome.




#### 8. Why is version control and configuration management critical in software development projects.

-  version control enables a team of developers to work on a project together. Each developer is able to take a fork of the main branch make changes (improve, fix bugs, add/remove features, etc), and then if the team agrees on the changes they are merged to the master branch. Each time the master is worked on a new branch is made, this is a version and can be restored if needed at a later date. This is also useful if someone messes up, the messed up branch can be discarded and the team or individual can revert back to a working version of the project. The ability to work on a copy of the project without having to work on the original is important because if the developer were to be working exclusively on the original project, the project would have to be taken offline which would be a terrible buisness model, being that development on projects is always taking place.




#### 9. What are the core functionalities of Git, Github, and Gitlab?

- Git is the most widely used version control platform. Git has many features but most common for a work flow is the following.

    - Staging: git add ~/file.ext. Add a file or modifications to a file to the staging area. 
    - git commit -m "Meaningful message". commit encapsulates all of the changes made to the local repository, ready to be "pushed" to the remote server.
    - git push -  updates the masterbranch (remote server) with the development branch (local server).
    
- Github is just git but it offers the developer a user interface. This is useful for group projects and individuals . Group projects can be worked on and submitted on github in order to distribute open-source software to the public, acting as a platform to host open-source projects. For the individual - github is used to showcase projects and experience to employers other developers. Hense acting as a platform to record all of the work the developer has done, current and future projects.
    
#### 10. What are your personal insights, aha moments, and epiphanies you experienced in the first part of SENG 265?

- Realizing that some tasks are actually hard, but if you have the right mindset and strategy that difficult task becomes managable.

<br>

##### Sources:

https://www.guru99.com/python-tutorials.html

https://www.w3schools.io/file/markdown-blockquotes/

https://www.markdownguide.org/basic-syntax/

https://towardsdatascience.com/write-markdown-latex-in-the-jupyter-notebook-10985edb91fd

https://www.geeksforgeeks.org/c-programming-language/



## Part 2

#### 1. How is Git used as a version control system?

- Just like if someone was working on a text document like an essay for school, they may have multiple versions to go back to. For example: essay1.odt, essay2.odt, essay3.odt. This would be an exaple of version control in a nieve sense. Git makes version control more sophisticated and useful in the following ways: When using git, there is a remote and local repository. The remote repository contains the main branch - the most up-to-date version of the software. Plus all of the other previous versions of the project (can be found in the .git file in all git repositories). The remote repository is useful to have because multiple people can then work on the project. The function of the local repository is - to clone the remote repository to your local repository (which is just your local computer your are using). Develop the code taken from the remote repo, make changes to the code, then - if your working alone use the following commands, add, commit, push. If youre working with others then you may have to submit a merge request. Whenever a push, or merge is performed git will make that the main branch which will be recorded as a "version" next time a push or merge is executed.

#### 2. How can Git be used effectively in a highly distributed software development environment involving multiple countries?

- Unlike a *centralized workflow*, which is used by having one central hub, or repository, with a number of developers. A *distributed workflow* has many applications as it can be structured hierarchical.  Distributed workflow uses multiple repositories, distributed among developers, access to such repository is dictated by the permission structure for that specific development team. Each development team would have a different hierarchy depending on the role of each member. For example, take a development team, the members of which are located around the world. From https://git-scm.com/book/en/v2/Distributed-Git-Distributed-Workflows there are two common ways to deploy distributed workflows:
    - Integreation-Manager Workflow:
        1. The project maintainer pushes to their public repository.
        2. A contributor clones that repository and makes changes.
        3. The contributor pushes to their own public copy.
        4. The contributor sends the maintainer an email asking them to pull changes.
        5. The maintainer adds the contributor’s repository as a remote and merges locally.
        6. The maintainer pushes merged changes to the main repository.
        <br><br>
    - Dictator and Lieutenants Workflow:
        1. Regular developers work on their topic branch and rebase their work on top of master. The master branch is that of the reference repository to which the dictator pushes.
        2. Lieutenants merge the developers' topic branches into their master branch.
        3. The dictator merges the lieutenants' master branches into the dictator’s master branch.
        4. Finally, the dictator pushes that master branch to the reference repository so the other developers can rebase on it.
        
#### 3. Breifly describe the history of version control systems.

- Version control has a long history. One of the first VCS's was Source Code Control System (SCCS) introduced in 1973. There were many releases of VCS's from 1973 until 2005 when Linus Torvalds released *git*. None of these older releases gained mass adoption like git did. A couple reason that git was so successful was (1) Linus was a huge name in the open source community at the time, therefore the word got out and it became the most successful and most used VSC (2) Linus's was able to solve the inefficiencies faced in the early developers of VCS's, making it a better, more useful, and space efficient program.  

#### 4. What are the most popular programming languages and why?

- Top 5 programming languages:
    1. Python
    2. C
    3. Java
    4. C++
    5. C#

- Python has gained popularity due to the rise in *AI*, *machine learning* and its application to these feilds. Its also used for *web development*, *data science*, *automation*. Another reason that Python is so popular is because it is a high-level prototyping language, meaning - developers can use Python to create a prototype of a project, then export it to a production language like C, or Java. Its also easy for humans to read and use (more intuitive).
    
- C is the most popular production programming language. Gives the programmer lots of control (lower level) but remains a fairly straight forward language to learn. The low level nature, rigidity,and simplicity makes C the most widely used programming language for long lasting software that can survive through the test of time. Also that C is a lower level language and is compiled, makes it lighter on resources, therefore would be good for huge and complex programs.
    
- Java is another popular production language, its a bit higher level than C but still low level enough to be fast. Is an object oriented language, platform independent, simple, secure, etc. 
    
#### 5.  C & Python are amont the most popular programming languages. You are learning them in SENG 265. How cool is that for your software development career?


- I am very excited that we are learning the top two programming languages, gives good experience in the persuit of mastering these languages. I feel more confident using C after completing assignment 1, and I'm exited to complete assignment 2 and get familiar with python. It's a really good place to build off, and it makes me excited to work on projects in the future.


#### 6. Describe the fundamental differences between C and Python.

- **C**: 
    - Type:
        - C is a structured programming language, statically typed.
    - Variable Declaration:
        - Variables must be declared before using a variable, and the data-type must be declared.
    - Compilation:
        - C code is compiled by a compiler, hence it is defined as a compiled language.
    - Built-in Functions:
        - C has a limited as percise set of built-in library functions.
    - Execution:
        - Since C is a compiled language, code is compiled directly to machine code which is executed directly by the CPU.
        
- **Python**: 
    - Type:
        - Python is an object-oriendted type programming language and is dynamically typed.
    - Variable Declaration:
        - Python declaring the data-type will result in error. 
    - Compilation:
        -  Python code is interpreted, hence it is defined as a interpreted language.
    - Built-in Functions:
        - Python has an extensive and robust set of built-in library functions.
    - Execution:
        - Python code is vist compile to a byte-code then it is interpreted by a C program.


#### 7. How challenging was Assignment 1 for you?

- Assignment 1 was difficult, but once I knew the strategy I was going to deploy everything fell into place and I was able to get it done. There was a whole lot of background knowledge required to complete assignment 1 and if I didn't have some degree of mastery over the language I would not have been able to finish it. Bill Bird's C video's really helped me understand the foundational concepts of C. The video's gave me a comprehensive enough overview of C to be able to implement the language to a real world problem. Really an invaluable resource for anyone learning C, my thanks goes out to Bill Bird for those video's.

#### 8. Describe your continued learning experience in SENG 265.

- In order to be an asset to either a company, development team, or customer, I'm looking forward to continuing my development as a software developer. The remainder of SENG 265 will be focused on dynamic memory, make files, GDB debugging tool in C, this will take place among assignment 3, labs, and exams. In Python we will be continuing learning object oriented programming, and solving small to medium sized problems, this will take place during assignment 2, and 4, labs, and exams.

##### Sources:

https://www.codesweetly.com/git-basic-introduction/

https://git-scm.com/book/en/v2/Distributed-Git-Distributed-Workflows

https://ericsink.com/vcbe/html/history_of_version_control.html#idp129536

https://www.tiobe.com/tiobe-index/

https://www.tutorialspoint.com/java/java_overview.htm

https://www.youtube.com/watch?v=rlA89I3Y0nQ&list=PLU4IQLU9e_Oq2dqhFV6n9shODnN8DR9b_

## Part 3

#### 1. How useful is SENG 265 for building your resume for future co-op applications and furture job applications?

- SENG 265 has been a very exciting and useful course, packed with very useful information. My ability to read, and develop software has been sharpened as a result of taking this course. It has extended my knowledge in using bash, and using Linux  as a development environment (including Vim as a text editor). Learning about incremental development changed my outlook on how to develop software effectively and efficiently. Learning about quantum computing opened my eyes to the future applications of this technology, and potential job opportunities related to this field. Some of these skills I was already working on and this class helped me extend my knowledge in those categories, I was also introduced to new ideas. In both cases I’m excited to extend my knowledge and learn more in the near future. The way in which I believe this course will help me find a co-op and job in the future is being competent in the field, also being exposed to, and interested in future technologies will be an important asset to posses. Given that most tech jobs and CSC co-op's recommend or require some experience with at least one of the topics we covered in SENG 265, it is extremely useful taking this course.

#### 2. In SENG 265 you acquired significant systems programming knowledge and learned many different skills (e.g., C, Python, Unix, Bash, make, pipes & filters SVG, HTML, static and dynamic data structures, testing and debugging, text processing, and many more. Which skills are most valuable for you? Which skills are you going to add to your resume?

- I have been using Linux as my daily driver OS for the past two years. Learning more about, and using Unix, Bash, pipes, and filters daily made me much more efficient, confident when using them, hence increasing the utility of these systems in my development. In other words going over Unix, Bash, pipes, and filters increased my mastery over Linux as a development environment, it was quite useful for me. Completing the assignments made me substantially better at reading, and debugging code, also I got a lot better at structuring a programs. I plan on including most of, if not all of these learning outcomes on my resume. Given that most of the topics we went over in this class are recommended or required for most of the positions posted, and also for most tech jobs.That I'm going to be applying for a co-op next fall I'm quite happy to have gone over the topics covered in this course, and that it has sparked some ideas for projects I can work on to gain more experience. 

**Uvic COOP Resume Outline**

![a2](/home/paul/newsite2/statis/coop.png "hello")

#### 3. Describe the difference between object-based and object-oriented programming. The first part of the Python lectures was object-based programming. The second part involves classes and is called object-oriented programming.

- Object-based programming is where the programmer uses imported packages and modules, primitive data types, functions, built-in functions,  and their functionality in code, but does not write classes and methods themselves. Usually the program is decomposed into various functions and main calls those functions.
- Object-oriented programming is where the entire project is evolves around the OOP philosophy. Meaning the program functionality is encapsulated in classes and their methods. When a class is instantiated that is classically called an object. That object then has access to all of the methods contained in that class. The benefits of OOP is that bugs can be found locally in the class/ method, making debugging much more straight forward and obvious where the bug might be. Another benefit is having private attributes in a class. Where the instance variable does not have direct access to attributes, in this case setters and getters are used when manipulating and viewing attribute members of that object.


**Code sample from Assignment 2**
- Here in assignment 2 we used Oject-based program most of the functionality is wrapped up in definitions, then those functions are called in main.

![a2](/a2screenshot.png "hello")

**Code sample from Assignment 4**
- Here in assignment 4 we used Oject-oriented programming. All of the functionality is wrapped up in classes, and their methods.

![a4](/a4screenshot.png "hello")


#### 4. Describe the notion of and motivation for typing and typing hints in Python.

- When declaring a variable the data type is specified, this is called type hinting. The benefits of using type hints is – if a bug occurs where the data type was changed somewhere in the program, this would be a difficult bug to find. If type hints were used when run this “type miss-match” would be detected and the bug would easily be found and fixed. Type hints make programs much easier to read and understand the functionality. Hence if working with others it would be a good idea to use type hints.

![a4](/typehints.png "hello")

#### 5. Python classes package and encapsulate data and functions that operate on those data. What are the big advantages of classes with respect to packaging and encapsulation.

- Simplicity – Break down a project into smaller portions rather than having one massive block of code. This makes code easier to write and less prone to buggy code.
- Maintainability – having a program broken up into classes and methods means the software will have high cohesion and low coupling. Meaning the code will not contain inter-dependencies, that would lead to a highly coupled program that would be virtually impossible to maintain. 
- Reusability – since each module has specific functionality the code from a package or module can easily be reused in one or more projects.
- Scoping – each module is made of classes, those classes contain methods. Hence the scope of each defined in separate namespace, which helps to avoid collisions among identifiers.


![](/tree.png "code created by a43.py")


#### 6. How challenging was Assignment 4 for you?

- I started off by integrating the provided methods given in the part 1 template into a class called ProEpilogue. The function of this class is to write the headers for the html document and to open the svg block, and to close these blocks with appropriate white space padding. I then created two simple classes called Circle and Rectangle, and followed the logic and structure proposed in the given code. The function of these classes is to write a line of text to a file that represents a circle or a rectangle in the svg format. To draw a circle or rectangle specific parameters are required. For example to specify the color parameters would be r=255, g=255, b=255 for that particular circle or rectangle to be drawn. Now the goal is to repeat this for n number of shape objects, in this case Circle and Rectangles, with random values. The approach I took was to make each randomly created art page an object. To achieve this I made a class called PyArt. PyArt's instance method receives all of the information to create an HTML, SVG art page, ie number of shapes, size, color, which shape. Therefore all we have to do is create one “art object” with all the values specified once, when that object is instantiated. This makes modifying values and flavor of the art straight forward and easy to do. I would say it was not a trivial project, it was certainly in reach to achieve for a student with limited python experience.     
- For example all I have to do is:
    pa1: PyArt = PyArt(f, "Python SVG Art1", \
            5000, (0, 1000, 0, 250), (0,0), (0, 10), (5, 100, 5, 50), \
            (0,0,0, 255, 255, 255, 0.5, 1.0))
            
            
![](/htmlpic.png "code created by a43.py")


#### 7. Did you send your art work to your friends and family?

- I sent the code to one of my brothers to run to show him what I did for assignment 4. I showed most of my family members the artwork I created, and I plan to send the rest there very own randomly generated greetings card.


![](/art02.png "hello")


#### 8. Describe your continued learning experience in SENG 265.

- I plan on expanding the knowledge and concepts introduced in SENG 265. All of the concepts were foundational and spanned across many important subjects. I plan on applying the knowledge gained to side projects, I can see that I will need C and Python for the side projects I have in mind. This would also give me a chance to apply this knowledge to a real world example, thereby solidifying and expanding that knowledge. For example I’m planning on installing a car PC which includes GPS, speedometer, tachometer, engine load meter,  backup camera, music from scratch in my car via raspberry pi connected to a screen and an OBD-II connection. I’m hoping to use exclusively open source software, therefore I can modify the code to my needs. From my research I see that most of the software and config files are written in either C or Python. I also have other projects in mind that I plan to do over the summer.


<table><tr>
    <td> <img src="/pi.png" alt="Raspberry" style="width: 250px;"/> </td>
    <td> <img src="/pi2.png" alt="Raspberry" style="width: 250px;"/> </td>
     <td> <img src="/pi3.png" alt="Raspberry" style="width: 250px;"/> </td>
    </tr></table>
<table><tr>
    <td> <img src="/map.png" alt="Raspberry" style="width: 750px;"/> </td>
    <td> <img src="/map2.png" alt="Raspberry" style="width: 350px;"/> </td>
    </tr></table>
    
    
##### Sources: 

https://realpython.com/lessons/type-hinting/

