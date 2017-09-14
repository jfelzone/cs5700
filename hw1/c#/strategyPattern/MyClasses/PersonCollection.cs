using System;
using System.Collections.Generic;

namespace MyClasses
{
	public class PersonCollection : List<Person>
	{
		public DataInput collectionDataInput {get; set;}

		 public PersonCollection(DataInput passedInInput)
    	{
      	  	collectionDataInput = passedInInput;
    	}
	}
}