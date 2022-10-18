#include "fix.h"
#include<stdio.h>
extern "C"{ void fixer_so(char*, char*, char*); }

void fixer_so(char* inputFile, char* outFile, char* baseAddr) {

	const char* openPath = (const char*)inputFile;
	const char* outPutPath = (const char*)outFile;
	const char* base_addr = (const char*)baseAddr;

	printf("FileName: %s\n", openPath);
	printf("OutPutPath: %s\n", outPutPath);
	printf("Base Address: %s\n", base_addr);

	uint64_t base = strtoull(base_addr, 0, 16);

	fix_so(openPath, outPutPath, base);

}