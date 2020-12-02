# UNIX

**Firstly, what is an operating system (OS)?**  
An OS is the low-level software that acts as a resource manager, supports a computer's basic functions and allows software to access system resources like processing, memory and storage. An operating system enables the computer to work.

## What?
UNIX is an operating system first developed in the 1960s. It is a stable, multi-user, multi-tasking system for servers, desktops and laptops.

UNIX systems often have a graphical user interface (GUI), a visual prompt which you can interact with and pass commands via clicking and typing, similar to Microsoft Windows; when you boot the machine, this is what you're seeing. Not all operations are included in a GUI but can be accessed via the systems command line interface.

### UNIX-like OS
There are many different versions of UNIX, although they share a common foundation. The most popular variations of UNIX are Linux and MacOS.

Linux is an incredibly popular OS to run on a server, for automation and hosting an application or service. It can be light-weight and flexible, often avoiding the problems of bloatware and pre-installed software.

## Inside UNIX
A UNIX operating system is made up of three parts: the kernel, shell and applications.

### The kernel
A system's kernel is the core of the operating system; it handles the file-system, system calls and received commands, memory allocations and processing time for applications.

### The shell
The shell is a command line interpreter (CLI) which acts as an interface between the user and the kernel. After processing a command, the shell returns a prompt allowing for more commands. Typically commands are handled serially (one at a time) but can be performed concurrently, likely in parallel (multiple commands running at the same time).

### Bash
Bash is the default UNIX shell for most Linux distributions and MacOS, up to Catalina, it has since been replaced on MacOS with [zsh](https://en.wikipedia.org/wiki/Z_shell).

The Bash language was written by Brian Fox for the GNU Project and was first released in 1989.

### The Terminal
Mac and Linux OS have a terminal (Command Prompt in Windows), it is a text input / output environment that sits on top of a shell. The shell receives the commands, interprets them, processes and returns any output back to the terminal. This is a human - machine interface.

### git BASH for windows
git BASH is a BASH emulator which will allow us to work in similar ways to UNIX-like, Linux and MacOS machines. Our aim is to work with similar patterns and tooling, to work in the same way across different operating systems. When installing git no a Windows machine, git BASH should come bundled with it.

Typically when putting code into production, this is done on servers which have a UNIX-like operating system and use BASH. Experienced developers also natively work on machines running a UNIX-like OS such as Linux or Ubuntu - for these reasons it's a good idea to work with similar tooling where everyone can run each other's code. Read about git BASH [here](https://gitforwindows.org/).
