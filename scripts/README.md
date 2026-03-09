# README.md

* scripts for getting models?  although we have to have instances for them so I guess we have to store the models themselves in this repo

* run dashplus -tla -cmd .als to produce .tla/.cfg file for all models
	* creates one tla model per als file
	* creates one cfg file per command in an als file - cmds in order by number

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