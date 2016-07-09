#!/usr/bin/env python
# Simple debugger
# See instructions around line 34
import sys
import readline

# Our buggy program
def remove_html_markup(s):
    tag   = False
    quote = False
    out   = ""

    for c in s:
        if c == '<' and not quote:
            tag = True
        elif c == '>' and not quote:
            tag = False
        elif c == '"' or c == "'" and tag:
            quote = not quote
        elif not tag:
            out = out + c
    return out

# main program that runs the buggy program
def main():
    print remove_html_markup('xyz')
    print remove_html_markup('"<b>foo</b>"')
    print remove_html_markup("'<b>foo</b>'")

# globals
breakpoints = {9: True}
watchpoints = {'c': True}
stepping = False

"""
Our debug function
Improve and expand the debug function to accept
a watchpoint command 'w <var name>'.
Add the variable name to the watchpoints dictionary
or print 'You must supply a variable name'
if 'w' is not followed by a string.
"""
def debug(command, my_locals):
    global stepping
    global breakpoints

    if command.find(' ') > 0:
        arg = command.split(' ')[1]
    else:
        arg = None

    if command.startswith('s'):     # step
        stepping = True
        return True
    elif command.startswith('c'):   # continue
        stepping = False
        return True
    elif command.startswith('p'):    # print
        if ' ' in command:
            var_name = command.split()[1]
            var_value = my_locals.get(var_name)
            if var_value or var_value == False:
                print "{0} = {1}".format(var_name, repr(var_value))
            else:
                print 'No such variable:', var_name
        else:
            print my_locals
    elif command.startswith('b'):    # breakpoint
        if ' ' in command:
            new_line = command.split()[1]
            breakpoints[int(new_line)] = True
        else:
            print 'You must supply a line number'
    elif command.startswith('w'):    # watch variable
        if ' ' in command:
            var_name = command.split()[1]
            watchpoints[var_name] = True
        else:
            print 'You must supply a variable name'
    elif command.startswith('q'):   # quit
        sys.exit(0)
    else:
        print "No such command", repr(command)

    return False

commands = ["p", "s", "p tag", "p foo", "q"]

def input_command():
    #command = raw_input("(my-spyder) ")
    global commands
    command = commands.pop(0)
    return command

def traceit(frame, event, trace_arg):
    global stepping

    if event == 'line':
        if stepping or breakpoints.has_key(frame.f_lineno):
            resume = False
            while not resume:
                print event, frame.f_lineno, frame.f_code.co_name, frame.f_locals
                command = input_command()
                resume = debug(command, frame.f_locals)
    return traceit

# Using the tracer
sys.settrace(traceit)
main()
sys.settrace(None)

#Simple test
# print watchpoints
# debug("w", {'s': 'xyz', 'tag': False})
# print watchpoints
#>>> {'c': True}
#>>> {'c': True, 's': True}