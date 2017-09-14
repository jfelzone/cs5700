using System.Collections.Generic;

namespace MyClasses
{
    public abstract class ConsoleOutput : Output
    {
        public string Name { get; set; }
        public string Description { get; set; }
        //public abstract void Write(List<ThingABob> list, string filename);
        //public abstract void Read(List<ThingABob> list, string filename);
        
        // this will need to take in a pair list
        // and also not return an int
        public override int Write(List<Person> list, string filename){
        	return 0;
        }

       
    }
}