#!/usr/bin/env python
# Simple Daikon-style invariant checker
# Andreas Zeller, May 2012
# Complete the provided code around lines 28 and 44
# Do not modify the __repr__ functions.
# Modify only the classes Range and Invariants,
# if you need additional functions, make sure
# they are inside the classes.

import sys
import math
import random

def square_root(x, eps = 0.00001):
    assert x >= 0
    y = math.sqrt(x)
    assert abs(square(y) - x) <= eps
    return y

def square(x):
    return x * x

# The Range class tracks the types and value ranges for a single variable.
class Range:
    def __init__(self):
        self.min = None  # Minimum value seen
        self.max = None  # Maximum value seen

    # Invoke this for every value
    def track(self, value):
        if (self.min == None) or (self.min > value):
            self.min = value

        if (self.max == None) or (self.max < value):
            self.max = value

    def __repr__(self):
        return repr(self.min) + ".." + repr(self.max)


# The Invariants class tracks all Ranges for all variables seen.
class Invariants:
    def __init__(self):
        # Mapping (Function Name) -> (Event type) -> (Variable Name)
        # e.g. self.vars["sqrt"]["call"]["x"] = Range()
        # holds the range for the argument x when calling sqrt(x)
        self.vars = {}

    def track(self, frame, event, arg):
        if event == "call" or event == "return":
            # get the current function name (just for ease of reading)
            function_name = frame.f_code.co_name

            # set up the local vars to include the return value
            local_vars = frame.f_locals
            if event == 'return':
                local_vars['ret'] = arg

            # initalise the dicts if needed
            (self.vars
                .setdefault(function_name, {})
                .setdefault(event, {}))

            # for each local variable
            for local, value in local_vars.iteritems():
                # check if the local is in the tracked vars
                if local not in self.vars[function_name][event]:
                    # if not create a new Range object for that local var
                    self.vars[function_name][event][local] = Range()
                # always track the current value of the local var
                self.vars[function_name][event][local].track(value)

            # print "square_root = {0}".format(self.vars.get('square_root'))
            # print "square = {0}".format(self.vars.get('square'))
            # print

    def __repr__(self):
        # Return the tracked invariants
        s = ""
        for function, events in self.vars.iteritems():
            for event, vars in events.iteritems():
                s += event + " " + function + ":\n"
                # continue

                for var, range in vars.iteritems():
                    s += "    assert "
                    if range.min == range.max:
                        s += var + " == " + repr(range.min)
                    else:
                        s += repr(range.min) + " <= " + var + " <= " + repr(range.max)
                    s += "\n"

        return s

invariants = Invariants()

def traceit(frame, event, arg):
    invariants.track(frame, event, arg)
    return traceit

sys.settrace(traceit)
# Tester. Increase the range for more precise results when running locally
eps = 0.000001
for i in range(1, 3):
    r = int(random.random() * 1000) # An integer value between 0 and 999.99
    z = square_root(r, eps)
    z = square(z)
sys.settrace(None)
print invariants

