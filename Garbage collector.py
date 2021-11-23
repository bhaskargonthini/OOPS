# by default garbage collector is enable, but we can disable based on our requirement in this content, we can use the following
#functions of g module
import gc
print(gc.isenabled())
gc.disable()
print(gc.isenabled())
gc.enable()
print(gc.isenabled())