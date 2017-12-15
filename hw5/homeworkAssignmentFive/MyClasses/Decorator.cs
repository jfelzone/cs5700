using System.Collections.Generic;
using System.IO;
using System.Runtime.Serialization.Json;

namespace MyClasses{

	public abstract class Decorator : JsonInput
	{	
		JsonInput dec_JsonInput = null;

		string dec_Name = "UnNamed Decorator";

		protected Decorator(JsonInput baseDataInput){
			dec_JsonInput = baseDataInput;
		}

		string GetName(){
			return dec_JsonInput.Name;
		}
	}		
}
	