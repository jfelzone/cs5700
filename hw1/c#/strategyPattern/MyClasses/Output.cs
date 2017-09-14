using System.Collections.Generic;

namespace MyClasses
{
    public abstract class Output
    {
        public string Name { get; set; }
        public string Description { get; set; }
        //public abstract void Write(List<ThingABob> list, string filename);
        //public abstract void Read(List<ThingABob> list, string filename);
        
        // this will need to take in a pair list
        public abstract void Write(List<Person> list, string filename);

       
    }
}