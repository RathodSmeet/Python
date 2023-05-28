# Arbitary keyword arguments
def my_function(**args):
    #print(args)
    for key in args:
        print(key,":",args[key])
        
my_function(arg1=10,arg2=20,arg3=30)