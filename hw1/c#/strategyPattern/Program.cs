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
            Console.WriteLine("Hello World!");
            Console.WriteLine(DataInputList[0].Name);
            Console.WriteLine(DataInputList[0].Description);
            Console.WriteLine(DataInputList[1].Name);
            Console.WriteLine(DataInputList[1].Description);

            Person bob = new Person(){FirstName = "Hello sicko", LastName = "dummy"};
            Console.WriteLine(bob.ToString());
            //Console.WriteLine(DataInputList[0].Check);
        }
    }
}
