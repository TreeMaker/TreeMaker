import argparse
import os
import subprocess
import sys
if os.environ["CMSSW_BASE"] is not "":
    try:
        sys.path.append(os.environ["CMSSW_BASE"] + "/src/Condor/Production/python/")
        import manageJobs
    except ModuleNotFoundError as e:
        print(e)
else:
    raise ImportError("Could not find the CMSSW base path")

# https://stackoverflow.com/questions/5136611/capture-stdout-from-a-script
import contextlib
@contextlib.contextmanager
def Capturing():
    import sys
    from cStringIO import StringIO
    oldout,olderr = sys.stdout, sys.stderr
    try:
        out=[StringIO(), StringIO()]
        sys.stdout,sys.stderr = out
        yield out
    finally:
        sys.stdout,sys.stderr = oldout, olderr
        out[0] = out[0].getvalue()
        out[1] = out[1].getvalue()

def get_input_file(basepath, outputs):
    file_per_job = {}
    for output in outputs:
        output_file = basepath+output+".stdout"
        with open(output_file, 'r') as f:
            for line in lines_that_contain("readFiles: ['", f):
                line = line.replace(" readFiles: ['", "")
                line = line.replace("']\n", "")
                line = line[line.find("/store/"):]
                if "/store/test/xrootd/" in line:
                    line = line[find_nth(line,"/store/",2):]
                file_per_job[output] = line
    return file_per_job

def find_job_output(user):
    with Capturing() as outputs:
        manageJobs.manageJobs(["-a", "-h", "-o", "--user", user])
    outputs = outputs[0].split('\n')
    outputs = [o for o in outputs if o is not '']
    return outputs

def find_file_and_resubmit(argv=None):
    if argv is None: argv = sys.argv[1:]

    parser = argparse.ArgumentParser(prog='file_finder_resubmitter.py', description = "Resubmit jobs using input from a specific site.")
    parser.add_argument("-b", "--basepath", default = os.environ["PWD"], help = "Path of the job logs (default: %(default)s)")
    parser.add_argument("-d", "--dry_run", action = "store_true", default = False, help = "Do everything except resubmit the jobs (default: %(default)s)")
    parser.add_argument("-g", "--grep")
    parser.add_argument("-u", "--user", default = os.environ["USER"], help = "The user whose jobs you want to resubmit (default: %(default)s)")
    parser.add_argument("--us", action = "store_true", default = False, help = "Preferentially select US sites over others (default: %(default)s)")
    parser.add_argument("--version", action='version', version='%(prog)s v1.0.0')
    args = parser.parse_args(args=argv)

    if args.basepath[-1] != '/':
        args.basepath += '/'

    outputs = find_job_output(args.user)
    file_per_job = get_input_file(args.basepath, outputs)
    file_and_site_per_file = find_site(file_per_job, args.us)

    jobs_resubmitted = {}
    jobs_not_resubmitted = {}
    print "Resubmitting jobs (dry_run = " + str(args.dry_run) + ") ...",
    for job, (file, site, sites) in file_and_site_per_file.iteritems():
        if site is None:
            jobs_not_resubmitted[job] = (file, site, sites)
        else:
            jobs_resubmitted[job] = (file, site, sites)
            with Capturing() as resub_outputs:
                if args.dry_run:
                    manageJobs.manageJobs(["-a", "-h","-o", "--user", args.user,"-g",job,"-x",site]) # output contained in resub_outputs[0]
                else:
                    manageJobs.manageJobs(["-a", "-hs","-o", "--user", args.user,"-g",job,"-x",site]) # output contained in resub_outputs[0]
    print "DONE"

    print "\nJobs resubmitted:"
    fmt = "\t{0:>80s}: file={1:<100s} site={2:<20s}"
    for job, (file, site, sites) in jobs_resubmitted.iteritems():
        print fmt.format(job,file,site)

    print "\nJobs not resubmitted due to lack of an acceptable site:"
    fmt = "\t{0:>80s}: file={1:<100s} sites={2:<30s}"
    for job, (file, site, sites) in jobs_not_resubmitted.iteritems():
        print fmt.format(job,file,str(sites))

#From: https://stackoverflow.com/questions/1883980/find-the-nth-occurrence-of-substring-in-a-string
def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

def find_site(file_per_job, prefer_us = False):
    file_and_site_per_job = {}
    print "Finding the sites for each file ... ",
    for i, (job, file) in enumerate(file_per_job.iteritems()):
        cmd = "dasgoclient -query=\"site file=" + file + "\""
        p = subprocess.Popen(cmd, shell = True, stdout=subprocess.PIPE)
        out, err = p.communicate()
        sites = [None] if "WARNING:" in out else out.split()
        site = select_site(sites, prefer_us)
        file_and_site_per_job[job] = (file,site,sites)
    print "DONE"
    return file_and_site_per_job

def lines_that_contain(string, fp):
    return [line for line in fp if string in line]

def select_site(sites, prefer_us = False):
    selected = None
    sites = [s for s in sites if s is not None and "Tape" not in s]
    sites = sorted(sites, key = lambda x: ("FNAL" in x.split('_')[2], "US" in x.split('_')[1] and prefer_us), reverse = True)
    if len(sites) > 0:
        selected = sites[0]
    if selected is not None:
        selected = selected.replace("_Disk","")
    return selected

if __name__ == "__main__":
    find_file_and_resubmit()