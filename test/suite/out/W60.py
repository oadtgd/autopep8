#: W601
if "b" in a:
    print a
#: W602
raise DummyError, "Message"
#: W602
raise ValueError, "hello %s %s" % (1, 2)
#: Okay
raise type_, val, tb
raise Exception, Exception("f"), t
#: W603
if x != 0:
    x = 0
#: W604
val = repr(1 + 2)
