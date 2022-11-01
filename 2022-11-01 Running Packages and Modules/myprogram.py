#importing from packages in folders and subfolders
from MyMainPackage import some_main_script
from MyMainPackage.SubPackage import mysubscript

#testing
some_main_script.report_main()

mysubscript.sub_report()

#now running at command line

# I ran in CMD: python myprogram.py
#returned: Hey I am in some_main_script in main package.
#returned: Hey I am a function inside mysubscript