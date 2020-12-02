# Markdown

## What?

Markdown is (confusingly) a markup language.

A markup language is a syntactic computing language of annotations which renders text and images based on the tags you give it, the syntax itself will not be rendered. HTML and XML are examples of a markup language.

Markdown files have the extension `.md`.

## Why?

Having a standard way to format and render information allows us to be consistent across devices, operating systems and includes all instructions needed to create clear, readable documents.

A common use for markdown is to write instruction files, like a `README.md`. A README contains all of the information, dependencies and instructions needed to run and contribute to a project.

## How?

We use hashes to define headings:

<script src="https://gist.github.com/AdamDewberry/cd9c8ba9fd22daf33a81013ab06740d2.js"></script>

# This is the highest order heading
## This is a sub-heading
### This is a sub-sub-heading

This is an example of a list / bullet points:

    - Text A
    - Text B
    - Text C

- Text A
- Text B
- Text C

This is an example of a numbered list:

    1. Point 1
    1. Point 2
    1. Point 3

1. Point 1
1. Point 2
1. Point 3

**This is bold text**  
__This is bold text__

*This text is in italics*  
_This text is in italics_

Use ticks to define a piece of code:  
`my_arg = 5`

To define a code block, indent the code four spaces or use a tab.

    my_arg = 5
    your_arg = 6

Another way to write a code block is with three ticks.

```
my_arg = 5
your_arg = 6
```

Hyperlinks look like this:  
[link to Python](https://github.com/python/cpython)
