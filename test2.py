import subprocess
import shlex


def runCmd(cmd):
    if isinstance(cmd, str):
        cmd = shlex.split(cmd)
    proc = subprocess.Popen(cmd,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            shell=True
                            )
    code, proc_id = proc.returncode, proc.pid
    stdoutData, stdoutErr = proc.communicate()
    return stdoutData.decode(), code, proc_id, stdoutErr