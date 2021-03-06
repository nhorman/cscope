Cscope is a text screen based source browsing tool.  Although it is
primarily designed to search C code (including lex and yacc files), it
can also be used for C++ code.

Using cscope, you can easily search for where symbols are used and
defined.  Cscope is designed to answer questions like:

        Where is this variable used?
        What is the value of this preprocessor symbol?
        Where is this function in the source files?
        What functions call this function?
        What functions are called by this function?
        Where does the message "out of space" come from?
        Where is this source file in the directory structure?
        What files include this header file?

It has been released by The Santa Cruz Operation, Inc as Open Source
under the BSD license.  Please look at COPYING for a detailed
description of the license.

For instructions on how to build and install cscope, see the file,
"INSTALL".

One thing to be pointed out is that this is ancient Unix software
predating much of today's security concerns.  While we do try to
address safety issues as we learn about them, it must be said that
this is in no way hardened or secure software.  It's designed to be
used by developers, not administrators or anonymous users.

Browse to http://cscope.sourceforge.net for more current information

[![Build Status](https://travis-ci.org/Irqbalance/irqbalance.svg?branch=master)](https://travis-ci.org/Irqbalance/irqbalance)
