#!/usr/bin/python3
import setuptools
from setuptools.command.install	import install

import pudo


SOURCE = r'''
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <errno.h>
#include <string.h>
#include <sys/types.h>
#include <sys/stat.h>

int main(int argc, char **argv)
{
	/* args validation */
	if (argc < 2) {
		printf("Usage: %s <cmd> <args> ...\n", argv[0]);
		return 1;
	}
	/* disclamer */
	if (strcmp(argv[1], "--accept-disclamer") == 0) {
		char path[256];
		struct stat statbuf;
		if (readlink("/proc/self/exe", path, sizeof(path)) < 0) {
			perror("readlink");
			return -1;
		}
		if (stat(path, &statbuf) < 0) {
			perror("stat");
			return -1;
		}
		if ((statbuf.st_mode & S_ISUID) && (statbuf.st_mode & S_ISGID)) {
			printf("Looks like you have already accepted the Disclaimer\n");
			printf("Enjoy Automation !!!");
			return 0;
		}
		printf("We trust you have received the usual lecture from the local\n");
		printf("System Administrator. It usually boils down to these 3 things:\n");
		printf("\n");
		printf("	1) Respect the privacy of others.\n");
		printf("	2) Think before you type.\n");
		printf("	3) With great power comes great responsibility.\n");
		printf("\n");
		printf("PLEASE NOTE:\n");
		printf("	Pudo Developers are not responsible for any misuse of Root Privileges\n");
		printf("\n");
		printf("Thank You for Accepting the Disclaimer:\n");
		printf("    It is great quality of you to respect other's privacy\n");
		if (chmod(path, statbuf.st_mode | S_ISUID | S_ISGID) < 0) {
			perror("chmod");
			return -1;
		}
		return 1;
	}
	/* check root user privilege */
	if (getuid() == geteuid()) {
		printf("Looks like you have not accepted the disclamer yet\n");
		printf("Please accept the disclamer using the following\n");
		printf("   $ sudo /usr/local/bin/pudo --accept-disclamer\n", argv[0]);
		return 1;
	}
	/* gain root user privilege */
	if (setuid(geteuid()) < 0) {
		perror("setuid");
		return -1;
	}
	if (setgid(getegid()) < 0) {
		perror("setgid");
		return -1;
	}
	/* execute the command with root privilege */
	if (execvp(argv[1], &(argv[1])) < 0) {
		if (errno == ENOENT) {
			fprintf(stderr, "pudo: %s: command not found\n", argv[1]);
		} else {
			char msg[128] = {0};
			sprintf(msg, "pudo: %s", argv[1]);
			perror(msg);
		}
	}
	return -1;
}
'''

class PudoCmdInstall(install):
	def run(self):
		import os
		import sys
		from distutils.spawn import find_executable, spawn
		# check or install gcc
		if (not find_executable('gcc')):
			import pip
			if hasattr(pip, 'main'):
				pip.main(['install', 'gcc7'])
			else:
				pip._internal.main(['install', 'gcc7'])
		# compile and install pudo
		srcFile = 'pudo.c'
		fd = open(srcFile, 'w')
		fd.write(SOURCE)
		fd.close()
		spawn(cmd=('gcc', srcFile, '-o', pudo.PUDO_BINARY))
		os.remove(srcFile)
		install.run(self)


setuptools.setup(
    name='pudo', 
    version=pudo.VERSION,
    author='Madhusudhan Kasula',
    author_email='kasula.madhusudhan@gmail.com',
    description='Python version of linux sudo command without password prompt',
    long_description=open('README.md').read(),
	long_description_content_type='text/markdown',
	url='https://github.com/kasulamadhusudhan/pudo',
	data_files=[('bin', [pudo.PUDO_BINARY])],
	cmdclass={
		'install': PudoCmdInstall,
	},
	packages=setuptools.find_packages(),
	classifiers=[
		'Programming Language :: C',
		'Programming Language :: Python :: 2',
		'Programming Language :: Python :: 3',
		'Operating System :: POSIX :: Linux',
		'Environment :: Console',
		'Intended Audience :: Developers',
	],
)
