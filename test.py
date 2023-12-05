#!/usr/bin/env python3
#
#program spustí všechny testy z složky test
#podle přípony se rozhodne jestly dopadly dobře
# .ok -> má vrátit hodnotu 0
# .e7 -> má vrátit hodnotu 7
# .e[číslo] -> má vrátit to číslo
#! pozor zatím jdou jen jednočíselné kódy

import sys
import os	
import getopt
import subprocess
from subprocess import run
from colorama import Fore, Back, Style

def printOK():
    print("  [" + Fore.GREEN + 'OK' + Style.RESET_ALL + ']')

def printOKfail():
    print("  [" + Fore.GREEN + 'OK' + Style.RESET_ALL + '] failed sucesfuly')

def printERRisOK():
    print("  [" + Fore.RED + 'X' + Style.RESET_ALL + '] dont fail')

def printERRdiferentError():
    print("  [" + Fore.RED + 'X' + Style.RESET_ALL + '] fail with diferent code')

def printERR():
    print("  [" + Fore.RED + 'X' + Style.RESET_ALL + ']')

def testFile(file,expectedOutcome):
    myinput = open(file)   # input file -NOT python
    compiler_process = subprocess.Popen(["./main"], stdin=myinput, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    compiler_stdout, compiler_stderr = compiler_process.communicate()
    compiler_process.kill()

    if(compiler_process.returncode == expectedOutcome and  expectedOutcome == 0):
        printOK()
        return
    if(compiler_process.returncode != expectedOutcome and expectedOutcome == 0):
        printERR()
        print(compiler_stderr.decode("utf-8"))
        return
    if(compiler_process.returncode == expectedOutcome and  expectedOutcome != 0):
        printOKfail()
        return
    if(compiler_process.returncode != expectedOutcome and compiler_process.returncode != 0):
        printERRdiferentError()
        print(compiler_stderr.decode("utf-8"))
        return
    if(compiler_process.returncode != expectedOutcome and expectedOutcome != 0 and compiler_process.returncode == 0):
        printERRisOK()
        print("------------------ program neselhal(jak bylo očekáváno)  výpis stdout -------------------------------")
        print(compiler_stdout.decode("utf-8"))
        print("------------------------------------- konec výpisu programu -----------------------------------------")
        return


#make makefile

print("--------------------- výpis z make -----------------------------------")
make_process = subprocess.Popen(["make"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
make_stdout, make_stderr = make_process.communicate()
print(make_stderr.decode("utf-8"))
print(make_stdout.decode("utf-8"))
print("------------------ konec výpisu z make -------------------------------\n\n\n\n")


files = os.listdir('test')



for file in files:

    testparams = file.split(".")[1]
    if testparams == "ok":
        print(Fore.LIGHTMAGENTA_EX + "testing " + Style.RESET_ALL + file.ljust(30,'.'), end='')
        testFile("test/"+file,0)
        continue
    if testparams[0] == 'e' :
        errret = file.split(".e")[1]
        print(Fore.LIGHTMAGENTA_EX + "testing " + Style.RESET_ALL + file.ljust(30,'.'), end='')
        testFile("test/"+file,int(errret))
        continue

    print(Fore.BLACK + "skiping " + file + Style.RESET_ALL)
