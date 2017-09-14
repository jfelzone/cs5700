using System.Collections.Generic;
using System.IO;
using System.Runtime.Serialization.Json;

namespace MyClasses
{
    public class JsonInput : DataInput
    {
        private static readonly DataContractJsonSerializer JsonSerializer = new DataContractJsonSerializer(typeof(List<Person>),
                     new [] { typeof(Person) });
        public override void Read(List<Person> list, string filename)
        {
            //filename = AppendExtension(filename, "json");
            StreamReader reader = new StreamReader(filename);
            List<Person> data = JsonSerializer.ReadObject(reader.BaseStream) as List<Person>;
            if (data!=null)
            {
                foreach(Person thing in data)
                    list.Add(thing);
            }
        }
    }
}
