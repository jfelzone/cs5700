using System.Collections.Generic;
using System;

namespace MyClasses
{
    public class OutputFile : Output
    {
        // public string Name { get; set; }
        // public string Description { get; set; }
        //public abstract void Write(List<ThingABob> list, string filename);
        //public abstract void Read(List<ThingABob> list, string filename);
        // this will need to take in a pair list
        // and also not return an int
        public override void Write(PairList list){
            string[] lines = new string[list.Count];
        	int index = 0;
            foreach (Pair thing in list)
            {
            	lines[index] = thing.First.ObjectId+','+thing.Second.ObjectId;
                index++;
            }
            System.IO.File.WriteAllLines(FileName, lines);
		}

       
    }
}