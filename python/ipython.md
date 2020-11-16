# iPython

## What?

IPython is a Python interpreter, an interactive shell which evaluates and runs Python code. You can run individual or multiple lines of code, this also includes evaluating whole files. IPython offers rich syntax highlighting, tab completion, history and introspection (examining the type or properties of an object) at runtime. The shell also accepts some common UNIX commands like `pwd` and `ls`.

## Why?

If Python is used to 'do a thing' or return an output, we need something to run our code which is also a friendly environment to develop in.

Evaluating a Python script processes all commands at runtime, this also clears out any variables and objects from memory which are no longer needed  when the script has completed; meaning once the code has finished running, nothing (unless explicitly outputted to the global system memory) will be stored as the session has closed, and we cannot retrieve objects used during the run.

IPython is a shell which remains open and so all global objects that the interpreter has access to remain in memory and we can call them. This is very useful to inspect objects and print them to the console. If you want to see the output of a function or need to debug, IPython is a useful environment to do this in.

## How?

Assuming you've already [set up IPython](../100/getting-started.md), open a terminal / git BASH and simply run the command:

    ipython

If you recieve an error along the lines of

    command not found: ipython

Then you need to either install IPython or add it to your system environment path, you can find the [Windows instructions here](../100/getting-started.md#windows-specific-installation), it's unlikely a UNIX system (MacOS, Linux etc) will have this issue.
