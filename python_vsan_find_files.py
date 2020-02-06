import os
import fnmatch


def recursive_glob(treeroot, pattern):
    results = []
    for base, dirs, files in os.walk(treeroot):
        goodfiles = fnmatch.filter(files, pattern)
        results.extend(os.path.join(base, f) for f in goodfiles)
    return results

list_of_all_logs = recursive_glob('.','vobd.log')
for i in list_of_all_logs:
	print(i)
