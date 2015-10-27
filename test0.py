import subprocess

# test multiple output
def f():
    return (1, "abc")
    # return [1, "abc"]

a, b = f()
print("output of a, b:")
print(a) # => 1
print(b) # => abc

# test subprocess()
print("output of \"ls -l\":")
subprocess.call(['ls', '-1'], shell=True)

#test subprocess.check_output()
output = subprocess.check_output(['ls', '-1'])
print('Have {0} bytes in output'.format(len(output)))
print("output={0}".format(output))
