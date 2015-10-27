import subprocess

# http://qiita.com/mokemokechicken/items/a84b0aa96b94d1931f08

def bad_impl(cmd):
    print("start bad_impl %s" % cmd)
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print("waiting")
    p.wait()
    stdout_data = p.stdout.read()
    stderr_data = p.stderr.read()
    print("finish: {0} {1}".format(len(stdout_data), len(stderr_data)))
    return (1, 2, 3)
#    return (p.returncode, stdout_data, stderr_data)


def better_impl(cmd):
    print("start better_impl %s" % cmd)
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print("waiting")
    stdout_data, stderr_data = p.communicate()
    print("finish: {0} {1}".format(len(stdout_data), len(stderr_data)))
    return (p.returncode, stdout_data, stderr_data)

command1 = "python -c 'print str(1) * 10000'"           # 10KB の出力
command2 = "python -c 'print str(1) * 100000'"          # 100KBの出力

better_impl(command1)
print("=" * 50)
a, b, c = bad_impl(command1)
print("=" * 50)
better_impl(command2)
print("=" * 50)
bad_impl(command2)            # not successs
