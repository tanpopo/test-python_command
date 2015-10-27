import subprocess

def exec_cmd_communicaet(cmd):
    print("start better_impl %s" % cmd)
    popen = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print("waiting")
    stdout_data, stderr_data = popen.communicate()
    print("finish output length={0} {1}".format(len(stdout_data), len(stderr_data)))
    print("returncode:{0}\n".format(popen.returncode))
    print("stdout:{0}\n".format(stdout_data))
    print("stderr:{0}\n".format(stderr_data))
    return (popen.returncode, stdout_data, stderr_data)

def exec_cmd(cmd, work_dir):
    print("cmd:%s" % cmd)
    try:
        output = subprocess.check_output(cmd.strip().split(" "), shell=True, universal_newlines=True, cwd=work_dir)
#    output = subprocess.check_output(["git","checkcout","release-x1"], shell=True, universal_newlines=True)
    except subprocess.CalledProcessError as grepexc:
        print("error code: {0},{1}".format(grepexc.returncode, grepexc.output))

    print("output:{0}\n".format(output))
    return (output)

git_dir = "/home/marikoyos/wk/test-git-2"
target_branch = "release-x1"
target_changeId = "hogehoge"

checkout_cmd = "git checkout " + target_branch
branch_cmd = "git --version"

out = exec_cmd("pwd", git_dir)
#out = exec_cmd(checkout_cmd, git_dir)
out = exec_cmd(branch_cmd, git_dir)
