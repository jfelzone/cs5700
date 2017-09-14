using System;
using MyClasses;

namespace strategyPattern
{
    class Program
    {
        private static readonly DataInput[] DataInputList = new DataInput[]
                        {
                            new JsonInput() { Name = "JSON", Description  = "JavaScript Object Notation"},
                            new XmlInput() { Name = "XML", Description = "Extensible Markup Language"}
                        };


        private static readonly Output[] DataOutputList = new Output[]{
        	new OutputConsole() {Name = "Console", Description = "Sending data to stdout Console"}
        };

        private static readonly Matcher[] MatcherList = new Matcher[]{
        	new MatcherOne() {Name = "1", Description = "First Matching Algorithm"}
        };

        static void Main(string[] args)
        {
        	String[] arguments = Environment.GetCommandLineArgs();
		    Console.WriteLine("GetCommandLineArgs: {0}", String.Join(", ", arguments));
		    Console.WriteLine(arguments.Length);
            Console.WriteLine("Hello World!");
            Console.WriteLine(DataInputList[0].Name);
            Console.WriteLine(DataInputList[0].Description);
            Console.WriteLine(DataInputList[1].Name);
            Console.WriteLine(DataInputList[1].Description);

            Person bob = new Person(){FirstName = "Hello sicko", LastName = "dummy"};
            Console.WriteLine(bob.ToString());
            DataInput newInput = GetInputFormat(arguments[2]);
            Console.WriteLine(newInput.Name);

            //ok now we need to play around with our person collection again
            // want to make a new person collection and pass in the datainput
            PersonCollection personList = new PersonCollection(newInput, arguments[2]);
            personList.Read();
            //personList.PrintCollection();
            // now we have successfully passed in the input into the person collection. 
            // i want to then call the read function from within the collection i think. if i can

            //at this point i need to determine the output based on the command lines... 
            	// let's write a function for this one

			//real quick let's determine the type of matcher that we are going to run
			Matcher resultingMatcher = GetMatcherAlgorithm(arguments[1]);
			Console.WriteLine(resultingMatcher.Name + " " + resultingMatcher.Description);

			// now we need to figure out how to determine the output... 
			Output resultingOutput = GetOutputType(arguments);
			Console.WriteLine(resultingOutput.Name);

			// next i want something like this

			// PersonPairList = personList.generatePairs(resultingMatcher);
			// PersonPairList.sendOutput(outputtype)
			//		what i did in python
  			//		matchList = newMatcherArg.findMatches(personList)
  			//		resultingMatcher.sendResults(matchList)

  			PairList resultingPairList = resultingMatcher.FindMatches(personList);
  			resultingOutput.Write(resultingPairList);

        }

	    private static DataInput GetInputFormat(string FileName){
			//Console.WriteLine(FileName.Split('.')[1]);
			DataInput result = null;
			string extension = FileName.Split('.')[1].ToUpper();
			foreach (DataInput item in DataInputList){
				if (item.Name == extension){
					result = item;
				}
			}
			return result;	
  	    }

  	    private static Matcher GetMatcherAlgorithm(string arg){
  	    	Matcher result = null;
  	    	foreach (Matcher item in MatcherList){
  	    		if (item.Name == arg){
  	    			result = item;
  	    		}
  	    	}
  	    	return result;
  	    }

  	    private static Output GetOutputType(string[] arg){
  	    	string outputtemp = null;
  	    	Output result = null;
  	    	if (arg.Length <= 4){
  	    		outputtemp = "Console";
  	    	}
  	    	else {
  	    		outputtemp = "File";
  	    	}
  	    	foreach (Output item in DataOutputList){
  	    		if(item.Name == outputtemp){
  	    			result = item;
  	    		}
  	    	}
  	    	return result;
  	    }

  	    // some of this we should off board in the fact that the functions above are resulting in null values if something i wasn't plannign for was entered
  	    private static bool ValidateCommandLineArguments(string[] arg){
  	    	if (arg.Length < 3){
  	    		return false;
  	    	}
  	    	return true;

  	    }

    }


}
