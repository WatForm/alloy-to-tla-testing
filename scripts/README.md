# README.md

* scripts for getting models?  although we have to have instances for them so I guess we have to store the models themselves in this repo

* run dashplus -tla -cmd .als to produce .tla/.cfg file for all models
	* creates one tla model per als file
	* creates one cfg file per command in an als file - cmds in order by number

* run AA to figure out cmd result:

	- must have java 12+ installed locally

	- `java -jar libs/org.alloytools.alloy.dist-6.2.0.jar help`
	shows the top-level CLI options

	- `java -jar bin/org.alloytools.alloy.dist-6.2.0.jar`
	runs the AA 6.2.0 gui

	- `java -jar bin/org.alloytools.alloy.dist-6.2.0.jar exec`
	shows options for executing an Alloy model

	- `java -jar bin/org.alloytools.alloy.dist-6.2.0.jar exec model.als`
    runs ALL commands in model and produces output such as:
    00. run   run$1                    1/1     SAT
	01. run   run$2                    1/1     SAT
	This cmd also creates a directory called "model/".  Within this directory is:
		- cmd-solution-0.md is a json file that is a rendered version of the instances for each cmd
		- a json file - something to do with the instances, but since there are two commands, I'm not sure

	- To overwrite the output files use -f:
	`java -jar bin/org.alloytools.alloy.dist-6.2.0.jar exec -f model.als`

	- to produce xml rather than md of the solutions use -t xml:
	`java -jar bin/org.alloytools.alloy.dist-6.2.0.jar exec -t xml model.als`

	- to produce multiple solutions to the same cmd use -r num:
	`java -jar bin/org.alloytools.alloy.dist-6.2.0.jar exec -r 5 model.als`
	(-t xml -r ? is likely useful for producing instances of the Alloy model.)

	- to run just one command in the Alloy model, use -c num; cmds are zero-indexed
	`java -jar bin/org.alloytools.alloy.dist-6.2.0.jar exec -c 1 model.als`
	If no cmd in the file, it will run the default command

	- To send all output to the screen and not generate the directory, use -o -:
	`java -jar bin/org.alloytools.alloy.dist-6.2.0.jar exec -o - model.als`
	But this did not generate a clear sat/unsat answer for a command.  Perhaps try it with an unsat and see what it generates; so the opposite it clearly sat.

	- to show all (textual) commands in the model:
	`java -jar libs/org.alloytools.alloy.dist-6.2.0.jar commands model.als`


* run tlc on all .tla/.cfg combinations and check against result running Alloy 6.2.0 (not dashplus)
	- cmds are executed in Alloy 6.2.0 
	- need to grep Alloy 6 and TLC results and make sure they agree for sat/unsat

* check instances
	- dashplus f.als -gen=n 
		- or should we use Alloy 6.2 to generate instances?
		- could do this for multiple scopes?
		- could use CompoSAT (but might be version issues)
	- dashplus f.dsh -tla -xml (instances have their scopes built in) on each instance file to create a .tla/.cfg pair 
	- use TLC to check if instances of tlc model 

* clean up script