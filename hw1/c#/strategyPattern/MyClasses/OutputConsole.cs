using System.Collections.Generic;
using System;

namespace MyClasses
{
    public class OutputConsole : Output
    {
        // public string Name { get; set; }
        // public string Description { get; set; }
        //public abstract void Write(List<ThingABob> list, string filename);
        //public abstract void Read(List<ThingABob> list, string filename);
        
        // this will need to take in a pair list
        // and also not return an int
        public override void Write(PairList list){

        	foreach (Pair thing in list)
            {
            	Console.WriteLine("Matches:");
                Console.WriteLine("\t"+thing.First.ToString());
                Console.WriteLine("\t"+thing.Second.ToString());
            }
		}

       
    }
}