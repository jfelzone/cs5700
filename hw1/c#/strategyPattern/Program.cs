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
            PersonCollection personList = new PersonCollection(newInput);
            // now we have successfully passed in the input into the person collection. 
            // i want to then call the read function from within the collection i think. if i can
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
    }


}
