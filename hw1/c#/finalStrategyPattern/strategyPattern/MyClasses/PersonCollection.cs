using System;
using System.Collections.Generic;

namespace MyClasses
{
	public class PersonCollection : List<Person>
	{
		public DataInput collectionDataInput {get; set;}
		public string CollectionDataFile {get; set;}
        public int Length {
        	get{return base.Count;}
        }
		 public PersonCollection(DataInput passedInInput, string passedinfile)
    	{
      	  	collectionDataInput = passedInInput;
      	  	CollectionDataFile = passedinfile;
    	}

    	// this one is mostly going to be for me here for a sec
    	public void PrintCollection () {
    		foreach (Person thing in this)
            {
                Console.WriteLine(thing);
            }
    	}

    	public void Read()
        {
            collectionDataInput?.Read(this, CollectionDataFile);
        }


	}
}