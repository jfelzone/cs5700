using System.Collections.Generic;

namespace MyClasses
{
    public abstract class Matcher
    {
        public string Name { get; set; }
        public string Description { get; set; }
        //public abstract void Write(List<ThingABob> list, string filename);
        //public abstract void Read(List<ThingABob> list, string filename);
        public abstract PairList FindMatches(PersonCollection inPersonCol);

       
    }
}