using System;
using MyClasses;


//jake felzien

// command line arguments for our testing currently: 1 JSON_PersonTestSet_3.json Results.txt
namespace strategyPattern
{
    class Program
    {
        private static readonly DataInput[] DataInputList = new DataInput[]{
                            new JsonInput() { Name = "JSON", Description  = "JavaScript Object Notation"},
                            new XmlInput() { Name = "XML", Description = "Extensible Markup Language"}
		};
        private static readonly Output[] DataOutputList = new Output[]{
        	new OutputConsole() {Name = "Console", Description = "Sending data to stdout Console"},
			new OutputFile() {Name = "File", Description = "Sending data to output file"}
        };

        private static readonly Matcher[] MatcherList = new Matcher[]{
        	new MatcherOne() {Name = "1", Description = "First Matching Algorithm, Firstname"},
			new MatcherTwo() {Name = "2", Description = "Second Matching Algorithm, Firstname, Lastname, Social"},
			new MatcherThree() {Name = "3", Description = "Third Matching Algorithm, Firstname, Lastname, Social, and Brithdate"}
		};

        static void Main(string[] args)
        {
        	String[] arguments = Environment.GetCommandLineArgs();
		    Console.WriteLine("GetCommandLineArgs: {0}", String.Join(", ", arguments));
		    Console.WriteLine(arguments.Length);
			if (!ValidateCommandLineArguments(arguments)){
				Console.WriteLine("Invalid arguments entered");
				return;		
			}
			DataInput newInput = GetInputFormat(AppendFileDirectory(arguments[2]));
			if (!IsValidObject(newInput)){
				Console.WriteLine("Invalid data input");
				return;				
			}
			Console.WriteLine(newInput.Name);
			

            //ok now we need to play around with our person collection again
            // want to make a new person collection and pass in the datainput
            PersonCollection personList = new PersonCollection(newInput, AppendFileDirectory(arguments[2]));
			if (!IsValidObject(personList)){
				Console.WriteLine("Invalid person list");
				return;				
			}
            personList.Read();
			
            //personList.PrintCollection();
            // now we have successfully passed in the input into the person collection. 
            // i want to then call the read function from within the collection i think. if i can

            //at this point i need to determine the output based on the command lines... 
            	// let's write a function for this one

			//real quick let's determine the type of matcher that we are going to run
			Matcher resultingMatcher = GetMatcherAlgorithm(arguments[1]);
			if (!IsValidObject(resultingMatcher)){
				Console.WriteLine("Invalid person matcher");
				return;				
			}
			Console.WriteLine(resultingMatcher.Name + " " + resultingMatcher.Description);
			
			// now we need to figure out how to determine the output... 
			Output resultingOutput = GetOutputType(arguments);
			if (!IsValidObject(resultingOutput)){
				Console.WriteLine("Invalid data output entered");
				return;				
			}
			Console.WriteLine(resultingOutput.Name);
			
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
  	    	if (arg.Length <= 3){
  	    		outputtemp = "Console";
  	    	}
  	    	else {
  	    		outputtemp = "File";
  	    	}
  	    	foreach (Output item in DataOutputList){
  	    		if(item.Name == outputtemp){
  	    			result = item;
					  if (result.Name == "File"){
							result.FileName = AppendOutputDirectory(arg[3]);
					  } else{
						  result.FileName = "";
					  }
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

		private static string AppendFileDirectory(string arg){
			return "InputFiles/"+arg;
		}

		private static string AppendOutputDirectory(string arg){
			return "OutputFiles/"+arg;
		}

		private static bool IsValidObject(object obj){
			if (obj == null){
				return false;
			} else{
				return true;
			}
		}

    }


}
