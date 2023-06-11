Elf-Fix-Memory-Dumper
====
[![GitHub stars](https://img.shields.io/github/stars/Anonym0usWork1221/Memory-Dumper.svg)](https://github.com/Anonym0usWork1221/Memory-Dumper/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Anonym0usWork1221/Memory-Dumper.svg)](https://github.com/Anonym0usWork1221/Memory-Dumper/network/members)
[![GitHub issues](https://img.shields.io/github/issues/Anonym0usWork1221/Memory-Dumper.svg)](https://github.com/Anonym0usWork1221/Memory-Dumper/issues)
[![GitHub watchers](https://img.shields.io/github/watchers/Anonym0usWork1221/Memory-Dumper.svg)](https://github.com/Anonym0usWork1221/Memory-Dumper/watchers)
[![Python](https://img.shields.io/badge/language-Python%203-blue.svg)](https://www.python.org)
[![CPP](https://img.shields.io/badge/language-CPP-pink.svg)](https://www.cpp.org)
[![C](https://img.shields.io/badge/language-C-red.svg)](https://www.c.org)
[![GPT_LICENSE](https://img.shields.io/badge/license-MIT-yellow.svg)](https://opensource.org/licenses/)
![code size](https://img.shields.io/github/languages/code-size/Anonym0usWork1221/android-memorytool)

-----------


**This is a script for Dumping Run Time Memory with elf fixer**

If you find any bug or not working functions you can contact me. 

 *  Author : Abdul Moez
 *  Version : 0.2
 *  Study  : UnderGraduate in GCU Lahore, Pakistan
 *  Repo  : (https://github.com/Anonym0usWork1221/Memory-Dumper)
 
 MIT License

 Copyright (c) 2022 AbdulMoez


# Version 0.2
    -> Optimized the code
    -> Update the MemoryTool to 0.4 androidmemorytool support
    -> Reduce complexity of installation
    -> Update the setup.py and remove errors of installation
    -> Disable logs so clean output can be seen
    -> Patch the fix.cpp file (to reduce logs and errors)
    
System & Env Requirements
-----------
* Needed python version 3.6+
* Android Requirements -> Rooted Device Needed

Installation on termux
----------------------------------------
* **__Installation__**  
  ```
  pkg update && pkg upgrade  
  pkg install cmake
  pkg install tsu  
  pkg install python3  
  pkg install git
  git clone https://github.com/Anonym0usWork1221/Memory-Dumper  
  cd Memory-Dumper/
  pip3 install .
  ```      
* **__Dumped lib will be appeared in same directory__** ``./dumped_lib/*`` 

Installation on Linux
----------------------------------------
* **__Installation__**  
  ```
  apt install cmake
  git clone https://github.com/Anonym0usWork1221/Memory-Dumper
  cd Memory-Dumper/    
  pip3 install .
  ```

* **__Dumped lib will be appeared in same directory__** ``./dumped_lib/*``  


Usage 
----------------------------------------
* **__Run Game/Process__**

* **__Run Script on Linux__**  
    ``python3 MemoryDumper.py``  
    
* **__Run Script on Android__**  
    ``sudo python3 MemoryDumper.py``

* **__Make your choice from given menu__**  

# Compare between no-fix and fixed ELF
![image_without_fixer](img/no-fix.png)
![image_with_fixer](img/fix.png)

Reference
----------
* [Android-MemoryTool](https://github.com/Anonym0usWork1221/android-memorytool)
* [Elf-Dump-Fixer](https://github.com/maiyao1988/elf-dump-fix)


# Contributor 

<a href = "https://github.com/Anonym0usWork1221/Memory-Dumper/graphs/contributors">
  <img src = "https://contrib.rocks/image?repo=Anonym0usWork1221/Memory-Dumper"/>
</a>


Assistance
----------
If you need assistance, you can ask for help on my mailing list:

* Email      : abdulmoez123456789@gmail.com

I also created a Discord group:

* Server     : https://discord.gg/RMNcqzmt9f


Buy Me a coffee
--------------
If you want to support me you can buy me coffee.
BitCoin_addr: ``` 19vwfRXfthPY7f2aqDBpxQvZa6AJFKcdBS ```
