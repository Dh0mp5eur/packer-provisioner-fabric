from fabric.api import *

@task
def test():
    run("echo \"This is a test\" >> test.txt")

def test2():
    run("echo \"This is another test\" >> test.txt")
