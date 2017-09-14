using System.Collections.Generic;

namespace MyClasses
{
    public abstract class Output
    {
        public string Name { get; set; }
        public string Description { get; set; }

        public string FileName {get; set;}
        //public abstract void Write(List<ThingABob> list, string filename);
        //public abstract void Read(List<ThingABob> list, string filename);
        
        // this will need to take in a pair list
        // this needs to be more extensible. 
        	// for whatever reason it doesn't seem to extend unless it matches the parameters of the kids calling it
        public virtual void Write(PairList list){}
        public virtual void Write(PairList list, string filename){}
       
    }
}